# Adaptive layout verification checklist

Run this against a design or implementation before calling it done. Each item is
a concrete pass/fail check drawn from Apple's HIG. Skip items for platforms the
app doesn't target.

## Structure & width
- [ ] Layout decisions are driven by **size class / available width**, not by
      hard-coded device models.
- [ ] There is a defined layout for **both regular and compact width** (compact
      matters on iPad in resized/Slide Over windows, not just iPhone).
- [ ] Navigation matches width: sidebar/split view in regular width, tab bar or
      stacked navigation in compact. On iPad, an **adaptable** tab bar↔sidebar is
      used where appropriate.
- [ ] Split views and popovers are only used in **regular width**; compact width
      falls back to a stack / full-screen modal.

## Safe area & control layer
- [ ] Content is laid out relative to the **safe area** (clears Dynamic Island,
      camera housing, status bar, bars).
- [ ] Backgrounds and scroll content **extend to the edges** beneath floating
      bars/sidebars; a scroll edge effect provides separation.
- [ ] No critical controls/info at the **bottom of a macOS window** or the bottom
      of a sidebar.

## Text & Dynamic Type (iOS/iPadOS)
- [ ] Uses built-in text styles / supports Dynamic Type.
- [ ] Layout still works at the **largest accessibility text size** — no overlap,
      minimal truncation; stacks instead of side-by-side and drops columns where
      needed.
- [ ] Meaningful icons scale with text (SF Symbols).

## Window size & orientation
- [ ] iPad/Mac: layout verified at the **smallest and largest window sizes** and
      at halves/thirds/quadrants; transitions are stable (full layout collapses
      only when it no longer fits; tertiary panes hide first).
- [ ] iPhone: verified in **portrait and landscape** (both rotation directions if
      landscape-only).
- [ ] Multi-window / multitasking (iPad) and drag-and-drop are accommodated where
      relevant.

## Sizing, spacing, input
- [ ] Hit targets meet the minimums (44×44 pt iOS/iPadOS; 28×28 pt macOS) with
      adequate padding.
- [ ] Controls work across all supported input methods (touch, pointer, keyboard,
      Pencil); layout adapts to hardware-keyboard presence on iPad.

## Appearance & internationalization
- [ ] Looks correct in **light and dark** appearance; uses system colors/materials.
- [ ] Verified in a **right-to-left** layout; directional controls flip, logos and
      numbers don't.
- [ ] Reasonable behavior for longer localized strings (no clipping).

## Platform fit
- [ ] iOS: reachable controls (mid/bottom), no unnecessary full-width buttons,
      status bar handled.
- [ ] macOS: standard menu bar with every toolbar item also a menu command;
      resizable windows; correct window-state appearances.
- [ ] Mac Catalyst (if used): iOS-specific patterns replaced with Mac equivalents
      (toolbars/sidebars, menu bar), window resizes to a sensible minimum.
