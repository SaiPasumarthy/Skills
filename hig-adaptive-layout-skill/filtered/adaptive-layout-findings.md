# Adaptive Layout Findings — iOS, iPadOS, macOS

Curated from Apple's Human Interface Guidelines (crawled July 2026). Every point cites the source HIG page. tvOS/visionOS/watchOS/games content encountered on shared pages was ignored except where explicitly noted as out of scope. Base URL: https://developer.apple.com/design/human-interface-guidelines/

Grouping: **Cross-platform core** (applies to iOS + iPadOS + macOS), then platform-specific sections for **iOS**, **iPadOS**, and **macOS**. A final **Component & pattern adaptation** section collects layout-relevant notes buried in component/pattern pages.

---

## 1. Cross-platform core concepts

### 1.1 Adaptability & traits
- Every app needs to adapt when the device or system context changes. In iOS and iPadOS the system defines a collection of **traits** that characterize variations in the device environment (screen size, orientation, Dynamic Type size, etc.). Using **SwiftUI or Auto Layout** ensures the interface adapts dynamically; otherwise you must do the work manually. [layout]
- Common device/system variations to handle: different screen sizes/resolutions/color spaces; different orientations (portrait/landscape); system features like Dynamic Island and camera controls; external display support, Display Zoom, and resizable windows on iPad; Dynamic Type text-size changes; locale-based internationalization including left-to-right/right-to-left layout direction, date/time/number formatting, and text length. [layout]
- Design a layout that adapts gracefully while remaining recognizably consistent — people expect the experience to work well and stay familiar when they rotate the device, resize a window, add a display, or switch devices. Respect system-defined safe areas, margins, and guides. [layout]
- Preserve a person's context as the design adapts across platforms and configurations: keep content and controls in consistent, predictable positions, and use natural animations to ease transitions. [design-principles → Flexibility]
- Approach every platform with intention; support as many devices, input methods, and perspectives as possible. [design-principles → Flexibility]

### 1.2 Safe areas, layout guides, and margins
- A **layout guide** defines a rectangular region for positioning, aligning, and spacing content. The system includes predefined guides for standard margins and for restricting text width for readability; you can define custom guides. (Developer: UILayoutGuide, NSLayoutGuide.) [layout]
- A **safe area** defines the region of a view not covered by a toolbar, tab bar, or other bars — essential for avoiding interactive/display features like Dynamic Island on iPhone or the camera housing on some Mac models. Safe areas also help account for bars, repositioning content dynamically when sizes change. (Developer: SafeAreaRegions.) [layout]
- Extend content to fill the screen or window: backgrounds and full-screen artwork extend to the edges; scrollable layouts continue to the bottom and sides. Controls and navigation components (sidebars, tab bars) appear **on top of** content (the Liquid Glass layer) rather than on the same plane — layout must account for this. [layout]
- When content doesn't span the full window, use a **background extension view** to give the appearance of content behind the control layer beside the sidebar/inspector. (Developer: backgroundExtensionEffect(), UIBackgroundExtensionView.) [layout]
- Status bar (iOS/iPadOS) occupies the top safe-area inset; its text color adapts (light/dark) to content behind it. Prefer a scroll edge effect to place a blurred view behind it; keep it readable. [status-bars]

### 1.3 The Liquid Glass control layer (affects layout structure)
- Liquid Glass forms a distinct **functional layer for controls and navigation** (tab bars, sidebars, toolbars) that **floats above the content layer**, establishing hierarchy; content scrolls and peeks through beneath it. This is consistent across iOS, iPadOS, and macOS. [materials, layout]
- Don't put Liquid Glass in the content layer; use standard materials there. Use a **scroll edge effect** to transition between content and the control area rather than a solid background. [materials, layout, scroll-views]
- Scroll edge effects provide visual separation between floating bars and scrolling content. Prefer the automatic style. Apply one per view; in split-view layouts on iPad and Mac each pane can have its own, kept consistent in height. [scroll-views]

### 1.4 Dynamic Type & text-driven layout (iOS + iPadOS; NOT macOS)
- **Dynamic Type** lets people adjust visible text size in iOS, iPadOS (also tvOS/visionOS/watchOS). **macOS does not support Dynamic Type.** Use the built-in text styles with system fonts to get Dynamic Type + larger accessibility sizes for free. [typography, accessibility]
- Make sure the layout adapts to **all** font sizes; verify the design scales and stays legible at the largest accessibility sizes (Settings > Accessibility > Display & Text Size > Larger Text). [typography]
- Increase meaningful interface icons as font size increases (SF Symbols scale automatically with Dynamic Type). [typography, sf-symbols]
- Keep text truncation to a minimum as font size increases; configure labels to use as many lines as needed. [typography]
- **Adjust layout at large font sizes:** when font size grows in a horizontally constrained context, inline items and container boundaries can crowd text — switch to a **stacked layout** (text above secondary items). **Reduce the number of columns** for multicolumn text as font size increases. (Developer: isAccessibilityCategory.) [typography]
- Maintain a consistent information hierarchy regardless of font size (keep primary elements toward the top even when text is very large). [typography]
- Default/minimum text sizes: iOS/iPadOS 17 pt / 11 pt; macOS 13 pt / 10 pt. [typography, accessibility]

