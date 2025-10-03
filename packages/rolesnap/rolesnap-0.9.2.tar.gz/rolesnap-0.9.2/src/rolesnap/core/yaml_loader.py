from __future__ import annotations

from pathlib import Path

import yaml

from ..constants import DEFAULT_EXCLUDE_DIRS, DEFAULT_UTILS_DIRS
from .models import Config, InputDTO, OutputDTO, Role, Settings


def _as_str_list(value: object, field_name: str, ctx_name: str) -> list[str]:
    """Normalize to list[str] and validate."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out: list[str] = []
        for i, v in enumerate(value):
            if not isinstance(v, str):
                raise TypeError(
                    f"'{ctx_name}': field '{field_name}' element #{i} must be a string, got {type(v).__name__}"
                )
            out.append(v)
        return out
    raise TypeError(
        f"'{ctx_name}': field '{field_name}' must be a string or list of strings, got {type(value).__name__}"
    )


def _as_opt_str(value: object, field_name: str, ctx_name: str) -> str | None:
    """Normalize to Optional[str]."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    raise TypeError(
        f"'{ctx_name}': field '{field_name}' must be a string if provided, got {type(value).__name__}"
    )


def _validate_roles(roles: dict[str, Role]) -> None:
    """Ensure imported roles exist and no cycles."""
    for name, role in roles.items():
        for dep in role.imports:
            if dep not in roles:
                raise ValueError(f"Role '{name}' imports unknown role '{dep}'")
        for dep in role.input_dto.import_dto_from:
            if dep not in roles:
                raise ValueError(f"Role '{name}' in 'input_dto.import_dto_from' imports unknown role '{dep}'")
        for dep in role.output_dto.exports_dto_to:
            if dep not in roles:
                raise ValueError(f"Role '{name}' in 'output_dto.exports_dto_to' exports to unknown role '{dep}'")

    visiting: set[str] = set()
    visited: set[str] = set()

    def dfs(node: str) -> None:
        if node in visiting:
            raise ValueError(f"Import cycle detected at role '{node}'")
        if node in visited:
            return
        visiting.add(node)
        for dep in roles[node].imports:
            dfs(dep)
        visiting.remove(node)
        visited.add(node)

    for role_name in roles:
        if role_name not in visited:
            dfs(role_name)


def _parse_input_dto(value: object, ctx_name: str) -> InputDTO:
    if value is None:
        return InputDTO()
    if isinstance(value, list):
        return InputDTO(paths=_as_str_list(value, "input_dto", ctx_name))
    if isinstance(value, dict):
        return InputDTO(
            paths=_as_str_list(value.get("paths"), "paths", f"{ctx_name}.input_dto"),
            import_dto_from=_as_str_list(
                value.get("import_dto_from"), "import_dto_from", f"{ctx_name}.input_dto"
            ),
        )
    raise TypeError(
        f"'{ctx_name}': field 'input_dto' must be a list or a mapping, got {type(value).__name__}"
    )


def _parse_output_dto(value: object, ctx_name: str) -> OutputDTO:
    if value is None:
        return OutputDTO()
    if isinstance(value, list):
        return OutputDTO(paths=_as_str_list(value, "output_dto", ctx_name))
    if isinstance(value, dict):
        return OutputDTO(
            paths=_as_str_list(value.get("paths"), "paths", f"{ctx_name}.output_dto"),
            exports_dto_to=_as_str_list(
                value.get("exports_dto_to"), "exports_dto_to", f"{ctx_name}.output_dto"
            ),
        )
    raise TypeError(
        f"'{ctx_name}': field 'output_dto' must be a list or a mapping, got {type(value).__name__}"
    )


def _parse_roles(raw_roles: dict) -> dict[str, Role]:
    roles: dict[str, Role] = {}
    for name, data in raw_roles.items():
        if not isinstance(data, dict):
            raise ValueError(f"Role '{name}' must be a mapping.")

        obsolete_fields = {"domain_models", "domain_services", "import_dto_from"}
        found_obsolete = obsolete_fields.intersection(data.keys())
        if found_obsolete:
            raise ValueError(
                f"Role '{name}' uses obsolete fields from schema < 0.9.2: {', '.join(sorted(found_obsolete))}. "
                "Please rename 'domain_models' to 'domain', remove 'domain_services', "
                "and move 'import_dto_from' under 'input_dto'."
            )

        # Accept both 'docs' and 'DOCS' for convenience
        docs_val = data.get("docs", data.get("DOCS"))
        role = Role(
            help=str(data.get("help", "")),
            domain=_as_str_list(data.get("domain"), "domain", name),
            ports=_as_str_list(data.get("ports"), "ports", name),
            output_dto=_parse_output_dto(data.get("output_dto"), name),
            input_dto=_parse_input_dto(data.get("input_dto"), name),
            internal_dto=_as_str_list(data.get("internal_dto"), "internal_dto", name),
            internal_logic=_as_str_list(data.get("internal_logic"), "internal_logic", name),
            base_tasks=_as_str_list(data.get("base_tasks"), "base_tasks", name),
            advanced_tasks=_as_str_list(data.get("advanced_tasks"), "advanced_tasks", name),
            docs=_as_str_list(docs_val, "docs", name),
            imports=_as_str_list(data.get("imports"), "imports", name),
        )
        roles[name] = role
    _validate_roles(roles)
    return roles


def _parse_settings(raw: dict[str, dict]) -> Settings:
    exclude_dirs: set[str] = set(DEFAULT_EXCLUDE_DIRS)
    utils_dirs: list[str] = list(DEFAULT_UTILS_DIRS)
    project_root: str | None = None
    docs_root: str | None = None

    s = raw.get("settings")
    if isinstance(s, dict):
        if "exclude_dirs" in s:
            exclude_dirs.update(_as_str_list(s["exclude_dirs"], "exclude_dirs", "settings"))
        if "utils_dirs" in s:
            utils_dirs = _as_str_list(s["utils_dirs"], "utils_dirs", "settings")
        if "project_root" in s:
            project_root = _as_opt_str(s["project_root"], "project_root", "settings")
        if "docs_root" in s:
            docs_root = _as_opt_str(s["docs_root"], "docs_root", "settings")

    return Settings(
        exclude_dirs=exclude_dirs,
        utils_dirs=utils_dirs,
        project_root=project_root,
        docs_root=docs_root,
    )


def load_config_from_yaml(config_path: Path) -> Config:
    """Load full config bundle (roles + settings with project_root/docs_root)."""

    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or "roles" not in raw or not isinstance(raw["roles"], dict):
        raise ValueError("Invalid YAML structure. Expected root key 'roles' with a mapping.")

    roles = _parse_roles(raw["roles"])
    settings = _parse_settings(raw)
    return Config(roles=roles, settings=settings)


def load_roles_from_yaml(config_path: Path) -> dict[str, Role]:
    """Backward-compat for existing callers (self-scan)."""
    return load_config_from_yaml(config_path).roles