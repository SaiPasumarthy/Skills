---
name: figma-to-swiftui
description: >-
  Convert a Figma design into production-ready SwiftUI (iOS/macOS) code by calling
  the Figma REST API directly. Use whenever the user points at a Figma source
  (file/frame URL, or file key + node id) AND wants SwiftUI / iOS output: e.g.
  "implement this Figma design in SwiftUI", "turn this Figma frame into iOS code",
  "build this screen from the mockup", "code up our design-system component", or
  "generate SwiftUI views + design tokens from this Figma file" — even if they only
  paste a figma.com link with SwiftUI/iOS intent implied. It runs bundled stdlib
  Python that extracts layout, color/type tokens, components/variants, and assets,
  then emits SwiftUI views plus a DesignTokens file; prefer it over eyeballing a
  screenshot. Do NOT use for non-Figma sources (Sketch, screenshot, "from scratch")
  or non-SwiftUI targets (React, web, Android/Compose).
---

# Figma → SwiftUI

This skill turns a Figma frame or component into SwiftUI source files by talking to
the **Figma REST API** with plain Python from the standard library and generating
code deterministically.

## When to use

Trigger this whenever someone wants Figma turned into SwiftUI: a shared design
URL, a file key + node id, "implement this screen", "build the login view from
the mockup", "generate views from our design system frame", etc.

## Prerequisites (check first)

1. **A Figma personal access token** in the `FIGMA_TOKEN` environment variable.
   Create it at Figma → Settings → Security → Personal access tokens (needs
   *File content* read scope). If it's missing, ask the user to export it:
   `export FIGMA_TOKEN=figd_xxx`. Never print or commit the token.
2. **What to convert** — a Figma URL (preferred; it carries the file key and
   `node-id`) or an explicit `--file-key` + `--node-id`. If the user gives only a
   file, you'll generate from the top-level frames on the first page.

## Workflow

Run everything from the skill's `scripts/` directory.

1. **Identify the target.** If you have a URL, pass it straight through — the
   script extracts the file key and node id. Confirm with the user which
   frame/screen they want if the URL points at a whole file.

2. **Generate.**
   ```bash
   python scripts/figma_to_swiftui.py "<figma-url>" --out ./Generated --export-assets
   ```
   or, without a URL:
   ```bash
   python scripts/figma_to_swiftui.py --file-key <KEY> --node-id 12:34 --out ./Generated --export-assets
   ```
   This writes, into `./Generated/`:
   - `<Name>View.swift` — one SwiftUI `View` per top-level frame/component
   - `DesignTokens.swift` — `Theme` colors + `Font` styles pulled from the design
   - `Assets.md` — manifest of icons/images to add to `Assets.xcassets`
   - `Assets/` — the downloaded SVG/PNG files (with `--export-assets`)
   - `figma_ir.json` — the normalized tree, for debugging

3. **Review and finish the code.** The generator handles layout, paint (solid +
   gradient), text, clipped/circular image fills, and component-set variants, but
   deliberately leaves `// TODO` markers where human judgment is needed. It tags
   `// TODO[button]:` on frames that read as buttons (wrap in `Button {}` + action)
   and `// TODO[input]:` on rounded bordered rectangles that read as inputs (swap
   for `TextField`/`SecureField`). Also promote literal strings to bindings and
   finish anything the script couldn't map (masks, blend modes, complex vectors).
   Open each generated view, resolve the TODOs, and read `references/mapping.md`
   for the conventions to apply.

4. **Integrate.** Drop the `.swift` files into the Xcode project, add the exported
   assets to `Assets.xcassets` (enable *Preserve Vector Data* for SVGs), and build.
   Each view ships with a `#Preview` so it renders in the canvas immediately.

## Offline / dry run

To validate the pipeline without a token (e.g. to show the user the shape of the
output), run against a saved Figma JSON response:
```bash
python scripts/figma_to_swiftui.py --from-json assets/sample_login_card.json --out ./Generated
```

## Bundled resources

- `scripts/figma_client.py` — Figma REST client (auth, file/nodes, image export).
  Stdlib only; runs anywhere with Python 3, no `pip install`.
- `scripts/figma_to_swiftui.py` — fetch → normalize → emit SwiftUI. The CLI entry.
- `references/figma-api.md` — the REST endpoints, auth, and node fields used. Read
  this when the API behaves unexpectedly or you need a field the script doesn't map.
- `references/mapping.md` — exact Figma→SwiftUI translation rules. Read this before
  hand-finishing generated views so your edits match the generator's conventions.
- `assets/sample_login_card.json` — a sample API response for offline testing.

## Notes

- The script never hard-codes colors inline; it registers every color as a
  `Theme.colorXXXXXX` token so the UI stays consistent and easy to retheme.
- Auto Layout maps cleanly to stacks; non-Auto-Layout frames fall back to `ZStack`
  so nothing is dropped, but the result is worth tidying by hand.
- Prefer converting a Figma **component** once and reusing it over re-emitting every
  instance — see the components/variants section of `references/mapping.md`.
- Single-color vector icons are emitted as `.renderingMode(.template)` images tinted
  from a design token, so the icon color stays in the token system.

## Roadmap

This skill targets **SwiftUI first**. The pipeline is intentionally split into a
Figma fetch/normalize stage and a SwiftUI emit stage so additional targets —
**Android (Jetpack Compose)** and **React** — can be added later as alternate
emitters over the same extracted data, without changing how the design is fetched.
