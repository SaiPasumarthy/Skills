# Status bars
URL: https://developer.apple.com/design/human-interface-guidelines/status-bars
A status bar appears along the upper edge of the screen and displays device state (time, cellular carrier, battery). (iOS/iPadOS.)
Best practices:
- Obscure content under the status bar. By default the background is transparent, allowing content to show through — keep the status bar readable, and don't imply content behind it is interactive. Prefer a scroll edge effect to place a blurred view behind the status bar. Developer: ScrollEdgeEffectStyle, UIScrollEdgeEffect.
- Consider temporarily hiding the status bar when displaying full-screen media.
ADAPTIVE NOTE: The status bar occupies the top safe-area inset; account for it in layout (see Layout > safe areas). The status bar text color adapts (light/dark) to the content behind it.
Platform considerations: iOS, iPadOS. Developer: preferredStatusBarStyle (UIKit).
