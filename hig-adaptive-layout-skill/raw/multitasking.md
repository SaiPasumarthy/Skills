# Multitasking
URL: https://developer.apple.com/design/human-interface-guidelines/multitasking

Multitasking lets people switch quickly from one app to another. With rare exceptions (some games, visionOS Full Space apps), every app needs to work well with multitasking.

## Best practices
- Because you don't know when people will initiate multitasking, your app always needs to be prepared to save and restore their context.
- Pause activities that require attention or active participation when people switch away; let them continue as if they never left.
- Respond smoothly to audio interruptions (pause for primary audio like music/podcasts; duck for shorter interruptions like GPS). See Playing audio.
- Finish user-initiated tasks in the background (downloads, video processing).
- Use notifications sparingly.

## Platform considerations
Not supported in watchOS.

### iOS
On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while using a different app. The app switcher displays all currently open apps. A current FaceTime call can continue while people use another app.

### iPadOS
On iPad, people can view and interact with the windows of several different apps at the same time. An individual app can also support multiple open windows. People can use iPad with either full-screen or windowed apps.
- Full screen: apps occupy the full screen; switch between individual app windows using the app switcher.
- Windowed: app windows are resizable, and people can arrange them to suit their needs with behavior similar to macOS. The system provides window controls for common tiling configurations, entering full screen, minimizing, and closing windows. The system identifies the frontmost window by coloring its window controls and casting a drop shadow on windows behind it.
- Videos and FaceTime calls can play in a Picture in Picture overlay above other content, regardless of whether apps are full screen or windowed.
- Apps DON'T control multitasking configurations or receive any indication of the ones people choose. To help your app respond correctly when people open it while windowed, make sure it adapts gracefully to different screen sizes. See Layout and Windows. Developer: Multitasking on iPad, Mac, and Apple Vision Pro.

### macOS
On Mac, multitasking is the default experience — people typically run more than one app at a time, switching between windows and tasks. When multiple app windows are open, macOS applies drop shadows so windows appear layered on the desktop, and applies visual effects to help people distinguish window states.

### tvOS / visionOS (out of scope, noted)
tvOS: Picture in Picture while browsing. visionOS: multiple apps in Shared Space; only one window active at a time.

Change log: June 9, 2025 — added guidance for multitasking with multiple windows in iPadOS.
