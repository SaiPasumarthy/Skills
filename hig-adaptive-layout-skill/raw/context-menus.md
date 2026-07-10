# Context menus
URL: https://developer.apple.com/design/human-interface-guidelines/context-menus
A context menu provides access to functionality directly related to an item without cluttering the interface. Revealed by the touch/pinch-and-hold gesture (visionOS, iOS, iPadOS), Control-click or secondary click (macOS, iPadOS). Hidden by default.

Best practices: prioritize relevancy; aim for a small number of items; support context menus consistently; always make context-menu items available in the main interface too; keep submenus to one level; hide unavailable items (don't dim them); place the most frequently used items where people encounter them first (a menu might open above or below the content, so reverse item order to match); show keyboard shortcuts in main menus, not context menus. In iOS/iPadOS/visionOS, warn about destructive items (list at end, mark destructive).

## Platform considerations
No additional considerations for tvOS. Not supported in watchOS.
### iOS, iPadOS
Provide either a context menu or an edit menu for an item, but not both. In iPadOS, consider a context menu to let people create a new object (e.g. Files new folder). A context menu can display a preview of the current content near the list of commands.
### macOS
Sometimes called a contextual menu.
### visionOS (out of scope, noted)
Consider a context menu instead of a panel/inspector window; avoid letting its height exceed the window height.

Resources: Menus, Edit menus, Pop-up buttons, Pull-down buttons. Developer: contextMenu (SwiftUI), UIContextMenuInteraction (UIKit).
