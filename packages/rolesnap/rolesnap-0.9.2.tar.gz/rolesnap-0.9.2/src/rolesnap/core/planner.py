from __future__ import annotations

from collections.abc import Iterable

from .models import Role


def add_all(target: set[str], items: Iterable[str]) -> None:
    for it in items:
        if it:
            target.add(it.rstrip("/"))


def collect_multi_role_categories(
    roles: dict[str, Role],
    target_roles: list[str],
    include_utils: bool,
    utils_dirs: list[str],
) -> dict[str, list[str]]:
    """
    Build a unified, categorized scan source map for a list of target roles.
    """

    # Initialize unified categories with sets for deduplication
    unified: dict[str, set[str]] = {
        "Domain": set(),
        "Ports": set(),
        "Output DTOs": set(),
        "Input DTOs": set(),
        "Internal DTOs": set(),
        "Imported DTOs": set(),
        "Internal Logic": set(),
        "Base Tasks": set(),
        "Collected Base Tasks": set(),
        "Advanced Tasks": set(),
        "Docs": set(),
    }

    target_role_set = set(target_roles)

    for role_name in target_roles:
        r = roles[role_name]

        # 1. Add own paths from the role
        add_all(unified["Domain"], r.domain)
        add_all(unified["Ports"], r.ports)
        add_all(unified["Output DTOs"], r.output_dto.paths)
        add_all(unified["Input DTOs"], r.input_dto.paths)
        add_all(unified["Internal DTOs"], r.internal_dto)
        add_all(unified["Internal Logic"], r.internal_logic)
        add_all(unified["Base Tasks"], r.base_tasks)
        add_all(unified["Advanced Tasks"], r.advanced_tasks)
        add_all(unified["Docs"], r.docs)

        # 2. Add paths from `imports`
        for dep_name in r.imports:
            dep = roles[dep_name]
            add_all(unified["Domain"], dep.domain)
            add_all(unified["Ports"], dep.ports)
            add_all(unified["Imported DTOs"], dep.output_dto.paths)
            add_all(unified["Collected Base Tasks"], dep.base_tasks)

        # 3. Add paths from `input_dto.import_dto_from`
        for dep_name in r.input_dto.import_dto_from:
            dep = roles[dep_name]
            add_all(unified["Imported DTOs"], dep.output_dto.paths)

    # 4. Add paths from roles that export to any of the target roles
    for exporter_name, exporter_role in roles.items():
        # Check if the exporter targets any of our selected roles
        if target_role_set.intersection(exporter_role.output_dto.exports_dto_to):
            add_all(unified["Imported DTOs"], exporter_role.output_dto.paths)

    # Add utils if requested
    if include_utils:
        add_all(unified["Internal Logic"], utils_dirs)

    # Convert sets to sorted lists and filter out empty categories
    result = {k: sorted(list(v)) for k, v in unified.items() if v}

    return result
