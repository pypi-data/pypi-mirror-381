#!/usr/bin/env python3
"""
erabytse-sweep v0.1
A ritualistic tool to recycle digital clutter with intention.

Philosophy:
- We do not delete blindly.
- We offer choices: archive, release, or donate.
- Every action is logged with care.
"""

import os
import json
import hashlib
import argparse
from datetime import datetime, timedelta
from pathlib import Path


# ────────────────────────────────
# 🌿 Core functions
# ────────────────────────────────

def human_readable_size(size_bytes):
    """Convert bytes to human-readable format."""
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {units[i]}"


def get_file_hash(filepath):
    """SHA-256 hash for duplicate detection."""
    h = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except (OSError, IOError):
        return None


def find_old_files(root_path: Path, days: int = 90):
    """Find files not modified in the last `days` days."""
    cutoff = datetime.now() - timedelta(days=days)
    old_files = []
    total_size = 0

    for item in root_path.rglob('*'):
        if item.is_file():
            try:
                mtime = datetime.fromtimestamp(item.stat().st_mtime)
                if mtime < cutoff:
                    size = item.stat().st_size
                    old_files.append((item, size, mtime))
                    total_size += size
            except (OSError, ValueError):
                continue
    return old_files, total_size


# ────────────────────────────────
# 📜 Ritual: the journal
# ────────────────────────────────

def log_ritual(journal_path: Path, action: str, details: dict):
    """Log the cleaning ritual in a human-readable journal."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "details": details
    }
    journal = []
    if journal_path.exists():
        try:
            journal = json.loads(journal_path.read_text())
        except:
            pass
    journal.append(entry)
    journal_path.write_text(json.dumps(journal, indent=2))


# ────────────────────────────────
# 🧘 Main ritual
# ────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="🧹 erabytse-sweep: recycle digital clutter with intention.",
        epilog="This is not deletion. This is care."
    )
    parser.add_argument("--path", type=Path, required=True, help="Path to sweep")
    parser.add_argument("--days", type=int, default=90, help="Files older than X days")
    parser.add_argument("--ritual", action="store_true", help="Perform the full ritual (journal + choices)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")

    args = parser.parse_args()

    print("🌿 erabytse-sweep v0.1 — a ritual of digital care")
    print(f"   Sweeping: {args.path} (files > {args.days} days old)\n")

    if not args.path.exists():
        print("❌ Path does not exist.")
        return

    old_files, total_size = find_old_files(args.path, args.days)

    if not old_files:
        print("🕊️  Nothing to sweep. Your space is already clear.")
        return

    print(f"📦 Found {len(old_files)} items ({human_readable_size(total_size)})")
    print("   Examples:")
    for item, size, mtime in old_files[:5]:
        print(f"   - {item} ({human_readable_size(size)}) — {mtime.strftime('%Y-%m-%d')}")
    if len(old_files) > 5:
        print(f"   ... and {len(old_files) - 5} more.")

    # 📜 Ritual journal
    journal_path = args.path / ".erabytse_journal.json"

    if args.ritual and not args.dry_run:
        print("\n✨ Performing the ritual...")
        # For v0.1, we only log the intention (no real action yet)
        log_ritual(journal_path, "ritual_initiated", {
            "path": str(args.path),
            "items_found": len(old_files),
            "total_size_bytes": total_size
        })
        print(f"   📖 Journal updated: {journal_path}")
        print("   💭 Next step: manual review. True care is deliberate.")
    elif args.dry_run:
        print("\n👁️  Dry run complete. No changes made.")
    else:
        print("\n💡 Use --ritual to begin the cleaning ritual.")


if __name__ == "__main__":
    main()