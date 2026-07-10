# Layout
URL: https://developer.apple.com/design/human-interface-guidelines/layout

A consistent layout that adapts to various contexts makes your experience more approachable and helps people enjoy their favorite apps and games on all their devices. People expect familiar relationships between controls and content.

## Best practices
- Group related items to help people find information. Use negative space, background shapes, colors, materials, or separator lines to show relationships and separate information into distinct areas. Keep content and controls clearly distinct.
- Make essential information easy to find by giving it sufficient space. Don't obscure important info by crowding it; make secondary information available in other parts of the window or an additional view.
- Extend content to fill the screen or window. Backgrounds and full-screen artwork extend to the edges of the display. Scrollable layouts continue all the way to the bottom and sides. Controls and navigation components like sidebars and tab bars appear on top of content rather than on the same plane — layout must take this into account.
- When content doesn't span the full window, use a background extension view to provide the appearance of content behind the control layer on either side (e.g. beneath the sidebar or inspector). Developer: backgroundExtensionEffect() and UIBackgroundExtensionView.

## Visual hierarchy
- Differentiate controls from content. Take advantage of the Liquid Glass material to provide a distinct appearance for controls that's consistent across iOS, iPadOS, and macOS. Instead of a background, use a scroll edge effect to provide a transition between content and the control area. See Scroll views.
- Place items to convey relative importance. People start viewing in reading order — top to bottom and leading to trailing — so place the most important items near the top and leading side. Reading order varies by language; account for right-to-left languages.
- Align components with one another to make them easier to scan and to communicate organization and hierarchy. Along with indentation, alignment helps people understand an information hierarchy.
- Take advantage of progressive disclosure to help people discover hidden content. Use a disclosure control, or display parts of items to hint that people can reveal additional content by scrolling.
- Make controls easier to use by providing enough space around them and grouping them in logical sections. See Toolbars.

## Adaptability
Every app and game needs to adapt when the device or system context changes. In iOS, iPadOS, tvOS, and visionOS, the system defines a collection of traits that characterize variations in the device environment that can affect the way your app looks. Using SwiftUI or Auto Layout helps ensure your interface adapts dynamically to these traits and other context changes.

Common device and system variations you need to handle:
- Different device screen sizes, resolutions, and color spaces
- Different device orientations (portrait/landscape)
- System features like Dynamic Island and camera controls
- External display support, Display Zoom, and resizable windows on iPad
- Dynamic Type text-size changes
- Locale-based internationalization: left-to-right/right-to-left layout direction, date/time/number formatting, font variation, and text length

Guidance:
- Design a layout that adapts gracefully to context changes while remaining recognizably consistent. People expect your experience to work well and remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. Respect system-defined safe areas, margins, and guides, and specify layout modifiers to fine-tune placement of views.
- Be prepared for text-size changes. Support Dynamic Type — a feature that lets people choose the size of visible text in iOS, iPadOS, tvOS, visionOS, and watchOS — so your app responds appropriately when people adjust text size. See Typography.
- Preview your app on multiple devices, using different orientations, localizations, and text sizes. Test the largest and smallest layouts first. Use the simulator to make sure layouts look great whether the device rotates left or right.
- When necessary, scale artwork in response to display changes. A different aspect ratio might make artwork appear cropped, letterboxed, or pillarboxed. Don't change the aspect ratio; instead scale so important visual content remains visible.

## Guides and safe areas
- A layout guide defines a rectangular region that helps you position, align, and space content. The system includes predefined layout guides for standard margins and to restrict the width of text for optimal readability. You can also define custom layout guides. Developer: UILayoutGuide and NSLayoutGuide.
- A safe area defines the area within a view that isn't covered by a toolbar, tab bar, or other views a window might provide. Safe areas are essential for avoiding a device's interactive and display features, like Dynamic Island on iPhone or the camera housing on some Mac models. Developer: SafeAreaRegions and Positioning content relative to the safe area.
- Respect key display and system features in each platform. In addition to helping avoid display and system features, safe areas help account for interactive components like bars, dynamically repositioning content when sizes change.

## Platform considerations

