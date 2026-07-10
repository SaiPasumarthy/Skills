# The menu bar
URL: https://developer.apple.com/design/human-interface-guidelines/the-menu-bar

On a Mac or an iPad, the menu bar at the top of the screen displays the top-level menus in your app. Menu bar menus on iPad are similar to those on Mac, appearing in the same order with familiar sets of menu items. Keyboard shortcuts in iPadOS use the same patterns as in macOS.

Standard menu order: YourAppName, File, Edit, Format, View, app-specific menus, Window, Help. macOS also includes the Apple menu (leading) and menu bar extras (trailing).

## Best practices
- Support the default system-defined menus and their ordering.
- Always show the same set of menu items; disable rather than hide unavailable actions.
- Prefer short, one-word menu titles (different display sizes and menu bar extras affect spacing).

## Platform considerations
Not supported in iOS, tvOS, visionOS, or watchOS.

### iPadOS (KEY ADAPTIVE DETAIL)
- People reveal the menu bar by moving the pointer to the top edge of the screen, or swiping down from it. When visible, it occupies the same vertical space as the status bar at the top edge.
- Differences iPadOS vs macOS: visibility = hidden until revealed (iPad) vs visible by default (Mac); horizontal alignment = centered (iPad) vs leading side (Mac); menu bar extras = not available on iPad; window controls = in the menu bar when the app is full screen (iPad) vs never (Mac); Apple menu = not available on iPad.
- Because the menu bar is often hidden when running full screen, ensure people can access all functions through the app's UI. Dynamic menu items are only available when a hardware keyboard is connected — always offer other ways.
- For apps with tab-style navigation, consider adding each tab as a menu item in the View menu (assign key bindings).
- Consider grouping menu items into submenus to conserve vertical space (menu item rows on iPad use more space than on Mac to be easier to tap; smaller iPad screens benefit from grouping).

### macOS
- Apple menu is always first on the leading side. Space permitting, the system displays menu bar extras at the trailing end.
- When menu bar space is constrained, the system prioritizes menus and essential extras; it may decrease space between titles, truncating if necessary. It hides menu bar extras to make room for app menus.
- In full-screen mode, the menu bar typically hides until revealed by moving the pointer to the top.
- Menu bar height is 24 pt.

Resources: Menus, Dock menus, Standard keyboard shortcuts. Developer: CommandMenu (SwiftUI), NSStatusBar (AppKit).
Change log: June 9, 2025 — added guidance for the menu bar in iPadOS.
