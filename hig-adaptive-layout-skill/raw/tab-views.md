# Tab views
URL: https://developer.apple.com/design/human-interface-guidelines/tab-views

A tab view presents multiple mutually exclusive panes of content in the same area, switched using a tabbed control.

## Best practices
- Use a tab view to present closely related areas of content.
- Provide a descriptive label for each tab (nouns/short noun phrases, title-style capitalization).
- Avoid using a pop-up button to switch between tabs (unless too many panes for tabs).
- Avoid providing more than six tabs — more can be overwhelming and create layout issues.

## Anatomy
The tabbed control appears on the top edge of the content area. You can hide the control (for programmatic switching). In general, inset a tab view by leaving a margin of window-body area on all sides; you can extend it to the window edges but this is unusual.

## Platform considerations
Not supported in iOS, iPadOS, tvOS, or visionOS. (This is a macOS component.)
- iOS, iPadOS: for similar functionality, consider using a segmented control instead.
- watchOS: displays tab views using page controls.

Resources: Tab bars, Segmented controls. Developer: NSTabView (AppKit), TabView (SwiftUI).
