# Modality
URL: https://developer.apple.com/design/human-interface-guidelines/modality

Modality presents content in a separate, dedicated mode that prevents interaction with the parent view and requires an explicit action to dismiss.

Components by platform: all platforms can present an alert. iOS, iPadOS, and macOS apps tend to use sheets or popovers for distinct tasks; iPadOS, macOS, and visionOS apps might also just use a separate window. For a temporary experience or multistep task, apps can offer a full-screen modal experience.

## Best practices
- Present content modally only when there's a clear benefit.
- Aim to keep modal tasks simple, short, and streamlined.
- Avoid creating a modal experience that feels like an app within your app.
- Consider a full-screen modal style for in-depth content or a complex task. In visionOS Shared Space, a full-screen modal fills a window; in a Full Space it can become a more immersive experience.
- Always give people an obvious way to dismiss a modal view. Platform conventions: in iOS, iPadOS, and watchOS people expect a button in the top toolbar or swipe down; in macOS and tvOS people expect a button in the main content view.
- When necessary, help people avoid data loss by getting confirmation before closing.
- Make it easy to identify a modal view's task (provide a title).
- Let people dismiss a modal view before presenting another one; never display more than one alert at a time.

## Platform considerations
No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Resources: Sheets, Alerts, Popovers, Action sheets, Activity views. Developer: UIModalPresentationStyle (UIKit).
