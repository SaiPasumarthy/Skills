import SwiftUI

// MARK: - Pricing Card

/// A production-ready pricing card converted from Figma.
///
/// Layout source (Figma node "Pricing Card", 320×360):
/// - Vertical stack, 16pt spacing, 24/20 padding, 20pt corner radius
/// - Linear gradient background (indigo → purple)
/// - Header row: plan name on the left, translucent "Popular" badge on the right
/// - Large price
/// - Feature row: check icon + label
/// - Full-width white CTA button
struct PricingCardView: View {

    // MARK: Model

    /// The content shown by a pricing card. Kept separate from the view so the
    /// card can be reused for different plans without touching layout code.
    struct Plan {
        var name: String
        var badge: String?
        var price: String
        var features: [String]
        var ctaTitle: String
    }

    // MARK: Inputs

    let plan: Plan

    /// Invoked when the CTA button is tapped.
    var onSelect: () -> Void = {}

    // MARK: Body

    var body: some View {
        VStack(alignment: .leading, spacing: Metrics.itemSpacing) {
            header
            priceLabel

            ForEach(plan.features, id: \.self) { feature in
                featureRow(feature)
            }

            ctaButton
        }
        .padding(.horizontal, Metrics.horizontalPadding)
        .padding(.vertical, Metrics.verticalPadding)
        .frame(width: Metrics.cardWidth, alignment: .leading)
        .background(Palette.cardGradient)
        .clipShape(RoundedRectangle(cornerRadius: Metrics.cardCornerRadius, style: .continuous))
        // Accessibility: expose the card as a single group while keeping the
        // CTA independently actionable.
        .accessibilityElement(children: .contain)
    }

    // MARK: Subviews

    private var header: some View {
        HStack(alignment: .center, spacing: 8) {
            Text(plan.name)
                .font(.system(size: 22, weight: .bold))
                .foregroundStyle(Palette.onGradient)

            Spacer(minLength: 8)

            if let badge = plan.badge {
                Text(badge)
                    .font(.system(size: 12, weight: .semibold))
                    .foregroundStyle(Palette.onGradient)
                    .padding(.horizontal, 10)
                    .padding(.vertical, 4)
                    .background(
                        Palette.onGradient.opacity(0.2),
                        in: RoundedRectangle(cornerRadius: 12, style: .continuous)
                    )
            }
        }
    }

    private var priceLabel: some View {
        Text(plan.price)
            .font(.system(size: 34, weight: .heavy))
            .foregroundStyle(Palette.onGradient)
            .minimumScaleFactor(0.7)
            .lineLimit(1)
    }

    private func featureRow(_ feature: String) -> some View {
        HStack(spacing: 8) {
            Image(systemName: "checkmark")
                .font(.system(size: 13, weight: .bold))
                .foregroundStyle(Palette.onGradient)
                .frame(width: 18, height: 18)
                .accessibilityHidden(true)

            Text(feature)
                .font(.system(size: 15, weight: .regular))
                .foregroundStyle(Palette.featureText)
        }
        .accessibilityElement(children: .combine)
    }

    private var ctaButton: some View {
        Button(action: onSelect) {
            Text(plan.ctaTitle)
                .font(.system(size: 16, weight: .bold))
                .foregroundStyle(Palette.accent)
                .frame(maxWidth: .infinity)
                .padding(.horizontal, 16)
                .padding(.vertical, 14)
                .background(
                    Palette.onGradient,
                    in: RoundedRectangle(cornerRadius: 12, style: .continuous)
                )
        }
        .buttonStyle(.plain)
        .contentShape(RoundedRectangle(cornerRadius: 12, style: .continuous))
    }
}

// MARK: - Design Tokens

private extension PricingCardView {

    /// Layout constants taken directly from the Figma frame.
    enum Metrics {
        static let cardWidth: CGFloat = 320
        static let cardCornerRadius: CGFloat = 20
        static let itemSpacing: CGFloat = 16
        static let horizontalPadding: CGFloat = 20
        static let verticalPadding: CGFloat = 24
    }

    /// Colors derived from the Figma fills. Figma exports normalized RGB
    /// (0...1), which maps directly onto SwiftUI's `Color(red:green:blue:)`.
    enum Palette {
        /// Gradient stop 0 — also reused as the CTA label / accent color.
        static let accent = Color(red: 0.36, green: 0.42, blue: 0.95)
        /// Gradient stop 1.
        static let gradientEnd = Color(red: 0.55, green: 0.32, blue: 0.90)
        /// White text/icons on top of the gradient.
        static let onGradient = Color.white
        /// Slightly cooler off-white used for the feature label (r0.95 g0.95 b1).
        static let featureText = Color(red: 0.95, green: 0.95, blue: 1.0)

        /// Linear gradient matching Figma's default left→right angle.
        static let cardGradient = LinearGradient(
            colors: [accent, gradientEnd],
            startPoint: .leading,
            endPoint: .trailing
        )
    }
}

// MARK: - Convenience

extension PricingCardView.Plan {
    /// The sample "Pro" plan exported from Figma.
    static let pro = PricingCardView.Plan(
        name: "Pro",
        badge: "Popular",
        price: "$29/mo",
        features: ["Unlimited projects"],
        ctaTitle: "Choose Pro"
    )
}

// MARK: - Preview

#Preview("Pricing Card") {
    PricingCardView(plan: .pro) {
        print("CTA tapped")
    }
    .padding()
}
