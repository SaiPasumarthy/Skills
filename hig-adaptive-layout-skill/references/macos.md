# macOS adaptive layout

The Mac's adaptivity is about **window resizing and multi-window density** rather
than size classes (macOS doesn't use size classes or Dynamic Type). Read
alongside `cross-platform-core.md`. Sourced from Designing for macOS, Windows,
Split views, Sidebars, The menu bar, Toolbars, Panels, Column/Outline views,
and Mac Catalyst.

## Windows, resizing & window states

- Let people **resize, hide, show, move, minimize, and zoom** windows, and
  support full-screen mode. Windows must adapt fluidly across sizes for
  multi-window workflows.
- **Window states** get distinct system appearances — **Main** (frontmost; one
  per app), **Key/active** (accepts input; one at a time; can be a floating
  panel), and **Inactive** (subdued, no vibrancy). Use system-provided components
  so these appearances update automatically; if you build custom windows you must
  replicate the state appearances yourself.
- **Avoid placing controls or critical information at the bottom of a window** —
  people frequently drag windows so the bottom edge is offscreen. A bottom bar
  should carry only minor, related info (like Finder's status bar).
- **Avoid content under the camera housing** at the top edge; the system's
  full-screen support accommodates it automatically. (Developer:
  `NSPrefersDisplaySafeAreaCompatibilityMode`.)

## Navigation structures (mostly macOS-only)

- **Split views** can be arranged vertically, horizontally, or both, with
  **draggable dividers**. Set sensible min/max pane sizes so the divider stays
  usable; let people hide/reveal panes; prefer the thin (1 pt) divider.
- **Sidebars**: consider **auto-hiding/revealing** as the container window
  resizes (e.g. Mail collapses its sidebar when narrow to give content room).
  Row height and glyph size follow the sidebar's small/medium/large size, set in
  General settings. Don't put critical info at the sidebar bottom.
- **The menu bar** is always visible at the top of the screen (except in full
  screen). Provide the standard menus in order: App, File, Edit, Format, View,
  app-specific, Window, Help. When space is tight the system truncates menu
  titles and hides menu bar extras to keep menus readable. **Every toolbar item
  must also exist as a menu command**, because the toolbar can be hidden or
  customized. Menu bar height is 24 pt.
- **Column views** (browser) and **outline views** are macOS-only structures for
  navigating hierarchies/files; let people resize columns.
- **Panels** float above windows for supplementary controls/inspectors
  (macOS-only). For an inspector you can also use a split-view pane.

## Toolbars: customization & overflow

- Support **toolbar customization**. The system **auto-adds an overflow menu**
  in macOS (and iPadOS) when items don't fit — don't add one manually, and avoid
  layouts that overflow by default. Center-area items collapse into the overflow
  as the window shrinks; **leading and trailing items stay put**.
- Support personalization broadly: customizable toolbars, saved window
  configurations, and chosen colors/fonts.

## Density & precision

- Leverage large displays to present **more content in fewer nested levels** with
  less modality, at a comfortable density. Support **high-precision pointer**
  input and **keyboard shortcuts / keyboard-only** workflows.
- macOS has **no Dynamic Type**; use the dynamic system font variants
  (`controlContentFont`, `labelFont`, `menuFont`, `titleBarFont`, etc.) so your
  text matches standard controls at the system text size.

## Mac Catalyst (bringing an iPad layout to the Mac)

Mac Catalyst creates a Mac version of an iPad app — a core "adapt an iPad layout
to a new environment" task.

- Best candidates already scale for **Split View / Slide Over / Picture in
  Picture** and support **drag-and-drop** and **keyboard navigation/shortcuts**,
  because that groundwork maps directly onto the extensive **window resizability**
  Mac users expect.
- Choose between the scaled iPad idiom (~77%) and **"Optimize for Mac"** (native
  control sizes and behavior).
- Adopt Mac conventions: a **menu bar** with standard menus, a **window toolbar**,
  **pointer/keyboard** support, and standard window controls.
- Replace iOS-specific patterns with Mac equivalents where needed — e.g. large
  navigation titles and bottom tab bars become **toolbars and sidebars**.
- Ensure the layout handles the full range of window sizes **down to a minimum**.
