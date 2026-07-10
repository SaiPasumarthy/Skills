# iOS (iPhone) adaptive layout

iPhone-specific guidance. Read alongside `cross-platform-core.md`. Sourced from
Designing for iOS, Layout, and iOS component pages.

## Size-class behavior

iPhone is **compact width almost everywhere**:

| Model group | Portrait | Landscape |
|---|---|---|
| Standard / Pro (e.g. 17, 17 Pro, 16, 15, SE) | Compact × Regular | Compact × Compact |
| Plus / Max / Air (e.g. 17 Pro Max, 16 Plus, iPhone Air) | Compact × Regular | **Regular × Compact** |

Implications:
- Design iPhone primarily for **compact width**: a single column, stacked
  (push/pop) navigation, a bottom tab bar, and full-screen modals.
- A **split view is generally not appropriate** on iPhone in portrait — there
  isn't horizontal room for multiple panes without truncating. Use it only in a
  regular-width context.
- Only the larger iPhones reach **regular width in landscape**; if you build a
  two-pane landscape layout, it only applies there.

## Orientation and full-bleed

- Aim to support both portrait and landscape. If you support only landscape,
  work equally well rotated left or right. Don't tell people to rotate — they'll
  try both.
- Prefer a **full-bleed** interface that accommodates the corner radius, sensor
  housing, and Dynamic Island; optionally offer letterbox/pillarbox for games or
  media.
- **Avoid full-width buttons** — respect system margins and inset from the edges.
  A required full-width button should harmonize with the hardware curvature and
  align with adjacent safe areas.
- Keep the **status bar** visible unless you're in an immersive media/game
  context; it occupies the top safe-area inset and its color adapts to the
  content behind it.

## Reachability and placement

- Place primary controls where a thumb reaches easily — the **middle or bottom**
  of the display. Support swipe-to-go-back and list-row swipe actions.
- Limit onscreen controls; make secondary details and actions discoverable with
  minimal interaction rather than crowding the screen.

## iOS component adaptation

- **Tab bar** floats at the bottom over content on a Liquid Glass background. It
  can minimize (with an attached accessory, e.g. a mini music player) as the
  person scrolls, and can include a dedicated **search tab** at the trailing end.
- **Sheets** use **detents** — `medium` (~half height) and `large` (full). Add a
  grabber, support swipe-to-dismiss, and use the medium detent for progressive
  disclosure (e.g. a share sheet) unless the content needs full height (compose
  views).
- **Popovers**: **avoid in compact width.** Reserve popovers for regular-width
  contexts; in compact width present the same information in a full-screen modal
  like a sheet. Adjust layout dynamically by size class.
- **Menus** support three layouts: small (a row of four symbol-only items),
  medium (three items with labels), and large (a full list). Use small/medium to
  streamline a few common actions.
- **Action sheets** slide up from the bottom edge on iPhone.
- **Search** entry point can be a tab, a bottom or top toolbar button, or inline
  with content — place at the bottom when there's room so it's reachable.
- **Large navigation titles** collapse to a standard title as the person scrolls
  and expand again at the top.
- **Alerts** are a fixed width and self-center regardless of orientation — keep
  content short.
