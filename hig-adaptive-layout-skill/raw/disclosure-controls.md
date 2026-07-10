# Disclosure controls
URL: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls

Disclosure controls reveal and hide information and functionality related to specific controls or views.

## Best practices
- Use a disclosure control to hide details until they're relevant. Place controls people are most likely to use at the top of the disclosure hierarchy (always visible), with advanced functionality hidden by default. (Progressive disclosure — relevant to adaptive/space-constrained layouts.)

Disclosure triangles: point inward from the leading edge when content is hidden, down when visible (used in Finder list view, Keynote export options). Provide a descriptive label.
Disclosure buttons: point down when hidden, up when visible (e.g. macOS Save sheet). Place near the content it shows/hides; use no more than one per view.

## Platform considerations
No additional considerations for macOS. Not supported in tvOS or watchOS.
- iOS, iPadOS, visionOS: available with the SwiftUI DisclosureGroup view.

Resources: Outline views, Lists and tables, Buttons. Developer: DisclosureGroup (SwiftUI).
