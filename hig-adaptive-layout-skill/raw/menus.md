# Menus
URL: https://developer.apple.com/design/human-interface-guidelines/menus
A menu reveals its options when people interact with it — a space-efficient way to present commands. Related components: pop-up buttons, pull-down buttons, context menus, and (macOS/iPadOS) menu bar menus.

Labels: write clear, succinct labels; use title-style capitalization; remove articles to save space; append an ellipsis when the action requires more info; show unavailable items as dimmed.
Organization: list important/frequently used items first; group logically related items with separators; be mindful of menu length (divide long menus or use submenus).
Submenus: use sparingly; limit to a single level; if a submenu has more than ~5 items consider a new menu.
Toggled items: use a changeable label describing current state (Show Map/Hide Map); use a checkmark for an attribute in effect.

## Platform considerations
No additional considerations for macOS, tvOS, or watchOS.
### iOS, iPadOS (KEY ADAPTIVE DETAIL)
A menu can display items in one of three layouts:
- Small: a row of four items at the top (symbol/icon only, no label), above a list of the remaining items. Use for closely related actions that appear as a group (Bold, Italic, Underline, Strikethrough).
- Medium: a row of three items at the top (symbol/icon above a short label), above a list. Use for three important actions (e.g. Notes: Scan, Lock, Pin).
- Large (default): all items in a list.
Developer: preferredElementSize.
### visionOS (out of scope, noted)
Can use the small or large layout styles; supports a breakthrough effect so a menu stays visible over 3D content.

Resources: Pop-up buttons, Pull-down buttons, Context menus, The menu bar. Developer: Menu (SwiftUI), UIMenu (UIKit), NSMenu (AppKit).
Change log: Sept 14, 2022 — added small/medium/large menu layouts in iPadOS.
