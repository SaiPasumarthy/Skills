# Collections
URL: https://developer.apple.com/design/human-interface-guidelines/collections

A collection manages an ordered set of content and presents it in a customizable, highly visual layout. Ideal for image-based content.

## Best practices
- Use the standard row or grid layout whenever possible. Collections display content by default in a horizontal row or a grid. Avoid custom layouts that confuse people.
- Consider using a table instead of a collection for text.
- Make it easy to choose an item. Use adequate padding around images to keep focus/hover effects easy to see and prevent content from overlapping.
- Add custom interactions when necessary.
- Consider animations to provide feedback when people insert, delete, or reorder items.

## Platform considerations
No additional considerations for macOS, tvOS, or visionOS. Not supported in watchOS.
### iOS, iPadOS
Use caution when making dynamic layout changes. The layout of a collection can change dynamically. Avoid changing the layout while people are viewing and interacting with it, unless in response to an explicit action.

Resources: Lists and tables, Image views, Layout. Developer: UICollectionView (UIKit), NSCollectionView (AppKit).
