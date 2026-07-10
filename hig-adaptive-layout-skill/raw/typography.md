# Typography
URL: https://developer.apple.com/design/human-interface-guidelines/typography

## Ensuring legibility — default and minimum text sizes
| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Avoid light font weights (prefer Regular/Medium/Semibold/Bold).

## Conveying hierarchy
- Maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes.
- Prioritize important content when responding to text-size changes. When someone chooses a larger text size, they typically want the content they care about easier to read — they don't always want every word larger (e.g. tab titles don't need to grow).

## Using system fonts and text styles
San Francisco (SF) and New York (NY). The system defines **text styles** (Large Title, Title 1/2/3, Headline, Body, Callout, Subhead, Footnote, Caption 1/2) — each specifies font weight, point size, and leading. Text styles allow text to scale proportionately when people change the system's text size or make accessibility adjustments (Larger Text).
- Consider using the built-in text styles. Using text styles with the system fonts ensures support for **Dynamic Type** and larger accessibility type sizes.
- You can adjust leading (loose leading for wide columns/long passages; tight leading in height-constrained areas like a list row — but avoid tight leading for 3+ lines).

## Supporting Dynamic Type (KEY ADAPTIVE CONTENT)
Dynamic Type is a system-level feature in iOS, iPadOS, tvOS, visionOS, and watchOS that lets people adjust the size of visible text. **macOS doesn't support Dynamic Type.**
- **Make sure your app's layout adapts to all font sizes.** Verify your design scales and that text and glyphs are legible at all font sizes. Test with Settings > Accessibility > Display & Text Size > Larger Text.
- Increase the size of meaningful interface icons as font size increases (SF Symbols scale automatically with Dynamic Type).
- Keep text truncation to a minimum as font size increases. Aim to display as much useful text at the largest accessibility font size as at the largest standard size. Configure labels to use as many lines as needed (numberOfLines).
- **Consider adjusting your layout at large font sizes.** When font size increases in a horizontally constrained context, inline items (glyphs, timestamps) and container boundaries can crowd text and cause truncation/overlap. Consider a **stacked layout** where text appears above secondary items. **Multicolumn text** can be less readable at large sizes — **reduce the number of columns when the font size increases** to avoid truncation. Developer: isAccessibilityCategory.
- Maintain a consistent information hierarchy regardless of the current font size (keep primary elements toward the top of a view even when the font size is very large).

## Platform considerations
- iOS, iPadOS: SF Pro is the system font; can also use NY.
- macOS: SF Pro is the system font; NY available via Mac Catalyst. **macOS doesn't support Dynamic Type.** Use dynamic system font variants (controlContentFont, labelFont, menuFont, etc.) to match standard controls.
- visionOS: uses bolder Dynamic Type body/title styles; adds Extra Large Title 1/2 for wide editorial layouts. Prefer 2D text.
- watchOS: SF Compact system font.

## Specifications (adaptive reference — abbreviated)
iOS/iPadOS Dynamic Type Body at Large (default) = 17 pt (in the size selector: xSmall→xxxLarge). At larger accessibility sizes (AX1–AX5), Body grows to 28 pt (AX1) and larger. Large Title ranges 31 pt (default) → 44 pt (AX1). macOS built-in text styles are fixed (Body 13 pt, Large Title 26 pt) — no Dynamic Type. (Full Dynamic Type size tables available in Apple Design Resources per platform.)

Resources: Fonts for Apple platforms, SF Symbols, Accessibility. Videos: Get started with Dynamic Type.
Change log: March 7, 2025 — expanded guidance for Dynamic Type.
