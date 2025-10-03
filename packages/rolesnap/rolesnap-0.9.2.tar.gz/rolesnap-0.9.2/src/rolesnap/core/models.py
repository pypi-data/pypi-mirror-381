from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class InputDTO:
    """Input DTOs configuration."""

    paths: list[str] = field(default_factory=list)
    import_dto_from: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class OutputDTO:
    """Output DTOs configuration."""

    paths: list[str] = field(default_factory=list)
    exports_dto_to: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Role:
    """Role definition (schema 0.9.2)."""

    help: str = ""
    # Core contract
    domain: list[str] = field(default_factory=list)
    ports: list[str] = field(default_factory=list)
    # DTOs
    output_dto: OutputDTO = field(default_factory=OutputDTO)
    input_dto: InputDTO = field(default_factory=InputDTO)
    internal_dto: list[str] = field(default_factory=list)
    # Internal implementation
    internal_logic: list[str] = field(default_factory=list)
    # Task sets
    base_tasks: list[str] = field(default_factory=list)
    advanced_tasks: list[str] = field(default_factory=list)
    # Documentation sources
    docs: list[str] = field(default_factory=list)
    # Dependencies
    imports: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Settings:
    """Global settings loaded from YAML."""

    exclude_dirs: set[str] = field(default_factory=set)
    utils_dirs: list[str] = field(default_factory=list)
    project_root: str | None = None  # absolute filesystem path to the project root
    docs_root: str | None = (
        None  # absolute filesystem path to top-level DOCS folder (sibling to project)
    )


@dataclass(frozen=True)
class Config:
    """Full config bundle."""

    roles: dict[str, Role] = field(default_factory=dict)
    settings: Settings = field(default_factory=Settings)