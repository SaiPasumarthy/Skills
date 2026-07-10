# Accessibility
URL: https://developer.apple.com/design/human-interface-guidelines/accessibility

An accessible interface is Intuitive, Perceivable, and **Adaptable** — it adapts to how people want to use their device, whether by supporting system accessibility features or letting people personalize settings.

## Vision (layout-relevant)
- Support larger text sizes. Give people the option to enlarge text by at least 200% (140% in watchOS). Support font size enlargement through custom UI or by adopting **Dynamic Type**. See Supporting Dynamic Type (Typography).
- Use recommended defaults for custom type sizes:
  | Platform | Default | Minimum |
  |---|---|---|
  | iOS, iPadOS | 17 pt | 11 pt |
  | macOS | 13 pt | 10 pt |
  | tvOS | 29 pt | 23 pt |
  | visionOS | 17 pt | 12 pt |
  | watchOS | 16 pt | 12 pt |
- Strive to meet color-contrast minimums (WCAG AA: 4.5:1 up to 17 pt; 3:1 at 18 pt or bold). Provide a higher-contrast scheme when Increase Contrast is on. Check contrast in both light and dark appearances.
- Prefer system-defined colors (accessible variants adapt when people adjust preferences).
- Convey information with more than color alone.

## Mobility — control sizes (KEY ADAPTIVE/LAYOUT REFERENCE)
Offer sufficiently sized controls:
| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

- Consider spacing between controls as important as size. ~12 pt of padding around elements with a bezel; ~24 pt around the visible edges of elements without a bezel.
- Support simple gestures; offer alternatives to gestures (e.g. provide a button alongside a swipe-to-dismiss).
- Support Full Keyboard Access, Voice Control, Switch Control.

## Cognitive
- Keep actions simple; minimize time-boxed interface elements.
- Respond to **Reduce Motion**: reduce automatic/repetitive animations (zooming, scaling, peripheral motion); replace x/y/z-axis transitions with fades; avoid animating depth changes in z-axis layers.
- Optimize your app's UI for **Assistive Access** (iOS/iPadOS) — a streamlined version with a default layout and control presentation that reduces cognitive load. Identify core functionality, break up multistep workflows to one interaction per screen.

## Platform considerations
No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS. visionOS: Pointer Control (head/hand), Zoom; prioritize comfort (keep elements within field of view, prefer horizontal layouts over vertical to avoid neck strain).

Resources: Inclusion, Typography, VoiceOver.
Change log: March 7, 2025 — moved Dynamic Type guidance to Typography.
