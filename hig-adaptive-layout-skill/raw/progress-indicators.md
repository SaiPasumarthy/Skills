# Progress indicators
URL: https://developer.apple.com/design/human-interface-guidelines/progress-indicators
Progress indicators let people know your app isn't stalled while loading or performing lengthy operations. All are transient. Two types: determinate (well-defined duration; fills a linear or circular track — progress bars fill from the LEADING side to the TRAILING side, so they reverse in RTL) and indeterminate (unquantifiable tasks; spinner).
Best practices: be specific about what's happening when possible; use a determinate indicator when you can estimate duration; keep the interface responsive.
Platform considerations: iOS, iPadOS, macOS, etc. Developer: ProgressView (SwiftUI), UIActivityIndicatorView/UIProgressView (UIKit), NSProgressIndicator (AppKit).