### 1.5 Control sizing & spacing (accessibility-driven layout minimums)
- Minimum comfortable hit target: **iOS/iPadOS 44×44 pt** (min 28×28); **macOS 28×28 pt** (min 20×20). A button needs a hit region of at least 44×44 pt. [accessibility, buttons]
- Spacing is as important as size: ~12 pt padding around bezeled elements; ~24 pt around the visible edges of non-bezeled elements. [accessibility]

### 1.6 Orientation, resolution, and artwork scaling
- A **point** is an abstract unit that keeps content consistent regardless of display; on 2D platforms it maps to a variable number of pixels by resolution. Provide bitmap assets at @2x and @3x (iPhones typically @3x, many iPads @2x). [images, layout]
- When context changes the aspect ratio, scale artwork so important content stays visible rather than changing the aspect ratio — accept letterboxing/pillarboxing. [layout, images, playing-video]

### 1.7 Right-to-left / internationalization
- System UI frameworks flip automatically for RTL; using system elements and standard layouts often needs no changes. Place important items on the leading/top and account for RTL. [right-to-left, layout]
- Flip directional controls (sliders, progress indicators, back/next) and reverse ordered image positions for RTL; don't flip logos, universal marks, or numerals within a number. [right-to-left, sliders, progress-indicators]
- Account for text-length changes across localizations (they affect truncation and wrapping). [layout, writing]

### 1.8 Appearance adaptation (Dark Mode, materials, color)
- Support both light and dark appearances; don't offer an app-specific appearance setting — respect the systemwide choice (and Auto). [dark-mode]
- Prefer system colors and materials — they adapt automatically across appearance and accessibility settings (Increase Contrast, Reduce Transparency). [color, materials, dark-mode]
- Respond to Reduce Motion by reducing/replacing animations (fades instead of x/y/z transitions; avoid animating z-axis depth). [accessibility, motion]

---

## 2. iOS (iPhone) specifics

### 2.1 Size classes
- iPhone is **compact width in portrait for all models**. In landscape, only the larger "Plus/Max" iPhones (and iPhone Air) become **regular width**; standard/Pro iPhones stay **compact width, compact height**. Portrait for all iPhones = compact width, regular height. (Developer: UserInterfaceSizeClass.) [layout]
- Implication: design iPhone primarily for compact width; a split view generally isn't appropriate on iPhone in portrait. [layout, split-views]

### 2.2 Orientation & full-bleed
- Aim to support both portrait and landscape; if landscape-only, work equally well rotated left or right. No need to tell people to rotate. [layout]
- Prefer a full-bleed interface that accommodates the corner radius, sensor housing, and Dynamic Island; optionally offer letterbox/pillarbox. [layout]
- Avoid full-width buttons; respect system margins and inset from the edges. A required full-width button should harmonize with the hardware curvature and align with safe areas. [layout]
- Hide the status bar only when it adds value (immersive media/games). [layout]

### 2.3 Reachability & placement
- Place controls where they're easy to reach — the middle or bottom of the display is more comfortable; support swipe-back and list-row swipe actions. [designing-for-ios]
- Limit onscreen controls; make secondary actions discoverable with minimal interaction. [designing-for-ios]

### 2.4 iOS component adaptation
- **Tab bar** floats at the bottom over content; can minimize with an attached accessory when scrolling; can include a trailing search tab. [tab-bars]
- **Sheets** use detents (medium ≈ half, large = full); include a grabber; support swipe-to-dismiss; medium detent enables progressive disclosure. [sheets]
- **Popovers**: avoid in compact views — reserve for regular width; in compact use a full-screen modal like a sheet. Adjust layout by size class. [popovers]
- **Menus** offer small/medium/large layouts (small = 4 symbol-only items; medium = 3 items with labels; large = full list). [menus]
- **Action sheets** slide up from the bottom on iPhone. [action-sheets]
- **Search** entry point can be a tab, a bottom/top toolbar button, or inline; place at bottom if there's room. [search-fields]
- Large navigation titles collapse to standard as people scroll. [toolbars]

---

## 3. iPadOS specifics

