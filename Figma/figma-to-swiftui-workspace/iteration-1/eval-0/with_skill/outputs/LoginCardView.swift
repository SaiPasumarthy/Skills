// LoginCardView.swift
// Generated from Figma node 'Login Card' (id 10:2).
// Hand-finished: the email rectangle is now a TextField, the Sign In
// container is now a Button, and literal copy is bound to @State.
// Colors/fonts come from DesignTokens.swift — no magic numbers inline.

import SwiftUI

struct LoginCardView: View {
    // Was: literal "Email Field" rectangle in Figma. Now an editable binding.
    @State private var email: String = ""
    @State private var password: String = ""

    // Wire this to your sign-in flow / view model.
    var onSignIn: (_ email: String, _ password: String) -> Void = { _, _ in }

    var body: some View {
        VStack(alignment: .center, spacing: 16) {
            Text("Welcome back")
                .font(.style24w700)
                .foregroundColor(Theme.color121726)
                .multilineTextAlignment(.center)
                // line height ~30pt (use .lineSpacing if needed)

            Text("Sign in to continue")
                .font(.style14w400)
                .foregroundColor(Theme.color6B7380)
                .multilineTextAlignment(.center)

            // Was: RoundedRectangle(cornerRadius: 8). A styled input field —
            // replaced with a real TextField per mapping.md.
            TextField("Email", text: $email)
                .textContentType(.emailAddress)
                .keyboardType(.emailAddress)
                .textInputAutocapitalization(.never)
                .autocorrectionDisabled()
                .padding(.horizontal, 12)
                .frame(height: 44)
                .background(
                    RoundedRectangle(cornerRadius: 8)
                        .fill(Theme.colorF2F5F7)
                )
                .overlay(
                    RoundedRectangle(cornerRadius: 8)
                        .stroke(Theme.colorD9DEE6, lineWidth: 1)
                )

            // Was: a styled HStack container. Now a Button that fires an action.
            Button(action: { onSignIn(email, password) }) {
                HStack(alignment: .center, spacing: 8) {
                    Text("Sign In")
                        .font(.style16w600)
                        .foregroundColor(Theme.colorFFFFFF)
                        .multilineTextAlignment(.center)
                }
                .frame(maxWidth: .infinity)
                .padding(.vertical, 12)
                .padding(.horizontal, 16)
                .background(Theme.color2163F5.cornerRadius(10))
            }
            .buttonStyle(.plain)
        }
        .padding(.vertical, 24)
        .padding(.horizontal, 20)
        .background(Theme.colorFFFFFF.cornerRadius(16))
        .frame(width: 320)
        .shadow(
            color: Color(red: 0, green: 0, blue: 0, opacity: 0.12),
            radius: 24, x: 0, y: 8
        )
    }
}

#Preview {
    LoginCardView()
}
