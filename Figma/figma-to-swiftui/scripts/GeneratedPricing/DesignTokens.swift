// DesignTokens.swift
// Colors and text styles extracted from the Figma design.
// Reuse these instead of hard-coding values so the UI stays consistent.

import SwiftUI

enum Theme {
    /// #5C6BF2
    static let color5C6BF2 = Color(red: 0.36, green: 0.42, blue: 0.95)
    /// #F2F2FF
    static let colorF2F2FF = Color(red: 0.95, green: 0.95, blue: 1)
    /// #FFFFFF
    static let colorFFFFFF = Color(red: 1, green: 1, blue: 1)
}

extension Font {
    static let style12w600 = Font.system(size: 12, weight: .semibold)
    static let style15w400 = Font.system(size: 15, weight: .regular)
    static let style16w700 = Font.system(size: 16, weight: .bold)
    static let style22w700 = Font.system(size: 22, weight: .bold)
    static let style34w800 = Font.system(size: 34, weight: .heavy)
}
