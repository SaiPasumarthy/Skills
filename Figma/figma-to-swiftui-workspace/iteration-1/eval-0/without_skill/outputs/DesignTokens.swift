//
//  DesignTokens.swift
//  Generated from Figma node "Login Card" (10:2)
//
//  Single source of truth for colors, typography, spacing, radii, and
//  shadows extracted from the Figma REST API export. Edit values here
//  to keep the design system in sync across the app.
//

import SwiftUI

// MARK: - Color

/// Figma colors are 0...1 sRGB component values. SwiftUI's `Color(red:green:blue:)`
/// expects the same 0...1 range, so values map 1:1.
enum AppColor {
    /// Card background — Figma fill r:1 g:1 b:1 (white).
    static let surface = Color(red: 1.0, green: 1.0, blue: 1.0)

    /// Title text — Figma r:0.07 g:0.09 b:0.15 (near-black navy).
    static let textPrimary = Color(red: 0.07, green: 0.09, blue: 0.15)

    /// Subtitle text — Figma r:0.42 g:0.45 b:0.5 (muted gray).
    static let textSecondary = Color(red: 0.42, green: 0.45, blue: 0.5)

    /// Input field fill — Figma r:0.95 g:0.96 b:0.97 (light gray).
    static let fieldFill = Color(red: 0.95, green: 0.96, blue: 0.97)

    /// Input field border — Figma r:0.85 g:0.87 b:0.9.
    static let fieldStroke = Color(red: 0.85, green: 0.87, blue: 0.9)

    /// Primary action / button — Figma r:0.13 g:0.39 b:0.96 (blue).
    static let accent = Color(red: 0.13, green: 0.39, blue: 0.96)

    /// Text on the accent button — Figma r:1 g:1 b:1 (white).
    static let onAccent = Color(red: 1.0, green: 1.0, blue: 1.0)

    /// Drop-shadow color — Figma black at 12% alpha.
    static let shadow = Color.black.opacity(0.12)
}

// MARK: - Typography

/// Maps Figma `fontWeight` (numeric) to SwiftUI `Font.Weight`.
private func fontWeight(_ figmaWeight: Int) -> Font.Weight {
    switch figmaWeight {
    case ...100: return .thin
    case 101...200: return .ultraLight
    case 201...300: return .light
    case 301...400: return .regular
    case 401...500: return .medium
    case 501...600: return .semibold
    case 601...700: return .bold
    case 701...800: return .heavy
    default: return .black
    }
}

enum AppFont {
    /// Title — 24pt / weight 700. lineHeightPx 30 in Figma.
    static let title = Font.system(size: 24, weight: fontWeight(700))
    static let titleLineHeight: CGFloat = 30

    /// Subtitle — 14pt / weight 400.
    static let subtitle = Font.system(size: 14, weight: fontWeight(400))

    /// Button label — 16pt / weight 600.
    static let button = Font.system(size: 16, weight: fontWeight(600))

    /// Field text — not specified in Figma; uses field height-appropriate size.
    static let field = Font.system(size: 16, weight: fontWeight(400))
}

// MARK: - Spacing

/// Layout values pulled directly from the Figma auto-layout frame.
enum AppSpacing {
    /// Card vertical item spacing (`itemSpacing`).
    static let cardItemSpacing: CGFloat = 16

    /// Card padding (`paddingTop/Bottom`, `paddingLeft/Right`).
    static let cardPaddingVertical: CGFloat = 24
    static let cardPaddingHorizontal: CGFloat = 20

    /// Button padding.
    static let buttonPaddingVertical: CGFloat = 12
    static let buttonPaddingHorizontal: CGFloat = 16

    /// Button internal item spacing.
    static let buttonItemSpacing: CGFloat = 8
}

// MARK: - Sizing

enum AppSize {
    /// Card fixed width (`layoutSizingHorizontal: FIXED`, width 320).
    static let cardWidth: CGFloat = 320

    /// Input field fixed height (44pt).
    static let fieldHeight: CGFloat = 44

    /// Button minimum height matches field (44pt total in Figma).
    static let buttonHeight: CGFloat = 44
}

// MARK: - Radius

enum AppRadius {
    static let card: CGFloat = 16   // Figma cornerRadius 16
    static let field: CGFloat = 8   // Figma cornerRadius 8
    static let button: CGFloat = 10 // Figma cornerRadius 10
}

// MARK: - Shadow

enum AppShadow {
    /// Figma DROP_SHADOW: radius 24, offset (0, 8), black @ 12%.
    /// Figma blur radius maps to SwiftUI's `radius` halved, which visually
    /// approximates Figma's gaussian blur more closely.
    static let cardColor = AppColor.shadow
    static let cardRadius: CGFloat = 12   // Figma radius 24 -> SwiftUI ~half
    static let cardOffsetX: CGFloat = 0
    static let cardOffsetY: CGFloat = 8
}
