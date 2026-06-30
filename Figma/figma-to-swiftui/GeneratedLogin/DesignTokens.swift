// DesignTokens.swift
// Colors and text styles extracted from the Figma design.
// Reuse these instead of hard-coding values so the UI stays consistent.

import SwiftUI

enum Theme {
    /// #121726
    static let color121726 = Color(red: 0.07, green: 0.09, blue: 0.15)
    /// #2163F5
    static let color2163F5 = Color(red: 0.13, green: 0.39, blue: 0.96)
    /// #6B7380
    static let color6B7380 = Color(red: 0.42, green: 0.45, blue: 0.5)
    /// #D9DEE6
    static let colorD9DEE6 = Color(red: 0.85, green: 0.87, blue: 0.9)
    /// #F2F5F7
    static let colorF2F5F7 = Color(red: 0.95, green: 0.96, blue: 0.97)
    /// #FFFFFF
    static let colorFFFFFF = Color(red: 1, green: 1, blue: 1)
}

extension Font {
    static let style14w400 = Font.system(size: 14, weight: .regular)
    static let style16w600 = Font.system(size: 16, weight: .semibold)
    static let style24w700 = Font.system(size: 24, weight: .bold)
}
