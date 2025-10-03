# Rolesnap

[![PyPI](https://img.shields.io/pypi/v/rolesnap.svg)](https://pypi.org/project/rolesnap/)
![Python](https://img.shields.io/pypi/pyversions/rolesnap.svg)
[![CI](https://github.com/MeshcheryTapo4ek/snapshot-pepester/actions/workflows/ci.yml/badge.svg)](https://github.com/MeshcheryTapo4ek/snapshot-pepester/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-mkdocs--material-success)](https://meshcherytapo4ek.github.io/snapshot-pepester/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

**Rolesnap creates structured, role-based context for LLMs from your codebase.**

Stop copy-pasting files. Describe your architecture in a small YAML file and let `rolesnap` build a clean JSON snapshot with only what matters.

## Key Features

- **Role-Based Snapshots**: Generate context for a specific feature, microservice, or architectural layer. Stop feeding the LLM irrelevant code.

- **Scan Multiple Roles at Once**: Create a unified snapshot of several roles and their dependencies with a single command.
  ```bash
  rolesnap role backend-api frontend-app
  ```

---

## Quickstart

### Path Snapshot in 5 seconds

Need a snapshot of one directory? Use `dir`.

```bash
# 1) Install
uv tool install rolesnap

# 2) Scan a directory
rolesnap dir /path/to/your/project/src/api
```

This writes `rolesnap.json` inside `/path/to/your/project/src/api`.

```json
{
  "Scanned Directory": {
    "src/api/main.py": "...",
    "src/api/routes.py": "..."
  }
}
```

---

### Project Roles in ~5 commands

Model parts of your system and get dependency-aware snapshots.

**1) Initialize in your repo**

```bash
cd /path/to/your/project
rolesnap init
```

A template is created at `docs/roles/rolesnap.yaml`.

**2) Set your project root**

```yaml
# docs/roles/rolesnap.yaml
settings:
  project_root: "/path/to/your/project"  # <-- set absolute path
```

**3) Define two roles with the schema**

```yaml
# docs/roles/rolesnap.yaml
roles:
  dtos:
    help: "Shared DTOs."
    output_dto:
      - "shared/dtos.py"

  booking_service:
    help: "Python backend for bookings."
    domain:
      - "services/booking/domain.py"
    input_dto:
      import_dto_from:
        - "dtos"
```

**4) Generate a role snapshot**

```bash
export ROLESNAP_CONFIG=./docs/roles/rolesnap.yaml
rolesnap role booking_service
```

This writes `rolesnap.json` in your project root.

**5) Result**

```json
{
  "Imported DTOs": {
    "shared/dtos.py": "class BookingDTO: ..."
  },
  "Domain": {
    "services/booking/domain.py": "..."
  }
}
```

Paste the JSON content into your LLM prompt together with your question.

---

## Common pitfalls

- **.env loading scope**  
  `.env` is loaded **only from the current working directory**. Parent folders are ignored.

- **Exclusions**  
  Extensive default glob excludes (caches, media, archives). Add more via `settings.exclude_dirs`.

- **Large files**  
  Files larger than 2 MiB are skipped and recorded as `"<skipped_large_file>"`. Control with `--max-file-size`.

- **Non-UTF-8**  
  Non-UTF-8 files are silently skipped.

---

## Links

- **Best Practices:** https://meshcherytapo4ek.github.io/snapshot-pepester/rolesnap_best_practices/
- **Full Documentation:** https://meshcherytapo4ek.github.io/snapshot-pepester/
- **CLI Reference:** https://meshcherytapo4ek.github.io/snapshot-pepester/cli/
- **Changelog:** https://meshcherytapo4ek.github.io/snapshot-pepester/changelog/

---

## License

MIT License. See [LICENSE](./LICENSE).