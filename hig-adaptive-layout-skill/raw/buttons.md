# Buttons
URL: https://developer.apple.com/design/human-interface-guidelines/buttons

A button initiates an instantaneous action. Combines Style, Content (symbol/label/both), and Role.

## Best practices
- Make buttons easy to use. Include enough space around a button. A button needs a **hit region of at least 44x44 pt — in visionOS, 60x60 pt** — so people can select it easily whether they use a fingertip, pointer, eyes, or remote.
- Always include a press state for a custom button.
- Use a prominent visual style for the most likely action (keep prominent buttons to one or two per view).
- Use style — not size — to visually distinguish the preferred choice.

## Roles
Normal, Primary (default; accent color; responds to Return), Cancel, Destructive (system red). Don't assign the primary role to a destructive action.

## Platform considerations
No additional considerations for tvOS.
### iOS, iPadOS
Configure a button to display an activity indicator for actions that don't instantly complete (label can change, e.g. "Checkout" → "Checking out…").
### macOS
Several button types: push buttons (standard; flexible-height for tall/variable content), square/gradient buttons (symbols only; use in a view, not the window frame), help buttons (circular, one per window), image buttons (~10 px padding between image and button edges; use in a view, not the window frame).
### visionOS (out of scope, noted)
Standard shapes: circle (icon-only), roundedRectangle/capsule (text), capsule (icon+text). Sizes: Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt. Place buttons so centers are ≥60 pt apart; prefer rounded-rectangle in a vertical stack and capsule in a horizontal row.
### watchOS (out of scope, noted)
All inline buttons use the capsule shape. Prefer full-width buttons for primary actions. Use a toolbar to place buttons in the corners (system moves time/title to accommodate).

Resources: Pop-up buttons, Pull-down buttons, Toggles, Segmented controls. Developer: Button (SwiftUI), UIButton (UIKit), NSButton (AppKit).
