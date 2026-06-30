//
//  LoginCardView.swift
//  Generated from Figma node "Login Card" (10:2)
//
//  A self-contained login card. Layout, colors, fonts, radii, and shadow
//  are driven by DesignTokens.swift so the visual spec stays centralized.
//
//  Figma structure:
//    Login Card (FRAME, VERTICAL auto-layout, 320pt fixed width, HUG height)
//      - Title       "Welcome back"
//      - Subtitle    "Sign in to continue"
//      - Email Field (RECTANGLE input)
//      - Sign In Button (FRAME) -> Button Label "Sign In"
//

import SwiftUI

struct LoginCardView: View {
    // Bindable so the card can be embedded in a real form.
    @State private var email: String = ""

    /// Invoked when the Sign In button is tapped.
    var onSignIn: (String) -> Void = { _ in }

    var body: some View {
        VStack(spacing: AppSpacing.cardItemSpacing) {
            // Title — "Welcome back"
            Text("Welcome back")
                .font(AppFont.title)
                .foregroundStyle(AppColor.textPrimary)
                .lineSpacing(AppFont.titleLineHeight - 24) // Figma lineHeightPx 30 over 24pt font
                .multilineTextAlignment(.center)

            // Subtitle — "Sign in to continue"
            Text("Sign in to continue")
                .font(AppFont.subtitle)
                .foregroundStyle(AppColor.textSecondary)
                .multilineTextAlignment(.center)

            // Email Field — Figma RECTANGLE rendered as a real text field.
            EmailField(text: $email)

            // Sign In Button
            SignInButton(title: "Sign In") {
                onSignIn(email)
            }
        }
        .padding(.vertical, AppSpacing.cardPaddingVertical)
        .padding(.horizontal, AppSpacing.cardPaddingHorizontal)
        .frame(width: AppSize.cardWidth)        // FIXED horizontal sizing
        .background(AppColor.surface)
        .clipShape(RoundedRectangle(cornerRadius: AppRadius.card, style: .continuous))
        .shadow(
            color: AppShadow.cardColor,
            radius: AppShadow.cardRadius,
            x: AppShadow.cardOffsetX,
            y: AppShadow.cardOffsetY
        )
    }
}

// MARK: - Email Field

/// Figma "Email Field" is a styled RECTANGLE (44pt tall, FILL width, 8pt radius,
/// light fill + 1pt border). Reproduced as a functional `TextField`.
private struct EmailField: View {
    @Binding var text: String

    var body: some View {
        TextField("Email", text: $text)
            .font(AppFont.field)
            .foregroundStyle(AppColor.textPrimary)
            .textContentType(.emailAddress)
            .keyboardType(.emailAddress)
            .textInputAutocapitalization(.never)
            .autocorrectionDisabled(true)
            .padding(.horizontal, 12)
            .frame(maxWidth: .infinity)         // FILL horizontal
            .frame(height: AppSize.fieldHeight) // FIXED 44pt
            .background(AppColor.fieldFill)
            .clipShape(RoundedRectangle(cornerRadius: AppRadius.field, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: AppRadius.field, style: .continuous)
                    .stroke(AppColor.fieldStroke, lineWidth: 1)
            )
    }
}

// MARK: - Sign In Button

/// Figma "Sign In Button" FRAME: HORIZONTAL auto-layout, centered, blue fill,
/// 10pt radius, 12/16 padding, FILL width, HUG height. Label "Sign In" 16/600 white.
private struct SignInButton: View {
    let title: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack(spacing: AppSpacing.buttonItemSpacing) {
                Text(title)
                    .font(AppFont.button)
                    .foregroundStyle(AppColor.onAccent)
            }
            .frame(maxWidth: .infinity)             // FILL horizontal
            .padding(.vertical, AppSpacing.buttonPaddingVertical)
            .padding(.horizontal, AppSpacing.buttonPaddingHorizontal)
            .background(AppColor.accent)
            .clipShape(RoundedRectangle(cornerRadius: AppRadius.button, style: .continuous))
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Preview

#Preview("Login Card") {
    ZStack {
        Color(red: 0.97, green: 0.98, blue: 0.99) // neutral backdrop to show shadow
            .ignoresSafeArea()
        LoginCardView { email in
            print("Sign in tapped with: \(email)")
        }
    }
}
