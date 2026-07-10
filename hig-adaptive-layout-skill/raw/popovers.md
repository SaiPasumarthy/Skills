# Popovers
URL: https://developer.apple.com/design/human-interface-guidelines/popovers

A popover is a transient view that appears above other content when people click or tap a control or interactive area.

## Best practices
- Use a popover to expose a small amount of information or functionality (a few related tasks).
- Consider popovers when you want more room for content (vs sidebars/panels which take up a lot of space).
- Position popovers appropriately — the arrow points as directly as possible to the element that revealed it; don't cover that element or essential content.
- Use a Close button for confirmation and guidance only; otherwise a popover closes when people click/tap outside or select an item.
- Always save work when automatically closing a nonmodal popover.
- Show one popover at a time; never a cascade/hierarchy.
- Don't show another view over a popover (except an alert).
- Avoid making a popover too big.
- Avoid using a popover to show a warning (use an alert).

## Platform considerations
No additional considerations for visionOS. Not supported in tvOS or watchOS.
### iOS, iPadOS (KEY ADAPTIVE CALLOUT)
- **Avoid displaying popovers in compact views.** Make your app dynamically adjust its layout based on the **size class** of the content area. Reserve popovers for **wide (regular-width) views**; for **compact views**, use all available screen space by presenting information in a full-screen modal view like a **sheet** instead. See Modality.
### macOS
- You can make a popover detachable, which becomes a separate panel when people drag it (remains visible while people interact with other content). Make minimal appearance changes to a detached popover.

Resources: Sheets, Action sheets, Alerts, Modality. Developer: popover (SwiftUI), UIPopoverPresentationController (UIKit), NSPopover (AppKit).
