# iPadOS adaptive layout

iPad is the platform where adaptive layout matters most, because a single app
window can be almost any size. Read alongside `cross-platform-core.md`. Sourced
from Designing for iPadOS, Layout, Multitasking, Windows, Split views, Sidebars,
Tab bars, The menu bar, and input pages.

## Freely resizable windows & size classes

- iPad windows are **freely resizable down to a minimum width and height**, much
  like macOS. Design for the **full range of window sizes**, not just full
  screen.
- At full screen an iPad is regular width in both orientations, but a **resized
  or Slide Over window can become compact width** — so your compact-width layout
  must exist and be good, not an afterthought.
- Windows present as **full screen** (switch via the app switcher) or
  **windowed** (freely resizable and repositionable; the system remembers size
  and placement). When windowed, window controls occupy the leading edge of the
  toolbar — **move leading toolbar buttons inward** so they aren't hidden.
- Test at the common system sizes: halves, thirds, and quadrants of the screen,
  on a variety of devices. Minimize unexpected UI changes across the whole range.

## Progressive layout collapse (the key iPad technique)

- **Design the full-screen (widest) view first, and defer collapsing to a
  compact view as long as possible** — collapse only when a version of the full
  layout no longer fits. This keeps the UI stable and familiar.
- For complex layouts like split views, **hide tertiary columns first** (e.g. an
  inspector) as the view narrows, before touching the primary structure.

## Adaptive navigation: the convertible tab bar / sidebar

- Prefer a **convertible tab bar** (`sidebarAdaptable`): the app launches with
  your choice of a sidebar or a tab bar, the person can switch between them, and
  the presentation **changes automatically to fit the view width** (and responds
  to rotation and resizing).
- The iPad tab bar sits near the **top** of the window and can convert to a
  sidebar for a wider set of navigation options. To present a **sidebar only**,
  use a navigation split view instead of a tab view.
- A toolbar and a tab bar can **coexist** in the same top horizontal space —
  useful when you want to navigate a few main areas while keeping the full window
  width for content.
- **Avoid overflow tabs:** if width limits the visible tabs, the trailing tab
  becomes a "More" tab, which hides content — limit when this happens, and if
  tabs are customizable aim for a default of five or fewer to keep continuity
  between compact and regular sizes.

## Multitasking, multi-window, drag & drop

- iPad shows multiple apps at once and supports **multiple windows per app**.
  Apps don't control multitasking configurations or get told which one is active
  — so **adapt gracefully to whatever size you're given**.
- Support **drag and drop** within the app, across split-view panes, and between
  apps (cross-app always copies). This is central to iPad multitasking and your
  layout should invite it (clear drop targets, sensible panes).
- Consider a **pinch gesture** to open content in a new window. To present a
  single file in its own window you must support multiple windows.

## The iPad menu bar

- iPadOS has a menu bar that mirrors macOS ordering, revealed by moving the
  pointer to the top edge or swiping down. It's hidden until revealed, centered,
  and shows window controls when the app is full screen.
- Because it's often hidden, **ensure every function is reachable through the app
  UI too**; dynamic menu items only appear with a hardware keyboard attached.
- Consider grouping items into submenus to conserve vertical space (iPad menu
  rows are taller for touch than on Mac).

## Multi-input adaptation

- Design for **touch AND pointer/trackpad, hardware keyboard, and Apple Pencil**
  simultaneously; people combine them. Use viewing distance and input mode to
  choose content size and density — pointer support can enable higher density.
- When a **hardware keyboard** is attached, the virtual keyboard doesn't occupy
  screen space — adapt the layout to the keyboard's presence/absence.
- The **search field** fluidly resizes with the window; for compact views,
  relocate it where it stays useful (e.g. Notes and Mail place search above the
  content-list column when compact).
- Mirror macOS keyboard-shortcut patterns and surface them in the menu bar.

## Transitioning to Mac

An iPad app that already scales across window sizes, supports drag-and-drop, and
handles keyboard navigation is well-positioned for **Mac Catalyst** — see
`macos.md`.
