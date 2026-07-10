# Going full screen
URL: https://developer.apple.com/design/human-interface-guidelines/going-full-screen

iPhone, iPad, and Mac offer full-screen modes that let people expand a window to fill the screen, hiding system controls for a distraction-free environment. Apple TV/Watch don't offer full-screen (apps already fill the screen); visionOS uses immersive experiences instead.

## Best practices
- Support full-screen mode when it makes sense (games, media viewing, in-depth tasks).
- If necessary, adjust your layout in full-screen mode, but DON'T programmatically resize your window. When a window is larger in full-screen mode, keep essential content prominent while making good use of the extra space — adjust proportions subtly without changing which items appear, to avoid jarring transitions.
- Continue to provide access to essential features and controls so people can complete their task without exiting full-screen.
- Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode.
- Help people resume where they left off after switching away.
- Let people choose when to exit full-screen mode.
- Prioritize content by temporarily hiding toolbars and navigation controls; let people restore hidden elements with a familiar gesture (tapping, swiping down, moving the cursor to the top of the screen). Keep controls visible when essential.

## Platform considerations
Not supported in tvOS, visionOS, or watchOS.
### iOS, iPadOS
Consider deferring system gestures to prevent accidental exits. By default the Home Screen indicator auto-hides shortly after switching to your app; it reappears on interaction with the bottom of the screen, allowing one swipe to exit. You can enable two swipes rather than one if needed. Developer: preferredScreenEdgesDeferringSystemGestures.
### macOS
Use the system-provided full-screen experience — it automatically accommodates areas like the camera housing at the top-center of some Mac models. Always let people choose when to enter full-screen (Enter Full Screen button, View menu, Control-Command-F). Developer: toggleFullScreen(_:).

Resources: Layout, Multitasking, Windows, The menu bar.
Change log: June 9, 2025 — updated guidance for hiding toolbars/navigation controls and deferring Home Screen indicator gestures.
