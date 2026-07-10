# Panels
URL: https://developer.apple.com/design/human-interface-guidelines/panels

In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection. Less prominent appearance than a main window; can use a dark translucent HUD style. When your app runs on other platforms, consider using a modal view for supplementary content instead. See Modality.

## Best practices
- Use a panel to give quick access to important controls or info related to the content people are working with.
- Consider a panel to present inspector functionality (auto-updates as selection changes). For an Info window with fixed contents, use a regular window. You might also use a split view pane to present an inspector.
- Prefer simple adjustment controls (sliders, steppers) over typing/selection.
- Write a brief title describing the panel's purpose.
- Show/hide panels appropriately (bring to front when app active, hide when inactive).
- HUD-style panels: darker, translucent; use only in media-oriented apps or when a standard panel would obscure essential content; keep HUDs small.

## Platform considerations
Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS. (macOS-only component.)

Resources: Windows, Modality. Developer: NSPanel (AppKit).
