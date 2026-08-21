#!/usr/bin/env python3
"""Focused structural and policy checks for the design flow skills."""

from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NEW_SKILLS = (
    "design-flow",
    "design-generation",
    "design-refinement",
    "frontend-design",
    "web-design-art-direction",
    "image-generation",
    "image-refinement",
)
CRAFT_REFS = {
    "design-generation": {"typography.md", "color.md", "anti-ai-slop.md", "accessibility-baseline.md", "state-coverage.md"},
    "design-refinement": {"typography.md", "color.md", "anti-ai-slop.md", "accessibility-baseline.md", "state-coverage.md"},
    "frontend-design": {"typography.md", "color.md", "anti-ai-slop.md", "accessibility-baseline.md", "state-coverage.md"},
    "web-design-art-direction": {"typography.md", "color.md", "anti-ai-slop.md", "accessibility-baseline.md", "state-coverage.md"},
    "image-generation": {"color.md", "anti-ai-slop.md"},
    "image-refinement": {"color.md", "anti-ai-slop.md"},
}


def skill_text(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


class DesignFlowSkillTests(unittest.TestCase):
    def test_workflow_dependencies_are_internal(self) -> None:
        workflow = json.loads((SKILLS / "design-flow" / "workflow.json").read_text(encoding="utf-8"))
        dependencies = {
            dependency
            for route in workflow["routes"]
            for step in route["steps"]
            for dependency in step.get("skills", [])
        }
        self.assertTrue(dependencies)
        for name in dependencies:
            text = skill_text(name)
            self.assertRegex(text, r"(?m)^visibility:\s*internal$")
            self.assertRegex(text, r"(?m)^owner:\s*design-flow$")
        self.assertNotRegex(skill_text("design-flow"), r"(?m)^visibility:\s*internal$")

    def test_workflow_manifest_routes_and_gates(self) -> None:
        workflow = json.loads((SKILLS / "design-flow" / "workflow.json").read_text(encoding="utf-8"))
        self.assertEqual(workflow["version"], 2)
        routes = {route["id"]: route for route in workflow["routes"]}
        self.assertEqual(
            set(routes),
            {"new-web", "new-mobile", "existing-web", "existing-mobile", "implement-web", "implement-mobile", "image-new", "image-edit"},
        )
        self.assertTrue(all(route["description"] and route["steps"] for route in routes.values()))
        policies = workflow["write_policies"]
        catalog_ids = {item["skill_id"] for item in json.loads((SKILLS / "manifest.json").read_text(encoding="utf-8"))["skills"]}
        catalog_ids.update(
            match.group(1).strip()
            for path in SKILLS.glob("*/SKILL.md")
            if (match := re.search(r"(?m)^name:\s*(.+)$", path.read_text(encoding="utf-8")))
        )
        self.assertEqual(policies, {"product": {"product": True}})
        for route in routes.values():
            ids = {step["id"] for step in route["steps"]}
            for step in route["steps"]:
                self.assertIn(step["write_policy"], policies)
                self.assertTrue(step["instructions"])
                transitions = step["transitions"]
                self.assertTrue(transitions.get("manual") or transitions.get("tools"))
                for dependency in step.get("skills", []):
                    self.assertIn(dependency, catalog_ids)
                targets = list(transitions.get("manual", {}).values()) + [item["target"] for item in transitions.get("tools", [])]
                if step.get("unavailable_target"):
                    targets.append(step["unavailable_target"])
                self.assertTrue(all(target in ids | {"completed", "cancelled"} for target in targets))
                if transitions.get("tools") and not transitions.get("manual"):
                    self.assertIn("unavailable_target", step)
        web_steps = {step["id"]: step for step in routes["new-web"]["steps"]}
        self.assertNotIn("visual-source", web_steps)
        self.assertEqual(web_steps["platform"]["skills"], ["frontend-design", "web-component-design"])
        self.assertNotIn("implementation", web_steps)
        self.assertNotIn("build-verification", web_steps)

        entry_steps = {
            "new-web": "brief",
            "new-mobile": "brief",
            "existing-web": "existing-assessment",
            "existing-mobile": "existing-assessment",
        }
        for route_id, entry_step in entry_steps.items():
            steps = {step["id"]: step for step in routes[route_id]["steps"]}
            self.assertEqual(steps[entry_step]["transitions"]["manual"], {"completed": "image-capability"})
            allocation = steps[entry_step]["instructions"]
            for required in (
                "only direct child directories",
                "^v([1-9]\\d*)$",
                "one more than the largest",
                "create-new operation that fails",
                "Never overwrite, reuse",
                "RUN_DIRECTORY",
            ):
                self.assertIn(required, allocation)
            for step_id, step in steps.items():
                if step_id != entry_step:
                    self.assertIn("Reuse exactly the RUN_DIRECTORY", step["instructions"])
            capability = steps["image-capability"]
            self.assertEqual(
                capability["transitions"]["manual"],
                {"available": "art-direction", "unavailable": "template-cards"},
            )
            self.assertIn("callable MCP text-to-image tool", capability["instructions"])
            self.assertIn("ToolSearch", capability["instructions"])

            art = steps["art-direction"]
            self.assertEqual(art["transitions"]["manual"], {"template": "template-cards"})
            art_cards = art["transitions"]["tools"]
            self.assertEqual(
                {item["equals"]: item["target"] for item in art_cards},
                {
                    "select": "visual-foundations",
                    "next": "art-direction",
                    "skip": "template-cards",
                    "cancel": "cancelled",
                },
            )
            self.assertIn("image-generation MCP", art["instructions"])
            self.assertEqual(art["unavailable_target"], "art-direction-question")

            art_question = steps["art-direction-question"]
            self.assertEqual(
                art_question["transitions"]["manual"],
                {
                    "direction-1": "visual-foundations",
                    "direction-2": "visual-foundations",
                    "direction-3": "visual-foundations",
                    "actions": "art-direction-actions",
                    "next": "art-direction-question",
                    "template": "template-question",
                    "cancel": "cancelled",
                },
            )
            self.assertEqual(
                {item["equals"]: item["target"] for item in art_question["transitions"]["tools"]},
                {
                    "Direction 1": "visual-foundations",
                    "Direction 2": "visual-foundations",
                    "Direction 3": "visual-foundations",
                    "More actions": "art-direction-actions",
                },
            )
            self.assertEqual(art_question["unavailable_target"], "art-direction-default")
            self.assertIn("free text", art_question["instructions"])

            art_actions = steps["art-direction-actions"]
            self.assertEqual(
                {item["equals"]: item["target"] for item in art_actions["transitions"]["tools"]},
                {
                    "Generate different directions": "art-direction-question",
                    "Use template recommendation": "template-question",
                    "Cancel": "cancelled",
                },
            )

            art_default = steps["art-direction-default"]
            self.assertEqual(
                art_default["transitions"]["manual"],
                {"selected": "visual-foundations", "template": "template-default"},
            )
            self.assertIn("SELECTED-DIRECTION.md", art_default["instructions"])

            template = steps["template-cards"]
            self.assertEqual(template["unavailable_target"], "template-question")
            self.assertIn("DesignTemplateCatalog", template["instructions"])
            self.assertIn("templateRef", template["instructions"])
            cards = template["transitions"]["tools"]
            self.assertEqual(
                {item["equals"]: item["target"] for item in cards},
                {
                    "select": "template-artifact",
                    "next": "template-cards",
                    "skip": "direct-thesis",
                    "cancel": "cancelled",
                },
            )

            template_question = steps["template-question"]
            self.assertEqual(
                template_question["transitions"]["manual"],
                {
                    "template-1": "template-artifact",
                    "template-2": "template-artifact",
                    "template-3": "template-artifact",
                    "actions": "template-actions",
                    "next": "template-question",
                    "skip": "direct-thesis",
                    "cancel": "cancelled",
                },
            )
            self.assertEqual(
                {item["equals"]: item["target"] for item in template_question["transitions"]["tools"]},
                {
                    "Template 1": "template-artifact",
                    "Template 2": "template-artifact",
                    "Template 3": "template-artifact",
                    "More actions": "template-actions",
                },
            )
            self.assertEqual(template_question["unavailable_target"], "template-default")
            self.assertIn("free text", template_question["instructions"])

            template_actions = steps["template-actions"]
            self.assertEqual(
                {item["equals"]: item["target"] for item in template_actions["transitions"]["tools"]},
                {
                    "Show different templates": "template-question",
                    "Continue without a template": "direct-thesis",
                    "Cancel": "cancelled",
                },
            )

            template_default = steps["template-default"]
            self.assertEqual(template_default["transitions"]["manual"], {"completed": "visual-foundations"})
            self.assertIn("strongest returned candidate", template_default["instructions"])
            self.assertIn("DesignTemplateArtifact", template_default["instructions"])

            artifact = steps["template-artifact"]["instructions"]
            self.assertIn("exact templateRef", artifact)
            self.assertIn("path RUN_DIRECTORY/DESIGN.md", artifact)
            self.assertIn("written atomically", artifact)
            self.assertIn("Read RUN_DIRECTORY/DESIGN.md back", artifact)
            self.assertIn("Never write or stage the template at .ohmyagent/design/DESIGN.md", artifact)
            default_artifact = steps["template-default"]["instructions"]
            self.assertIn("path RUN_DIRECTORY/DESIGN.md", default_artifact)
            self.assertIn("written atomically", default_artifact)
            self.assertIn("Never write or stage the template at .ohmyagent/design/DESIGN.md", default_artifact)
            for step_id in ("template-cards", "template-question", "template-default"):
                self.assertIn("RUN_DIRECTORY/template-previews/", steps[step_id]["instructions"])
            for step_id in ("art-direction", "art-direction-question", "art-direction-default"):
                self.assertIn("RUN_DIRECTORY/directions/", steps[step_id]["instructions"])
            self.assertIn("RUN_DIRECTORY/SELECTED-DIRECTION.md", steps["visual-foundations"]["instructions"])
            for step_id in ("visual-foundations", "html-prototype"):
                self.assertIn("RUN_DIRECTORY/DESIGN.md", steps[step_id]["instructions"])
                self.assertIn("any other version or the design root", steps[step_id]["instructions"])
            self.assertIn("template-default", steps["visual-foundations"]["instructions"])
        for route_id in ("new-web", "new-mobile", "existing-web", "existing-mobile"):
            steps = {step["id"]: step for step in routes[route_id]["steps"]}
            prototype = steps["html-prototype"]
            jury = steps["design-jury"]
            quality_gate = steps["prototype-quality-gate"]
            self.assertEqual(steps["platform"]["transitions"]["manual"], {"completed": "html-prototype"})
            self.assertEqual(prototype["transitions"]["manual"], {"completed": "design-jury"})
            self.assertEqual(jury["skills"], ["headless-design-jury"])
            self.assertEqual(
                jury["transitions"]["manual"],
                {"passed": "prototype-quality-gate", "failed": "cancelled"},
            )
            for required in (
                "exactly five independent read-only Agent reviews",
                "Designer, Critic, Brand, Accessibility, and Copy",
                "DesignJurySubmit",
                "Never calculate or override the score",
                "After round three",
            ):
                self.assertIn(required, jury["instructions"])
            self.assertEqual(
                quality_gate["transitions"]["manual"],
                {"passed": "completed", "revise": "html-prototype", "failed": "cancelled"},
            )
            self.assertEqual(quality_gate["skills"], ["design-refinement"])
            self.assertIn("RUN_DIRECTORY/prototype.html", prototype["instructions"])
            self.assertIn("RUN_DIRECTORY/quality-report.md", quality_gate["instructions"])
            for required in (
                "actual screenshots",
                "75%, 100%, and 125%",
                "content-width utilization below 60%",
                "outer-whitespace asymmetry above 15%",
                "80/100 overall",
                "at least 60% in every category",
                "after three failed audits",
            ):
                self.assertIn(required, quality_gate["instructions"])
            self.assertIn("ask to develop the product", quality_gate["instructions"])
            self.assertTrue(
                {"html-approval", "implementation", "screenshot-comparison", "refinement-checkpoint",
                 "build-verification", "accessibility-verification", "responsive-verification",
                 "states-verification"}.isdisjoint(steps)
            )
        for route_id, platform_skills in {
            "implement-web": ["frontend-design", "web-component-design"],
            "implement-mobile": ["react-native-design"],
        }.items():
            steps = {step["id"]: step for step in routes[route_id]["steps"]}
            self.assertEqual(
                steps["prototype-check"]["transitions"]["manual"],
                {"completed": "implementation", "missing": "cancelled"},
            )
            self.assertEqual(steps["prototype-check"]["write_policy"], "product")
            resolution = steps["prototype-check"]["instructions"]
            for required in (
                "explicit version token vN",
                "strictly to .ohmyagent/design/vN",
                "only direct child directories",
                "greatest numeric N",
                "RUN_DIRECTORY/prototype.html",
                "complete with outcome missing",
                "never fall back",
            ):
                self.assertIn(required, resolution)
            for step_id, step in steps.items():
                if step_id != "prototype-check":
                    self.assertIn("Reuse exactly the RUN_DIRECTORY resolved", step["instructions"])
            self.assertIn("RUN_DIRECTORY/prototype.html", steps["implementation"]["instructions"])
            self.assertIn("RUN_DIRECTORY/DESIGN.md", steps["implementation"]["instructions"])
            self.assertEqual(steps["implementation"]["skills"], platform_skills)
            self.assertEqual(steps["implementation"]["write_policy"], "product")
            comparison = steps["screenshot-comparison"]
            self.assertEqual(
                comparison["transitions"]["manual"],
                {"passed": "build-verification", "revise": "refinement-checkpoint", "failed": "cancelled"},
            )
            for required in (
                "identical representative frames",
                "75%, 100%, and 125%",
                "content-width utilization below 60%",
                "outer-whitespace asymmetry above 15%",
                "80/100 overall",
                "After three failed comparisons",
            ):
                self.assertIn(required, comparison["instructions"])
            self.assertEqual(
                steps["refinement-checkpoint"]["transitions"]["manual"],
                {"completed": "screenshot-comparison"},
            )
            self.assertIn("fresh capture and score", steps["refinement-checkpoint"]["instructions"])
            self.assertEqual(steps["states-verification"]["transitions"]["manual"], {"completed": "completed"})

        image_steps = {step["id"]: step for step in routes["image-new"]["steps"]}
        self.assertEqual(image_steps["image-cards"]["unavailable_target"], "image-verification")
        verification = image_steps["image-verification"]["instructions"].lower()
        self.assertIn("no interactive selection", verification)
        self.assertIn("actual generated output", verification)

    def test_react_native_directory_matches_manifest_and_frontmatter(self) -> None:
        manifest = json.loads((SKILLS / "manifest.json").read_text(encoding="utf-8"))
        entry = next(skill for skill in manifest["skills"] if skill["skill_id"] == "react-native-design")
        self.assertEqual(entry["skill_md_path"], "react-native-design/SKILL.md")
        self.assertTrue((SKILLS / entry["skill_md_path"]).is_file())
        self.assertIn("name: react-native-design", skill_text("react-native-design"))
        self.assertFalse((SKILLS / "react-native-ui-animation").exists())

    def test_manifest_paths_match_skill_ids_and_frontmatter(self) -> None:
        manifest = json.loads((SKILLS / "manifest.json").read_text(encoding="utf-8"))
        for entry in manifest["skills"]:
            skill_id = entry["skill_id"]
            with self.subTest(skill=skill_id):
                self.assertEqual(entry["skill_md_path"], f"{skill_id}/SKILL.md")
                path = SKILLS / entry["skill_md_path"]
                self.assertTrue(path.is_file())
                self.assertRegex(path.read_text(encoding="utf-8"), rf"(?m)^name:\s*{re.escape(skill_id)}$")

    def test_workflow_dependency_directories_match_skill_names(self) -> None:
        workflow = json.loads((SKILLS / "design-flow" / "workflow.json").read_text(encoding="utf-8"))
        manifest = json.loads((SKILLS / "manifest.json").read_text(encoding="utf-8"))
        manifest_by_id = {skill["skill_id"]: skill for skill in manifest["skills"]}
        dependencies = {
            dependency
            for route in workflow["routes"]
            for step in route["steps"]
            for dependency in step.get("skills", [])
        }
        for dependency in dependencies:
            with self.subTest(skill=dependency):
                path = SKILLS / dependency / "SKILL.md"
                self.assertTrue(path.is_file(), f"workflow dependency must use its skill name as the directory: {dependency}")
                self.assertRegex(path.read_text(encoding="utf-8"), rf"(?m)^name:\s*{re.escape(dependency)}$")
                if dependency in manifest_by_id:
                    self.assertEqual(manifest_by_id[dependency]["skill_md_path"], f"{dependency}/SKILL.md")

    def test_frontmatter_and_directory_names(self) -> None:
        for name in NEW_SKILLS:
            with self.subTest(skill=name):
                text = skill_text(name)
                match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
                self.assertIsNotNone(match)
                frontmatter = match.group(1)
                self.assertRegex(frontmatter, rf"(?m)^name: {re.escape(name)}$")
                self.assertRegex(frontmatter, r"(?m)^description: .+$")
                keys = re.findall(r"(?m)^([a-z][a-z-]*):", frontmatter)
                if name == "design-flow":
                    self.assertEqual(keys, ["name", "description"])
                else:
                    self.assertEqual(keys, ["name", "description", "visibility", "owner"])
                    self.assertRegex(frontmatter, r"(?m)^visibility: internal$")
                    self.assertRegex(frontmatter, r"(?m)^owner: design-flow$")

    def test_craft_references_are_copied_and_named_in_skill(self) -> None:
        for name, references in CRAFT_REFS.items():
            text = skill_text(name)
            for reference in references:
                with self.subTest(skill=name, reference=reference):
                    path = SKILLS / name / "references" / reference
                    self.assertTrue(path.is_file())
                    self.assertGreater(path.stat().st_size, 500)
                    self.assertIn(f"references/{reference}", text)

    def test_main_flow_omits_legacy_protocol_identifiers(self) -> None:
        combined = "\n".join(skill_text(name) for name in NEW_SKILLS)
        for forbidden in ("MonkeyDesignRoute", "MonkeyDesignSelectCards", "Prepare Contract"):
            with self.subTest(identifier=forbidden):
                self.assertNotIn(forbidden, combined)
        for name in NEW_SKILLS:
            self.assertFalse((SKILLS / name / "skill.json").exists())

    def test_design_flow_is_a_thin_workflow_entry(self) -> None:
        flow = skill_text("design-flow")
        self.assertLessEqual(len(flow.splitlines()), 40)
        for required in ("Workflow", "complete_step", "DesignSelectCards", "AskUserQuestion", ".ohmyagent/design/", "implement-web", "implement-mobile"):
            self.assertIn(required, flow)
        self.assertNotIn("exactly three materially relevant candidates", flow)

    def test_image_generation_contract(self) -> None:
        image = skill_text("image-generation")
        art = skill_text("web-design-art-direction")
        for text in (image, art):
            with self.subTest(skill="preview-path-contract"):
                self.assertIn("workspace-relative", text.lower())
                self.assertIn("not an absolute path", text.lower())
            for required in (
                "image.text_to_image",
                ".ohmyagent/design/",
                "DesignSelectCards",
                "2400 px",
                "1 MiB",
                "PNG, JPEG, or GIF",
                "never crop",
            ):
                with self.subTest(required=required):
                    self.assertIn(required.lower(), text.lower())
        self.assertIn("exactly three", image)
        self.assertIn("materially different", image)


if __name__ == "__main__":
    unittest.main()
