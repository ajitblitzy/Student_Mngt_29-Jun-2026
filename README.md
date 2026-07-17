# society_mgmt

`society_mgmt` is a small, idiomatic Python package that was migrated **in place**
from a large, synthetic JavaScript corpus. The original corpus (rooted at
`society_mgmt_300k/`) contained roughly **300,000 lines across 29 `.js` files**
organized into nine layered namespaces, holding **33,105 byte-identical functions**
named `mod_<N>_<i>(x)` — none of which were ever imported, exported, or invoked.
The migration consolidates all of that duplicated logic into a single pure function,
`compute(x)`, and preserves the nine original namespaces as **thin subpackages** that
each re-export `compute`. The package has **no user interface, no endpoints, and no
I/O** — it is a pure, deterministic arithmetic library.

## Package layout

The importable package follows the PyPA "src layout" and lives under
`society_mgmt_300k/src/society_mgmt/`:

```
society_mgmt_300k/
├── pyproject.toml                     # PEP 621 metadata, requires-python >= 3.12, build backend, pytest config
├── LICENSE/
│   └── LICENSE.txt                    # MIT (nested corpus license)
├── src/
│   └── society_mgmt/
│       ├── __init__.py                # package public API; re-exports compute
│       ├── core.py                    # canonical compute(x)
│       ├── config/__init__.py         # re-exports compute
│       ├── controllers/__init__.py    # re-exports compute
│       ├── domain/__init__.py         # re-exports compute
│       ├── middleware/__init__.py     # re-exports compute
│       ├── models/__init__.py         # re-exports compute
│       ├── repositories/__init__.py   # re-exports compute
│       ├── routes/__init__.py         # re-exports compute
│       ├── services/__init__.py       # re-exports compute
│       └── utils/__init__.py          # re-exports compute
└── tests/
    ├── conftest.py                    # shared fixtures / import-path setup
    ├── unit/
    │   └── test_unit.py               # parametrized known-answer tests
    └── integration/
        └── test_integration.py        # cross-package import + compute checks
```

## Requirements

- **CPython ≥ 3.12**
- **No third-party runtime dependencies** — the runtime is standard-library-only.

The build backend is `setuptools` and `pytest` is provided as an optional
development/test extra (see below); neither is required to *import and use* the
package at runtime.

## Installation

The project metadata (`pyproject.toml`) lives in `society_mgmt_300k/`, so the
install target is that directory. Editable installs from the repository root:

```bash
# Runtime only (no third-party dependencies)
pip install -e ./society_mgmt_300k

# With the test extra (adds pytest to run the suite)
pip install -e "./society_mgmt_300k[test]"
```

Equivalently, from inside the project directory:

```bash
cd society_mgmt_300k && pip install -e .
```

## Usage

`compute(x)` is the single public function. It computes `6 * x` and adds `10` when
the result is even:

```python
from society_mgmt import compute

compute(2)    # -> 22
compute(2.5)  # -> 15.0
```

Every layer subpackage re-exports the same function, so any of the nine namespaces
resolves to the identical `compute`:

```python
from society_mgmt.controllers import compute
from society_mgmt.utils import compute
# ...config, domain, middleware, models, repositories, routes, services all re-export compute
```

## Behavior (known-answer table)

`compute(x)` is a pure, deterministic function equal to `6 * x`, plus `10` when that
result is even. The following input/output pairs are verified and preserved exactly
from the original corpus:

| Input `x` | `compute(x)` |
|-----------|--------------|
| `0`       | `10`         |
| `1`       | `16`         |
| `2`       | `22`         |
| `3`       | `28`         |
| `5`       | `40`         |
| `10`      | `70`         |
| `-4`      | `-14`        |
| `2.5`     | `15.0`       |

## Running tests

The suite is a set of **parametrized known-answer tests** located under
`tests/unit/` and `tests/integration/`. After installing the `[test]` extra, run
`pytest` from the project directory:

```bash
cd society_mgmt_300k && pytest
```

Or point `pytest` at the project directory from the repository root:

```bash
pytest society_mgmt_300k
```

## Migration notes

- **Consolidated duplication.** All **33,105** byte-identical `mod_<N>_<i>(x)`
  functions collapse into a single canonical `compute(x)` in `core.py`.
- **Normalized the arithmetic.** The three-step accumulation
  `r += x*1; r += x*2; r += x*3` is folded into `6 * x`, while the parity branch
  (`+ 10` when the result is even) is **retained** to preserve float edge cases
  (for example, `compute(2.5) == 15.0`).
- **Removed dead code.** The unused `const store = []` present in every module and
  the comment-only `src/utils/filler.js` (1,999 lines) are dropped.
- **Real tests.** The assertion-less generated `.js` test files are replaced with an
  executable `pytest` suite.
- **Clean structure.** Idiomatic intra-package imports (`from society_mgmt.core import compute`)
  replace the corpus's isolation-via-duplication pattern; the nine layer namespaces
  are preserved as thin subpackages.
- **Behavior preserved.** The observable output of `compute` is unchanged across the
  documented numeric domain.

## License

This repository is **dual-licensed**:

- The repository root is licensed under **Apache-2.0** — see [`LICENSE`](LICENSE).
- The nested corpus retains its **MIT** license — see
  [`society_mgmt_300k/LICENSE/LICENSE.txt`](society_mgmt_300k/LICENSE/LICENSE.txt).

Both license files are preserved unchanged by this migration.
