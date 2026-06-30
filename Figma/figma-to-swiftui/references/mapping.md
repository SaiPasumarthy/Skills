# Figma → SwiftUI mapping rules

These are the conventions the generator follows and the ones you should apply when
hand-finishing the output. The goal is SwiftUI a senior iOS engineer would accept
in review — Auto Layout, design tokens, no magic numbers where a token exists.

## Containers / layout

| Figma | SwiftUI |
| --- | --- |
| Frame, `layoutMode: VERTICAL` | `VStack(alignment:, spacing: itemSpacing)` |
| Frame, `layoutMode: HORIZONTAL` | `HStack(alignment:, spacing: itemSpacing)` |
| Frame, `layoutMode: NONE` / Group | `ZStack` (absolute layout preserved) |
| `paddingTop/Bottom/Left/Right` | `.padding(.vertical/.horizontal/edge, n)` |
| `counterAxisAlignItems` | stack `alignment:` (MIN→leading/top, CENTER, MAX→trailing/bottom) |
| `primaryAxisAlignItems: SPACE_BETWEEN` | insert `Spacer()` between children |
| `layoutSizingHorizontal: FIXED` | `.frame(width:)` — HUG/FILL are left to flow |

## Leaves

| Figma | SwiftUI |
| --- | --- |
| TEXT | `Text("…")` + `.font(.system(size:weight:))` + `.foregroundColor` |
| RECTANGLE (cornerRadius>0) | `RoundedRectangle(cornerRadius:)` |
| RECTANGLE/ELLIPSE | `Rectangle()` / `Ellipse()` |
| VECTOR / BOOLEAN_OPERATION / icon | `Image("AssetName")` (export as SVG) |
| Fill `type: IMAGE` | `Image("AssetName")` (export as PNG @2x) |

## Paint & effects

- **Solid fill** → `.fill(...)` on shapes, `.background(...)` on containers,
  `.foregroundColor(...)` on text. Every color is registered as a `Theme.colorXXXXXX`
  token in `DesignTokens.swift` so values are reused, not duplicated.
- **Stroke** → `.overlay(RoundedRectangle(...).stroke(color, lineWidth:))`.
- **cornerRadius** on a container with a background → `.background(color.cornerRadius(n))`.
- **DROP_SHADOW** → `.shadow(color:radius:x:y:)`.
- **opacity < 1** → `.opacity(n)`.

## Components & variants

- A Figma COMPONENT/COMPONENT_SET should become a reusable SwiftUI `View` struct.
- Variants (e.g. Button/Primary, Button/Secondary) map to an `enum` style property
  on one view, or to `ViewModifier`s — don't generate near-duplicate structs.
- INSTANCE nodes reference a component; ideally render them as the component view
  with overridden text/props rather than re-emitting the whole subtree.

## Things to finish by hand (the generator marks these)

- Interactivity: buttons become styled containers, not `Button {}` — wire up actions.
- Editable fields: a styled rectangle that's clearly an input → replace with
  `TextField`/`SecureField`.
- Data binding: literal strings from the design should become `@State`/`@Binding`
  or view-model properties.
- `lineHeightPx` is emitted as a comment; convert to `.lineSpacing` if it matters.
- Gradients, blend modes, masks, and complex vectors are left as `// TODO`.
