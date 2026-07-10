---
name: hig-adaptive-layout
description: >-
  Produce adaptive, responsive layouts for iOS, iPadOS, and macOS that follow
  Apple's Human Interface Guidelines — for a brand-new screen or an existing one
  that must work across devices and window sizes. Use whenever the user wants to
  design, build, lay out, adapt, fix, or review an iPhone, iPad, or Mac screen:
  e.g. "lay out a settings screen for iPhone and iPad", "make this SwiftUI view
  adaptive", "why does my iPad layout break in Split View", "tab bar or sidebar
  here?", "make my screen work in landscape and at large text sizes", or "port my
  iPad app to Mac Catalyst". Covers size classes, safe areas, trait collections,
  Split View / Slide Over / Stage Manager, resizable and multi-window behavior,
  orientation, adaptive navigation, and Dynamic Type's effect on layout. Trigger
  it even when the user doesn't say "adaptive" or "HIG" — any request to build or
  rework an iOS/iPadOS/macOS screen layout qualifies. Applies to iOS, iPadOS, and
  macOS only; excludes tvOS, visionOS, and watchOS.
---

# Produce Adaptive Layouts for iOS, iPadOS & macOS (Apple HIG)

## What this skill does

Given a screen — described in words, sketched, or handed over as existing
SwiftUI/UIKit/AppKit code — this skill produces a **concrete adaptive layout**:
a plan for how that screen should be structured and how it reshapes itself across
iPhone, iPad, and Mac, across window sizes, orientations, text sizes, and
appearances, all grounded in Apple's Human Interface Guidelines. The output is
something the user can build from directly, not just advice.

The reason this matters: the same app runs on a compact iPhone in portrait, an
iPad in a resized Split View window, and a Mac window dragged to a quarter of the
screen. A layout that only works at one size fails the person using it at another.
The job is to make one design that stays recognizable and usable across all of
them.

Scope: iOS, iPadOS, and macOS. If a request is specifically about tvOS,
visionOS, watchOS, or games, this skill doesn't apply — say so instead of
guessing.

## The mental model (internalize this first)

A handful of load-bearing ideas drive almost every decision:

1. **Adapt to traits, not device models.** The system reports the environment as
   traits — chiefly the horizontal and vertical **size class** (regular or
   compact), plus orientation, Dynamic Type size, and appearance. Design against
   these, never against "if iPhone 15." Lean on SwiftUI or Auto Layout to do the
   adapting.
2. **Width drives structure.** The most useful question is "how wide is the space
   right now?" Regular width affords side-by-side structure (split views,
   sidebars, multi-column, popovers). Compact width wants a single column, stacked
   navigation, full-screen modals, and bottom-reachable controls. On iPhone this
   tracks the device; on iPad and Mac it tracks the **window**, which the user
   resizes freely.
3. **Respect the safe area and the control layer.** Lay content out relative to
   the safe area so it dodges the Dynamic Island, camera housing, and system bars.
   Bars and sidebars (the Liquid Glass control layer) **float above** content —
   extend content to the edges beneath them.
4. **Text size is a layout input.** Dynamic Type (iOS/iPadOS) can grow text
   dramatically; layouts must reflow — stack instead of sit side-by-side, drop
   columns, add lines — not truncate or overlap. (macOS has no Dynamic Type but
   still resizes windows.)
5. **Preserve context as things change.** When the device rotates, the window
   resizes, a display is added, or the app moves platforms, keep controls and
   content in predictable places and animate transitions. Defer disruptive layout
   changes as long as possible.

## How to produce the layout

Follow these steps. Pull in the reference file(s) for the platform(s) and
components involved — each has the concrete rules, tables, and gotchas. Then emit
the deliverable in the format below.

1. **Establish the inputs.** Identify (a) the target platforms (iPhone / iPad /
   Mac — ask if unstated but assume all three the app plausibly targets), (b) the
   screen's content and controls (from the description or by reading the existing
   code), and (c) the width contexts to support. If given existing code, read it
   first and diagnose what breaks when the width or text size changes.

2. **Choose the navigation & container structure per width.** This is usually the
   biggest decision. Regular width → sidebar or split view; compact width → tab
   bar or a stacked navigation. On iPad, prefer an **adaptable** structure
   (`NavigationSplitView`, or a `sidebarAdaptable` tab view) that becomes a
   sidebar when there's room and collapses when there isn't. See
   `references/component-adaptation.md`.

3. **Lay out the content for each size class.** Decide what sits side-by-side in
   regular width and how it **stacks** in compact width; what anchors to the safe
   area; where scroll content runs to the edges under floating bars; and which
   secondary/tertiary elements (inspectors, columns) hide first as space shrinks.
   See `references/cross-platform-core.md`.

4. **Make it survive text-size and window-size changes.** State explicitly what
   happens at the largest accessibility text size (what stacks, what drops to
   fewer columns) and at the smallest and largest window sizes. See
   `references/cross-platform-core.md` (Dynamic Type) and the iPadOS/macOS
   references (window resizing).

5. **Handle orientation, multitasking & multi-window** where relevant — landscape
   on iPhone; Split View / Slide Over / Stage Manager / free resizing / multiple
   windows on iPad; full window management and Mac Catalyst on Mac.

6. **Write the SwiftUI scaffold.** Translate the plan into adaptive SwiftUI that
   demonstrates the structure (size-class branching, `NavigationSplitView`, safe
   area handling, Dynamic Type–friendly stacks). Use
   `references/swiftui-patterns.md` for ready-to-adapt snippets. If the user's
   codebase is UIKit/AppKit, describe the equivalent (trait collections /
   `UISplitViewController` / Auto Layout) instead.

