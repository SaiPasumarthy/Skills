# Labels
URL: https://developer.apple.com/design/human-interface-guidelines/labels

A label is a static piece of text that people can read and often copy, but not edit. Labels display text throughout the interface — in buttons, menu items, and views.

## Best practices
- Use a label to display a small amount of text people don't need to edit (text field for editing; text view for large amounts).
- Prefer system fonts. A label supports **Dynamic Type** (where available) by default. If you adjust the style or use custom fonts, make sure text remains legible. (Dynamic Type support is key for adaptive layout — see Typography.)
- Use system-provided label colors to communicate relative importance (four levels: Label/primary, Secondary, Tertiary, Quaternary).
- Make useful label text selectable.

## Platform considerations
No additional considerations for iOS, iPadOS, tvOS, or visionOS.
- macOS: use isEditable property of NSTextField.
- watchOS: date/time and timer text components auto-adjust presentation to fit available space.

Resources: Text fields, Text views. Developer: Label/Text (SwiftUI), UILabel (UIKit), NSTextField (AppKit).
