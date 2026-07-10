# Component & pattern adaptation

How individual components change with size class, window size, orientation, and
platform. Use this when deciding which component to use or how it should behave
as the layout adapts. Sourced from the HIG component and pattern pages.

## Navigation: tab bar vs sidebar vs split view

This is usually the biggest adaptive decision. Pick by available width:

- **Compact width → tab bar** (bottom, on iOS) or stacked push/pop navigation.
  A tab bar gives quick access to a few top-level sections.
- **Regular width → sidebar or split view.** A sidebar suits many top-level
  destinations and customization; a split view shows two or three levels of
  hierarchy at once (list → detail, optionally → inspector).
- **iPad: prefer an adaptable tab bar** (`sidebarAdaptable`) that presents as a
  sidebar when there's room and a tab bar when there isn't, converting
  automatically with rotation and window resizing. Use a navigation split view
  when you want a **sidebar only** (no tab-bar conversion).
- **Split views need regular width.** In compact width, collapse a split view to
  a single navigation stack. On iPad, account for narrow/compact/intermediate
  widths and hide tertiary panes (inspectors) first as the window narrows.
- **Tab views** (the boxed tabbed control) are a **macOS** component — on
  iOS/iPadOS use a segmented control for similar in-place switching.

## Toolbars

- Three item regions: **leading** (back, sidebar toggle, title — not
  customizable, always available), **center** (common controls; collapses into
  the system overflow menu as the window shrinks; customizable), and **trailing**
  (important items, search, primary action — stays visible at all sizes).
- Define which items move to the overflow menu as the toolbar narrows; don't add
  a manual overflow menu (the system does it on macOS/iPadOS).
- On iPad a toolbar and tab bar can share the top row; on iOS use large titles
  that collapse on scroll.

## Modals: sheets, popovers, alerts, action sheets

- **Sheets** (iOS/iPadOS) rest at **detents** — medium (~half) and large (full);
  add a grabber and support swipe-to-dismiss. On iPadOS prefer the page or form
  sheet styles (centered, default size). On macOS a sheet is a card over its
  parent window.
- **Popovers** require **regular width**. In compact width, present the same
  content as a full-screen modal (a sheet) instead. On macOS a popover can be
  detached into a panel.
- **Alerts** are a fixed width and self-center regardless of device/orientation
  — keep content short and to two buttons where possible.
- **Action sheets / confirmation dialogs** adapt: on iPhone they slide up from
  the bottom; on iPad they appear in a **popover** anchored to the triggering
  control, so give it a sensible anchor.
- **Activity views (share sheets)** present as a **sheet or a popover depending
  on device and orientation**.

## Content components

- **Collections** can change layout dynamically; avoid changing layout while
  people interact unless in response to an explicit action.
- **Lists & tables** use platform-appropriate styles — grouped (iOS/iPadOS) vs
  bordered/alternating rows (macOS). Preserve readability when a table is narrow
  (middle-truncate to keep the start and end of text).
- **Charts**: in a **compact** environment maximize the plot area, shorten
  vertical-axis labels, and consider moving units into the title; align chart
  edges with surrounding UI.
- **Page controls** clip their dots when they exceed the available width, so they
  adapt to width; pair with a paged scroll view.
- **Scroll views**: use a scroll edge effect to separate floating bars from
  content; don't nest same-orientation scroll views.

## System presentations that require multiple layouts

- **Widgets** come in several sizes and adapt appearance to context (Home Screen,
  Lock Screen, StandBy, Notification Center, tinted/dark). Design **each size**
  deliberately — don't scale one layout.
- **Live Activities** need distinct presentations for the Lock Screen, the
  Dynamic Island (compact leading/trailing, minimal, and expanded), StandBy, and
  the Mac menu bar. Design each.
- **Launch screens** (iOS/iPadOS) must adapt to every device size and orientation
  and should resemble the first screen (use a storyboard/auto-layout launch
  screen, not fixed images).

## Full-screen, video, and embedded contexts

- **Full-screen mode**: adjust the layout to use the extra space but **don't
  programmatically resize the window**; keep essential controls reachable; on
  iPadOS/macOS preserve Dock access (except games).
- **Video** auto-selects aspect-fill vs aspect-fit by aspect ratio and supports
  Picture in Picture, which floats over other apps during multitasking.
- **CarPlay** uses system templates that iOS renders and adapts to varied car
  displays — you supply content, not pixel layouts. (Out of the core three
  platforms but a useful example of template-driven adaptation.)

## Focus and input

- **Focus** appearance differs by platform (a ring or highlight on iPadOS/macOS).
  Space focusable elements so focus rings don't overlap.
- Design controls and hit targets to work across **all** input methods a platform
  supports (touch, pointer, keyboard, Pencil), not just the primary one.
