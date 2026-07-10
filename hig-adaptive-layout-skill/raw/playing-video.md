# Playing video
URL: https://developer.apple.com/design/human-interface-guidelines/playing-video
System-provided video players embed playback in iOS, iPadOS, macOS, tvOS, visionOS. Support different aspect-ratio playback modes and (most platforms) Picture in Picture (PiP).
ADAPTIVE NOTE: The system selects a playback mode based on the video's aspect ratio — full-screen/aspect-fill (scales to fill, some edges cropped) vs aspect-fit (letterbox/pillarbox). PiP lets video continue in a floating overlay while people use other apps (see Multitasking). Design player controls to overlay and adapt to orientation/size.
Best practices: use the system video player; make controls easy to reveal/hide; support PiP.
Developer: AVPlayerViewController (UIKit), VideoPlayer (SwiftUI).
