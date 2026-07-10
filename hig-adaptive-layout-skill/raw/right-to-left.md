# Right to left
URL: https://developer.apple.com/design/human-interface-guidelines/right-to-left

Support right-to-left (RTL) languages like Arabic and Hebrew by reversing your interface as needed to match the reading direction. System-provided UI frameworks support RTL by default — system components flip automatically. If you use system-provided elements and standard layouts, you might not need any changes.

## Text alignment
- Adjust text alignment to match interface direction if the system doesn't do so automatically (left-align in LTR → right-align in RTL).
- Align a paragraph (3+ lines) based on its language, not the current context. Continue aligning one- and two-line text blocks to match the reading direction of the current context, but align a paragraph to match its language.
- Use a consistent alignment for all text items in a list (reverse alignment of all items, including items in a different script).

## Numbers and characters
- Different RTL languages use different number systems (Hebrew uses Western Arabic numerals; Arabic may use Western or Eastern).
- Don't reverse the order of numerals in a specific number (phone number, credit card).
- Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves.

## Controls
- Flip controls that show progress from one value to another (sliders, progress indicators); reverse the positions of accompanying begin/end glyphs.
- Flip controls that help people navigate or access items in a fixed order (in RTL, a back button points to the right; next/previous buttons flip).
- Preserve the direction of a control that refers to an actual direction or points to an onscreen area.
- Visually balance adjacent Latin and RTL scripts (increase RTL font size by ~2 points next to uppercased Latin text).

## Images and interface icons
- Avoid flipping images like photographs, illustrations, general artwork.
- Reverse the positions of images when their order is meaningful.
- SF Symbols provides RTL variants and localized symbols for Arabic/Hebrew.
- Flip interface icons that represent text/reading direction or forward/backward motion.
- Don't flip logos or universal signs/marks. In general avoid flipping icons that depict real-world objects.

## Platform considerations
No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Resources: Layout, Inclusion, SF Symbols, Localization. Videos: Design for Arabic.
