# Drag and drop
URL: https://developer.apple.com/design/human-interface-guidelines/drag-and-drop
People move or duplicate content by dragging from a source to a destination. Locations can be in the same container (a text view), different containers (text views on opposite sides of a SPLIT VIEW), or DIFFERENT APPS.
Rules: dropping within the same container moves; dropping in a different container copies; dragging between apps always copies.
ADAPTIVE NOTE: Drag and drop across apps and across split-view panes is central to iPadOS multitasking — design layouts (split views, multiple windows) to support it (see Multitasking, Split views).
Best practices: provide clear drop targets and visual feedback; support spring loading on macOS/iPad.
Platform considerations: iOS, iPadOS, macOS. Developer: drag/drop modifiers (SwiftUI), UIDragInteraction (UIKit).
