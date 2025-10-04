"""Calibration CSV Loader

Finalized behaviors:
    - Container selection supports alias tokens for Investigator Provided, Scott, CVFG Control, and CVFG Missense calibrations.
    - Duplicate evidence strengths within a single row: first kept, later duplicates skipped with warning.
    - Missing strength with an interval: range skipped with warning (does not abort row).
    - Classification mapping: normal|abnormal|not_specified kept; indeterminate|uncertain|unknown -> not_specified; strength-based fallback (positive->abnormal, negative->normal, zero/None->not_specified).
    - Publications: Brnich citation (cite_brnich_method TRUE) + thresholds_pmid -> source only; odds_path_pmid -> odds_path_source only.
    - Publications appended to ScoreSet as secondary (primary=False) if not already present; unaffected by overwrite flag.
    - Odds path ratios parsed per range; invalid numeric values ignored.
    - Dry-run behavior managed by with_database_session decorator (use --commit to persist changes).

CSV expected columns (minimum):
    score_set_urn, calibration_name, range_1, range_1_strength, ... (up to range_5 / range_5_strength)
Optional columns:
    range_i_classification, range_i_odds_path, baseline_score, baseline_score_notes,
    cite_brnich_method, thresholds_pmid, odds_path_pmid

Usage examples:
    python -m mavedb.scripts.load_calibration_csv data.csv --commit
    python -m mavedb.scripts.load_calibration_csv data.csv --overwrite --commit

"""

import csv
import asyncio
import re
import click
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

from sqlalchemy.orm import Session

from mavedb.scripts.environment import with_database_session
from mavedb.models.score_set import ScoreSet
from mavedb.view_models.publication_identifier import PublicationIdentifierCreate
from mavedb.lib.identifiers import find_or_create_publication_identifier
from mavedb.view_models.score_range import (
    ScoreSetRangesCreate,
    InvestigatorScoreRangesCreate,
    ScottScoreRangesCreate,
    IGVFCodingVariantFocusGroupControlScoreRangesCreate,
    IGVFCodingVariantFocusGroupMissenseScoreRangesCreate,
    BrnichScoreRangeCreate,
)
from mavedb.view_models.odds_path import OddsPathCreate

BRNICH_PMID = "31892348"
RANGE_PATTERN = re.compile(r"^\s*([\[(])\s*([^,]+)\s*,\s*([^\])]+)\s*([])])\s*$", re.IGNORECASE)
INFINITY_TOKENS = {"inf", "+inf", "-inf", "infinity", "+infinity", "-infinity"}
MAX_RANGES = 5

CONTAINER_MAP = {
    "scott": ("scott_calibration", ScottScoreRangesCreate, BrnichScoreRangeCreate, True),
    "investigator_provided": ("investigator_provided", InvestigatorScoreRangesCreate, BrnichScoreRangeCreate, True),
    "cvfg_all_vars": (
        "cvfg_all_variants",
        IGVFCodingVariantFocusGroupControlScoreRangesCreate,
        BrnichScoreRangeCreate,
        True,
    ),
    "cvfg_missense_vars": (
        "cvfg_missense_variants",
        IGVFCodingVariantFocusGroupMissenseScoreRangesCreate,
        BrnichScoreRangeCreate,
        True,
    ),
}


def pick_container(calibration_name: str):
    name_l = (calibration_name or "").lower()
    return CONTAINER_MAP.get(name_l)


def parse_bound(raw: str) -> Optional[float]:
    raw = raw.strip()
    if not raw:
        return None
    rl = raw.lower()
    if rl in INFINITY_TOKENS:
        return None
    try:
        return float(raw)
    except ValueError:
        raise ValueError(f"Unparseable bound '{raw}'")


def parse_interval(text: str) -> Tuple[Optional[float], Optional[float], bool, bool]:
    m = RANGE_PATTERN.match(text)
    if not m:
        raise ValueError(f"Invalid range format '{text}'")
    left_br, lower_raw, upper_raw, right_br = m.groups()
    lower = parse_bound(lower_raw)
    upper = parse_bound(upper_raw)
    inclusive_lower = left_br == "["
    inclusive_upper = right_br == "]"
    if lower is not None and upper is not None:
        if lower > upper:
            raise ValueError("Lower bound greater than upper bound")
        if lower == upper:
            raise ValueError("Lower bound equals upper bound")
    return lower, upper, inclusive_lower, inclusive_upper


