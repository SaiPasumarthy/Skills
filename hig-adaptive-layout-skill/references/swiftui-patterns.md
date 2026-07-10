# SwiftUI adaptive layout patterns

Copy-and-adapt SwiftUI snippets for the structures this skill produces. These are
scaffolds — shape them to the actual screen. They embody the HIG guidance in the
other reference files (size-class branching, safe areas, adaptable navigation,
Dynamic Type–friendly stacks). For UIKit/AppKit codebases, the equivalents are
noted at the end.

## Contents
- Reading the size class
- Compact-vs-regular structural branch
- Adaptive split view / sidebar (NavigationSplitView)
- Adaptable tab bar ↔ sidebar
- Stack that reflows for Dynamic Type
- Adaptive grid
- Safe area & scroll edge
- Popover-in-regular / sheet-in-compact
- UIKit / AppKit equivalents

## Reading the size class

```swift
struct ContentView: View {
    @Environment(\.horizontalSizeClass) private var hSize
    // .compact  → iPhone (most), iPad narrow window, Slide Over
    // .regular  → iPad full/large window, Mac, large iPhone landscape

    var body: some View {
        if hSize == .regular {
            RegularLayout()
        } else {
            CompactLayout()
        }
    }
}
```

Prefer letting a container adapt on its own (next sections) over manual branching;
branch manually only when the two layouts genuinely differ.

## Compact-vs-regular structural branch

```swift
// Regular width: label and control sit side by side.
// Compact width (or large Dynamic Type): they stack.
struct FieldRow: View {
    @Environment(\.horizontalSizeClass) private var hSize
    @Environment(\.dynamicTypeSize) private var typeSize
    let title: String
    @Binding var value: String

    private var shouldStack: Bool {
        hSize == .compact || typeSize.isAccessibilitySize
    }

    var body: some View {
        let layout = shouldStack
            ? AnyLayout(VStackLayout(alignment: .leading, spacing: 4))
            : AnyLayout(HStackLayout(alignment: .firstTextBaseline, spacing: 16))
        layout {
            Text(title).font(.headline)
            TextField("", text: $value).textFieldStyle(.roundedBorder)
        }
    }
}
```

`ViewThatFits` is another option when you want the system to pick the first
layout that fits:

```swift
ViewThatFits {
    HStack { Label(); Spacer(); Control() }   // preferred when it fits
    VStack(alignment: .leading) { Label(); Control() }  // fallback
}
```

## Adaptive split view / sidebar (NavigationSplitView)

The workhorse for list→detail (and list→content→detail) screens. It shows columns
side by side in regular width and automatically collapses to a single navigation
stack in compact width — no manual branching needed.

```swift
struct LibraryView: View {
    @State private var selectedFolder: Folder?
    @State private var selectedItem: Item?
    @State private var columnVisibility: NavigationSplitViewVisibility = .automatic

    var body: some View {
        NavigationSplitView(columnVisibility: $columnVisibility) {
            SidebarList(selection: $selectedFolder)          // primary
                .navigationSplitViewColumnWidth(min: 220, ideal: 260)
        } content: {
            ItemList(folder: selectedFolder, selection: $selectedItem)  // secondary
        } detail: {
            DetailView(item: selectedItem)                   // detail
        }
        // Tertiary columns (content) collapse before the primary as width shrinks.
    }
}
```

Two-column form is the same with just `sidebar` + `detail`. Set sensible
`navigationSplitViewColumnWidth(min:ideal:max:)` so panes stay usable on Mac.

## Adaptable tab bar ↔ sidebar (iPadOS/iOS)

Lets the app present a tab bar in compact width and convert to a sidebar in
regular width, with the person able to switch.

```swift
TabView {
    Tab("Home", systemImage: "house") { HomeView() }
    Tab("Browse", systemImage: "square.grid.2x2") { BrowseView() }
    Tab("Search", systemImage: "magnifyingglass", role: .search) { SearchView() }
    TabSection("Library") {
        Tab("Recents", systemImage: "clock") { RecentsView() }
        Tab("Favorites", systemImage: "star") { FavoritesView() }
    }
}
.tabViewStyle(.sidebarAdaptable)   // tab bar in compact, sidebar in regular
```

## Stack that reflows for Dynamic Type

At accessibility text sizes, a horizontal row of label + value + chevron crowds
and truncates. Detect the size and stack instead.

```swift
struct SummaryCard: View {
    @Environment(\.dynamicTypeSize) private var typeSize
    var body: some View {
        let stack = typeSize.isAccessibilitySize
        Group {
            if stack {
                VStack(alignment: .leading, spacing: 8) { title; value; action }
            } else {
                HStack(spacing: 16) { title; value; Spacer(); action }
            }
        }
        .padding()
    }
    private var title: some View { Text("Total").font(.headline) }
    private var value: some View { Text("$1,240").font(.title2) }
    private var action: some View { Button("Details") {} }
}
```

Always use text styles (`.headline`, `.body`, …) so text scales; never hard-code
point sizes for body text.

## Adaptive grid

A grid that grows its column count with available width (and thus adapts across
iPhone → iPad → Mac and window resizing) without hard-coding counts.

```swift
ScrollView {
    LazyVGrid(
        columns: [GridItem(.adaptive(minimum: 160, maximum: 240), spacing: 16)],
        spacing: 16
    ) {
        ForEach(items) { ItemCell(item: $0) }
    }
    .padding()
}
```

`.adaptive(minimum:)` is the single most useful tool for content grids — one line
that fills 1 column on a narrow iPhone and many on a wide Mac window.

## Safe area & scroll edge

```swift
ScrollView {
    content
}
// Content runs under the bars; the system keeps interactive content in the safe area.
.ignoresSafeArea(edges: .horizontal)          // let backgrounds reach the sides
.background(Color(.systemGroupedBackground))
.toolbar { /* floats above content on the Liquid Glass layer */ }
// Add a background extension beside a sidebar/inspector when content is narrower:
// .backgroundExtensionEffect()
```

Anchor decorative backgrounds edge-to-edge; keep controls and text within the
safe area. Don't fight the safe area with fixed insets.

## Popover-in-regular / sheet-in-compact

Popovers need regular width; in compact, present a sheet instead. `.popover`
already adapts on iOS by falling back to a sheet, but be explicit when you want
control:

```swift
.popover(isPresented: $showInfo) { InfoView() }
// or, to force a sheet in compact and a popover in regular, branch on hSize.
```

## UIKit / AppKit equivalents

- Size class → `UITraitCollection.horizontalSizeClass`; respond in
  `traitCollectionDidChange` / `registerForTraitChanges`.
- Adaptive split view → `UISplitViewController` (`.doubleColumn` /
  `.tripleColumn`, `preferredDisplayMode`), which collapses in compact width.
- Adaptable tab/sidebar → `UITabBarController` with `sidebar` mode on iPad
  (`UITab`, `UITabBarController.Mode.tabSidebar`).
- Reflow / stacking → Auto Layout with size-class-varied constraints, or
  `UIStackView` whose `axis` you switch on trait changes.
- Adaptive grid → `UICollectionViewCompositionalLayout` with item counts derived
  from the layout environment's container width.
- Dynamic Type → `UIFont.preferredFont(forTextStyle:)` +
  `adjustsFontForContentSizeCategory = true`.
- macOS → `NSSplitViewController`, `NSToolbar` (auto overflow), Auto Layout;
  no size classes or Dynamic Type, but full window resizing.
