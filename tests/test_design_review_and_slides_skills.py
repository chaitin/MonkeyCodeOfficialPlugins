#!/usr/bin/env python3
"""Contracts for review, jury, and slide resources added to the plugin catalog."""

import ast
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ADDED = {
    "design-review",
    "plan-design-review",
    "review-animations",
    "pr-feedback-quality-gate",
    "headless-design-jury",
    "slides",
    "pptx-html-fidelity-audit",
}


class DesignReviewAndSlidesTests(unittest.TestCase):
    def test_manifest_discovers_every_added_skill(self) -> None:
        manifest = json.loads((SKILLS / "manifest.json").read_text(encoding="utf-8"))
        by_id = {item["skill_id"]: item for item in manifest["skills"]}
        self.assertTrue(ADDED <= by_id.keys())
        for skill_id in ADDED:
            path = SKILLS / by_id[skill_id]["skill_md_path"]
            self.assertEqual(path, SKILLS / skill_id / "SKILL.md")
            self.assertTrue(path.is_file())
            self.assertIn(f"name: {skill_id}", path.read_text(encoding="utf-8"))

    def test_review_skills_are_executable_not_catalog_stubs(self) -> None:
        review = (SKILLS / "design-review" / "SKILL.md").read_text(encoding="utf-8")
        plan = (SKILLS / "plan-design-review" / "SKILL.md").read_text(encoding="utf-8")
        for text in (review, plan):
            self.assertNotIn("install the upstream", text.lower())
            self.assertIn("score", text.lower())
            self.assertIn("output", text.lower())
        animation = (SKILLS / "review-animations" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("STANDARDS.md", animation)
        self.assertTrue((SKILLS / "review-animations" / "STANDARDS.md").is_file())
        self.assertIn("MIT License", (SKILLS / "review-animations" / "LICENSE").read_text(encoding="utf-8"))
        for forbidden in ("triggers:", "od:", "disable-model-invocation:"):
            self.assertNotIn(forbidden, animation.split("---", 2)[1])

    def test_jury_contract_is_tool_mediated_and_bounded(self) -> None:
        jury = (SKILLS / "headless-design-jury" / "SKILL.md").read_text(encoding="utf-8")
        for required in ("exactly five", "read-only", "DesignJurySubmit", "MUST_FIX", "three rounds", "RUN_DIRECTORY"):
            self.assertIn(required, jury)
        self.assertIn("Never calculate", jury)

    def test_slides_export_and_mandatory_audit_contract(self) -> None:
        slides = (SKILLS / "slides" / "SKILL.md").read_text(encoding="utf-8")
        for required in ('<section class="slide">', "1600px", "900px", "non-editable", ".pptx.fidelity.json", "pptx-html-fidelity-audit", "Mandatory gate"):
            self.assertIn(required, slides)
        script = SKILLS / "slides" / "scripts" / "export_html_to_pptx.py"
        self.assertTrue(script.is_file())
        requirements = SKILLS / "slides" / "scripts" / "requirements.txt"
        self.assertTrue(requirements.is_file())
        self.assertIn("playwright", requirements.read_text(encoding="utf-8"))
        self.assertIn("python-pptx", requirements.read_text(encoding="utf-8"))
        source = script.read_text(encoding="utf-8")
        ast.parse(source)
        for required in ('locator("section.slide")', "playwright", "python-pptx", "add_picture", "full-slide-render", "sha256", "pptx_sha256", "device_scale_factor", "commit_outputs"):
            self.assertIn(required, source)

    def test_slide_pair_install_rolls_back_on_manifest_failure(self) -> None:
        script = SKILLS / "slides" / "scripts" / "export_html_to_pptx.py"
        spec = importlib.util.spec_from_file_location("slides_export", script)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        class FakePresentation:
            def save(self, path: Path) -> None:
                Path(path).write_bytes(b"new-pptx")

        with tempfile.TemporaryDirectory() as success_dir:
            output = Path(success_dir) / "deck.pptx"
            module.commit_outputs(FakePresentation(), {"mode": "high-fidelity-image"}, output)
            manifest_data = json.loads(Path(str(output) + ".fidelity.json").read_text(encoding="utf-8"))
            self.assertEqual(
                manifest_data["pptx_sha256"],
                module.hashlib.sha256(output.read_bytes()).hexdigest(),
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "deck.pptx"
            manifest = Path(str(output) + ".fidelity.json")
            output.write_bytes(b"old-pptx")
            manifest.write_text("old-manifest", encoding="utf-8")
            real_replace = module.os.replace
            failed = False

            def fail_manifest_install(source: Path, target: Path) -> None:
                nonlocal failed
                if Path(source).name == "deck.pptx.fidelity.json" and Path(target) == manifest and not failed:
                    failed = True
                    raise OSError("simulated manifest install failure")
                real_replace(source, target)

            with mock.patch.object(module.os, "replace", side_effect=fail_manifest_install):
                with self.assertRaises(SystemExit):
                    module.commit_outputs(FakePresentation(), {"mode": "high-fidelity-image"}, output)
            self.assertEqual(output.read_bytes(), b"old-pptx")
            self.assertEqual(manifest.read_text(encoding="utf-8"), "old-manifest")

    def test_full_fidelity_audit_resource_tree(self) -> None:
        audit = SKILLS / "pptx-html-fidelity-audit"
        expected = (
            "SKILL.md", "LICENSE",
            "references/audit-table-template.md",
            "references/font-discipline.md",
            "references/layout-discipline.md",
            "scripts/.gitignore",
            "scripts/extract_pptx.py",
            "scripts/verify_layout.py",
        )
        for relative in expected:
            self.assertTrue((audit / relative).is_file(), relative)
        frontmatter = (audit / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        self.assertNotIn("od:", frontmatter)
        audit_skill = (audit / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("MonkeyCode", audit_skill)
        self.assertIn("high-fidelity-image", audit_skill)
        verifier = (audit / "scripts" / "verify_layout.py").read_text(encoding="utf-8")
        self.assertIn("full-slide-render", verifier)
        self.assertNotIn("or top >= footer_zone_top", verifier)
        self.assertIn("position alone is ambiguous", verifier)
        self.assertIn("pptx_sha256 does not match", verifier)
        self.assertIn("requires exactly one", verifier)


if __name__ == "__main__":
    unittest.main()
