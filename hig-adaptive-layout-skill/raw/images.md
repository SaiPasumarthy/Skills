# Images
URL: https://developer.apple.com/design/human-interface-guidelines/images
Deliver artwork at the appropriate scale factors so it looks great on all devices.

ADAPTIVE/RESOLUTION REFERENCE:
- A POINT is an abstract unit of measurement that keeps visual content consistent regardless of display. In 2D platforms, a point maps to a number of pixels that varies with display resolution; in visionOS a point is an angular value.
- SCALE FACTOR determines the resolution of a bitmap image: @1x = 1:1 pixel density; @2x and @3x pack more pixels per point. Provide @2x and @3x assets so images stay crisp across iPhone/iPad displays (iPhones are typically @3x; many iPads @2x).
- Design so artwork scales gracefully across aspect ratios (see Layout: scale artwork, avoid changing aspect ratio; letterbox/pillarbox rather than distort).

Best practices: provide all needed scale factors; prefer SF Symbols/vector for icons; use PNG for bitmaps, support wide color/HDR where relevant.
Platform considerations: iOS, iPadOS, macOS. Developer: asset catalogs.
