#!/usr/bin/env python3
"""
figma_to_swiftui.py — convert a Figma frame/component into production-ready SwiftUI.

Pipeline:
  1. Fetch the node tree (live via the Figma REST API, or offline from a saved
     JSON fixture with --from-json).
  2. Walk the tree once to collect design tokens (colors, text styles) and to
     identify asset nodes (vectors / image fills) that must be exported.
  3. Emit:
       - <Name>View.swift        one SwiftUI View per top-level frame/component
       - DesignTokens.swift       Color + Font helpers derived from the design
       - Assets.md                manifest of images/icons to drop into Assets.xcassets
       - figma_ir.json            the normalized intermediate representation (for debugging)
  4. When online and --export-assets is set, download the rendered assets too.

The generator favours Auto Layout: HORIZONTAL/VERTICAL frames become HStack/VStack
with the right spacing, padding and alignment. Frames without Auto Layout fall
back to a ZStack so nothing is lost. Anything it can't map cleanly is emitted as
a clearly-marked // TODO so a human (or Devin) can finish it — silent guesses are
worse than visible gaps.

Usage:
  export FIGMA_TOKEN=figd_xxx
  python figma_to_swiftui.py "https://www.figma.com/design/<key>/...?node-id=12-34" --out ./Generated
  python figma_to_swiftui.py --file-key <key> --node-id 12:34 --out ./Generated --export-assets
  python figma_to_swiftui.py --from-json sample.json --out ./Generated   # offline, no token needed
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figma_client import FigmaClient, FigmaError, parse_figma_url  # noqa: E402

INDENT = "    "


# --------------------------------------------------------------------------- #
# Naming helpers
# --------------------------------------------------------------------------- #
def pascal_case(name: str) -> str:
    cleaned = re.sub(r"[^0-9a-zA-Z]+", " ", name or "").strip()
    if not cleaned:
        return "Untitled"
    parts = cleaned.split()
    pascal = "".join(p[:1].upper() + p[1:] for p in parts)
    if pascal[0].isdigit():
        pascal = "_" + pascal
    return pascal


def camel_case(name: str) -> str:
    p = pascal_case(name)
    return p[:1].lower() + p[1:]


# --------------------------------------------------------------------------- #
# Color helpers — Figma colors are 0..1 floats
# --------------------------------------------------------------------------- #
def color_to_hex(c: dict) -> str:
    r = round(c.get("r", 0) * 255)
    g = round(c.get("g", 0) * 255)
    b = round(c.get("b", 0) * 255)
    return f"#{r:02X}{g:02X}{b:02X}"


def color_literal(c: dict, opacity: float = 1.0) -> str:
    """A SwiftUI Color(...) literal with sRGB components."""
    r = round(c.get("r", 0), 4)
    g = round(c.get("g", 0), 4)
    b = round(c.get("b", 0), 4)
    a = round(c.get("a", 1) * opacity, 4)
    if a >= 0.999:
        return f"Color(red: {r}, green: {g}, blue: {b})"
    return f"Color(red: {r}, green: {g}, blue: {b}, opacity: {a})"


FONT_WEIGHTS = {
    100: ".ultraLight", 200: ".thin", 300: ".light", 400: ".regular",
    500: ".medium", 600: ".semibold", 700: ".bold", 800: ".heavy", 900: ".black",
}


def font_weight(w: int | float | None) -> str:
    if not w:
        return ".regular"
    nearest = min(FONT_WEIGHTS, key=lambda k: abs(k - w))
    return FONT_WEIGHTS[nearest]


# --------------------------------------------------------------------------- #
# Token collection
# --------------------------------------------------------------------------- #
class TokenRegistry:
    """Collects unique colors and text styles so we can emit reusable tokens."""

    def __init__(self) -> None:
        self.colors: dict[str, dict] = {}   # hex -> color dict
        self.text_styles: dict[str, dict] = {}  # key -> style dict
        self.assets: dict[str, dict] = {}   # node_id -> {name, fmt}

    def add_color(self, c: dict) -> str:
        hexv = color_to_hex(c)
        self.colors.setdefault(hexv, c)
        return hexv

    def color_name(self, hexv: str) -> str:
        return "color" + hexv.lstrip("#")

    def add_text_style(self, style: dict) -> str:
        size = round(style.get("fontSize", 17))
        weight = style.get("fontWeight", 400)
        key = f"{size}_{weight}"
        self.text_styles.setdefault(key, style)
        return key

    def add_asset(self, node: dict, fmt: str) -> str:
        nid = node["id"]
        if nid not in self.assets:
            self.assets[nid] = {"name": pascal_case(node.get("name", nid)), "fmt": fmt}
        return self.assets[nid]["name"]


# --------------------------------------------------------------------------- #
# Style extraction for a single node
# --------------------------------------------------------------------------- #
def first_solid_fill(node: dict) -> dict | None:
    for fill in node.get("fills", []) or []:
        if fill.get("visible", True) and fill.get("type") == "SOLID":
            return fill
    return None


def has_image_fill(node: dict) -> bool:
    return any(f.get("type") == "IMAGE" for f in node.get("fills", []) or [])


def is_vector_like(node: dict) -> bool:
    return node.get("type") in {"VECTOR", "BOOLEAN_OPERATION", "STAR", "LINE", "REGULAR_POLYGON"}


# --------------------------------------------------------------------------- #
# Code emitter for a node subtree
# --------------------------------------------------------------------------- #
class SwiftUIEmitter:
    def __init__(self, tokens: TokenRegistry):
        self.t = tokens

    def emit(self, node: dict, depth: int) -> list[str]:
        ntype = node.get("type")
        if not node.get("visible", True):
            return []

        if ntype == "TEXT":
            return self._emit_text(node, depth)
        if is_vector_like(node) or has_image_fill(node):
            return self._emit_asset(node, depth)
        if ntype in {"RECTANGLE", "ELLIPSE"}:
            return self._emit_shape(node, depth)
        if ntype in {"FRAME", "GROUP", "COMPONENT", "INSTANCE", "COMPONENT_SET"}:
            return self._emit_container(node, depth)
        # Unknown node type: leave a marker so nothing silently disappears.
        return [f"{INDENT * depth}// TODO: unsupported node '{node.get('name')}' ({ntype})"]

    # --- containers ---
    def _emit_container(self, node: dict, depth: int) -> list[str]:
        children = [c for c in node.get("children", []) if c.get("visible", True)]
        layout = node.get("layoutMode", "NONE")
        spacing = node.get("itemSpacing", 0)

        ind = INDENT * depth
        lines: list[str] = []

        # Surface interactivity the static design can't express. Devin (or a human)
        # then knows exactly where to wire actions instead of shipping a dead view.
        if self._looks_like_button(node):
            lines.append(f"{ind}// TODO[button]: this frame reads as a button — wrap the "
                         f"content in `Button {{ /* action */ }}` and hook up its handler.")

        if layout == "HORIZONTAL":
            align = self._counter_align(node, axis="h")
            stack = f"HStack(alignment: {align}, spacing: {round(spacing)})"
        elif layout == "VERTICAL":
            align = self._counter_align(node, axis="v")
            stack = f"VStack(alignment: {align}, spacing: {round(spacing)})"
        else:
            stack = "ZStack"  # absolute / no auto-layout

        # SPACE_BETWEEN pushes children to the two ends — model it with Spacers.
        space_between = (node.get("primaryAxisAlignItems") == "SPACE_BETWEEN"
                         and layout in {"HORIZONTAL", "VERTICAL"} and len(children) > 1)

        if not children:
            lines.append(f"{ind}{stack} {{ }}")
        else:
            lines.append(f"{ind}{stack} {{")
            for i, child in enumerate(children):
                lines.extend(self.emit(child, depth + 1))
                if space_between and i < len(children) - 1:
                    lines.append(f"{INDENT * (depth + 1)}Spacer()")
            lines.append(f"{ind}}}")

        lines.extend(self._modifiers(node, depth))
        return lines

    def _counter_align(self, node: dict, axis: str) -> str:
        counter = node.get("counterAxisAlignItems", "MIN")
        if axis == "h":  # HStack vertical alignment
            return {"MIN": ".top", "CENTER": ".center", "MAX": ".bottom"}.get(counter, ".center")
        return {"MIN": ".leading", "CENTER": ".center", "MAX": ".trailing"}.get(counter, ".leading")

    # --- text ---
    def _emit_text(self, node: dict, depth: int) -> list[str]:
        ind = INDENT * depth
        text = (node.get("characters") or "").replace("\\", "\\\\").replace('"', '\\"')
        text = text.replace("\n", "\\n")
        lines = [f'{ind}Text("{text}")']

        style = node.get("style", {}) or {}
        size = round(style.get("fontSize", 17))
        weight = font_weight(style.get("fontWeight"))
        lines.append(f"{ind}{INDENT}.font(.system(size: {size}, weight: {weight}))")
        self.t.add_text_style(style)

        fill = first_solid_fill(node)
        if fill:
            hexv = self.t.add_color(fill["color"])
            opacity = fill.get("opacity", 1)
            lines.append(f"{ind}{INDENT}.foregroundColor({self._color_ref(hexv, opacity)})")

        align = style.get("textAlignHorizontal")
        if align in {"CENTER", "RIGHT", "JUSTIFIED"}:
            mapping = {"CENTER": ".center", "RIGHT": ".trailing", "JUSTIFIED": ".leading"}
            lines.append(f"{ind}{INDENT}.multilineTextAlignment({mapping[align]})")

        if style.get("lineHeightPx"):
            lines.append(f"{ind}{INDENT}// line height ~{round(style['lineHeightPx'])}pt "
                         f"(use .lineSpacing if needed)")
        return lines

    # --- shapes ---
    def _emit_shape(self, node: dict, depth: int) -> list[str]:
        ind = INDENT * depth
        radius = node.get("cornerRadius", 0)
        if node.get("type") == "ELLIPSE":
            shape = "Ellipse()"
        elif radius:
            shape = f"RoundedRectangle(cornerRadius: {round(radius)})"
        else:
            shape = "Rectangle()"

        lines = []
        if self._looks_like_input(node):
            lines.append(f"{ind}// TODO[input]: this looks like a text field — consider "
                         f"replacing the shape with a TextField/SecureField bound to state.")
        lines.append(f"{ind}{shape}")
        kind, expr = self._fill_expr(node)
        if expr:
            # .fill() takes any ShapeStyle, so solids and gradients both work.
            lines.append(f"{ind}{INDENT}.fill({expr})")
        lines.extend(self._frame_modifier(node, depth))
        lines.extend(self._stroke_shadow(node, depth))
        return lines

    # --- assets (vectors + image fills) ---
    def _emit_asset(self, node: dict, depth: int) -> list[str]:
        ind = INDENT * depth
        vector = is_vector_like(node)
        fmt = "svg" if vector else "png"
        asset = self.t.add_asset(node, fmt)
        lines = [f'{ind}Image("{asset}")']
        # Single-color vector icons are best shipped as template images so the tint
        # comes from the design token rather than being baked into the asset.
        tint = None
        if vector:
            fill = first_solid_fill(node)
            if fill:
                hexv = self.t.add_color(fill["color"])
                tint = self._color_ref(hexv, fill.get("opacity", 1))
                lines.append(f"{ind}{INDENT}.renderingMode(.template)")
        lines.append(f"{ind}{INDENT}.resizable()")
        # Vector icons scale to fit; photo/image fills usually fill their frame.
        lines.append(f"{ind}{INDENT}{'.scaledToFit()' if vector else '.scaledToFill()'}")
        if tint:
            lines.append(f"{ind}{INDENT}.foregroundColor({tint})")
        lines.extend(self._frame_modifier(node, depth))
        # Clip image fills to the shape they were painted into so avatars stay round
        # and rounded thumbnails stay rounded.
        if not vector:
            if node.get("type") == "ELLIPSE":
                lines.append(f"{ind}{INDENT}.clipShape(Circle())")
            elif node.get("cornerRadius"):
                lines.append(f"{ind}{INDENT}.clipShape(RoundedRectangle("
                             f"cornerRadius: {round(node['cornerRadius'])}))")
            else:
                lines.append(f"{ind}{INDENT}.clipped()")
        return lines

    # --- shared modifier emission ---
    def _modifiers(self, node: dict, depth: int) -> list[str]:
        ind = INDENT * depth
        lines: list[str] = []

        # padding (Auto Layout). Collapse to .all / .vertical / .horizontal where
        # the values are symmetric — that's how a SwiftUI dev would write it by hand.
        top = round(node.get("paddingTop", 0))
        bottom = round(node.get("paddingBottom", 0))
        left = round(node.get("paddingLeft", 0))
        right = round(node.get("paddingRight", 0))
        if top or bottom or left or right:
            if top == bottom == left == right:
                lines.append(f"{ind}{INDENT}.padding({top})")
            else:
                if top == bottom and top:
                    lines.append(f"{ind}{INDENT}.padding(.vertical, {top})")
                else:
                    if top:
                        lines.append(f"{ind}{INDENT}.padding(.top, {top})")
                    if bottom:
                        lines.append(f"{ind}{INDENT}.padding(.bottom, {bottom})")
                if left == right and left:
                    lines.append(f"{ind}{INDENT}.padding(.horizontal, {left})")
                else:
                    if left:
                        lines.append(f"{ind}{INDENT}.padding(.leading, {left})")
                    if right:
                        lines.append(f"{ind}{INDENT}.padding(.trailing, {right})")

        # background fill for containers (solid or gradient)
        kind, bg = self._fill_expr(node)
        if bg and node.get("type") in {"FRAME", "COMPONENT", "INSTANCE", "GROUP", "COMPONENT_SET"}:
            radius = node.get("cornerRadius", 0)
            if radius:
                lines.append(f"{ind}{INDENT}.background({bg}.cornerRadius({round(radius)}))")
            else:
                lines.append(f"{ind}{INDENT}.background({bg})")
        elif node.get("cornerRadius"):
            lines.append(f"{ind}{INDENT}.cornerRadius({round(node['cornerRadius'])})")

        lines.extend(self._frame_modifier(node, depth))
        lines.extend(self._stroke_shadow(node, depth))

        if node.get("opacity", 1) < 1:
            lines.append(f"{ind}{INDENT}.opacity({round(node['opacity'], 3)})")
        return lines

    def _frame_modifier(self, node: dict, depth: int) -> list[str]:
        ind = INDENT * depth
        box = node.get("absoluteBoundingBox") or {}
        w, h = box.get("width"), box.get("height")
        # Only pin sizes the designer marked FIXED; let HUG/FILL flow naturally.
        hz = node.get("layoutSizingHorizontal")
        vt = node.get("layoutSizingVertical")
        parts = []
        if w and (hz == "FIXED" or hz is None and node.get("type") in {"RECTANGLE", "ELLIPSE", "VECTOR"}):
            parts.append(f"width: {round(w)}")
        if h and (vt == "FIXED" or vt is None and node.get("type") in {"RECTANGLE", "ELLIPSE", "VECTOR"}):
            parts.append(f"height: {round(h)}")
        if parts:
            return [f"{ind}{INDENT}.frame({', '.join(parts)})"]
        return []

    def _stroke_shadow(self, node: dict, depth: int) -> list[str]:
        ind = INDENT * depth
        lines: list[str] = []
        strokes = node.get("strokes") or []
        if strokes and strokes[0].get("type") == "SOLID":
            hexv = self.t.add_color(strokes[0]["color"])
            weight = round(node.get("strokeWeight", 1))
            radius = round(node.get("cornerRadius", 0))
            shape = f"RoundedRectangle(cornerRadius: {radius})" if radius else "Rectangle()"
            lines.append(
                f"{ind}{INDENT}.overlay({shape}.stroke({self._color_ref(hexv)}, lineWidth: {weight}))"
            )
        for effect in node.get("effects", []) or []:
            if effect.get("type") == "DROP_SHADOW" and effect.get("visible", True):
                c = effect.get("color", {})
                radius = round(effect.get("radius", 0))
                off = effect.get("offset", {})
                lines.append(
                    f"{ind}{INDENT}.shadow(color: {color_literal(c)}, radius: {radius}, "
                    f"x: {round(off.get('x', 0))}, y: {round(off.get('y', 0))})"
                )
        return lines

    def _looks_like_button(self, node: dict) -> bool:
        if node.get("type") not in {"FRAME", "INSTANCE", "COMPONENT"}:
            return False
        name = (node.get("name") or "").lower()
        if any(k in name for k in ("button", "btn", "cta")):
            return True
        children = [c for c in node.get("children", []) if c.get("visible", True)]
        texts = [c for c in children if c.get("type") == "TEXT"]
        has_fill = bool(self._fill_expr(node)[1])
        # A small pill with a fill, rounded corners and (mostly) just a label.
        return bool(has_fill and node.get("cornerRadius", 0) and texts and len(children) <= 2)

    @staticmethod
    def _looks_like_input(node: dict) -> bool:
        name = (node.get("name") or "").lower()
        if any(k in name for k in ("field", "input", "search", "email", "password", "textbox")):
            return True
        # A standalone bordered, rounded rectangle is usually an input affordance.
        return bool(node.get("type") == "RECTANGLE" and node.get("cornerRadius", 0)
                    and node.get("strokes"))

    def _fill_expr(self, node: dict) -> tuple[str | None, str | None]:
        """Return ('solid'|'gradient', swift-expression) for the first visible fill."""
        for fill in node.get("fills", []) or []:
            if not fill.get("visible", True):
                continue
            ftype = fill.get("type")
            if ftype == "SOLID":
                hexv = self.t.add_color(fill["color"])
                return "solid", self._color_ref(hexv, fill.get("opacity", 1))
            if ftype in {"GRADIENT_LINEAR", "GRADIENT_RADIAL"}:
                stops = fill.get("gradientStops", []) or []
                colors = ", ".join(color_literal(s["color"]) for s in stops) or "Color.clear"
                if ftype == "GRADIENT_LINEAR":
                    return ("gradient",
                            f"LinearGradient(gradient: Gradient(colors: [{colors}]), "
                            f"startPoint: .top, endPoint: .bottom)")
                return ("gradient",
                        f"RadialGradient(gradient: Gradient(colors: [{colors}]), "
                        f"center: .center, startRadius: 0, endRadius: 200)")
        return None, None

    def _color_ref(self, hexv: str, opacity: float = 1.0) -> str:
        name = self.t.color_name(hexv)
        if opacity < 1:
            return f"Theme.{name}.opacity({round(opacity, 3)})"
        return f"Theme.{name}"


# --------------------------------------------------------------------------- #
# Top-level file generation
# --------------------------------------------------------------------------- #
def build_view_file(node: dict, tokens: TokenRegistry) -> tuple[str, str]:
    view_name = pascal_case(node.get("name", "Generated")) + "View"
    emitter = SwiftUIEmitter(tokens)
    body = emitter.emit(node, depth=3)

    header = (
        f"// {view_name}.swift\n"
        f"// Generated from Figma node '{node.get('name')}' (id {node.get('id')}).\n"
        f"// Review // TODO markers and wire up data/actions before shipping.\n\n"
        f"import SwiftUI\n\n"
        f"struct {view_name}: View {{\n"
        f"{INDENT}var body: some View {{\n"
    )
    footer = (
        f"{INDENT}}}\n}}\n\n"
        f"#Preview {{\n{INDENT}{view_name}()\n}}\n"
    )
    return view_name, header + "\n".join(body) + "\n" + footer


def variant_case_name(child_name: str) -> str:
    """'State=Primary, Size=Large' -> 'primaryLarge'; 'Secondary' -> 'secondary'."""
    parts = []
    for seg in (child_name or "").split(","):
        seg = seg.strip()
        val = seg.split("=", 1)[1] if "=" in seg else seg
        parts.append(val.strip())
    name = pascal_case(" ".join(p for p in parts if p)) or "Default"
    return name[:1].lower() + name[1:]


def build_component_set_file(node: dict, tokens: TokenRegistry) -> tuple[str, str]:
    """A Figma COMPONENT_SET becomes ONE view with a Variant enum + switch, rather
    than N near-duplicate structs. This is how a SwiftUI dev models design-system
    components (e.g. Button with .primary/.secondary styles)."""
    base = pascal_case(node.get("name", "Component"))
    view_name = base + "View"
    emitter = SwiftUIEmitter(tokens)

    variants = [c for c in node.get("children", [])
                if c.get("type") in {"COMPONENT", "FRAME", "INSTANCE"} and c.get("visible", True)]

    cases: list[tuple[str, dict]] = []
    seen: dict[str, int] = {}
    for v in variants:
        cname = variant_case_name(v.get("name", ""))
        if cname in seen:
            seen[cname] += 1
            cname = f"{cname}{seen[cname]}"
        else:
            seen[cname] = 0
        cases.append((cname, v))

    case_list = ", ".join(c for c, _ in cases) or "default"
    default_case = cases[0][0] if cases else "default"

    out = [
        f"// {view_name}.swift",
        f"// Generated from Figma component set '{node.get('name')}' (id {node.get('id')}).",
        f"// Each Figma variant maps to a case of Variant. Wire actions/data per variant.",
        "",
        "import SwiftUI",
        "",
        f"struct {view_name}: View {{",
        f"{INDENT}enum Variant {{ case {case_list} }}",
        f"{INDENT}var variant: Variant = .{default_case}",
        "",
        f"{INDENT}var body: some View {{",
        f"{INDENT*2}switch variant {{",
    ]
    for cname, _ in cases:
        out.append(f"{INDENT*2}case .{cname}: {cname}Body")
    out += [f"{INDENT*2}}}", f"{INDENT}}}", ""]

    for cname, v in cases:
        out.append(f"{INDENT}@ViewBuilder private var {cname}Body: some View {{")
        out.extend(emitter.emit(v, depth=2))
        out.append(f"{INDENT}}}")
        out.append("")

    out += ["}", "", "#Preview {", f"{INDENT}{view_name}()", "}", ""]
    return view_name, "\n".join(out)


def build_tokens_file(tokens: TokenRegistry) -> str:
    lines = [
        "// DesignTokens.swift",
        "// Colors and text styles extracted from the Figma design.",
        "// Reuse these instead of hard-coding values so the UI stays consistent.",
        "",
        "import SwiftUI",
        "",
        "enum Theme {",
    ]
    for hexv, c in sorted(tokens.colors.items()):
        name = tokens.color_name(hexv)
        lines.append(f"{INDENT}/// {hexv}")
        lines.append(f"{INDENT}static let {name} = {color_literal(c)}")
    lines.append("}")
    lines.append("")
    lines.append("extension Font {")
    for key, style in sorted(tokens.text_styles.items()):
        size = round(style.get("fontSize", 17))
        weight = font_weight(style.get("fontWeight"))
        fname = f"style{key.replace('_', 'w')}"
        lines.append(f"{INDENT}static let {fname} = Font.system(size: {size}, weight: {weight})")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def build_assets_manifest(tokens: TokenRegistry, downloaded: dict[str, str]) -> str:
    lines = [
        "# Asset manifest",
        "",
        "Add these to `Assets.xcassets` (SVGs: enable *Preserve Vector Data*).",
        "Image names below match the `Image(\"...\")` references in the generated views.",
        "",
        "| Asset name | Figma node id | Format | Downloaded file |",
        "| --- | --- | --- | --- |",
    ]
    for nid, info in tokens.assets.items():
        path = downloaded.get(nid, "(run with --export-assets)")
        lines.append(f"| {info['name']} | {nid} | {info['fmt']} | {path} |")
    if not tokens.assets:
        lines.append("| _none_ | | | |")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Tree loading + traversal entry points
# --------------------------------------------------------------------------- #
def extract_target_nodes(doc: dict, node_id: str | None) -> list[dict]:
    """Return the list of top-level frames/components to generate from."""
    # /v1/files/.../nodes response
    if "nodes" in doc:
        return [v["document"] for v in doc["nodes"].values() if v.get("document")]
    # full /v1/files response — find the requested node or top-level frames on page 1
    document = doc.get("document", doc)
    if node_id:
        found = _find_node(document, node_id)
        if found:
            return [found]
    # default: first canvas's direct children that are frames/components
    for canvas in document.get("children", []):
        if canvas.get("type") == "CANVAS":
            frames = [c for c in canvas.get("children", [])
                      if c.get("type") in {"FRAME", "COMPONENT", "COMPONENT_SET"}]
            if frames:
                return frames
    return [document]


def _find_node(node: dict, node_id: str) -> dict | None:
    if node.get("id") == node_id:
        return node
    for child in node.get("children", []) or []:
        hit = _find_node(child, node_id)
        if hit:
            return hit
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert a Figma design into SwiftUI views.")
    ap.add_argument("url", nargs="?", help="Figma file/design URL (contains key and node-id)")
    ap.add_argument("--file-key", help="Figma file key (if not passing a URL)")
    ap.add_argument("--node-id", help="Node id like 12:34 (optional; defaults to top frames)")
    ap.add_argument("--token", help="Figma token (else uses FIGMA_TOKEN env var)")
    ap.add_argument("--from-json", help="Load a saved Figma JSON response instead of calling the API")
    ap.add_argument("--out", default="./Generated", help="Output directory")
    ap.add_argument("--export-assets", action="store_true",
                    help="Download rendered vectors/images via the Figma image API")
    ap.add_argument("--scale", type=float, default=2.0, help="PNG export scale (default 2x)")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)

    # 1. Load the tree -----------------------------------------------------
    file_key = args.file_key
    node_id = args.node_id
    client: FigmaClient | None = None

    if args.from_json:
        with open(args.from_json, "r", encoding="utf-8") as f:
            doc = json.load(f)
    else:
        if args.url:
            file_key, url_node = parse_figma_url(args.url)
            node_id = node_id or url_node
        if not file_key:
            print("error: provide a Figma URL, or --file-key (or use --from-json).", file=sys.stderr)
            return 2
        try:
            client = FigmaClient(args.token)
            doc = client.get_nodes(file_key, [node_id]) if node_id else client.get_file(file_key)
        except FigmaError as e:
            print(f"error: {e}", file=sys.stderr)
            return 1

    targets = extract_target_nodes(doc, node_id)
    if not targets:
        print("error: no frames/components found to generate from.", file=sys.stderr)
        return 1

    # 2. Generate views + collect tokens/assets ---------------------------
    tokens = TokenRegistry()
    written: list[str] = []
    for node in targets:
        if node.get("type") == "COMPONENT_SET":
            view_name, content = build_component_set_file(node, tokens)
        else:
            view_name, content = build_view_file(node, tokens)
        path = os.path.join(args.out, f"{view_name}.swift")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        written.append(path)

    # 3. Tokens + asset manifest ------------------------------------------
    with open(os.path.join(args.out, "DesignTokens.swift"), "w", encoding="utf-8") as f:
        f.write(build_tokens_file(tokens))
    written.append(os.path.join(args.out, "DesignTokens.swift"))

    # 4. Optionally export assets -----------------------------------------
    downloaded: dict[str, str] = {}
    if args.export_assets and tokens.assets and client and file_key:
        assets_dir = os.path.join(args.out, "Assets")
        os.makedirs(assets_dir, exist_ok=True)
        for fmt in {"svg", "png"}:
            ids = [nid for nid, info in tokens.assets.items() if info["fmt"] == fmt]
            if not ids:
                continue
            urls = client.get_image_urls(file_key, ids, fmt=fmt, scale=args.scale)
            for nid, url in urls.items():
                if not url:
                    continue
                fname = f"{tokens.assets[nid]['name']}.{fmt}"
                dest = os.path.join(assets_dir, fname)
                try:
                    client.download(url, dest)
                    downloaded[nid] = os.path.relpath(dest, args.out)
                except Exception as e:  # noqa: BLE001
                    print(f"warning: failed to download asset {nid}: {e}", file=sys.stderr)

    with open(os.path.join(args.out, "Assets.md"), "w", encoding="utf-8") as f:
        f.write(build_assets_manifest(tokens, downloaded))
    written.append(os.path.join(args.out, "Assets.md"))

    # Dump the IR for debugging / inspection
    with open(os.path.join(args.out, "figma_ir.json"), "w", encoding="utf-8") as f:
        json.dump({"targets": [t.get("name") for t in targets],
                   "colors": list(tokens.colors.keys()),
                   "assets": tokens.assets}, f, indent=2)

    # 5. Summary -----------------------------------------------------------
    print("Generated SwiftUI from Figma:")
    for p in written:
        print(f"  - {p}")
    print(f"  colors: {len(tokens.colors)}  text styles: {len(tokens.text_styles)}  "
          f"assets: {len(tokens.assets)}")
    if tokens.assets and not args.export_assets:
        print("  (re-run with --export-assets to download the images/icons)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