7. **Verify.** Run the design against `references/verification-checklist.md` and
   report the result inline — it's the fast way to catch the common failures.

## Output format — the adaptive layout deliverable

Produce these sections. Adapt depth to the request (a quick question needs less
than a full screen build), but keep the structure so the output is predictable
and buildable.

```
## <Screen name> — Adaptive Layout

### 1. Layout summary
One paragraph: what the screen contains and the core adaptive strategy
(e.g. "single scrolling column in compact width; two-column split view in
regular width; inspector hides first as the window narrows").

### 2. Per-size-class layout
- Compact width (iPhone portrait; narrow iPad/Mac window): <structure, what
  stacks, control placement, modality choices>
- Regular width (iPad/Mac full size; large iPhone landscape): <structure,
  side-by-side arrangement, sidebar/split view>
- Transition behavior: <what changes and when as width shrinks/grows>

### 3. Safe area, bars & control layer
<safe-area anchoring, edge-to-edge content under floating bars, scroll edge
effect, status bar / camera housing / Dynamic Island considerations>

### 4. Dynamic Type & orientation
<what reflows at large text sizes; landscape/portrait behavior; note macOS has
no Dynamic Type but resizes>

### 5. Platform specifics
<iOS / iPadOS / macOS notes that apply — e.g. bottom tab bar on iOS, adaptable
tab bar↔sidebar on iPad, menu bar + toolbar on Mac, Mac Catalyst adjustments>

### 6. SwiftUI scaffold
<compilable-shaped adaptive SwiftUI (or UIKit/AppKit equivalent if that's the
user's stack)>

### 7. Verification
<the checklist result: which items pass, any caveats>
```

When reviewing or fixing an **existing** screen rather than building new, keep the
same sections but lead each with what's wrong today and what to change, and make
section 6 a diff or targeted edits rather than a from-scratch view.

## Reference files

Read the file(s) relevant to the task rather than loading everything:

- `references/cross-platform-core.md` — concepts that apply everywhere: traits &
  size classes, safe areas & layout guides, the Liquid Glass control layer &
  scroll edge effects, Dynamic Type reflow, control-sizing minimums, RTL,
  appearance/Dark Mode, artwork scaling. **Start here** for anything conceptual.
- `references/ios.md` — iPhone specifics: size-class behavior per model,
  orientation and full-bleed, reachability, iOS component adaptation.
- `references/ipados.md` — iPad specifics: freely resizable windows, progressive
  collapse, adaptable tab bar↔sidebar, multitasking / multi-window /
  drag-and-drop, iPad menu bar, multi-input.
- `references/macos.md` — Mac specifics: window resizing & states, split
  views/sidebars/panels/columns/outlines, menu bar, toolbar overflow, density,
  and **Mac Catalyst**.
- `references/component-adaptation.md` — how individual components adapt (tab bar
  vs sidebar vs split view, toolbars, sheets & detents, popovers, alerts, page
  controls, widgets, tables, charts).
- `references/swiftui-patterns.md` — copy-and-adapt SwiftUI snippets for the
  common adaptive structures (size-class branching, `NavigationSplitView`, safe
  area & scroll edge, adaptive stacks, adaptive grid).
- `references/verification-checklist.md` — the pass/fail checklist to run against
  any layout.

Deeper sourced findings (every point cited to its HIG page) live in
`filtered/adaptive-layout-findings.md`; the full crawled HIG pages, if bundled,
are in `raw/` (and always in the source project alongside `manifest.md`).

## Quick reference

### iOS / iPadOS size classes (the core adaptive signal)
Regular = larger screen or landscape; compact = smaller screen or portrait,
independently for width and height.

| Context | Width × Height |
|---|---|
| All iPad models, full screen, both orientations | Regular × Regular |
| iPad in a narrow/resized window or Slide Over | can become **Compact** width |
| iPhone (standard/Pro), portrait | Compact × Regular |
| iPhone (standard/Pro), landscape | Compact × Compact |
| iPhone Plus/Max/Air, portrait | Compact × Regular |
| iPhone Plus/Max/Air, landscape | **Regular** × Compact |

Rule of thumb: **regular width → side-by-side (sidebar/split view/popover);
compact width → single column + full-screen modals.** iPhone is compact width
almost everywhere; only Plus/Max/Air go regular width in landscape.

### Comfortable control sizes (minimum hit targets)
| Platform | Default | Minimum |
|---|---|---|
| iOS / iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |

Add ~12 pt padding around bezeled controls, ~24 pt around non-bezeled ones.

### Default / minimum text sizes
| Platform | Default | Minimum |
|---|---|---|
| iOS / iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |

iOS/iPadOS support Dynamic Type (design for reflow to the largest accessibility
size). macOS does not — but windows still resize.

### One-line heuristics
- Branch on size class / available width, never on device model.
- Design the widest layout first; collapse to compact only when it no longer
  fits, hiding tertiary panes (inspectors) before primary ones.
- Bars and sidebars float above content — run content to the edges beneath them.
- Popovers and split views need regular width; in compact, use a sheet /
  full-screen modal.
- On iPad, prefer an adaptable structure that converts sidebar↔tab bar.
- Verify at: smallest & largest window size, both orientations, largest
  accessibility text size, light & dark, and RTL.
