# Text views
URL: https://developer.apple.com/design/human-interface-guidelines/text-views
A text view displays multiline, styled text content, optionally editable. Can be any height and allows scrolling when content extends outside the view. Content aligns to the leading edge and uses the system label color by default. In iOS, iPadOS, and visionOS, an editable text view shows a keyboard when selected.

Best practices: Use a text view for long, editable, or specially-formatted text (label or text field for small amounts). Keep text legible — adopt Dynamic Type so text still looks good if people change text size; test with accessibility options (bold text). Make useful text selectable.

Platform considerations: No additional considerations for macOS, visionOS, or watchOS. iOS, iPadOS: show the appropriate keyboard type (see Virtual keyboards).
Resources: Labels, Text fields, Combo boxes. Developer: Text (SwiftUI), UITextView (UIKit), NSTextView (AppKit).
