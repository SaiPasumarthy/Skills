# Materials
URL: https://developer.apple.com/design/human-interface-guidelines/materials

A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements. Two types: Liquid Glass and standard materials.

## Liquid Glass (relevant to adaptive layout — the control/navigation layer)
Liquid Glass forms a distinct **functional layer for controls and navigation elements — like tab bars and sidebars — that floats above the content layer**, establishing a clear visual hierarchy. Content scrolls and peeks through from beneath these elements.
- Don't use Liquid Glass in the content layer; use standard materials for content-layer elements like app backgrounds.
- Use Liquid Glass effects sparingly. Standard system components pick up the appearance/behavior automatically.
- Two variants: **regular** (blurs and adjusts luminosity of background to maintain legibility; most system components; use for alerts, sidebars, popovers) and **clear** (highly translucent; for components over visually rich media backgrounds).
- The variants' appearance can differ in response to system settings (preferred look, reduce transparency, increase contrast).

## Standard materials
Convey structure in the content beneath Liquid Glass (blur, vibrancy, blending). Thicker materials = more opaque = better contrast; thinner materials = more translucent = help retain context.

## Platform considerations
### iOS, iPadOS
Four standard materials: ultraThin, thin, regular (default), thick. Vibrant colors for labels/fills/separators designed to work with each material.
### macOS
Several standard materials with designated purposes; vibrant versions of all system colors. Two background blending modes: behind window and within window.
### tvOS / visionOS / watchOS (out of scope, noted)
visionOS: windows use a system-defined "glass" material; no distinct Dark Mode (glass adapts to luminance). watchOS: use materials for context in full-screen modal views.

Resources: Color, Accessibility, Dark Mode. Developer: Material (SwiftUI), UIVisualEffectView (UIKit), NSVisualEffectView (AppKit).
Change log: Sept 9, 2025 / June 9, 2025 — Liquid Glass guidance.
