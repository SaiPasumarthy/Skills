// ProfileHeaderView.swift
// Generated from Figma node 'Profile Header' (id 20:1).
// Hand-finished per references/mapping.md:
//  - Avatar (ELLIPSE + IMAGE fill, scaleMode FILL) -> circular, scaledToFill + clip.
//  - Literal strings promoted to bindable properties (data binding).
//  - Settings icon (VECTOR) wired up as a tappable Button (interactivity) and
//    tinted with its Figma fill color (#666E7A), which the generator left for
//    human judgment on vectors.
//  - Trailing Spacer so the settings icon sits at the row's trailing edge
//    (the frame is FILL width, primaryAxisAlignItems MIN).

import SwiftUI

struct ProfileHeaderView: View {
    let name: String
    let handle: String
    var avatarImage: String = "Avatar"
    var onSettingsTapped: () -> Void = {}

    var body: some View {
        HStack(alignment: .center, spacing: 12) {
            Image(avatarImage)
                .resizable()
                .scaledToFill()
                .frame(width: 48, height: 48)
                .clipShape(Circle())
            VStack(alignment: .leading, spacing: 2) {
                Text(name)
                    .font(.system(size: 16, weight: .semibold))
                    .foregroundColor(Theme.color1A1F29)
                Text(handle)
                    .font(.system(size: 13, weight: .regular))
                    .foregroundColor(Theme.color808794)
            }
            Spacer()
            Button(action: onSettingsTapped) {
                Image("SettingsIcon")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 24, height: 24)
                    .foregroundColor(Theme.color666E7A)
            }
            .accessibilityLabel("Settings")
        }
        .padding(.vertical, 12)
        .padding(.horizontal, 16)
        .background(Theme.colorFFFFFF)
    }
}

#Preview {
    ProfileHeaderView(name: "Ada Lovelace", handle: "@ada")
}
