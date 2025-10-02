#!/usr/bin/env python3
"""
darkbin.py - BIN info & CC extractor with interactive menu
"""

from __future__ import annotations
import re
import json
import time
import textwrap
from typing import Optional, Dict, Any, Set
import requests
import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import track

API_URL = "https://bins.antipublic.cc/bins/{}"
console = Console()

###########
# BIN Lookup
###########
def stormx_bininfo(bin_number: str) -> Dict[str, Any]:
    """Fetch BIN info from antipublic.cc API using first 6 digits."""
    bin_number = str(bin_number)[:6]
    url = API_URL.format(bin_number)
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def pretty_table(data: Dict[str, Any], title="BIN Info") -> None:
    """Display BIN info in a colored table inside a panel."""
    table = Table(show_header=True, header_style="bold cyan", expand=True)
    table.add_column("Field", style="bold yellow", no_wrap=True)
    table.add_column("Value", style="bold green")
    for k, v in data.items():
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v)
        table.add_row(str(k), str(v))
    console.print(Panel(table, title=title, border_style="bright_blue"))

###########
# CC Extraction
###########
CC_LINE_RE = re.compile(r"^(\d{13,19})\|(\d{2})\|(\d{4})\|(\d{3,4})$")

def _first_six(cc: str) -> str:
    return cc[:6]

def extract_ccs_from_file(
    input_path: str,
    output_path: str,
    bin_prefix: Optional[str] = None,
    country: Optional[str] = None,
    api_lookup: bool = True,
    verbose: bool = False
) -> Dict[str, Any]:
    """Extract CCs from a file (CC|MM|YYYY|CVV), filter by BIN/country, write output preserving format."""
    summary = {
        "input": input_path,
        "output": output_path,
        "found_candidates": 0,
        "matched": 0,
        "skipped": 0,
        "unique_written": 0,
        "errors": [],
    }

    try:
        with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        summary["errors"].append(f"Failed to read input file: {e}")
        return summary

    candidate_lines = [line for line in lines if CC_LINE_RE.match(line)]
    summary["found_candidates"] = len(candidate_lines)
    if verbose:
        console.print(f"[cyan]Found {len(candidate_lines)} valid CC lines[/cyan]")

    matched_set: Set[str] = set()
    bin_prefix = str(bin_prefix)[:6] if bin_prefix else None
    country_norm = country.lower() if country else None

    # Country API lookup
    bin_cache: Dict[str, Optional[str]] = {}
    if country_norm and api_lookup:
        unique_bins = {_first_six(line.split("|")[0]) for line in candidate_lines}
        for b in track(unique_bins, description="BIN lookup"):
            info = stormx_bininfo(b)
            bin_country = None
            if info and isinstance(info, dict):
                bin_country = (info.get("country") or info.get("country_name") or "").lower()
            bin_cache[b] = bin_country
            time.sleep(0.2)

    # Apply filters
    for line in candidate_lines:
        cc = line.split("|")[0]
        b = _first_six(cc)
        if bin_prefix and b != bin_prefix:
            summary["skipped"] += 1
            continue
        if country_norm:
            bin_country = bin_cache.get(b)
            if not bin_country or country_norm not in bin_country:
                summary["skipped"] += 1
                continue
        matched_set.add(line)

    matched_list = sorted(matched_set)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for line in matched_list:
                f.write(line + "\n")
        summary["matched"] = len(matched_list)
        summary["unique_written"] = len(matched_list)
    except Exception as e:
        summary["errors"].append(str(e))

    # Display summary table
    tbl = Table(show_header=False, box=None)
    tbl.add_column("Key", style="bold cyan")
    tbl.add_column("Value", style="white")
    for k, v in summary.items():
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v[:5]) + ("..." if len(v) > 5 else "")
        tbl.add_row(k, str(v))
    console.print(Panel(tbl, title="Extraction Summary", border_style="bright_green"))

    # Show top 10 examples
    if matched_list:
        tbl2 = Table(show_header=True, header_style="bold magenta")
        tbl2.add_column("Top 10 Matched CCs", style="bold green")
        for line in matched_list[:10]:
            tbl2.add_row(line)
        console.print(Panel(tbl2, title="Examples", border_style="bright_yellow"))

    return summary

