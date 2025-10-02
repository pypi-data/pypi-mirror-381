from __future__ import annotations

from collections.abc import Iterable

from .models import Role


def collect_role_categories(
    roles: dict[str, Role],
    selected_role: str,
    include_utils: bool,
    utils_dirs: list[str],
) -> dict[str, list[str]]:
    """
    Build categorized scan sources for a role based on the new architectural schema.
    """
    if selected_role not in roles:
        raise ValueError(f"Unknown role '{selected_role}'. Available: {', '.join(sorted(roles))}")

    r: Role = roles[selected_role]

    def add_all(target: set[str], items: Iterable[str]) -> None:
        for it in items:
            if it:
                target.add(it.rstrip("/"))

    # --- New categories for the selected role ---
    domain_models_self: set[str] = set()
    ports_self: set[str] = set()
    domain_services_self: set[str] = set()
    output_dto_self: set[str] = set()
    input_dto_self: set[str] = set()
    internal_dto_self: set[str] = set()

    add_all(domain_models_self, r.domain_models)
    add_all(ports_self, r.ports)
    add_all(domain_services_self, r.domain_services)
    add_all(output_dto_self, r.output_dto)
    add_all(input_dto_self, r.input_dto)
    add_all(internal_dto_self, r.internal_dto)

    # --- Imported DTOs ---
    imported_dtos: set[str] = set()
    for dep_name in r.import_dto_from:
        dep = roles.get(dep_name)
        if dep is None:
            raise ValueError(f"Role '{selected_role}' imports DTOs from unknown role '{dep_name}'")
        add_all(imported_dtos, dep.output_dto)

    # --- Logic for other categories (preserved) ---
    internal_self: set[str] = set()
    base_self: set[str] = set()
    adv_self: set[str] = set()
    docs_self: set[str] = set()

    add_all(internal_self, r.internal_logic)
    add_all(base_self, r.base_tasks)
    add_all(adv_self, r.advanced_tasks)
    add_all(docs_self, r.docs)
    if include_utils:
        add_all(internal_self, utils_dirs)

    # --- Collect base tasks from main imports ---
    base_imports: set[str] = set()
    for dep_name in r.imports:
        dep = roles.get(dep_name)
        if dep is None:
            raise ValueError(f"Role '{selected_role}' imports unknown role '{dep_name}'")
        add_all(base_imports, dep.base_tasks)

    # --- Assemble the final dictionary ---
    result = {
        "Domain Models": sorted(domain_models_self),
        "Ports": sorted(ports_self),
        "Domain Services": sorted(domain_services_self),
        "Output DTOs": sorted(output_dto_self),
        "Input DTOs": sorted(input_dto_self),
        "Internal DTOs": sorted(internal_dto_self),
        "Imported DTOs": sorted(imported_dtos),
        "Internal Logic": sorted(internal_self),
        "Base Tasks": sorted(base_self),
        "Collected Base Tasks": sorted(base_imports),
        "Advanced Tasks": sorted(adv_self),
        "Docs": sorted(docs_self),
    }

    # Filter out empty categories
    return {k: v for k, v in result.items() if v}
