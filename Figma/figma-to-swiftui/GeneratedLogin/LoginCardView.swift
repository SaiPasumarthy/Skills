// LoginCardView.swift
// Generated from Figma node 'Login Card' (id 10:2).
// Hand-finished: input rectangle -> TextField, button container -> Button,
// literal strings -> bindings/state, per references/mapping.md.

import SwiftUI

struct LoginCardView: View {
    /// Bound to the "Email Field" input (Figma node 10:5).
    @State private var email: String = ""
    /// Action fired when the "Sign In Button" (Figma node 10:6) is tapped.
    var onSignIn: (String) -> Void = { _ in }

    var body: some View {
        VStack(alignment: .center, spacing: 16) {
            Text("Welcome back")
                .font(.style24w700)
                .foregroundColor(Theme.color121726)
                .multilineTextAlignment(.center)

            Text("Sign in to continue")
                .font(.style14w400)
                .foregroundColor(Theme.color6B7380)
                .multilineTextAlignment(.center)

            // Figma node 10:5 "Email Field": styled rectangle -> TextField.
            TextField("Email", text: $email)
                .textContentType(.emailAddress)
                .keyboardType(.emailAddress)
                .textInputAutocapitalization(.never)
                .autocorrectionDisabled(true)
                .foregroundColor(Theme.color121726)
                .padding(.horizontal, 12)
                .frame(height: 44)
                .frame(maxWidth: .infinity)
                .background(Theme.colorF2F5F7.cornerRadius(8))
                .overlay(
                    RoundedRectangle(cornerRadius: 8)
                        .stroke(Theme.colorD9DEE6, lineWidth: 1)
                )

            // Figma node 10:6 "Sign In Button": styled frame -> Button.
            Button {
                onSignIn(email)
            } label: {
                HStack(alignment: .center, spacing: 8) {
                    Text("Sign In")
                        .font(.style16w600)
                        .foregroundColor(Theme.colorFFFFFF)
                        .multilineTextAlignment(.center)
                }
                .padding(.vertical, 12)
                .padding(.horizontal, 16)
                .frame(maxWidth: .infinity)
                .background(Theme.color2163F5.cornerRadius(10))
            }
        }
        .padding(.vertical, 24)
        .padding(.horizontal, 20)
        .background(Theme.colorFFFFFF.cornerRadius(16))
        .frame(width: 320)
        .shadow(color: Color(red: 0, green: 0, blue: 0, opacity: 0.12), radius: 24, x: 0, y: 8)
    }
}

#Preview {
    LoginCardView()
}
