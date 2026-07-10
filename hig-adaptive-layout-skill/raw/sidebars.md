# Sidebars
URL: https://developer.apple.com/design/human-interface-guidelines/sidebars

A sidebar appears on the leading side of a view and lets people navigate between areas of your app or top-level collections of content. A sidebar requires a large amount of vertical and horizontal space. When space is limited, a more compact control such as a tab bar may provide a better navigation experience. For many apps you don't need to choose — you can adopt a style of tab bar that provides both. See Tab bars and Layout.

## Best practices
- Extend visually rich content beneath the sidebar. In iOS, iPadOS, and macOS, sidebars can float above content in the Liquid Glass layer. Extend content beneath the sidebar by letting it horizontally scroll or by applying a background extension effect (mirrors adjacent content to give the impression of stretching under the sidebar). Developer: backgroundExtensionEffect().
- When possible, let people customize the contents of a sidebar.
- Group hierarchy with disclosure controls if your app has a lot of content, to keep vertical space manageable.
- Consider using familiar SF Symbols to represent items.
- Consider letting people hide the sidebar. Use platform-specific interactions: in iPadOS people expect the built-in edge swipe gesture; in macOS include a show/hide button or Show/Hide Sidebar commands in the View menu; in visionOS a window typically expands to accommodate a sidebar so people rarely need to hide it. Avoid hiding the sidebar by default.
- In general, show no more than two levels of hierarchy in a sidebar. When deeper, consider a split view with a content list between the sidebar items and detail view.

## Platform considerations
No additional considerations for tvOS. Not supported in watchOS.

### iOS, iPadOS
When you use the **sidebarAdaptable** style of tab view to present a sidebar, you choose whether to display a sidebar or a tab bar when your app opens. Both variations include a button to switch between them. This style adapts its appearance depending on the platform, and **responds automatically to rotation and window resizing**, providing a version of the control appropriate to the width of the view.
- To display a sidebar only, use NavigationSplitView or UISplitViewController.
- Consider using a tab bar first — it provides more space to feature content. If you need more areas than fit in a tab bar, the tab bar's convertible sidebar-style appearance can provide access to less-frequently-used content.

### macOS
A sidebar's row height, text, and glyph size depend on its overall size (small/medium/large), set programmatically or by the person in General settings.
- Consider automatically hiding and revealing a sidebar when its container window resizes (e.g. reducing a Mail viewer window can collapse its sidebar to make room for message content).
- Avoid putting critical information or actions at the bottom of a sidebar.

### visionOS (out of scope, noted)
If the hierarchy is deep, consider using a sidebar within a tab in a tab bar.

Resources: Split views, Tab bars, Layout. Developer: sidebarAdaptable (SwiftUI), NavigationSplitView (SwiftUI), UICollectionLayoutListConfiguration (UIKit).
Change log: June 8, 2026 — updated sidebar icon colors and clarified the adaptable sidebar style. June 9, 2025 — added guidance for extending content beneath the sidebar. Aug 6, 2024 — SwiftUI adaptable sidebar style.
