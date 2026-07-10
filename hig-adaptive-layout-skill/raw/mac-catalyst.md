# Mac Catalyst
URL: https://developer.apple.com/design/human-interface-guidelines/mac-catalyst
Mac Catalyst creates a Mac version of your iPad app. KEY ADAPTIVE TOPIC: adapting an iPad layout to the Mac environment.

Great candidates already support key iPad features:
- Drag and drop — carries over to the Mac version automatically.
- Keyboard navigation and shortcuts — Mac users expect both; build them into the iPad app.
- Multitasking — apps that scale their interface to support Split View, Slide Over, and Picture in Picture lay the groundwork for the extensive WINDOW RESIZABILITY Mac users expect.

Guidance:
- Choose whether to scale the interface to match the Mac idiom (the "Optimize for Mac" option renders controls at native macOS sizes and enables full native behavior) or keep the iPad idiom scaled to ~77%.
- Adopt Mac conventions: a menu bar with standard menus, a window toolbar, pointer/keyboard support, and standard window controls.
- Ensure your layout handles the wide range of window sizes (down to a minimum) that Mac users expect — the same adaptability that supports iPad windowing (see Layout, Windows, Multitasking).
- Replace iOS-specific patterns (e.g. large titles, bottom tab bars) with Mac-appropriate equivalents (toolbars, sidebars) where needed.

Platform considerations: macOS (from iPad apps). Developer: Mac Catalyst.
