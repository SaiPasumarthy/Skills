#!/usr/bin/env python3
import json, os, glob, re

ROOT = "/sessions/sleepy-elegant-bell/mnt/outputs/figma-to-swiftui-workspace/iteration-1"
EVAL_DIRS = {"login-card": "eval-0", "profile-header": "eval-1"}

def read_all(d):
    blob = ""
    for p in glob.glob(os.path.join(d, "outputs", "*")):
        try:
            with open(p, encoding="utf-8") as f:
                blob += "\n" + f.read()
        except Exception:
            pass
    return blob, [os.path.basename(p) for p in glob.glob(os.path.join(d, "outputs", "*"))]

def view_text(d):
    for p in glob.glob(os.path.join(d, "outputs", "*View.swift")):
        with open(p, encoding="utf-8") as f:
            return f.read()
    return ""

def grade_login(d):
    blob, files = read_all(d)
    vt = view_text(d)
    tokens_file = any("Token" in f or ("Color" in f and "swift" in f.lower()) for f in files)
    has_color_token_def = bool(re.search(r"static let \w+ *= *Color\(red", blob))
    checks = [
        ("Emits a separate design-tokens file with Color(red:..) tokens",
         (tokens_file or has_color_token_def) and has_color_token_def,
         f"files={files}; color-token defs found={has_color_token_def}"),
        ("Uses VStack for the vertical auto-layout", "VStack" in vt, "VStack in view" if "VStack" in vt else "no VStack"),
        ("Preserves text content ('Welcome back' and 'Sign In')",
         "Welcome back" in blob and "Sign In" in blob, "both strings present" if ("Welcome back" in blob and "Sign In" in blob) else "missing string"),
        ("Captures card sizing: 320pt width, 16pt corner radius, drop shadow",
         "320" in blob and "16" in blob and "shadow" in blob.lower(),
         f"320={'320' in blob} radius16={'16' in blob} shadow={'shadow' in blob.lower()}"),
        ("Upgrades the email RECTANGLE into a real TextField",
         "TextField" in blob, "TextField present" if "TextField" in blob else "still a Rectangle"),
        ("View references named color tokens rather than only inline Color literals",
         bool(re.search(r"(Theme|AppColor|Color)\.\w*[Cc]olor", vt)) or vt.count("Color(red") <= 1,
         f"inline Color(red literals in view={vt.count('Color(red')}"),
    ]
    return checks

def grade_profile(d):
    blob, files = read_all(d)
    vt = view_text(d)
    has_color_token_def = bool(re.search(r"(static let|case) *\w+ *= *Color\(red", blob)) or "Color(red" in blob
    checks = [
        ("Uses HStack for the horizontal row", "HStack" in vt, "HStack present" if "HStack" in vt else "no HStack"),
        ("Nested VStack holds name 'Ada Lovelace' and handle '@ada'",
         "VStack" in vt and "Ada Lovelace" in blob and "@ada" in blob,
         f"VStack={'VStack' in vt} name={'Ada Lovelace' in blob} handle={'@ada' in blob}"),
        ("Avatar rendered as a circular image (clipShape(Circle))",
         "clipShape(Circle" in blob, "circular clip present" if "clipShape(Circle" in blob else "no circular clip"),
        ("Settings icon present (Image or SF Symbol)",
         ("SettingsIcon" in blob) or ("gear" in blob.lower()) or ("systemName" in blob),
         "settings glyph present"),
        ("Produces an asset manifest listing Avatar and SettingsIcon",
         any(f == "Assets.md" for f in files) and "Avatar" in blob and "SettingsIcon" in blob,
         f"Assets.md={'Assets.md' in files}"),
        ("Defines reusable Color tokens", has_color_token_def, "color tokens present" if has_color_token_def else "no color tokens"),
    ]
    return checks

for eval_name, grader in [("login-card", grade_login), ("profile-header", grade_profile)]:
    edir = EVAL_DIRS[eval_name]
    for cfg in ("with_skill", "without_skill"):
        d = os.path.join(ROOT, edir, cfg)
        checks = grader(d)
        expectations = [{"text": t, "passed": bool(p), "evidence": e} for (t, p, e) in checks]
        passed = sum(1 for x in expectations if x["passed"])
        total = len(expectations)
        summary = {"passed": passed, "failed": total - passed, "total": total,
                   "pass_rate": round(passed/total, 3)}
        out = {"expectations": expectations, "summary": summary}
        for target in (os.path.join(d, "grading.json"), os.path.join(d, "run-1", "grading.json")):
            with open(target, "w") as f:
                json.dump(out, f, indent=2)
        print(f"{eval_name:16} {cfg:14} {passed}/{total}")
