# Boxes
URL: https://developer.apple.com/design/human-interface-guidelines/boxes

A box creates a visually distinct group of logically related information and components (visible border or background color; can include a title).

## Best practices
- Prefer keeping a box relatively small compared with its containing view. As a box's size approaches the containing window or screen, it becomes less effective at communicating separation and can crowd other content.
- Consider using padding and alignment to communicate additional grouping within a box (avoid nested boxes).

## Platform considerations
No additional considerations for visionOS. Not supported in tvOS or watchOS.
- iOS, iPadOS: by default use the secondary and tertiary background colors in boxes.
- macOS: by default displays a box's title above it.

Resources: Layout. Developer: GroupBox (SwiftUI), NSBox (AppKit).
