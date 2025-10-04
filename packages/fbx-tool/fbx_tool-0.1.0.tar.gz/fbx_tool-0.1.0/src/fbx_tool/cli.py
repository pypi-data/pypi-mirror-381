"""CLI tool to create PCD files from FBX models filtered by name.

Features:
 - List all model (parent) names in an FBX
 - Filter meshes by include / exclude substring patterns (case-insensitive)
 - Sample surface points and export to .pcd (Open3D format)
 - Optionally also export excluded meshes or visualize via rerun viewer
 - Count path segments and output JSON summaries
"""
from __future__ import annotations

import argparse
import json
import pathlib
from typing import List, Sequence, Dict

# Heavy / optional imports are deferred until actually needed so that --help works

def _lazy_imports():  # noqa: D401
    import numpy as np  # type: ignore
    import trimesh  # type: ignore
    import open3d as o3d  # type: ignore
    from fbxloader import FBXLoader, Mesh  # type: ignore
    import rerun as rr  # type: ignore
    return np, trimesh, o3d, FBXLoader, Mesh, rr

def sanitize_name(name: str) -> str:
    cleaned = ''.join(ch for ch in name if ord(ch) >= 32)
    return cleaned if cleaned.strip() else name

def list_model_names(loader) -> List[str]:
    models = loader.fbxtree.get("Objects", {}).get("Model", {})
    names: List[str] = []
    for v in models.values():
        try:
            raw = v["propertyList"][1]
            names.append(sanitize_name(raw))
        except Exception:
            continue
    return names

def _match(name: str, includes: Sequence[str], excludes: Sequence[str]) -> bool:
    lname = name.lower()
    if includes and not any(p.lower() in lname for p in includes):
        return False
    if excludes and any(p.lower() in lname for p in excludes):
        return False
    return True

def extract_meshes(loader, includes: Sequence[str], excludes: Sequence[str]):
    np, trimesh, _, _, Mesh, _ = _lazy_imports()
    included_meshes = []
    excluded_meshes = []
    model_meta = loader.fbxtree.get("Objects", {}).get("Model", {})
    def visit(node):
        if isinstance(node, Mesh):
            parent = node.parent
            if parent is None:
                return
            parent_id = parent.id
            meta = model_meta.get(parent_id)
            if not meta:
                return
            name = sanitize_name(meta["propertyList"][1])
            vertices = np.hstack([node.vertices, np.ones((node.vertices.shape[0], 1))]).T
            vertices = node.matrixWorld @ vertices
            vertices = vertices[:3].T
            mesh = trimesh.Trimesh(vertices=vertices, faces=node.faces, process=False)
            if _match(name, includes, excludes):
                included_meshes.append(mesh)
            else:
                excluded_meshes.append(mesh)
    loader.scene.traverse(visit)
    return included_meshes, excluded_meshes

def sample_points(meshes, count: int, radius: float):
    if not meshes:
        return None
    _, trimesh, _, _, _, _ = _lazy_imports()
    if len(meshes) == 1:
        big = meshes[0]
    else:
        big = trimesh.util.concatenate(meshes)
    sampled, _ = trimesh.sample.sample_surface_even(big, count=count, radius=radius)
    return sampled

def save_pcd(points, path: pathlib.Path):
    if points is None:
        print("[warn] No points to save for", path)
        return
    np, _, o3d, *_ = _lazy_imports()
    points = points.astype(np.float32)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    path.parent.mkdir(parents=True, exist_ok=True)
    o3d.io.write_point_cloud(str(path), pcd)
    print(f"[ok] Wrote {points.shape[0]} points -> {path}")

def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Create PCD from filtered FBX meshes")
    p.add_argument("fbx", help="Path to FBX file")
    p.add_argument("--include", "-i", action="append", default=[], help="Substring pattern to include (case-insensitive). Repeatable. If omitted, all meshes are included unless excluded.")
    p.add_argument("--exclude", "-e", action="append", default=[], help="Substring pattern to exclude (case-insensitive). Repeatable.")
    p.add_argument("--list-names", action="store_true", help="Only list model names and exit")
    p.add_argument("--count-path-segments", action="store_true", help="Count occurrences of each path segment after '/' across all model names and exit (can be combined with --list-names)")
    p.add_argument("--output", "-o", help="Output PCD filename (default: <fbx_stem>-filtered.pcd)")
    p.add_argument("--unwanted-output", help="Optional PCD path for excluded meshes")
    p.add_argument("--sample-count", type=int, default=200_000, help="Number of points to sample from included meshes (default: 200000)")
    p.add_argument("--unwanted-sample-count", type=int, default=100_000, help="Points to sample from excluded meshes if --unwanted-output is set (default: 100000)")
    p.add_argument("--radius", type=float, default=0.0, help="Sampling radius passed to trimesh.sample_surface_even (default: 0.0)")
    p.add_argument("--viewer", action="store_true", help="Open Rerun viewer and stream point clouds")
    p.add_argument("--no-viewer", action="store_true", help="Explicitly disable viewer (overrides --viewer)")
    p.add_argument("--save-unwanted", action="store_true", help="Also save excluded meshes point cloud (requires --unwanted-output or uses <fbx_stem>-excluded.pcd)")
    p.add_argument("--dry-run", action="store_true", help="Parse & report counts but do not sample or write files")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON summary to stdout")
    return p

