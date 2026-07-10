# Edit menus
URL: https://developer.apple.com/design/human-interface-guidelines/edit-menus
An edit menu lets people make changes to selected content (Copy, Select, Translate, Look Up, etc.). Commands apply to text and other selectable content. In iOS, iPadOS, and visionOS the system auto-detects the data type of a selected item and can add a related action (e.g. selecting an address adds "Get directions").

Platform-adaptive behavior:
- iOS: the edit menu displays commands in a compact, horizontal list that appears on touch-and-hold or double-tap; people can tap a trailing chevron to expand it into a context menu.
- iPadOS: the edit menu looks different depending on how people reveal it (touch vs pointer).
- iOS/iPadOS: provide either a context menu or an edit menu for an item, but not both.

Developer: editMenu (SwiftUI), UIEditMenuInteraction (UIKit).
