// DesignTokens.swift
// Colors and text styles extracted from the Figma design.
// Reuse these instead of hard-coding values so the UI stays consistent.

import SwiftUI

enum Theme {
    /// #1A1F29
    static let color1A1F29 = Color(red: 0.1, green: 0.12, blue: 0.16)
    /// #808794
    static let color808794 = Color(red: 0.5, green: 0.53, blue: 0.58)
    /// #666E7A (Settings icon tint)
    static let color666E7A = Color(red: 0.4, green: 0.43, blue: 0.48)
    /// #FFFFFF
    static let colorFFFFFF = Color(red: 1, green: 1, blue: 1)
}

extension Font {
    static let style13w400 = Font.system(size: 13, weight: .regular)
    static let style16w600 = Font.system(size: 16, weight: .semibold)
}
