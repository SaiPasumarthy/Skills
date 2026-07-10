# Sheets
URL: https://developer.apple.com/design/human-interface-guidelines/sheets

A sheet helps people perform a scoped task closely related to their current context.

## Anatomy
In macOS, tvOS, visionOS, and watchOS, a sheet is always modal. In iOS and iPadOS, a sheet can be either modal or nonmodal (a nonmodal sheet affects the parent view without dismissing, e.g. Notes format sheet). Common buttons: Cancel/Close (dismiss without saving), Done (dismiss after completing/saving), Back (previous step; not for dismissing). Button placement varies by platform.

## Best practices
- For complex or prolonged flows, consider alternatives: iOS/iPadOS full-screen modal for media or multistep tasks; macOS a new window or full-screen mode; visionOS a Full Space.
- Display only one sheet at a time from the main interface.
- Use a nonmodal view when presenting supplementary items that affect the main task: split view in visionOS, a panel in macOS, or a nonmodal sheet in iOS/iPadOS.
- Provide an alternative to the Done button (pair with Cancel or Back). Avoid showing all three (Cancel, Done, Back) together.

## Platform considerations
No additional considerations for tvOS.
### iOS, iPadOS (KEY ADAPTIVE DETAIL)
- For single-view sheets, the Cancel button belongs on the leading edge of the top toolbar; Done on the trailing edge.
- A resizable sheet expands via scrolling or dragging the grabber. Sheets resize according to **detents** — heights at which a sheet naturally rests. The system defines two: **large** (fully expanded height) and **medium** (about half). Sheets can have custom detent values. Sheets automatically support large; adding medium allows resting at both heights.
- In an iPhone app, consider supporting the medium detent for progressive disclosure (e.g. share sheet). Some sheets (Messages/Mail compose) display only at full height.
- Include a grabber in a resizable sheet (tap to cycle detents; works with VoiceOver).
- Support swiping to dismiss.
- Prefer the **page or form sheet** presentation styles in an iPadOS app — each uses a default size, centering content on a dimmed background for a consistent experience. Developer: UIModalPresentationStyle.
### macOS
- A cardlike view floating on top of its parent window; parent window is dimmed. Present in a reasonable default size (people don't generally expect to resize sheets, but support resizing when useful).
- Let people interact with other app windows without first dismissing a sheet.
- Use a panel instead of a sheet if people need to repeatedly provide input and observe results.
### visionOS / watchOS (out of scope, noted)
visionOS: floats in front of parent, avoid emerging from bottom edge, center in field of view. watchOS: full-screen semitransparent view.

Resources: Modality, Action sheets, Popovers, Panels. Developer: sheet (SwiftUI), UISheetPresentationController (UIKit), presentAsSheet (AppKit).
Change log: March 29, 2024 — use form or page sheet styles in iPadOS apps.
