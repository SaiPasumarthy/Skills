# Installing the `hig-adaptive-layout` skill

This is an **Agent Skill** (the open `SKILL.md` standard, agentskills.io). The same
file works in GitHub Copilot (VS Code), Claude Code, and the Claude apps.

You only need **one file**: `hig-adaptive-layout.skill` (or the identical
`hig-adaptive-layout.zip`). Everything the skill needs is inside it.

---

## GitHub Copilot in VS Code

1. **Unzip it.** The `.skill` file is a zip. Rename `hig-adaptive-layout.skill`
   to `hig-adaptive-layout.zip` if needed, then extract it. You'll get a folder:
   `hig-adaptive-layout/` containing `SKILL.md`, `references/`, and `filtered/`.

2. **Drop the folder into a skills directory.** Choose one:
   - Per-project (only in one repo): put it at
     `<your-repo>/.github/skills/hig-adaptive-layout/`
     (`.claude/skills/` or `.agents/skills/` also work)
   - Personal (all projects):
     `~/.copilot/skills/hig-adaptive-layout/`  (or `~/.agents/skills/`)

   The folder name must stay `hig-adaptive-layout` (it matches the skill's `name`).
   So the final path looks like:
   `.github/skills/hig-adaptive-layout/SKILL.md`

3. **Enable it in Copilot chat.** In VS Code, open Copilot Chat and type `/skills`
   to open the Configure Skills menu and turn it on.

4. **Use it.** Just ask a normal question — Copilot matches by the skill's
   description. Try:
   - "Lay out a profile screen for iPhone, iPad, and Mac in SwiftUI."
   - "Make this SwiftUI view adaptive for iPad and Mac." (with a file open)
   - "Tab bar or sidebar for this screen?"

---

## Claude Code (CLI or its VS Code extension)

1. Unzip as above.
2. Put the `hig-adaptive-layout/` folder in:
   - Personal: `~/.claude/skills/hig-adaptive-layout/`
   - Per-project: `<repo>/.claude/skills/hig-adaptive-layout/`
3. It's picked up automatically. Ask a layout question, or invoke it explicitly.

---

## Claude desktop app / Cowork

Open the `hig-adaptive-layout.skill` file and click **Save skill** on the card.
(Requires that the account/org allows adding skills.)

---

## Quick check that it's installed

Ask: *"Design an adaptive settings screen for iPhone, iPad, and Mac."*
A working install returns a structured layout (per-size-class plan + safe-area /
Dynamic Type notes + a SwiftUI scaffold + a verification pass), not just generic advice.
