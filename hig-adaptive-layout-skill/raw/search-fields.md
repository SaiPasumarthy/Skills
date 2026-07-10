# Search fields
URL: https://developer.apple.com/design/human-interface-guidelines/search-fields

A search field lets people search a collection of content for specific terms. Across each platform there are different patterns for accessing search based on the goals and design of your app.

## Best practices
- Use placeholder text to help people know what they can search for.
- Start search immediately when a person types, if possible.
- Consider showing suggested search terms; simplify and categorize results; let people filter (scope bars, tokens).

## Platform considerations
No additional considerations for visionOS.

### iOS
Three main places to position the entry point for search, depending on layout, content, and navigation:
- As a tab in a tab bar (standard tab → dedicated search landing page; button appearance → immediately focuses the field and shows keyboard).
- In a toolbar at the bottom or top. Bottom toolbar: as an expanded field or a toolbar button depending on available space; animates into a search field above the keyboard. Top toolbar (navigation bar): appears as a button; animates into a search field above the keyboard or at the top if there isn't space at the bottom. Place search at the bottom if there's room; place at the top when it's important to defer to content at the bottom.
- Inline with content (place next to the content it searches; pin to the top toolbar when scrolling).

### iPadOS, macOS (KEY ADAPTIVE DETAIL)
Placement/behavior is similar across iPadOS and macOS; keep the experience consistent if your app is on both.
- Put a search field at the trailing side of the toolbar for many common uses, particularly apps with split views that search across multiple columns (Mail, Notes, Voice Memos).
- Include search at the top of the sidebar when filtering content or navigation there (e.g. Settings).
- Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery (Music, TV).
- In a dedicated-area search field, consider immediately focusing the field on navigation — EXCEPT on iPad when only a virtual keyboard is available (leave unfocused to prevent the keyboard from covering the view).
- **Account for window resizing with the placement of the search field.** On iPad, the search field fluidly resizes with the app window like on Mac. For **compact views on iPad**, ensure search is available where it's most contextually useful — e.g. Notes and Mail place search above the column for the content list when they resize down to a compact view.

### tvOS / watchOS (out of scope, noted)
tvOS: specialized search keyboard screen. watchOS: full-screen text-input control.

Resources: Searching, Token fields. Developer: searchable (SwiftUI), UISearchBar (UIKit), NSSearchField (AppKit).
Change log: June 9, 2025 — updated search placement in iOS, consolidated iPadOS and macOS considerations.
