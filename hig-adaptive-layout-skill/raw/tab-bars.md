# Tab bars
URL: https://developer.apple.com/design/human-interface-guidelines/tab-bars

A tab bar lets people navigate between top-level sections of your app while preserving the current navigation state within each section.

## Best practices
- Use a tab bar to support navigation, not to provide actions (use a toolbar for actions on the current view).
- Make sure the tab bar is visible when people navigate to different sections (exception: a modal view covering it).
- Use the appropriate number of tabs; fewer is easier to navigate. For a complex information structure, consider a sidebar or a tab bar that adapts to a sidebar.
- **Avoid overflow tabs.** Depending on device size and orientation, the number of visible tabs can be smaller than the total. If horizontal space limits the number of visible tabs, the trailing tab becomes a **More** tab in iOS and iPadOS, revealing remaining items in a separate list. The More tab makes hidden content harder to reach, so limit scenarios where this happens.
- Don't disable or hide tab bar buttons, even when content is unavailable.
- Include tab labels (single words where possible).
- Consider SF Symbols for familiar, scalable icons. Tab bar icons automatically adapt to different contexts: the tab bar can be **regular or compact depending on device and orientation**. Tab bar icons appear ABOVE labels in compact views, whereas in regular views the icons and labels appear SIDE BY SIDE.
- Use a badge for critical information.

## Platform considerations
No additional considerations for macOS. Not supported in watchOS.

### iOS
A tab bar floats above content at the bottom of the screen, items resting on a Liquid Glass background. For tab bars with an attached accessory (like MiniPlayer in Music), you can minimize the tab bar and move the accessory inline when a person scrolls down. A tab bar can include a dedicated search tab at the trailing end.

### iPadOS
The system displays a tab bar near the **top** of the screen. You can have it appear as a fixed element, or with a button that converts it to a sidebar. Developer: tabBarOnly and sidebarAdaptable.
- To present a sidebar WITHOUT the option to convert to a tab bar, use a navigation split view instead of a tab view.
- Prefer a tab bar for navigation. If more complex, provide the option to convert the tab bar to a sidebar for a wider set of navigation options.
- Let people customize the tab bar. If you let people select their own tabs, aim for a default list of five or fewer to preserve continuity between compact and regular view sizes. Developer: TabViewCustomization, UITab.Placement.

### tvOS / visionOS (out of scope, noted)
tvOS: highly customizable, height 68 pt, top edge 46 pt from top. visionOS: always vertical, fixed relative to the window's leading side; expands when looked at.

Resources: Tab views, Toolbars, Sidebars, Materials. Developer: TabView (SwiftUI), UITabBar (UIKit), Elevating your iPad app with a tab bar and sidebar.
Change log: June 8, 2026 — updated terminology and art. Aug 6, 2024 — guidance for the tab bar in iPadOS 18.
