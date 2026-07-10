# Windows
URL: https://developer.apple.com/design/human-interface-guidelines/windows

A window presents UI views and components. In iPadOS, macOS, and visionOS, windows define visual boundaries of app content and enable multitasking workflows within and between apps. Windows include system-provided frames and window controls.

Two types: a **primary window** presents the main navigation and content; an **auxiliary window** presents a specific task or area (no navigation to other app areas, typically has a close button).

## Best practices
- Make sure your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows. See Layout and Multitasking.
- Choose the right moment to open a new window (great for multitasking or preserving context). Avoid opening new windows as default behavior unless it makes sense.
- Consider providing the option to view content in a new window (context menu or File menu command).
- Avoid creating custom window UI — system-provided windows look and behave in a recognizable way.
- Use the term "window" in user-facing content.

## Platform considerations
Not supported in iOS, tvOS, or watchOS.

### iPadOS
Windows present in one of two ways depending on the person's choice in Multitasking & Gestures settings:
- Full screen: app windows fill the entire screen; people switch using the app switcher.
- Windowed: people can freely resize app windows; multiple windows can be onscreen at once; people can reposition and bring them to the front. The system remembers window size and placement even when an app is closed.
- Make sure window controls don't overlap toolbar items. When windowed, app windows include window controls at the leading edge of the toolbar. If your app has leading-edge toolbar buttons, move them inward when the window controls appear.
- Consider letting people use a gesture to open content in a new window (e.g. pinch to expand a Notes item).
- Tip: you must support multiple windows in your app to present a single file in its own window.

### macOS
People typically run several apps at once, viewing windows from multiple apps on one desktop and switching frequently — moving, resizing, minimizing, revealing.
- Window anatomy: a frame and a body area. People move a window by dragging the frame and resize by dragging edges. The frame can include window controls and a toolbar; rarely a bottom bar below body content.
- Window states: **Main** (frontmost window people view; one per app), **Key/active** (accepts input; one onscreen at a time; usually the main window but could be a floating panel), **Inactive** (not in foreground). The system gives each a different appearance (key window uses color in title bar controls; inactive/non-key main windows use gray; inactive windows don't use vibrancy).
- Make sure custom windows use the system-defined appearances so people can identify the foreground window.
- Avoid putting critical information or actions in a bottom bar, because people often relocate a window so its bottom edge is hidden. If used, display only a small amount of related info (e.g. Finder status bar). Consider an inspector on the trailing side of a split view for more info.

### visionOS (out of scope, noted)
Two window styles: default (window) and volumetric (volume); both display 2D/3D content. Default window is 1280x720 pt, glass background, dynamic scale. Set minimum and maximum window sizes so layout adjusts across all sizes.

Resources: Layout, Split views, Multitasking. Developer: WindowGroup (SwiftUI), UIWindow (UIKit), NSWindow (AppKit).
Change log: June 9, 2025 — added best practices and guidance for resizable windows in iPadOS.
