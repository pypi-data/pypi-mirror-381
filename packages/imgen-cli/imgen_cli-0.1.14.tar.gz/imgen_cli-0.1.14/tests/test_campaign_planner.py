from __future__ import annotations

import sys

from pathlib import Path

import pytest

from imagemcp.campaign.planner import (
    CollectCampaignBriefPayload,
    PlanBatchGenerationPayload,
    PlanCampaignRoutesPayload,
    PlacementPlanInput,
    RoutePlanInput,
    collect_campaign_brief,
    normalize_collect_campaign_brief_payload,
    normalize_plan_batch_generation_payload,
    normalize_plan_campaign_routes_payload,
    plan_batch_generation,
    plan_campaign_routes,
)
from imagemcp.campaign.orchestrator import CliAction, execute_cli_actions


def test_collect_campaign_brief_reports_missing_fields():
    payload = CollectCampaignBriefPayload()
    result = collect_campaign_brief(payload)
    missing_fields = {item["field"] for item in result["missing"]}
    assert "campaign_id" in missing_fields
    assert "name" in missing_fields
    assert "objective" in missing_fields
    assert "routes" in missing_fields
    assert "placements" in missing_fields
    defaults = result["defaults"]
    assert defaults["variants"] == 2
    expected_tags = ["mock"] if defaults["generator"] == "mock" else []
    assert defaults["tags"] == expected_tags
    assert "placements" in result["catalog"]


def test_normalize_collect_campaign_brief_payload_accepts_json():
    normalized = normalize_collect_campaign_brief_payload(
        '{"brief": {"campaign_id": "spring_wave", "tags": ["mock", "qa"]}}'
    )
    assert isinstance(normalized, CollectCampaignBriefPayload)
    assert normalized.brief.campaign_id == "spring_wave"
    assert normalized.brief.tags == ["mock", "qa"]


def test_collect_campaign_brief_defaults_mock_tags():
    payload = CollectCampaignBriefPayload(
        brief=normalize_collect_campaign_brief_payload(
            '{"brief": {"generator": "mock"}}'
        ).brief
    )
    result = collect_campaign_brief(payload)
    assert result["defaults"]["generator"] == "mock"
    assert result["defaults"]["tags"] == ["mock"]


def test_plan_campaign_routes_emits_cli_actions(tmp_path: Path):
    payload = PlanCampaignRoutesPayload(
        campaign_id="spring_wave",
        name="Spring Wave",
        objective="Exercise the campaign toolchain",
        routes=[
            RoutePlanInput(
                route_id="ocean_luxury",
                name="Ocean Luxury",
                summary="Premium seaside visuals",
                prompt_template="Luxurious oceanfront aesthetic",
                prompt_tokens=["ocean", "luxury"],
            )
        ],
        placements=[
            PlacementPlanInput(placement_id="meta_square_awareness", template_id="meta_square_awareness")
        ],
        projectRoot=str(tmp_path),
        summary_only=True,
        tags=["mock", "qa"],
        generator="mock",
    )
    result = plan_campaign_routes(payload)
    cli_payload = result["cli"]
    actions = cli_payload["actions"]
    assert actions[0]["command"][:3] == ["imgen", "campaign", "init"]
    assert any(action["step"] == "generate" for action in actions)
    assert cli_payload["requirements"]["command"] == "imgen"
    assert result["plan"]["generator"] == "mock"
    assert result["plan"]["provider"] == "mock"


def test_normalize_plan_campaign_routes_payload_accepts_dict():
    raw = {
        "campaign_id": "spring_wave",
        "routes": [
            {"route_id": "ocean_luxury"},
        ],
        "placements": [
            {"placement_id": "meta_square_awareness"},
        ],
    }
    normalized = normalize_plan_campaign_routes_payload(raw)
    assert isinstance(normalized, PlanCampaignRoutesPayload)
    assert normalized.routes[0].route_id == "ocean_luxury"
    assert normalized.placements[0].placement_id == "meta_square_awareness"


def test_plan_batch_generation_actions(tmp_path: Path):
    payload = PlanBatchGenerationPayload(
        campaign_id="spring_wave",
        routes=["ocean_luxury"],
        placements=["meta_square_awareness"],
        generator="mock",
        projectRoot=str(tmp_path),
    )
    result = plan_batch_generation(payload)
    actions = result["cli"]["actions"]
    steps = [action["step"] for action in actions]
    assert steps == ["batch-scaffold", "batch", "export"]
    assert result["plan"]["generator"] == "mock"


def test_normalize_plan_batch_generation_payload_accepts_string():
    normalized = normalize_plan_batch_generation_payload(
        '{"campaign_id": "spring_wave", "routes": ["capsule"], "placements": ["meta"]}'
    )
    assert isinstance(normalized, PlanBatchGenerationPayload)
    assert normalized.routes == ["capsule"]


def test_execute_cli_actions_runs_commands(tmp_path: Path):
    ok_action = {
        "step": "echo",
        "description": "Echo text",
        "command": [sys.executable, "-c", "print('ok')"],
    }
    from io import StringIO

    buffer = StringIO()
    codes = execute_cli_actions([ok_action], project_root=str(tmp_path), stream=buffer)
    assert codes == [0]
    assert "step=echo" in buffer.getvalue()


def test_execute_cli_actions_stops_on_failure(tmp_path: Path):
    actions = [
        CliAction(step="pass", description="", command=[sys.executable, "-c", "import sys; sys.exit(0)"]),
        CliAction(step="fail", description="", command=[sys.executable, "-c", "import sys; sys.exit(3)"]),
        CliAction(step="skip", description="", command=[sys.executable, "-c", "import sys; sys.exit(0)"]),
    ]
    from io import StringIO

    buffer = StringIO()
    codes = execute_cli_actions(actions, project_root=str(tmp_path), stream=buffer)
    assert codes == [0, 3]
