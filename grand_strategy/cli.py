from __future__ import annotations

import argparse

from .map_loader import list_neighbors, load_provinces


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Python Grand Strategy prototype")
    parser.add_argument(
        "--data",
        default=None,
        help="Path to province data JSON (defaults to data/provinces.json)",
    )
    parser.add_argument(
        "--province",
        default=None,
        help="Show neighbors for a specific province",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    state = load_provinces(args.data) if args.data else load_provinces()

    if args.province:
        neighbors = list(list_neighbors(state, args.province))
        if not neighbors:
            print(f"Province '{args.province}' not found or has no neighbors.")
            return
        print(f"Neighbors of {args.province}:")
        for neighbor in neighbors:
            print(f"- {neighbor}")
        return

    print("Loaded provinces:")
    for line in state.province_summary():
        print(f"- {line}")


if __name__ == "__main__":
    main()
