# Dark Mode
URL: https://developer.apple.com/design/human-interface-guidelines/dark-mode
Dark Mode is a systemwide appearance setting using a dark color palette. In iOS, iPadOS, macOS, and tvOS people often choose Dark Mode as default and expect all apps to respect their preference.
Best practices:
- Avoid offering an app-specific appearance setting (people expect the systemwide choice to apply).
- Ensure your app looks good in BOTH appearance modes (adapt appearance — a form of adaptive design). People can also choose Auto, which switches between light and dark.
- Use system colors and materials (they adapt automatically to the current appearance).
- Test your content in both light and dark appearances.
Platform considerations: not supported in watchOS; visionOS has no distinct Dark Mode (glass adapts to luminance).
Developer: preferredColorScheme (SwiftUI), UIUserInterfaceStyle (UIKit).
