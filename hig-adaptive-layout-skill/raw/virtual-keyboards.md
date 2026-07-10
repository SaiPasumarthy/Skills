# Virtual keyboards
URL: https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards
On devices without physical keyboards, the system offers various types of virtual keyboards. A virtual keyboard can provide a set of keys optimized for the current task (e.g. an email keyboard includes "@", ".", ".com"). A virtual keyboard doesn't support keyboard shortcuts. In iOS, iPadOS, and tvOS you can create a custom keyboard app extension.

ADAPTIVE NOTE: A virtual keyboard covers part of the screen when it appears — layouts must account for the keyboard reducing available content area (scroll the insertion point into view; on iPad, avoid auto-focusing a dedicated-area field to prevent the keyboard from unexpectedly covering the view — see Search fields).

Best practices: choose a keyboard type that matches the content people are editing; specify a semantic meaning for a text input area so the system provides the right keyboard.
Platform considerations: iOS, iPadOS, tvOS, visionOS. Developer: keyboardType (UIKit), textContentType.
