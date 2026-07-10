# Lists and tables
URL: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

Lists and tables present data in one or more columns of rows. Can represent grouped or hierarchical data and support selecting, adding, deleting, reordering. iOS Settings uses a hierarchy of lists; Mail in iPadOS and macOS uses a table within a split view.

## Best practices
- Prefer displaying text in a list or table. For items that vary widely in size or many images, consider a collection instead.
- Let people edit a table when it makes sense. In iOS and iPadOS, people must enter an edit mode before they can select table items.
- Provide appropriate feedback when people select a list item.

## Content
- Keep item text succinct so row content is comfortable to read; minimize truncation and wrapping.
- Consider ways to preserve readability of text that might otherwise get clipped or truncated. When a table is narrow (e.g. if people can vary its width), an ellipsis in the middle of text can help by preserving the beginning and end.
- Use descriptive column headings in a multicolumn table.

## Style
- Choose a table or list style that coordinates with your data and platform. In iOS and iPadOS the grouped style uses headers, footers, and space to separate groups; macOS defines a bordered style with alternating row backgrounds for large tables. Developer: ListStyle.
- Choose a row style that fits the information. iOS/iPadOS/tvOS: UIListContentConfiguration to lay out content in rows, headers, footers.

## Platform considerations
### iOS, iPadOS, visionOS
- Use an info button only to reveal more info about a row's content (detail disclosure button); it doesn't support navigation. For drilling into subviews, use a disclosure indicator accessory. 
- Avoid adding an index to a table that displays trailing-edge controls like disclosure indicators (both appear on the trailing side and conflict).

### macOS
- Let people click a column heading to sort; click again to reverse.
- Let people resize columns.
- Consider alternating row colors in a multicolumn table to help track row values across columns (especially wide tables).
- Use an outline view instead of a table view to present hierarchical data.

### tvOS / watchOS (out of scope, noted)
tvOS: rows increase in size and round corners when focused. watchOS: limit number of rows; constrain detail view length for vertical page-based navigation.

Resources: Collections, Outline views, Layout. Developer: List/Tables (SwiftUI), UITableView (UIKit), NSTableView (AppKit).