### 3.1 Resizable windows & size classes
- iPad windows are **freely resizable down to a minimum width/height**, similar to macOS. Account for the full range of window sizes, not just full screen. A resized iPad window can become **compact width** even though full-screen iPad is regular width in both orientations. [designing-for-ipados, layout, multitasking, windows]
- Windows present as **full screen** (switch via app switcher) or **windowed** (freely resizable, repositionable; the system remembers size/placement). Window controls appear at the leading edge of the toolbar — move leading toolbar buttons inward so they aren't hidden. [windows, multitasking]
- Test at common system-provided sizes (halves, thirds, quadrants) on a variety of devices; minimize unexpected UI changes from minimum to maximum size. [layout]

### 3.2 Progressive layout collapse
- As a window narrows, **defer switching to a compact view as long as possible** — design the full-screen view first and only collapse when a version of the full layout no longer fits, for UI stability. For complex layouts like split views, hide tertiary columns (e.g. inspectors) first as the view narrows. [layout, split-views]

### 3.3 Adaptive navigation
- Use a **convertible tab bar** (`sidebarAdaptable`): launch with a sidebar or a tab bar, let people switch, and let the presentation style change to fit the view width. The tab bar sits near the **top** on iPad and can convert to a sidebar. To present a sidebar-only, use a navigation split view. [layout, tab-bars, sidebars]
- The `sidebarAdaptable` tab view responds automatically to rotation and window resizing, providing a control appropriate to the width. [sidebars]
- A toolbar and a tab bar can coexist in the same top horizontal space on iPad — useful to navigate main areas while keeping full window width for content. [toolbars]
- Avoid **overflow tabs**: if horizontal space limits visible tabs, the trailing tab becomes "More" — limit scenarios where this happens; aim for a default of five or fewer customizable tabs to preserve continuity between compact and regular sizes. [tab-bars]

### 3.4 Multitasking, multi-window, drag & drop
- iPad supports multiple apps onscreen and multiple windows per app; apps don't control multitasking configs or get notified of them — adapt gracefully to different screen sizes. [multitasking, windows]
- Support drag and drop within the app, across split-view panes, and between apps (cross-app always copies) — a core iPad multitasking capability that layout must accommodate. [drag-and-drop, multitasking]
- Consider a pinch gesture to open content in a new window; you must support multiple windows to present a single file in its own window. [windows]

### 3.5 iPad menu bar
- iPadOS has a menu bar mirroring macOS ordering, revealed by moving the pointer to the top edge or swiping down; hidden until revealed; centered; window controls appear in it when full screen. Ensure all functions are reachable through the app UI too, since the menu bar is often hidden. Consider grouping items into submenus to conserve vertical space (iPad rows are taller for touch). [the-menu-bar]

### 3.6 Multi-input adaptation
- Design for touch AND pointer/trackpad, hardware keyboard, and Apple Pencil; use viewing distance and input mode to determine size and density of content. Pointer support can enable higher density. [designing-for-ipados, pointing-devices, keyboards, apple-pencil-and-scribble]
- When a hardware keyboard is attached, the virtual keyboard doesn't occupy screen space — adapt layout to the keyboard's presence/absence. [keyboards, virtual-keyboards]
- Search field fluidly resizes with the window; for compact views, relocate search (e.g. Notes/Mail place it above the content-list column). [search-fields]

---

## 4. macOS specifics

### 4.1 Windows, resizing & window states
- Let people resize, hide, show, move, minimize, and zoom windows to fit their work style; support full-screen mode. Windows must adapt fluidly to different sizes for multiwindow workflows. [designing-for-macos, windows]
- Window states — **Main** (frontmost; one per app), **Key/active** (accepts input; one at a time), **Inactive** — get distinct system appearances; use system components so appearance updates automatically. [windows]
- Avoid placing controls or critical info at the **bottom** of a window (people move windows so the bottom edge is offscreen); a bottom bar should hold only minor related info. [layout, windows, sidebars]
- Avoid displaying content within the **camera housing** at the top edge; the system's full-screen support accommodates it automatically. (Developer: NSPrefersDisplaySafeAreaCompatibilityMode.) [layout, going-full-screen]

### 4.2 macOS navigation structures
- **Split views** can be arranged vertically, horizontally, or both, with draggable dividers; set sensible min/max pane sizes; let people hide/reveal panes; prefer the thin divider. [split-views]
- **Sidebars**: consider auto-hiding/revealing when the container window resizes (e.g. Mail collapses its sidebar as the window shrinks). Row height/glyph size follow the sidebar's small/medium/large size (set in General settings). Avoid critical info at the sidebar bottom. [sidebars]
- **The menu bar** is always visible at the top of the screen (except full screen); provide standard menus in order (App, File, Edit, Format, View, app-specific, Window, Help). When space is constrained, the system truncates menu titles and hides menu bar extras to prioritize menus. Every toolbar item must also be a menu command (toolbar can be hidden/customized). Menu bar height 24 pt. [the-menu-bar, toolbars]
- **Column views** and **outline views** are macOS-only structures for hierarchical/file navigation; let people resize columns. [column-views, outline-views]
- **Panels** float above windows for supplementary controls/inspectors (macOS-only). Consider a split-view pane instead for an inspector. [panels, split-views]