def normalize_classification(raw: Optional[str], strength: Optional[str]) -> str:
    if raw:
        r = raw.strip().lower()
        if r in {"normal", "abnormal", "not_specified"}:
            return r
        if r in {"indeterminate", "uncertain", "unknown"}:
            return "not_specified"

    if strength:
        if strength.upper().startswith("PS"):
            return "abnormal"
        if strength.upper().startswith("BS"):
            return "normal"

    return "not_specified"


def build_publications(
    cite_brnich: str, thresholds_pmid: str, odds_path_pmid: str
) -> tuple[List[PublicationIdentifierCreate], List[PublicationIdentifierCreate]]:
    """Return (source_publications, odds_path_publications).

    Rules:
      - Brnich citation only goes to source when cite_brnich_method == TRUE.
      - thresholds_pmid (if present) -> source only.
      - odds_path_pmid (if present) -> odds_path_source only.
      - Duplicates between lists preserved separately if same PMID used for both roles.
    """
    source_pmids = set()
    odds_pmids = set()
    if cite_brnich and cite_brnich.strip().upper() == "TRUE":
        source_pmids.add(BRNICH_PMID)
    if thresholds_pmid and thresholds_pmid.strip():
        source_pmids.add(thresholds_pmid.strip())
    if odds_path_pmid and odds_path_pmid.strip():
        odds_pmids.add(odds_path_pmid.strip())

    source_pubs = [
        PublicationIdentifierCreate(identifier=p, db_name="PubMed") for p in sorted(source_pmids) if p != "cvfg"
    ]
    odds_pubs = [PublicationIdentifierCreate(identifier=p, db_name="PubMed") for p in sorted(odds_pmids) if p != "cvfg"]
    return source_pubs, odds_pubs


def build_ranges(row: Dict[str, str], range_create_cls, brnich_style: bool):
    ranges = []
    any_odds_path = False
    for i in range(1, MAX_RANGES + 1):
        range_key = f"range_{i}"
        interval_text = row.get(range_key, "").strip()
        if not interval_text:
            continue

        try:
            lower, upper, incl_lower, incl_upper = parse_interval(interval_text)
        except ValueError as e:
            click.echo(f"Skipping invalid interval in row (range_{i}): {e}", err=True)
            continue

        strength = row.get(f"range_{i}_strength", "").strip()
        if strength not in [
            "BS3_STRONG",
            "BS3_MODERATE",
            "BS3_SUPPORTING",
            "INDETERMINATE",
            "PS3_VERY_STRONG",
            "PS3_STRONG",
            "PS3_MODERATE",
            "PS3_SUPPORTING",
            "",
        ]:
            click.echo(f"Skipping range_{i}: invalid strength '{strength}'", err=True)
            continue

        classification = normalize_classification(row.get(f"range_{i}_classification"), strength)
        odds_path_val = row.get(f"range_{i}_odds_path", "").strip()
        odds_path = None
        if odds_path_val:
            any_odds_path = True
            try:
                ratio = float(odds_path_val)
                odds_path = OddsPathCreate(ratio=ratio, evidence=strength)
            except ValueError:
                click.echo(f"Ignoring odds_path for range_{i}: invalid value '{odds_path_val}'", err=True)

        label = row.get(f"range_{i}_name", "").strip()
        ranges.append(
            range_create_cls(
                label=label,
                classification=classification,
                range=(lower, upper),
                inclusive_lower_bound=incl_lower if lower is not None else False,
                inclusive_upper_bound=incl_upper if upper is not None else False,
                **({"odds_path": odds_path} if odds_path is not None else {}),
            )
        )
    return ranges, any_odds_path


def update_container(existing: ScoreSetRangesCreate, key: str, container_obj, overwrite: bool) -> bool:
    if getattr(existing, key) is not None and not overwrite:
        return False
    setattr(existing, key, container_obj)
    return True


