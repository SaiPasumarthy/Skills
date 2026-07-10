# Column views
URL: https://developer.apple.com/design/human-interface-guidelines/column-views

A column view (browser) lets people view and navigate a data hierarchy using a series of vertical columns. Each column represents one level; selecting a parent shows its children in the next column.

Note: If you need to manage hierarchical content in your iPadOS or visionOS app, consider using a split view instead.

## Best practices
- Use for deep data hierarchies where people navigate back and forth frequently and don't need sorting (e.g. Finder column view).
- Show the root level in the first column.
- Consider showing information about the selected item when there are no nested items.
- Let people resize columns.

## Platform considerations
Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS. (macOS-only component.)

Resources: Lists and tables, Outline views, Split views. Developer: NSBrowser (AppKit).