### 4.3 macOS toolbars & customization
- Support toolbar customization; the system auto-adds an overflow menu in macOS/iPadOS when items don't fit — don't add one manually and avoid layouts that overflow by default. Center-area items collapse into the overflow menu as the window shrinks; leading and trailing items stay put. [toolbars]
- Support personalization: customizable toolbars, window configurations, colors, fonts. [designing-for-macos]

### 4.4 Density & precision
- Leverage large displays to present more content in fewer nested levels with less modality, at a comfortable density. Support high-precision pointer input and keyboard shortcuts / keyboard-only workflows. [designing-for-macos]
- macOS uses no Dynamic Type; match dynamic system font variants (controlContentFont, labelFont, menuFont, etc.) to standard controls. [typography]

### 4.5 Mac Catalyst (iPad → Mac adaptation)
- Mac Catalyst brings an iPad app to the Mac. Apps that already scale for Split View/Slide Over/PiP and support drag-and-drop and keyboard navigation/shortcuts are best positioned, because they've done the groundwork for the extensive **window resizability** Mac users expect. [mac-catalyst]
- Choose between the scaled iPad idiom (~77%) and "Optimize for Mac" (native control sizes/behavior); adopt Mac conventions (menu bar, window toolbar, pointer/keyboard, standard window controls); replace iOS-specific patterns (large titles, bottom tab bars) with Mac equivalents (toolbars, sidebars). Ensure the layout handles the full range of window sizes down to a minimum. [mac-catalyst]

---

## 5. Component & pattern adaptation notes (cross-cutting)

- **Split views**: prefer a regular (not compact) environment; on iPad account for narrow/compact/intermediate widths and keep pane navigation logical. [split-views]
- **Tab views** are a macOS component (not iOS/iPadOS); on iOS/iPadOS use a segmented control for similar function. [tab-views]
- **Toolbars**: three item regions (leading — non-customizable; center — collapses into overflow; trailing — always visible). Define which items move to the overflow menu as the toolbar narrows. [toolbars]
- **Collections** can change layout dynamically; avoid changing layout while people interact unless in response to an explicit action. [collections]
- **Lists & tables** use platform-appropriate styles (grouped in iOS/iPadOS; bordered/alternating rows in macOS); preserve readability when narrow (middle-truncation). [lists-and-tables]
- **Charts**: in a compact environment maximize the plot area; shorten axis labels; align chart edges with surrounding UI. [charts, charting-data]
- **Activity views / share sheets** present as a **sheet or a popover depending on device and orientation**. [activity-views, collaboration-and-sharing]
- **Alerts** are a fixed width and self-center regardless of device/orientation — keep content short. [alerts]
- **Page controls** clip dots when they exceed the width, adapting to available width; use with a paged scroll view. [page-controls, scroll-views]
- **Widgets** come in multiple sizes and adapt appearance to context (Home Screen, Lock Screen, StandBy, Notification Center, tinted/dark) — design each size deliberately. [widgets]
- **Live Activities** require multiple presentations (Lock Screen, Dynamic Island compact/minimal/expanded, StandBy, Mac menu bar) — design each. [live-activities]
- **Launch screens** (iOS/iPadOS) must adapt to every device size/orientation and resemble the first screen. [launching]
- **Full-screen mode**: adjust the layout to use extra space but don't programmatically resize the window; keep essential controls reachable; on iPadOS/macOS keep Dock access (except games). [going-full-screen]
- **Video** playback auto-selects aspect-fill vs aspect-fit by aspect ratio and supports Picture in Picture (adapts across multitasking). [playing-video]
- **CarPlay** uses system templates that iOS renders and adapts to varied car display sizes/inputs — you supply content, not pixel layouts. [carplay]
- **Focus** appearance differs by platform (ring/highlight on iPadOS/macOS); space focusable elements so focus rings don't overlap. [focus-and-selection]

---

## 6. Out-of-scope pages encountered (noted, not used)
`spatial-layout`, `immersive-experiences` (visionOS-only); `digit-entry-views`, `remotes`, `top-shelf`, `live-viewing-apps` grids (tvOS); `lockups` (tvOS); `activity-rings`, `watch-faces`, `complications`, `digital-crown`, `always-on` (watchOS); `eyes` (visionOS); `game-controls`, `designing-for-games` (games). Shared pages' excluded-platform sections (tvOS/visionOS/watchOS) were ignored.