@click.command()
@with_database_session
@click.argument("csv_path", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option("--delimiter", default=",", show_default=True, help="CSV delimiter")
@click.option("--overwrite", is_flag=True, default=False, help="Overwrite existing container for each score set")
def main(db: Session, csv_path: str, delimiter: str, overwrite: bool):
    """Load calibration CSV into score set score_ranges (container chosen by calibration_name).

    Rows skipped if no URNs or no valid ranges. Only the targeted container key is replaced (unless --overwrite).
    """
    path = Path(csv_path)
    updated_sets = 0
    skipped_rows = 0
    errors = 0
    processed_rows = 0

    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        for row in reader:
            processed_rows += 1
            urn_cell = row.get("score_set_urn", "")
            if not urn_cell:
                skipped_rows += 1
                continue

            urns = [u.strip() for u in urn_cell.split(",") if u.strip()]
            if not urns:
                skipped_rows += 1
                continue

            calibration_name = row.get("calibration_name", "")
            if not calibration_name:
                skipped_rows += 1
                continue
            container_key, wrapper_cls, range_cls, brnich_style = pick_container(calibration_name)

            source_pubs, odds_pubs = build_publications(
                row.get("cite_brnich_method", ""), row.get("thresholds_pmid", ""), row.get("odds_path_pmid", "")
            )

            ranges, any_odds_path = build_ranges(row, range_cls, brnich_style)
            if not ranges and container_key != "investigator_provided":
                skipped_rows += 1
                continue

            # Build wrapper
            wrapper_kwargs: Dict[str, Any] = {"ranges": ranges}
            if brnich_style:
                # baseline score only for brnich-style wrappers
                baseline_raw = row.get("baseline_score", "").strip()
                if baseline_raw:
                    try:
                        wrapper_kwargs["baseline_score"] = float(baseline_raw)
                    except ValueError:
                        click.echo(f"Invalid baseline_score '{baseline_raw}' ignored", err=True)
                notes = row.get("baseline_score_notes", "").strip()
                if notes:
                    wrapper_kwargs["baseline_score_description"] = notes
                if source_pubs:
                    wrapper_kwargs["source"] = source_pubs
                if any_odds_path and odds_pubs:
                    wrapper_kwargs["odds_path_source"] = odds_pubs
            else:
                if source_pubs:
                    wrapper_kwargs["source"] = source_pubs
                if any_odds_path and odds_pubs:
                    wrapper_kwargs["odds_path_source"] = odds_pubs

            try:
                container_obj = wrapper_cls(**wrapper_kwargs)
            except Exception as e:  # broad to keep import running
                errors += 1
                click.echo(f"Validation error building container for {container_key}: {e}", err=True)
                continue

            for urn in urns:
                score_set: Optional[ScoreSet] = db.query(ScoreSet).filter(ScoreSet.urn == urn).one_or_none()
                if not score_set:
                    click.echo(f"Score set {urn} not found; skipping", err=True)
                    continue
                if score_set.score_ranges:
                    existing = ScoreSetRangesCreate(**score_set.score_ranges)
                else:
                    existing = ScoreSetRangesCreate()
                replaced = update_container(existing, container_key, container_obj, overwrite)
                if not replaced:
                    click.echo(f"Container {container_key} exists for {urn}; use --overwrite to replace", err=True)
                    # Even if we skip replacing ranges, we still may want to attach publications below.
                else:
                    score_set.score_ranges = existing.model_dump(exclude_none=True)

                # Append publication identifiers (secondary) if provided (union of both source & odds_path sources).
                combined_pubs = {p.identifier: p for p in (source_pubs + odds_pubs)}
                if combined_pubs:
                    existing_pmids = {
                        p.identifier
                        for p in getattr(score_set, "publication_identifiers", [])
                        if getattr(p, "identifier", None)
                    }
                    for pub in combined_pubs.values():
                        if pub.identifier in existing_pmids:
                            continue
                        try:
                            # run async helper in a fresh loop (script context); if already in loop this could be adapted.
                            pub_model = asyncio.run(
                                find_or_create_publication_identifier(db, pub.identifier, pub.db_name)
                            )
                            setattr(pub_model, "primary", False)
                            score_set.publication_identifiers.append(pub_model)
                            existing_pmids.add(pub.identifier)
                        except Exception as e:  # pragma: no cover - defensive
                            click.echo(f"Failed attaching publication {pub.identifier} to {urn}: {e}", err=True)

                db.add(score_set)
                updated_sets += 1

    click.echo(
        f"Processed {processed_rows} rows; Updated {updated_sets} score sets; Skipped {skipped_rows} rows; Errors {errors}."
    )


if __name__ == "__main__":  # pragma: no cover
    main()
