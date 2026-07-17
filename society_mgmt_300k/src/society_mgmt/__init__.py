"""society_mgmt: an idiomatic Python package migrated in place from a large,
synthetic JavaScript corpus.

The original corpus contained thousands of byte-identical ``mod_<N>_<i>(x)``
functions spread across nine layered namespaces. All of that duplicated logic
is consolidated here into a single canonical, pure function, :func:`compute`.
The nine original namespaces (``config``, ``controllers``, ``domain``,
``middleware``, ``models``, ``repositories``, ``routes``, ``services`` and
``utils``) are preserved as thin subpackages that each re-export ``compute``.

The package has no user interface, no endpoints and no I/O; it is a pure,
deterministic arithmetic library with no third-party runtime dependencies.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
