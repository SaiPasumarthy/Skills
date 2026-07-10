# Outline views
URL: https://developer.apple.com/design/human-interface-guidelines/outline-views

An outline view presents hierarchical data in a scrolling list of cells organized into columns and rows. Parent containers have disclosure triangles that expand to reveal children (e.g. Finder).

## Best practices
- Works well to display text-based content and often appears on the leading side of a split view, with related content on the opposite side.
- Use a table instead for non-hierarchical data.
- Expose data hierarchy in the first column only.
- Use descriptive column headings.
- Consider letting people click column headings to sort.
- Let people resize columns.
- Make it easy to expand/collapse nested containers; retain people's expansion choices.
- Consider alternating row colors in multi-column outline views.
- Consider a centered ellipsis to truncate cell text.
- Consider a search field for lengthy outline views.

## Platform considerations
Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS. (macOS-only component.)

Resources: Column views, Lists and tables, Split views. Developer: OutlineGroup (SwiftUI), NSOutlineView (AppKit).
