"""Every rule in evidence/check_evidence.py must be able to fail.

Each case copies the repository to a temporary directory, plants one defect,
and asserts the checker exits 1 **with that rule's message**. A healthy copy
must exit 0.

Each case also names the condition in the checker that catches it. The test
disables that condition (`if False:`) in a copy of the checker and asserts the
planted defect then slips through. That shows the case exercises its own rule
and is not failing for some other reason. A case that fails either way tests
nothing.

So every rule's condition in the checker fits on one line. The first version
of this test found a two-line condition: disabling it produced a syntax error,
which "failed" for the wrong reason.

Run: python -m unittest discover -s tests
"""

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "evidence" / "check_evidence.py"
C = "evidence/claims.yml"
S = "evidence/sources.yml"

# name: (file or "DELETE", old, new, expected message, checker condition or None)
CASES = {
    "unknown source key": (
        C, "sources: [xie_wuzazu]\n    pages:\n      - path: notes/01-global-chronology.md\n        anchor: should not",
        "sources: [no_such_source, xie_wuzazu]\n    pages:\n      - path: notes/01-global-chronology.md\n        anchor: should not",
        "unknown source 'no_such_source'", "if k not in source_by_key:"),
    "layer out of vocabulary": (
        C, "layer: recollection", "layer: memory",
        "layer 'memory' not in", "if layer not in LAYERS:"),
    "status out of vocabulary": (
        C, "status: open", "status: probable",
        "status 'probable' not in", "if status not in STATUSES:"),
    "hypothesis marked supported": (
        C, "anchor: should not be repeated as a demonstrated fact",
        "anchor: should not be repeated as a demonstrated fact\n    status: supported",
        "a hypothesis cannot be 'supported'",
        'if layer == "hypothesis" and status == "supported":'),
    "absence without searched": (
        C, "    searched: Catalogue records only. The printed book has not been consulted.\n", "",
        "an absence claim must record what was searched",
        'if layer == "absence" and not str(c.get("searched") or "").strip():'),
    "supported on secondary report only": (
        C, "status: partly_supported\n    sources: [culin1895]",
        "status: supported\n    sources: [culin1895]",
        "'supported' needs a source at",
        'if status == "supported" and not read_deep_enough:'),
    "anchor edited away from page": (
        "notes/01-global-chronology.md", "It does not describe modern rock–paper–scissors.",
        "It does not describe the game.",
        "anchor not found in notes/01-global-chronology.md",
        "elif norm(str(anchor)) not in text:"),
    "page missing": (
        "DELETE", "notes/05-regional-comparisons.md", None,
        "page notes/05-regional-comparisons.md does not exist",
        None),  # cannot be disabled: the anchor check would then read a missing file
    "duplicate claim id": (
        C, "id: claim.china.han_origin\n", "id: claim.china.wuzazu_not_rps\n",
        "duplicate id", "elif cid in seen_ids:"),
    "malformed claim id": (
        C, "id: claim.china.han_origin\n", "id: han_origin\n",
        "id must look like claim.area.name",
        "if not cid or not CLAIM_ID_RE.match(str(cid)):"),
    "access out of vocabulary": (
        S, "access: user_screenshot", "access: seen_it",
        "access 'seen_it' not in", 'if s.get("access") not in ACCESS:'),
    "unused source": (
        C, "sources: [best1925]", "sources: [nz_moe_takaro]",
        "'best1925' is not used by any claim", "if k not in used:"),
    "unknown claim mentioned in prose": (
        "notes/06-open-questions.md", "# 6. What would resolve the open questions",
        "# 6. What would resolve the open questions\n\nSee claim.thai.no_such_claim.",
        "mentions unknown claim claim.thai.no_such_claim", "if m not in seen_ids:"),
}


def run(root, checker=None):
    checker = checker or root / "evidence" / "check_evidence.py"
    proc = subprocess.run([sys.executable, str(checker), str(root)],
                          capture_output=True, text=True, encoding="utf-8")
    return proc.returncode, proc.stdout + proc.stderr


def fresh_copy(dst):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns(".git", "__pycache__"))


def plant(root, case):
    target, old, new = case[:3]
    if target == "DELETE":
        (root / old).unlink()
        return
    path = root / target
    text = path.read_text(encoding="utf-8")
    assert old in text, f"fixture drifted: {old!r} not in {target}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


class CheckerCanFail(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.root = self.tmp / "repo"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_healthy_copy_passes(self):
        fresh_copy(self.root)
        code, out = run(self.root)
        self.assertEqual(code, 0, out)
        self.assertIn("all checked", out)

    def test_harness_propagates_failure(self):
        proc = subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"])
        self.assertEqual(proc.returncode, 3)

    def test_each_defect_fails_for_its_reason(self):
        for name, case in CASES.items():
            with self.subTest(name):
                fresh_copy(self.root)
                plant(self.root, case)
                code, out = run(self.root)
                self.assertEqual(code, 1, f"{name} passed the checker:\n{out}")
                self.assertIn(case[3], out, f"{name} failed for another reason:\n{out}")

    def test_each_case_exercises_its_rule(self):
        source = CHECKER.read_text(encoding="utf-8")
        for name, case in CASES.items():
            condition = case[4]
            if condition is None:
                continue
            with self.subTest(name):
                m = re.search(r"^( *)" + re.escape(condition), source, re.M)
                self.assertIsNotNone(m, "checker changed; update this case's condition")
                kw = "elif" if condition.startswith("elif") else "if"
                disabled = source.replace(m.group(0), f"{m.group(1)}{kw} False:", 1)
                checker = self.tmp / "disabled_check.py"
                checker.write_text(disabled, encoding="utf-8")
                fresh_copy(self.root)
                plant(self.root, case)
                code, out = run(self.root, checker)
                self.assertEqual(code, 0, f"{name}: still fails with its rule disabled, "
                                          f"so the case is not testing that rule:\n{out}")


if __name__ == "__main__":
    unittest.main()
