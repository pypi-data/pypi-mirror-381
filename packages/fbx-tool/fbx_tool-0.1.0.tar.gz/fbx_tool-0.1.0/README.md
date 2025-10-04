# fbx-tool

Filter FBX meshes by name patterns and export sampled point clouds (PCD) using Open3D.

## Features
- Include / exclude substring filters (case-insensitive)
- Sample mesh surfaces to generate point clouds
- Optional export of excluded mesh points
- Path segment frequency analysis of model names
- JSON summary output and dry-run mode
- Rerun viewer streaming of sampled points

## Installation
From source:
```bash
pip install .
```
Or (editable dev install):
```bash
pip install -e .[dev]
```

## CLI Usage
```bash
fbx-pcd --help
```
Example:
```bash
fbx-pcd model.fbx -i ESTRUTURAS -i CIVIL -o estruturas.pcd --viewer
```
List names and segment counts:
```bash
fbx-pcd model.fbx --list-names --count-path-segments
```
JSON output:
```bash
fbx-pcd model.fbx --list-names --count-path-segments --json > names.json
```

## Programmatic Use
```python
from fbx_tool import cli
cli(["model.fbx", "-i", "CIVIL"])  # returns exit code
```

## License
MIT
