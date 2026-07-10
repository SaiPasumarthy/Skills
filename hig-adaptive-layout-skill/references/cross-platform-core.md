# Cross-platform core concepts (iOS + iPadOS + macOS)

These concepts apply across all three platforms. They are the foundation the
platform-specific references build on. Sourced from Apple's HIG (Layout,
Typography, Materials, Accessibility, Right to left, Color, Dark Mode, Images,
Design principles, Scroll views).

## Contents
- Traits and size classes
- Safe areas, layout guides, margins
- The Liquid Glass control layer & scroll edge effects
- Dynamic Type and text-driven layout
- Control sizing and spacing
- Orientation, resolution, artwork scaling
- Right-to-left and internationalization
- Appearance adaptation (Dark Mode, materials, color, motion)

## Traits and size classes

The system characterizes the environment as a collection of **traits**. The most
important for layout is the **size class** — `regular` or `compact` — reported
separately for width and height. Regular means a larger screen or landscape;
compact means a smaller screen or portrait.

- Design against traits so a single layout serves many devices and window sizes.
  Use SwiftUI or Auto Layout to adapt dynamically; without them you must adapt
  manually.
- Handle these common variations: different screen sizes/resolutions/color
  spaces; orientation changes; system features like Dynamic Island and the
  camera housing; external displays, Display Zoom, and resizable iPad windows;
  Dynamic Type size changes; and locale differences including layout direction
  and text length.
- **Width is the primary structural signal.** Regular width affords side-by-side
  layouts (split views, sidebars, popovers, multi-column). Compact width wants a
  single column, stacked navigation, and full-screen modals.

## Safe areas, layout guides, margins

- A **layout guide** is a rectangular region for positioning, aligning, and
  spacing content. The system provides guides for standard margins and for
  constraining text width to a readable measure; you can define custom guides.
  (Developer: `UILayoutGuide`, `NSLayoutGuide`.)
- A **safe area** is the part of a view not covered by bars or system features.
  Lay content out relative to it to avoid the Dynamic Island, the camera housing
  on some Macs, the status bar, and system bars. Safe areas also shift content
  automatically when bar sizes change. (Developer: `SafeAreaRegions`,
  positioning content relative to the safe area.)
- **Extend content to fill the screen/window.** Backgrounds and full-screen
  artwork reach the edges; scroll content continues to the bottom and sides.
  Because controls sit on a floating layer above content (next section), your
  content layer should pass beneath them rather than stop short.
- When content doesn't span the full width, use a **background extension view**
  to mirror adjacent content behind the control layer (e.g. beneath a sidebar or
  inspector). (Developer: `backgroundExtensionEffect()`, `UIBackgroundExtensionView`.)

## The Liquid Glass control layer & scroll edge effects

- Controls and navigation (tab bars, sidebars, toolbars) live on a distinct
  **Liquid Glass functional layer that floats above the content layer**,
  consistent across iOS, iPadOS, and macOS. Content scrolls and peeks through
  beneath them. This is why content should extend to the edges under bars.
- Don't put Liquid Glass in the content layer; use standard materials there.
- Use a **scroll edge effect** (not a solid bar background) to separate a
  floating bar from the scrolling content behind it. Prefer the automatic style;
  apply one per view; in split-view layouts each pane can have its own, kept
  consistent in height for alignment. (Developer: `ScrollEdgeEffectStyle`,
  `UIScrollEdgeEffect`, `NSScrollEdgeEffectStyle`.)

## Dynamic Type and text-driven layout

Dynamic Type lets people change text size in **iOS and iPadOS** (macOS does
**not** support it). It is a first-class layout input, not just a font setting.

- Use the built-in **text styles** with the system fonts (Body, Headline, Title,
  Caption, etc.) to get Dynamic Type and larger accessibility sizes automatically
  and scale proportionally.
- **The layout must adapt to every text size.** Verify at the largest
  accessibility size (Settings → Accessibility → Display & Text Size → Larger
  Text).
- Grow meaningful interface icons alongside text — SF Symbols scale with Dynamic
  Type automatically.
- Minimize truncation as size grows; let labels use as many lines as needed.
- **Reflow at large sizes:** when text grows in a horizontally constrained
  context, inline items and container edges crowd it. Switch to a **stacked
  layout** (text above secondary items) and **reduce column count** for
  multicolumn text. (Developer: `isAccessibilityCategory`.)
- Keep the information hierarchy stable regardless of text size (primary
  elements stay near the top).
- Default/minimum sizes: iOS/iPadOS 17 / 11 pt; macOS 13 / 10 pt. Prefer
  Regular–Bold weights over Ultralight/Thin/Light.

## Control sizing and spacing

Minimum comfortable hit targets (also an accessibility requirement):

| Platform | Default | Minimum |
|---|---|---|
| iOS / iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |

Spacing matters as much as size: ~12 pt padding around bezeled elements, ~24 pt
around the visible edges of non-bezeled elements. A button needs a hit region of
at least 44×44 pt on iOS/iPadOS.

## Orientation, resolution, artwork scaling

- A **point** is an abstract unit that keeps content consistent across displays;
  on 2D platforms it maps to a variable number of pixels by resolution. Provide
  bitmap assets at **@2x and @3x** (iPhones are typically @3x; many iPads @2x).
- When a context change alters the aspect ratio, **scale artwork, don't distort
  it** — keep important content visible and accept letterboxing/pillarboxing.
- Support both orientations where you can; if you support only one, work equally
  well rotated either way and don't instruct the user to rotate.

## Right-to-left and internationalization

- System frameworks flip the interface for RTL automatically; using system
  components and standard layouts often needs no work. Place important items on
  the leading/top and account for RTL when you customize.
- Flip directional controls (sliders, progress bars, back/next) and reverse the
  order of meaningfully-ordered images for RTL. Don't flip logos, universal
  marks, or the digits within a single number.
- Account for **text-length changes across localizations** — they drive
  truncation and wrapping. Keep labels short.

## Appearance adaptation (Dark Mode, materials, color, motion)

- Support both light and dark appearances and Auto; don't offer an app-specific
  appearance toggle — respect the systemwide choice.
- Prefer **system colors and materials**: they adapt automatically across
  appearance and accessibility settings (Increase Contrast, Reduce Transparency)
  and maintain contrast on varied backgrounds.
- Respond to **Reduce Motion**: reduce or replace animations (fades instead of
  x/y/z transitions; avoid animating z-axis depth) — relevant when layouts
  animate between adaptive states.
