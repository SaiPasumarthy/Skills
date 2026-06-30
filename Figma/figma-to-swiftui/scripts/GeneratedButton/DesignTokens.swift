// DesignTokens.swift
// Colors and text styles extracted from the Figma design.
// Reuse these instead of hard-coding values so the UI stays consistent.

import SwiftUI

enum Theme {
    /// #2163F5
    static let color2163F5 = Color(red: 0.13, green: 0.39, blue: 0.96)
    /// #80858F
    static let color80858F = Color(red: 0.5, green: 0.52, blue: 0.56)
    /// #CCD1DB
    static let colorCCD1DB = Color(red: 0.8, green: 0.82, blue: 0.86)
    /// #E6EDFF
    static let colorE6EDFF = Color(red: 0.9, green: 0.93, blue: 1)
    /// #FFFFFF
    static let colorFFFFFF = Color(red: 1, green: 1, blue: 1)
}

extension Font {
    static let style16w600 = Font.system(size: 16, weight: .semibold)
}
