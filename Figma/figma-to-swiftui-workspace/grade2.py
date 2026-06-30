#!/usr/bin/env python3
import json, os, glob, re

ROOT = "/sessions/sleepy-elegant-bell/mnt/outputs/figma-to-swiftui-workspace/iteration-2"

def read_all(d):
    blob = ""; files = []
    for p in glob.glob(os.path.join(d, "outputs", "*")):
        files.append(os.path.basename(p))
        try:
            blob += "\n" + open(p, encoding="utf-8").read()
        except Exception: pass
    return blob, files

def main_swift(d):
    cands = [p for p in glob.glob(os.path.join(d, "outputs", "*.swift")) if "DesignTokens" not in p]
    return open(cands[0], encoding="utf-8").read() if cands else ""

def has_color_tokens(blob):
    return bool(re.search(r"(static let|case)\s+\w+\s*=\s*Color\(", blob)) or "Color(red" in blob

def grade_login(d):
    blob, files = read_all(d); vt = main_swift(d)
    return [
        ("Emits design-color tokens", has_color_tokens(blob), f"files={files}"),
        ("Uses VStack layout", "VStack" in vt, ""),
        ("Preserves text ('Welcome back' + 'Sign In')", "Welcome back" in blob and "Sign In" in blob, ""),
        ("Card sizing 320 / radius 16 / shadow", "320" in blob and "shadow" in blob.lower(), ""),
        ("Email field becomes TextField", "TextField" in blob, ""),
        ("View uses token refs not only inline colors", vt.count("Color(red") <= 1 or "Theme." in vt, f"inline={vt.count('Color(red')}"),
    ]

def grade_profile(d):
    blob, files = read_all(d); vt = main_swift(d)
    return [
        ("Uses HStack row", "HStack" in vt, ""),
        ("Nested VStack name+handle", "VStack" in vt and "Ada Lovelace" in blob and "@ada" in blob, ""),
        ("Avatar circular (clipShape(Circle))", "clipShape(Circle" in blob, ""),
        ("Settings icon present", "Settings" in blob or "gear" in blob.lower() or "systemName" in blob, ""),
        ("Asset manifest lists Avatar + SettingsIcon", "Assets.md" in files and "Avatar" in blob and "SettingsIcon" in blob, ""),
        ("Defines color tokens", has_color_tokens(blob), ""),
    ]

def grade_pricing(d):
    blob, files = read_all(d); vt = main_swift(d)
    return [
        ("Gradient background (LinearGradient)", "LinearGradient" in blob, ""),
        ("Header SPACE_BETWEEN -> Spacer + 'Pro' + 'Popular'", "Spacer()" in vt and "Pro" in blob and "Popular" in blob, ""),
        ("Big price '$29/mo'", "$29/mo" in blob, ""),
        ("Feature row: check icon + 'Unlimited projects'", "Unlimited projects" in blob and ("checkmark" in blob.lower() or "CheckIcon" in blob or "Image(" in vt), ""),
        ("CTA becomes a Button ('Choose Pro')", "Choose Pro" in blob and "Button" in vt, ""),
        ("Color tokens, not only inline magic colors", has_color_tokens(blob), ""),
    ]

def grade_variants(d):
    blob, files = read_all(d); vt = main_swift(d)
    struct_views = len(re.findall(r"struct\s+\w+\s*:\s*View", vt))
    idiomatic = ("ButtonStyle" in vt) or ("enum Variant" in vt) or ("enum " in vt and "switch" in vt)
    return [
        ("Single view, NOT 3 near-duplicate View structs", struct_views <= 1 or idiomatic, f"View structs={struct_views}, idiomatic={idiomatic}"),
        ("All three variants represented", all(k in blob.lower() for k in ("primary","secondary","disabled")), ""),
        ("Secondary has a stroke/border", "stroke" in blob.lower(), ""),
        ("Disabled handled (opacity .5 or .disabled)", "0.5" in blob or ".disabled" in blob, ""),
        ("Idiomatic variant modeling (enum/ButtonStyle)", idiomatic, ""),
        ("Defines color tokens", has_color_tokens(blob), ""),
    ]

GRADERS = {"eval-0": grade_login, "eval-1": grade_profile, "eval-2": grade_pricing, "eval-3": grade_variants}

for edir, grader in GRADERS.items():
    for cfg in ("with_skill", "without_skill"):
        d = os.path.join(ROOT, edir, cfg)
        checks = grader(d)
        exps = [{"text": t, "passed": bool(p), "evidence": e} for (t, p, e) in checks]
        passed = sum(1 for x in exps if x["passed"]); total = len(exps)
        out = {"expectations": exps, "summary": {"passed": passed, "failed": total-passed, "total": total, "pass_rate": round(passed/total,3)}}
        os.makedirs(os.path.join(d, "run-1"), exist_ok=True)
        for target in (os.path.join(d,"grading.json"), os.path.join(d,"run-1","grading.json")):
            json.dump(out, open(target,"w"), indent=2)
        # mirror timing into run-1 for the aggregator
        tj = os.path.join(d,"timing.json")
        if os.path.exists(tj): json.dump(json.load(open(tj)), open(os.path.join(d,"run-1","timing.json"),"w"))
        print(f"{edir:8} {cfg:14} {passed}/{total}")