### iOS
- Aim to support both portrait and landscape orientations. If your experience needs to run in only portrait or only landscape, rely on people trying both orientations — no need to tell people to rotate. If landscape-only, make sure it runs equally well whether people rotate left or right.
- Prefer a full-bleed interface for your game, accommodating the corner radius, sensor housing, and Dynamic Island; optionally offer letterboxed/pillarboxed appearance.
- Avoid full-width buttons. Buttons feel at home when they respect system-defined margins and are inset from the edges. A full-width button should harmonize with the curvature of the hardware and align with adjacent safe areas.
- Hide the status bar only when it adds value (e.g. in-depth game or media viewing). Otherwise keep it visible.

### iPadOS
- People can freely resize windows down to a minimum width and height, similar to macOS. Account for this resizing behavior and the full range of possible window sizes when designing your layout. See Multitasking and Windows.
- As someone resizes a window, defer switching to a compact view for as long as possible. Design for a full-screen view first, and only switch to a compact view when a version of the full layout no longer fits. This makes the UI feel more stable and familiar. For complex layouts such as split views, prefer hiding tertiary columns such as inspectors as the view narrows.
- Test your layout at common system-provided sizes, and provide smooth transitions. Window controls let people arrange windows to fill halves, thirds, and quadrants of the screen; check your layout at each of these sizes on a variety of devices. Minimize unexpected UI changes from minimum to maximum window size.
- Consider a convertible tab bar for adaptive navigation. You don't need to choose between a tab bar or sidebar; adopt a style of tab bar that provides both. The app first launches with your choice of a sidebar or tab bar, and people can tap to switch. As the view resizes, the presentation style changes to fit the width of the view. See Tab bars. Developer: sidebarAdaptable.

### macOS
- Avoid placing controls or critical information at the bottom of a window. People often move windows so the bottom edge is below the bottom of the screen.
- Avoid displaying content within the camera housing at the top edge of the window. Developer: NSPrefersDisplaySafeAreaCompatibilityMode.

### tvOS (out of scope — noted only)
Layouts don't automatically adapt to screen size; same interface on every display. Inset primary content 60 pt top/bottom, 80 pt sides.

### visionOS (out of scope — noted only)
Center important content and controls; keep a window's content within its bounds; use ornaments for extra controls; place buttons at least 60 pt apart.

### watchOS (out of scope — noted only)
Content extends edge to edge; avoid more than two or three controls side by side.

## Specifications — iOS/iPadOS size classes (KEY ADAPTIVE REFERENCE)
A size class is a value that's either **regular** or **compact**, where regular refers to a larger screen or a screen in landscape orientation and compact refers to a smaller screen or a screen in portrait orientation. Developer: UserInterfaceSizeClass. Different size class combinations apply to the full-screen experience on different devices based on screen size.

- All iPad models (Pro 12.9/11/10.5-inch, Air 13/11-inch, iPad 11/9.7-inch, iPad mini): **Regular width, Regular height** in BOTH portrait and landscape.
- iPhone (standard/Pro, non-Plus/non-Max, e.g. iPhone 17 Pro, 17, 16 Pro, 16, 16e, 15 Pro, 15, SE): **Portrait = Compact width, Regular height**; **Landscape = Compact width, Compact height**.
- iPhone Plus/Max models (e.g. 17 Pro Max, 16 Pro Max, 16 Plus, 15 Pro Max, 15 Plus, 14 Pro Max, iPhone Air): **Portrait = Compact width, Regular height**; **Landscape = Regular width, Compact height**.

Implication: iPhone is compact-width in portrait for all models; only the larger "Max/Plus" iPhones become regular-width in landscape. iPad is regular-width/height in all orientations at full screen (but multitasking/resized windows change the effective size class — a resized iPad window can become compact width).

Note: iOS/iPadOS device screen dimensions are given in points and pixels at their UIKit scale factor (@2x or @3x). Examples: iPad Pro 13-inch 1032x1376 pt @2x; iPhone 16 393x852 pt @3x; iPhone 16 Pro Max 440x956 pt @3x; iPhone SE (4.7-inch) 375x667 pt @2x. UIKit scale factors may differ from native scale factors (scale vs nativeScale).

Resources: Right to left, Spatial layout, Layout and organization. Developer: Composing custom layouts with SwiftUI. Videos: Compose custom layouts with SwiftUI, Essential Design Principles.

Change log highlights: June 9, 2025 — Added guidance for Liquid Glass. June 21, 2023 — Updated to include guidance for visionOS.
