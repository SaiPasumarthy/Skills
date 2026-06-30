import SwiftUI

// MARK: - Design Tokens
//
// Generated from the Figma "Button" component set (node 40:1).
// All three Figma variants share the same layout/typography and differ
// only in their color tokens + interactivity, so the geometry lives here
// once and the per-variant palette lives in `DesignButtonStyle.Variant`.

enum ButtonTokens {
    // Layout (identical across all variants in the Figma file)
    static let paddingHorizontal: CGFloat = 20
    static let paddingVertical: CGFloat = 12
    static let cornerRadius: CGFloat = 10
    static let strokeWeight: CGFloat = 1

    // Typography
    static let fontSize: CGFloat = 16
    static let fontWeight: Font.Weight = .semibold // Figma fontWeight 600
}

// Convenience for the r/g/b (0...1) colors exported by the Figma REST API.
private extension Color {
    init(figma r: Double, _ g: Double, _ b: Double, _ a: Double = 1) {
        self.init(.sRGB, red: r, green: g, blue: b, opacity: a)
    }
}

// MARK: - Variant Style

/// A single `ButtonStyle` that renders any of the Figma button variants.
/// One source of truth — the variant only swaps color tokens.
struct DesignButtonStyle: ButtonStyle {

    enum Variant {
        case primary
        case secondary
        case disabled

        var background: Color {
            switch self {
            case .primary:   return Color(figma: 0.13, 0.39, 0.96)
            case .secondary: return Color(figma: 0.90, 0.93, 1.00)
            case .disabled:  return Color(figma: 0.80, 0.82, 0.86)
            }
        }

        var foreground: Color {
            switch self {
            case .primary:   return Color(figma: 1, 1, 1)
            case .secondary: return Color(figma: 0.13, 0.39, 0.96)
            case .disabled:  return Color(figma: 0.50, 0.52, 0.56)
            }
        }

        /// Only the secondary variant has a stroke in Figma.
        var border: Color? {
            switch self {
            case .secondary: return Color(figma: 0.13, 0.39, 0.96)
            default:         return nil
            }
        }

        /// Figma applies 0.5 opacity to the whole disabled component.
        var opacity: Double {
            self == .disabled ? 0.5 : 1
        }

        /// The disabled variant is not interactive.
        var isInteractive: Bool {
            self != .disabled
        }
    }

    let variant: Variant

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.system(size: ButtonTokens.fontSize, weight: ButtonTokens.fontWeight))
            .multilineTextAlignment(.center)
            .foregroundStyle(variant.foreground)
            .padding(.horizontal, ButtonTokens.paddingHorizontal)
            .padding(.vertical, ButtonTokens.paddingVertical)
            .background(variant.background)
            .overlay(
                RoundedRectangle(cornerRadius: ButtonTokens.cornerRadius)
                    .strokeBorder(variant.border ?? .clear, lineWidth: ButtonTokens.strokeWeight)
            )
            .clipShape(RoundedRectangle(cornerRadius: ButtonTokens.cornerRadius))
            .opacity(variant.opacity)
            .opacity(configuration.isPressed ? 0.85 : 1)
    }
}

// MARK: - Public API

/// The Figma "Button" component, expressed as one SwiftUI view.
///
/// ```swift
/// DesignButton("Button", variant: .primary) { … }
/// DesignButton("Button", variant: .secondary) { … }
/// DesignButton("Button", variant: .disabled)            // inert by design
/// ```
struct DesignButton: View {
    private let title: String
    private let variant: DesignButtonStyle.Variant
    private let action: () -> Void

    init(_ title: String = "Button",
         variant: DesignButtonStyle.Variant = .primary,
         action: @escaping () -> Void = {}) {
        self.title = title
        self.variant = variant
        self.action = action
    }

    var body: some View {
        Button(title, action: action)
            .buttonStyle(DesignButtonStyle(variant: variant))
            .disabled(!variant.isInteractive)
    }
}

// MARK: - Preview

#Preview("Button Variants") {
    VStack(spacing: 16) {
        DesignButton("Button", variant: .primary)
        DesignButton("Button", variant: .secondary)
        DesignButton("Button", variant: .disabled)
    }
    .padding()
}
