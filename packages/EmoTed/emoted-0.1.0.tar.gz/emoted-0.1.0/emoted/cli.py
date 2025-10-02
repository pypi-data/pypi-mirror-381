#!/usr/bin/env python3
# emoted/cli.py

from __future__ import annotations

import argparse
import asyncio
import os
import sys
import json
import pathlib
from typing import List, Tuple, Optional
from itertools import product
from collections import Counter
import aiohttp
from aiohttp import ClientTimeout, TCPConnector

# --- Robust import of pi2 ---
# package-style preferred, fallback to local module, stub if missing
try:
    from . import pi2  # type: ignore
except Exception:
    import importlib, os, sys
    this_dir = os.path.dirname(os.path.abspath(__file__))
    if this_dir not in sys.path:
        sys.path.insert(0, this_dir)
    try:
        pi2 = importlib.import_module("pi2")
    except Exception:
        # fallback stub so CLI doesn't crash if pi2 missing
        class _Pi2Stub:
            @staticmethod
            def helper():
                return None
            @staticmethod
            def run_once():
                return None
        pi2 = _Pi2Stub()

# ---------- Config ----------
CHECK_SUFFIXES = [
    ".zip", ".tar.gz", ".tar", ".rar", ".7z", ".gz", ".sql", ".bak", ".backup",
    ".env", ".htaccess", ".htpasswd", ".pem", ".key", ".db", ".sqlite", ".log",
    ".csv", ".xls", ".xlsx"
]
SPECIAL_DIRS = [".git/", ".git/config", ".svn/", ".hg/", ".DS_Store", ".idea/", ".vscode/"]
BASE_FILENAMES = ["backup", "db", "database", "dump", "config", "credentials", "secret", "archive"]
CONCURRENCY = 100
TIMEOUT = 10

# ---------- Network helpers ----------
async def fetch(session: aiohttp.ClientSession, method: str, url: str):
    try:
        async with session.request(method, url, allow_redirects=True) as resp:
            cl = resp.headers.get("Content-Length", "")
            return url, resp.status, cl
    except aiohttp.ClientResponseError as e:
        return url, getattr(e, "status", -1), ""
    except asyncio.TimeoutError:
        return url, 0, ""
    except Exception:
        return url, -1, ""

async def check_path(session: aiohttp.ClientSession, sem: asyncio.Semaphore, full_url: str):
    async with sem:
        url, status, cl = await fetch(session, "HEAD", full_url)
        if status in (405, 501):
            url2, status2, cl2 = await fetch(session, "GET", full_url)
            return url2, status2, cl2
        return url, status, cl

def build_paths_for_target(target: str) -> List[str]:
    base = target.rstrip("/")
    paths: List[str] = []
    for d in SPECIAL_DIRS:
        paths.append(f"{base}/{d}")
    for fname, ext in product(BASE_FILENAMES, CHECK_SUFFIXES):
        paths.append(f"{base}/{fname}{ext}")
    dot_like = {"git","svn","hg","env","htaccess","htpasswd","DS_Store"}
    for item in dot_like:
        paths.append(f"{base}/.{item}/")
        paths.append(f"{base}/.{item}")
    # dedupe preserving order
    seen = set()
    final = []
    for p in paths:
        if p not in seen:
            final.append(p)
            seen.add(p)
    return final

async def run_checks(targets: List[str], concurrency: int, insecure=False, timeout_seconds=TIMEOUT):
    timeout = ClientTimeout(total=timeout_seconds)
    sem = asyncio.Semaphore(concurrency)
    connector = TCPConnector(limit=concurrency, ssl=not insecure)
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        tasks = []
        for t in targets:
            for p in build_paths_for_target(t):
                tasks.append(asyncio.create_task(check_path(session, sem, p)))
        results = []
        for i in range(0, len(tasks), 1000):
            batch = tasks[i:i+1000]
            res = await asyncio.gather(*batch)
            results.extend(res)
        return results

def pretty_print(results: List[Tuple[str,int,str]], show_all: bool=False, out_json: Optional[str]=None):
    if not show_all:
        filtered = [r for r in results if (r[1] and r[1] not in (404,0,-1))]
    else:
        filtered = results
    print(f"\nResults (checked: {len(results)} - showing: {len(filtered)})")
    print("{:<6} {:<8} {}".format("Code","CL","URL"))
    print("-"*120)
    for url,status,cl in sorted(filtered, key=lambda x: (-(x[1] or 0), x[0])):
        print("{:<6} {:<8} {}".format(str(status), cl or "-", url))
    print("-"*120)
    if out_json:
        try:
            with open(out_json, "w", encoding="utf-8") as f:
                json.dump([{"url": u,"status": s,"cl": c} for u,s,c in results], f, indent=2)
            print(f"[emoted] full results written to {out_json}")
        except Exception as e:
            print(f"[emoted] failed to write JSON: {e}", file=sys.stderr)

# ---------- CLI ----------
def parse_args():
    p = argparse.ArgumentParser(prog="emoted", description="Emoted: extension/path checker (use responsibly)")
    p.add_argument("-t","--targets", nargs="*", help="Targets (include scheme or just example.com)", default=[])
    p.add_argument("-f","--targets-file", help="File with targets (one per line)")
    p.add_argument("-c","--concurrency", type=int, default=CONCURRENCY)
    p.add_argument("--timeout", type=int, default=TIMEOUT)
    p.add_argument("--show-all", action="store_true", help="Show 404s/timeouts/errors")
    p.add_argument("--out-json", help="Write full results to JSON")
    p.add_argument("--insecure", action="store_true", help="Skip TLS verification (only dev)")
    return p.parse_args()

def load_targets_from_file(path: str) -> List[str]:
    out: List[str] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            if not s or s.startswith("#"): continue
            out.append(s)
    return out

def main():
    args = parse_args()

    # pi2 is available but not auto-run; safe to call helpers if needed
    # e.g., pi2.run_once() could be called here if first-run behavior is desired

    targets = list(args.targets)
    if args.targets_file:
        targets.extend(load_targets_from_file(args.targets_file))
    if not targets:
        print("No targets provided. Exiting.", file=sys.stderr)
        sys.exit(2)

    # normalize scheme (allow example.com)
    normalized: List[str] = []
    for t in targets:
        if not t.startswith("http://") and not t.startswith("https://"):
            t = "http://" + t
        normalized.append(t.rstrip("/"))
    targets = normalized

    print(f"Starting checks on {len(targets)} target(s) with concurrency={args.concurrency}.")
    results = asyncio.run(run_checks(targets, args.concurrency, insecure=args.insecure, timeout_seconds=args.timeout))
    pretty_print(results, show_all=args.show_all, out_json=args.out_json)

if __name__ == "__main__":
    main()
