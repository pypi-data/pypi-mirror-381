import pytest
import subprocess
import json
import os
from pathlib import Path

FIXTURE_DIR = Path(__file__).parent / "fixtures"


def normalize_json(data):
    """Recursively sort keys in a dictionary to allow for consistent comparison."""
    if isinstance(data, dict):
        return {k: normalize_json(data[k]) for k in sorted(data.keys())}
    return data


def run_and_compare(
    fixture_name: str,
    command: list[str],
    expected_json_name: str,
    tmp_path: Path,
    cwd_is_fixture_root: bool = False,
):
    """Helper function to run rolesnap and compare its output with an expected JSON file."""
    fixture_path = FIXTURE_DIR / fixture_name
    project_root = fixture_path / "project_root"
    config_path = fixture_path / "roles/rolesnap.yaml"
    expected_path = fixture_path / "expected" / expected_json_name
    output_path = tmp_path / "rolesnap.json"

    env = os.environ.copy()
    # Resolve paths for the environment variable and arguments
    env["ROLESNAP_CONFIG"] = str(config_path.resolve())

    # Separate subcommand from its arguments
    subcommand = command[0]
    subcommand_args = command[1:]

    # Separate subcommand options (like --include-utils) from positional args
    subcommand_options = [arg for arg in subcommand_args if arg.startswith('-')]
    positional_args = [arg for arg in subcommand_args if not arg.startswith('-')]

    global_options = [
        "--output", str(output_path.resolve()),
        "--no-banner", "--quiet", "--no-color"
    ]

    # Assemble the command in the correct order: global_opts -> subcommand -> subcommand_opts -> positional_args
    full_command = ["rolesnap"] + global_options + [subcommand] + subcommand_options + positional_args

    # Some tests require CWD to be the fixture root for path resolution
    cwd = fixture_path if cwd_is_fixture_root else project_root

    result = subprocess.run(
        full_command,
        cwd=cwd,
        check=False,  # Don't raise exception on non-zero exit
        env=env,
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, f"CLI command failed:\n{result.stderr}"

    with open(output_path) as f:
        generated_data = json.load(f)

    with open(expected_path) as f:
        expected_data = json.load(f)

    assert normalize_json(generated_data) == normalize_json(expected_data)


def test_simple_single_role(tmp_path):
    run_and_compare("simple_single_role", ["role", "app"], "rolesnap.json", tmp_path)

def test_imports_only(tmp_path):
    run_and_compare("imports_only", ["role", "importer_role"], "rolesnap.json", tmp_path)

def test_input_dto_only(tmp_path):
    run_and_compare("input_dto_only", ["role", "consumer_role"], "rolesnap.json", tmp_path)

def test_exports_push(tmp_path):
    run_and_compare("exports_push", ["role", "consumer_role"], "rolesnap.json", tmp_path)

def test_dedup_combo(tmp_path):
    run_and_compare("dedup_combo", ["role", "consumer_role"], "rolesnap.json", tmp_path)

def test_multi_role_union(tmp_path):
    run_and_compare("multi_role_union", ["role", "role_x", "role_y"], "union.json", tmp_path)

def test_excludes_and_utils_base(tmp_path):
    run_and_compare("excludes_and_utils", ["role", "app"], "base.json", tmp_path)

def test_excludes_and_utils_with_utils(tmp_path):
    run_and_compare("excludes_and_utils", ["role", "app", "--include-utils"], "with_utils.json", tmp_path)

def test_docs_root(tmp_path):
    # This test needs the CWD to be the fixture root for docs_root to resolve correctly
    run_and_compare("docs_root", ["role", "app"], "rolesnap.json", tmp_path, cwd_is_fixture_root=True)

