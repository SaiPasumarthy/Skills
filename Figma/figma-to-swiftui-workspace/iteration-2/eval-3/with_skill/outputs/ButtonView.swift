// ButtonView.swift
// Generated from Figma component set 'Button' (id 40:1), hand-finished.
//
// The Figma set has three variants: Primary, Secondary, Disabled.
// Idiomatically these are NOT three views. "Primary" and "Secondary" are visual
// *styles*; "Disabled" is the *state* SwiftUI already models via `.disabled()`,
// which is why the Disabled variant is just the Primary shape greyed out at 0.5
// opacity. So this file ships a single reusable `Button` + one `ButtonStyle`
// that picks colors per (style, enabled) — no near-duplicate structs.

import SwiftUI

// MARK: - Button style

/// Visual style of the app's primary button, matching the Figma "Button" set.
enum AppButtonStyleKind {
    case primary
    case secondary
}

/// A `ButtonStyle` that renders the Figma "Button" variants.
/// Disabled appearance is driven by the environment's `isEnabled`, so callers
/// use the native `.disabled(_:)` modifier rather than a separate "disabled" case.
struct AppButtonStyle: ButtonStyle {
    var kind: AppButtonStyleKind = .primary

    @Environment(\.isEnabled) private var isEnabled

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.style16w600)            // 16 / semibold, from DesignTokens
            .multilineTextAlignment(.center)
            .foregroundColor(foreground)
            .padding(.vertical, 12)
            .padding(.horizontal, 20)
            .frame(maxWidth: .infinity)    // fill the container; drop for HUG sizing
            .background(background.cornerRadius(10))
            .overlay(borderOverlay)
            .opacity(isEnabled ? (configuration.isPressed ? 0.85 : 1) : 0.5)
            .animation(.easeOut(duration: 0.1), value: configuration.isPressed)
    }

    // Disabled (Figma "Style=Disabled"): grey fill + grey label at 0.5 opacity.
    private var foreground: Color {
        guard isEnabled else { return Theme.color80858F }
        switch kind {
        case .primary:   return Theme.colorFFFFFF
        case .secondary: return Theme.color2163F5
        }
    }

    private var background: Color {
        guard isEnabled else { return Theme.colorCCD1DB }
        switch kind {
        case .primary:   return Theme.color2163F5
        case .secondary: return Theme.colorE6EDFF
        }
    }

    @ViewBuilder private var borderOverlay: some View {
        if isEnabled, kind == .secondary {
            RoundedRectangle(cornerRadius: 10)
                .stroke(Theme.color2163F5, lineWidth: 1)
        }
    }
}

extension ButtonStyle where Self == AppButtonStyle {
    static var appPrimary: AppButtonStyle { AppButtonStyle(kind: .primary) }
    static var appSecondary: AppButtonStyle { AppButtonStyle(kind: .secondary) }
}

// MARK: - Convenience wrapper

/// Thin convenience view so callers can write `ButtonView("Save") { ... }`.
/// Use a plain `Button(...) { }.buttonStyle(.appPrimary)` directly if preferred.
struct ButtonView: View {
    var title: String = "Button"
    var style: AppButtonStyleKind = .primary
    var isEnabled: Bool = true
    var action: () -> Void = {}

    var body: some View {
        Button(title, action: action)
            .buttonStyle(AppButtonStyle(kind: style))
            .disabled(!isEnabled)
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 16) {
        ButtonView(title: "Button", style: .primary) {}
        ButtonView(title: "Button", style: .secondary) {}
        ButtonView(title: "Button", style: .primary, isEnabled: false) {}
    }
    .padding()
}
