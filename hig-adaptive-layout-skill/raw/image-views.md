# Image views
URL: https://developer.apple.com/design/human-interface-guidelines/image-views
An image view displays a single image (or animated sequence) on a transparent/opaque background. Within an image view you can stretch, scale, size to fit, or pin the image to a specific location. Typically not interactive.

Best practices: Use an image view when the primary purpose is to display an image. Consider SF Symbols/interface icons for icons. Take care when overlaying text on images (ensure contrast). Use a consistent size for all images in an animated sequence to avoid runtime scaling.

Platform considerations: No additional considerations for iOS or iPadOS. macOS: use an image well for editable; use an image button for a clickable image. (tvOS/visionOS/watchOS out of scope.)
Resources: Images, Image wells, SF Symbols. Developer: Image (SwiftUI), UIImageView (UIKit), NSImageView (AppKit).
