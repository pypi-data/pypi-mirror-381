from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from .workspace import CampaignWorkspace
from .schemas import CampaignRoute, PlacementRef


def add_route_from_args(
    workspace: CampaignWorkspace,
    route_id: str,
    *,
    name: Optional[str] = None,
    summary: Optional[str] = None,
    prompt_template: Optional[str] = None,
    source: Optional[str] = None,
    prompt_tokens: Optional[Iterable[str]] = None,
    copy_tokens: Optional[Iterable[str]] = None,
    notes: Optional[str] = None,
) -> CampaignRoute:
    route = CampaignRoute(
        route_id=route_id,
        name=name or route_id.replace("_", " ").title(),
        summary=summary or "TODO: fill summary",
        prompt_template=prompt_template or "TODO: fill prompt",
        source=source or "manual",
        prompt_tokens=list(prompt_tokens or ()),
        copy_tokens=list(copy_tokens or ()),
        notes=notes,
    )
    workspace.save_route(route)
    return route


def add_placement_to_campaign(
    workspace: CampaignWorkspace,
    placement_id: str,
    *,
    template_id: Optional[str] = None,
    variants: Optional[int] = None,
    copy_tokens: Optional[Iterable[str]] = None,
    provider: Optional[str] = None,
    notes: Optional[str] = None,
) -> PlacementRef:
    config = workspace.load_config()
    template_slug = template_id or placement_id
    placement_ref = PlacementRef(
        template_id=template_slug,
        override_id=placement_id if placement_id != template_slug else None,
        variants=variants,
        copy_tokens=list(copy_tokens or ()),
        provider=provider,
        notes=notes,
    )
    placements = [ref for ref in config.placements if ref.effective_id != placement_id]
    placements.append(placement_ref)
    config = config.model_copy(update={"placements": placements})
    workspace.save_config(config)
    return placement_ref


def ensure_campaign_exists(workspace: CampaignWorkspace) -> None:
    if not workspace.config_path.exists():
        raise FileNotFoundError(
            f"Campaign '{workspace.campaign_id}' is not initialized."
        )
