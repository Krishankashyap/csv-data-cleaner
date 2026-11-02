# CSV Data Cleaner

A small Python tool (standard library only) to clean a CSV file.

## What it does
- Trims leading/trailing spaces from every cell.
- Drops fully empty rows.
- Removes exact duplicate rows, keeping the first occurrence and the original order.
- Keeps the header row as-is.

## How to run
```bash
python clean_csv.py sample.csv cleaned.csv
```

The input file is never modified; a new cleaned file is written.

## Example
`sample.csv` contains duplicate and messy rows. Running the tool on it produces a shorter, cleaner file with one copy of each row.