def cli(argv: Sequence[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    fbx_path = pathlib.Path(args.fbx)
    if not fbx_path.is_file():
        parser.error(f"FBX file not found: {fbx_path}")
    np, trimesh, o3d, FBXLoader, Mesh, rr = _lazy_imports()
    loader = FBXLoader(str(fbx_path))
    names = list_model_names(loader)
    def path_segment_counts(model_names: Sequence[str]) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for full in model_names:
            if '/' not in full:
                continue
            path_part = full[full.find('/') :]
            segments = [s for s in path_part.split('/') if s]
            for s in segments:
                counts[s] = counts.get(s, 0) + 1
        return counts
    if args.list_names:
        names_sorted = sorted(set(names))
        if args.json:
            out = {"names": names_sorted}
            if args.count_path_segments:
                seg_counts = path_segment_counts(names)
                out["segment_counts"] = sorted(
                    ({"segment": k, "count": v} for k, v in seg_counts.items()),
                    key=lambda d: (-d["count"], d["segment"]),
                )
            print(json.dumps(out, indent=2))
        else:
            print("Model names ({}):".format(len(names_sorted)))
            for n in names_sorted:
                print(" -", n)
            if args.count_path_segments:
                seg_counts = path_segment_counts(names)
                if seg_counts:
                    print("\nPath segment frequencies:")
                    for seg, cnt in sorted(seg_counts.items(), key=lambda kv: (-kv[1], kv[0])):
                        print(f" {seg}: {cnt}")
                else:
                    print("\n(no '/' path segments found)")
        if args.count_path_segments:
            return 0
    elif args.count_path_segments:
        seg_counts = path_segment_counts(names)
        if args.json:
            print(json.dumps({
                "segment_counts": sorted(
                    ({"segment": k, "count": v} for k, v in seg_counts.items()),
                    key=lambda d: (-d["count"], d["segment"]),
                )
            }, indent=2))
        else:
            print("Path segment frequencies ({} unique):".format(len(seg_counts)))
            for seg, cnt in sorted(seg_counts.items(), key=lambda kv: (-kv[1], kv[0])):
                print(f" {seg}: {cnt}")
        return 0
    included_meshes, excluded_meshes = extract_meshes(loader, args.include, args.exclude)
    summary = {
        "fbx": str(fbx_path),
        "total_models": len(names),
        "include_patterns": args.include,
        "exclude_patterns": args.exclude,
        "included_mesh_count": len(included_meshes),
        "excluded_mesh_count": len(excluded_meshes),
        "sample_count": args.sample_count,
        "radius": args.radius,
    }
    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print("[info] Included meshes: {} | Excluded: {}".format(len(included_meshes), len(excluded_meshes)))
    if args.dry_run:
        return 0
    if not included_meshes:
        print("[warn] No meshes matched include/exclude criteria. Nothing to do.")
        return 1
    out_path = pathlib.Path(args.output) if args.output else fbx_path.with_name(fbx_path.stem + "-filtered.pcd")
    included_points = sample_points(included_meshes, args.sample_count, args.radius)
    save_pcd(included_points, out_path)
    excluded_points = None
    if args.save_unwanted:
        excluded_out_path = pathlib.Path(args.unwanted_output) if args.unwanted_output else fbx_path.with_name(fbx_path.stem + "-excluded.pcd")
        excluded_points = sample_points(excluded_meshes, args.unwanted_sample_count, args.radius)
        save_pcd(excluded_points, excluded_out_path)
    use_viewer = args.viewer and not args.no_viewer
    if use_viewer:
        rr.init("fbx-filter", spawn=True)
        if included_points is not None:
            rr.log("included", rr.Points3D(included_points, colors=[200, 100, 50]))
        if excluded_points is not None:
            rr.log("excluded", rr.Points3D(excluded_points, colors=[50, 100, 200]))
        print("[info] Rerun viewer opened (close window to end).")
    return 0

__all__ = ["cli", "build_arg_parser"]

if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(cli())
