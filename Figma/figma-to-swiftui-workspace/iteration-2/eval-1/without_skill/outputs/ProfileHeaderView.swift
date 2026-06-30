import SwiftUI

// Generated from Figma node "Profile Header" (20:1)
//
// Layout summary from the Figma JSON:
//   FRAME "Profile Header"  — HORIZONTAL auto-layout
//     itemSpacing: 12, padding: 12 / 16 / 12 / 16 (T/R-L/B)
//     counterAxisAlignItems: CENTER (vertical centering)
//     primaryAxisAlignItems: MIN (leading), fills width, hugs height
//     fill: white (#FFFFFF), frame size 375 x 72
//   ├─ ELLIPSE "Avatar"        — 48 x 48, IMAGE fill (scaleMode FILL)
//   ├─ FRAME  "Name Block"     — VERTICAL auto-layout, itemSpacing 2, leading aligned, hugs
//   │    ├─ TEXT "User Name"   — "Ada Lovelace", 16pt / weight 600, color #1A1F29
//   │    └─ TEXT "Handle"      — "@ada",        13pt / weight 400, color #80878F
//   └─ VECTOR "Settings Icon"  — 24 x 24, tint #666E7A

struct ProfileHeaderView: View {

    // MARK: - Model (mirrors the values baked into the Figma design)

    var name: String = "Ada Lovelace"
    var handle: String = "@ada"

    /// Optional avatar image. When nil a neutral placeholder is shown so the
    /// view renders without a remote/asset dependency.
    var avatar: Image? = nil

    /// Invoked when the trailing settings icon is tapped.
    var onSettingsTapped: () -> Void = {}

    // MARK: - Design tokens (derived from Figma RGBA values)

    private enum Tokens {
        // Frame
        static let background = Color.white                                   // r:1 g:1 b:1
        static let itemSpacing: CGFloat = 12
        static let paddingHorizontal: CGFloat = 16
        static let paddingVertical: CGFloat = 12

        // Avatar
        static let avatarSize: CGFloat = 48

        // Name block
        static let nameBlockSpacing: CGFloat = 2
        static let nameSize: CGFloat = 16
        static let nameColor = Color(red: 0.10, green: 0.12, blue: 0.16)       // #1A1F29
        static let handleSize: CGFloat = 13
        static let handleColor = Color(red: 0.50, green: 0.53, blue: 0.58)     // #80878F

        // Settings icon
        static let iconSize: CGFloat = 24
        static let iconColor = Color(red: 0.40, green: 0.43, blue: 0.48)       // #666E7A
    }

    // MARK: - Body

    var body: some View {
        HStack(spacing: Tokens.itemSpacing) {            // HORIZONTAL layout
            avatarView                                   // Avatar (ELLIPSE)

            VStack(alignment: .leading, spacing: Tokens.nameBlockSpacing) {  // Name Block
                Text(name)                               // User Name
                    .font(.system(size: Tokens.nameSize, weight: .semibold)) // weight 600
                    .foregroundColor(Tokens.nameColor)

                Text(handle)                             // Handle
                    .font(.system(size: Tokens.handleSize, weight: .regular)) // weight 400
                    .foregroundColor(Tokens.handleColor)
            }
            .fixedSize(horizontal: true, vertical: true) // HUG contents

            Spacer(minLength: 0)                         // primaryAxisAlignItems: MIN -> push icon to trailing

            settingsButton                              // Settings Icon (VECTOR)
        }
        .padding(.horizontal, Tokens.paddingHorizontal)
        .padding(.vertical, Tokens.paddingVertical)
        .frame(maxWidth: .infinity, alignment: .center)  // layoutSizingHorizontal: FILL
        .background(Tokens.background)                    // white frame fill
    }

    // MARK: - Subviews

    private var avatarView: some View {
        Group {
            if let avatar {
                avatar
                    .resizable()
                    .scaledToFill()                      // scaleMode: FILL
            } else {
                placeholderAvatar
            }
        }
        .frame(width: Tokens.avatarSize, height: Tokens.avatarSize)
        .clipShape(Circle())                             // ELLIPSE (square -> circle)
    }

    private var placeholderAvatar: some View {
        Circle()
            .fill(Color(red: 0.90, green: 0.91, blue: 0.93))
            .overlay(
                Image(systemName: "person.fill")
                    .font(.system(size: Tokens.avatarSize * 0.5))
                    .foregroundColor(Tokens.handleColor)
            )
    }

    private var settingsButton: some View {
        Button(action: onSettingsTapped) {
            Image(systemName: "gearshape")               // stand-in for the VECTOR settings glyph
                .resizable()
                .scaledToFit()
                .frame(width: Tokens.iconSize, height: Tokens.iconSize)
                .foregroundColor(Tokens.iconColor)
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Settings")
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 0) {
        ProfileHeaderView(name: "Ada Lovelace", handle: "@ada")
        Divider()
    }
    .frame(width: 375)
    .background(Color(white: 0.96))
}
