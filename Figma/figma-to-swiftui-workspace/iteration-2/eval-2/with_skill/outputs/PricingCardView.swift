// PricingCardView.swift
// Generated from Figma node 'Pricing Card' (id 30:1).
// TODOs resolved: CTA wired to a Button; design copy lifted to bindable
// properties per references/mapping.md.

import SwiftUI

struct PricingCardView: View {
    // Data binding: literal strings from the design surfaced as properties.
    var planName: String = "Pro"
    var badgeText: String = "Popular"
    var price: String = "$29/mo"
    var featureText: String = "Unlimited projects"
    var ctaTitle: String = "Choose Pro"

    // Interactivity: CTA action wired by the caller.
    var onChoosePlan: () -> Void = {}

    var body: some View {
            VStack(alignment: .leading, spacing: 16) {
                HStack(alignment: .center, spacing: 0) {
                    Text(planName)
                        .font(.system(size: 22, weight: .bold))
                        .foregroundColor(Theme.colorFFFFFF)
                    Spacer()
                    HStack(alignment: .center, spacing: 0) {
                        Text(badgeText)
                            .font(.system(size: 12, weight: .semibold))
                            .foregroundColor(Theme.colorFFFFFF)
                    }
                        .padding(.vertical, 4)
                        .padding(.horizontal, 10)
                        .background(Theme.colorFFFFFF.opacity(0.2).cornerRadius(12))
                }
                Text(price)
                    .font(.system(size: 34, weight: .heavy))
                    .foregroundColor(Theme.colorFFFFFF)
                HStack(alignment: .center, spacing: 8) {
                    Image("CheckIcon")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 18, height: 18)
                    Text(featureText)
                        .font(.system(size: 15, weight: .regular))
                        .foregroundColor(Theme.colorF2F2FF)
                }
                // TODO resolved: CTA "Choose Pro" frame → Button with wired action.
                Button(action: onChoosePlan) {
                    HStack(alignment: .center, spacing: 0) {
                        Text(ctaTitle)
                            .font(.system(size: 16, weight: .bold))
                            .foregroundColor(Theme.color5C6BF2)
                            .multilineTextAlignment(.center)
                    }
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 14)
                        .padding(.horizontal, 16)
                        .background(Theme.colorFFFFFF.cornerRadius(12))
                }
                .buttonStyle(.plain)
            }
                .padding(.vertical, 24)
                .padding(.horizontal, 20)
                .background(LinearGradient(gradient: Gradient(colors: [Color(red: 0.36, green: 0.42, blue: 0.95), Color(red: 0.55, green: 0.32, blue: 0.9)]), startPoint: .top, endPoint: .bottom).cornerRadius(20))
                .frame(width: 320)
    }
}

#Preview {
    PricingCardView(onChoosePlan: { print("Choose Pro tapped") })
}
