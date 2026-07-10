# Split views
URL: https://developer.apple.com/design/human-interface-guidelines/split-views

A split view manages the presentation of multiple adjacent panes of content. Typically used to show multiple levels of your app's hierarchy at once and support navigation between them: selecting an item in the primary pane displays its contents in the secondary pane; a tertiary pane can show additional content. Commonly used to display a sidebar for navigation (leading pane = top-level items; secondary/tertiary = child collections and item details).

## Best practices
- Persistently highlight the current selection in each pane that leads to the detail view, to keep people oriented.
- Consider letting people drag and drop content between panes.

## Platform considerations

### iOS
Prefer using a split view in a **regular — not a compact — environment**. A split view needs horizontal space to display multiple panes. In a compact environment (iPhone in portrait), it's difficult to display multiple panes without wrapping or truncating content.

### iPadOS
A split view can include either two vertical panes (like Mail) or three vertical panes (like Keynote).
- Account for narrow, compact, and intermediate window widths. Since iPad windows are fluidly resizable, consider the design of a split-view layout at multiple widths. Ensure it's possible to navigate between the panes logically. See Layout. Developer: NavigationSplitView, UISplitViewController.

### macOS
You can arrange panes vertically, horizontally, or both. Dividers between panes support dragging to resize.
- Set reasonable defaults for minimum and maximum pane sizes; keep the divider visible.
- Consider letting people hide a pane when it makes sense (e.g. hide navigator/notes to allow more room for editing).
- Provide multiple ways to reveal hidden panes (toolbar button, menu command, keyboard shortcut).
- Prefer the thin divider style (one point wide) for maximum content space.

### tvOS / visionOS / watchOS (out of scope, noted)
tvOS: split view for filtering (default 1/3 primary, 2/3 secondary). visionOS: prefer a split view instead of a new window for supplementary info. watchOS: displays list or detail as full-screen.

Resources: Sidebars, Tab bars, Layout. Developer: NavigationSplitView (SwiftUI), UISplitViewController (UIKit), NSSplitViewController (AppKit).
Change log: June 9, 2025 — added iOS and iPadOS platform considerations.