###########
# Interactive Menu
###########
def interactive_menu():
    console.print(Panel("[bold green]BIN Info & CC Extractor Tool[/bold green]\nSelect an option:", border_style="bright_blue"))
    console.print("1. Lookup BIN info")
    console.print("2. Extract CCs from file (CC|MM|YYYY|CVV)")
    console.print("3. Help / Instructions")
    console.print("4. Exit")
    choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"], default="1")

    if choice == "1":
        bin_number = Prompt.ask("Enter BIN or card number")
        info = stormx_bininfo(bin_number)
        pretty_table(info)
    elif choice == "2":
        input_file = Prompt.ask("Enter input file path")
        output_file = Prompt.ask("Enter output file path")
        filter_bin = Prompt.ask("Filter by BIN (first 6 digits, optional)", default="")
        filter_bin = filter_bin.strip() if filter_bin else None
        filter_country = Prompt.ask("Filter by country (name/code, optional)", default="")
        filter_country = filter_country.strip() if filter_country else None
        extract_ccs_from_file(
            input_path=input_file,
            output_path=output_file,
            bin_prefix=filter_bin,
            country=filter_country,
            api_lookup=True,
            verbose=True
        )
    elif choice == "3":
        help_text = textwrap.dedent("""
            [bold cyan]BIN Info & CC Extractor - Full Usage[/bold cyan]

            [bold]1. Lookup BIN info:[/bold]
               - CLI: python3 darkbin.py -b <BIN|CardNumber>
                 --json  : optional, show raw JSON
               - Interactive menu: select 1, enter BIN or card number
               - Displays pretty table with BIN, brand, bank, country, type, level, currency

            [bold]2. Extract CCs from file:[/bold]
               - Input file format: CC|MM|YYYY|CVV (one per line)
               - CLI:
                 python3 darkbin.py -i input.txt -o output.txt [--filter-bin 512356] [--filter-country KZ]
                 --no-api : skip country filtering API calls
               - Interactive menu: select 2, follow prompts
               - Output preserves original format, filters by BIN/country if specified
               - Shows summary and top 10 matched CCs

            [bold]3. Import and use programmatically:[/bold]
               from darkbin import stormx_bininfo, extract_ccs_from_file, pretty_table

               # Lookup BIN
               info = stormx_bininfo("512356")
               print(info)
               pretty_table(info)

               # Extract CCs from file
               summary = extract_ccs_from_file(
                   input_path="dump.txt",
                   output_path="matched.txt",
                   bin_prefix="512356",    # optional
                   country="KZ",           # optional
                   api_lookup=True,
                   verbose=True
               )
               print(summary)

            [bold]4. Exit[/bold]: Exit the tool
        """)
        console.print(Panel(help_text, title="Help / Instructions", border_style="bright_magenta"))
    elif choice == "4":
        console.print("[bold red]Exiting...[/bold red]")
        return
    interactive_menu()

###########
# CLI / Entry Point
###########
def main():
    parser = argparse.ArgumentParser(description="BIN info & CC extractor")
    parser.add_argument("-b", "--bin", help="BIN number or card number (first 6 digits)")
    parser.add_argument("--json", action="store_true", help="Show raw JSON instead of table")
    parser.add_argument("--extract-file", "-i", help="Input file to scan for CCs")
    parser.add_argument("--out", "-o", help="Output file for matched CCs")
    parser.add_argument("--filter-bin", help="Filter CCs by BIN prefix")
    parser.add_argument("--filter-country", help="Filter CCs by country (name or 2-letter code)")
    parser.add_argument("--no-api", action="store_true", help="Do not perform API lookup for country")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output during extraction")

    args = parser.parse_args()

    if args.bin:
        info = stormx_bininfo(args.bin)
        if args.json:
            console.print_json(json.dumps(info, ensure_ascii=False))
        else:
            pretty_table(info)
        return

    if args.extract_file:
        if not args.out:
            console.print("[red]Error: --out required when using --extract-file[/red]")
            return
        extract_ccs_from_file(
            input_path=args.extract_file,
            output_path=args.out,
            bin_prefix=args.filter_bin,
            country=args.filter_country,
            api_lookup=not args.no_api,
            verbose=args.verbose
        )
        return

    # No CLI args → interactive menu
    interactive_menu()

if __name__ == "__main__":
    main()
