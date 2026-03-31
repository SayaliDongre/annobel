# Changelog

All notable changes to this project will be documented in this file.

The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and uses semantic-ish versioning while still in 0.x (breaking changes may occur).

## [0.0.3] - 2025-10-09
### Added
- Automatic creation of empty label `.txt` files for images with zero detections (`write_empty_detection_files` now defaults to `True`). Ensures strict 1:1 mapping between images and label files.
- Progress log now prints whether empty label writing is ON.
- README upgrade notes and Git tag workflow.

### Changed
- Default of `write_empty_detection_files` from `False` to `True`.
- Internal CONFIG default updated accordingly.

### How to restore old behavior
Pass `write_empty_detection_files=False` to `annobel.run()`.

## [0.0.2] - 2025-10-09
### Added
- Initial packaged release under the name `annobel` (manual + automatic YOLO annotation, Tkinter editor, subset class filtering, autosave, console fallback).

---

## Version Retrieval
Programmatically check version:
```python
import annobel
print(annobel.__version__)
```

## Git Tagging (Reminder)
Tag releases after committing:
```bash
git tag -a v0.0.2 -m "annobel 0.0.2"
git tag -a v0.0.3 -m "annobel 0.0.3"
git push origin --tags
```
