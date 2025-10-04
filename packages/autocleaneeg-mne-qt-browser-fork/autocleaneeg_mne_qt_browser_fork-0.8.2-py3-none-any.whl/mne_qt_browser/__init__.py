# License: BSD-3-Clause
# Copyright the MNE Qt Browser contributors.

try:
    from importlib.metadata import version, PackageNotFoundError

    __version__ = "0.0.0"
    # Try our forked distribution name first, then fall back to upstream name
    for _dist in (
        "autocleaneeg-mne-qt-browser-fork",
        "mne-qt-browser",
    ):
        try:
            __version__ = version(_dist)
            break
        except PackageNotFoundError:
            continue
except Exception:
    __version__ = "0.0.0"

# Keep references to all created brower instances to prevent them from being
# garbage-collected prematurely
_browser_instances = list()
