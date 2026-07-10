# Toolbars
URL: https://developer.apple.com/design/human-interface-guidelines/toolbars

A toolbar provides convenient access to frequently used commands, controls, navigation, and search — one or more sets of controls arranged horizontally along the top or bottom edge of the view, grouped into logical sections. Contains: the title of the current view; navigation controls (back/forward, search fields); actions/bar items (buttons, menus). (A tab bar, by contrast, is specifically for navigating between areas of an app.)

## Best practices
- Choose items deliberately to avoid overcrowding. To accommodate variable view widths, define which items move to the overflow menu as the toolbar becomes narrower.
- The system automatically adds an overflow menu in macOS or iPadOS when items no longer fit. Don't add an overflow menu manually, and avoid layouts that cause toolbar items to overflow by default.
- Add a More menu to contain additional actions.
- In iPadOS and macOS apps, consider letting people customize the toolbar.
- Reduce use of toolbar backgrounds and tinted controls; use the content layer to inform color, and use a ScrollEdgeEffectStyle to distinguish the toolbar area from content.
- Prefer standard components (corner radii concentric with bar corners).
- Consider temporarily hiding toolbars for a distraction-free experience. See Going full screen.

## Titles
- Provide a useful title for each window. If titling seems redundant, leave the title area empty. Don't title windows with your app name. Keep the title under 15 characters.

## Navigation
A toolbar with navigation controls appears at the top of a window. In iOS, a navigation-specific toolbar is sometimes called a navigation bar. Use the standard Back and Close buttons.

## Actions
- Provide actions that support the main tasks. Make sure the meaning of each control is clear; prefer simple recognizable symbols. Prefer system-provided symbols without borders.
- Use the .prominent style for key actions such as Done or Submit; only one primary action, on the trailing side.

## Item groupings (KEY ADAPTIVE DETAIL)
Three locations: leading edge, center area, trailing edge.
- Leading edge: back button, show/hide sidebar, view title, document menu. Items on the leading edge aren't customizable (always available).
- Center area: common controls; view title can appear here. In macOS and iPadOS, people can add/remove/rearrange items here if you allow customization, and items in this section automatically collapse into the system-managed overflow menu when the window shrinks enough.
- Trailing edge: important items that need to remain available, inspector buttons, optional search field, the More menu, and a primary action like Done. Items on the trailing edge remain visible at all window sizes.
- Group items logically by function and frequency of use; minimize the number of groups (aim for a maximum of three). Keep consistent groupings and placement across platforms.

## Platform considerations
No additional considerations for tvOS.
### iOS
- Prioritize only the most important items for the main toolbar area; create a More menu for additional items.
- Use a large title to help people stay oriented. A large title transitions to a standard title as people scroll, and back to large when they scroll to the top. Developer: prefersLargeTitles.
### iPadOS
- Consider combining a toolbar with a tab bar. In iPadOS, a toolbar and a tab bar can coexist in the same horizontal space at the top of the view — useful for navigating between a few main app areas while keeping the full window width available for content. See Layout and Windows.
### macOS
- The toolbar resides in the frame at the top of a window, below or integrated with the title bar. Make every toolbar item available as a command in the menu bar (people can customize or hide the toolbar).
### visionOS (out of scope, noted)
Toolbar appears along the bottom edge; avoid vertical toolbars; try to prevent windows from resizing below the width of the toolbar.
### watchOS (out of scope, noted)
Toolbar buttons in top corners or along the bottom, or in the scrolling view.

Resources: Sidebars, Tab bars, Layout, Buttons, Search fields. Developer: Toolbars (SwiftUI), UIToolbar (UIKit), NSToolbar (AppKit).
Change log: June 9, 2025 — added guidance for grouping bar items and incorporated navigation bar guidance.
