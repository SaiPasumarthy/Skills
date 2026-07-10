# Scroll views
URL: https://developer.apple.com/design/human-interface-guidelines/scroll-views

A scroll view lets people view content larger than the view's boundaries by moving it vertically or horizontally. Displays a translucent scroll indicator showing whether visible content is near the beginning, middle, or end.

## Best practices
- Support default scrolling gestures and keyboard shortcuts; custom scrolling should use the elastic behavior people expect.
- Make it apparent when content is scrollable (e.g. display partial content at the edge of a view to indicate more content).
- Avoid putting a scroll view inside another scroll view with the same orientation. It's fine to place a horizontal scroll view inside a vertical scroll view (or vice versa).
- Consider supporting page-by-page scrolling. Developer: PagingScrollTargetBehavior.
- Scroll automatically to help people find their place when relevant content is no longer in view.
- If you support zoom, set appropriate maximum and minimum scale values.

## Scroll edge effects (iOS, iPadOS, macOS — KEY LAYOUT DETAIL)
A scroll edge effect provides a visual separation between certain interface elements (such as toolbars) and the scrolling content area behind them. If you use custom bars, add this effect manually if the top layer needs extra clarity, or adjust its style from automatic to the hard or soft style.
- Prefer the automatic scroll edge effect style. Provides a more opaque visual separation for top toolbars with many controls, text outside Liquid Glass controls, and pinned table headers.
- Only use a scroll edge effect when a scroll view is behind floating interface elements. They aren't decorative.
- Apply one scroll edge effect per view. In split view layouts on iPad and Mac, each pane can have its own scroll edge effect — keep them consistent in height to maintain alignment.
- Developer: ScrollEdgeEffectStyle, UIScrollEdgeEffect.Style, NSScrollEdgeEffectStyle.

## Platform considerations
### iOS, iPadOS
Consider showing a page control when a scroll view is in page-by-page mode (e.g. Weather). If you show a page control with a scroll view, don't show the scrolling indicator on the same axis to avoid redundant controls.

### macOS
A scroll indicator is commonly called a scroll bar. Use small or mini scroll bars in a panel when space is tight.

### tvOS / visionOS / watchOS (out of scope, noted)
tvOS: system auto-scrolls to keep focused items visible. visionOS: fixed small scroll indicator, Look to Scroll (eye scrolling). watchOS: Digital Crown scrolling, tab views for page-by-page.

Resources: Page controls, Gestures, Pointing devices. Developer: ScrollView (SwiftUI), UIScrollView (UIKit), NSScrollView (AppKit).
Change log: June 8, 2026 / July 28, 2025 — scroll edge effects guidance.
