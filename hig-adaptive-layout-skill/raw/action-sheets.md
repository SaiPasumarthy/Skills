# Action sheets
URL: https://developer.apple.com/design/human-interface-guidelines/action-sheets
An action sheet is a modal view presenting choices related to an action people initiate. In SwiftUI, use a confirmation dialog; in UIKit, UIAlertController.Style.actionSheet (iOS, iPadOS, tvOS).
ADAPTIVE NOTE: On iPhone an action sheet slides up from the bottom edge; on iPad it's presented in a POPOVER anchored to the control that triggered it. Design the trigger so the popover has a sensible anchor. (Confirmation dialogs adapt presentation by size class.)
Best practices: use an action sheet (not an alert) to offer choices related to an intentional action; keep the number of choices small; place destructive choices carefully.
