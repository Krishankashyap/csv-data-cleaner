#!/usr/bin/env python3
"""Clean a CSV file: trim whitespace, drop empty rows, remove exact duplicate rows.

Usage:
    python clean_csv.py input.csv output.csv

Only the Python standard library is used. The input file is never modified;
a new cleaned file is written to the output path.
"""
import argparse
import csv
import sys


def clean_rows(rows):
    """Return cleaned rows: trimmed, non-empty, de-duplicated (order kept)."""
    seen = set()
    cleaned = []
    for row in rows:
        trimmed = [cell.strip() if isinstance(cell, str) else cell for cell in row]
        if not any(trimmed):
            continue  # drop fully empty rows
        key = tuple(trimmed)
        if key in seen:
            continue  # drop exact duplicate rows
        seen.add(key)
        cleaned.append(trimmed)
    return cleaned


def main(argv=None):
    parser = argparse.ArgumentParser(description="Clean a CSV file.")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file to write")
    args = parser.parse_args(argv)

    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("Input file is empty.", file=sys.stderr)
        return 1

    header, data = rows[0], rows[1:]
    cleaned = clean_rows(data)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(cleaned)

    print(f"Read {len(data)} data rows, wrote {len(cleaned)} cleaned rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
