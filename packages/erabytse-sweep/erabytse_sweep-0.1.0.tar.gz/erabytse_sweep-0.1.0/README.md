# 🧹 erabytse-sweep  
*A ritualistic tool to recycle digital clutter with intention.*

> "Before you delete, ask: does this deserve to be remembered differently?"

## 🌿 Philosophy
- We do not erase. We **recontextualize**.  
- We do not automate blindly. We **invite intention**.  
- Every sweep is a **ritual of care**, not a purge.

## ✨ Features (v0.1)
- Finds files untouched for >90 days  
- Shows size, date, and examples  
- Creates a **human-readable journal** (`.erabytse_journal.json`)  
- **100% offline, no tracking, no AI**  
- Pure Python — no external dependencies

## 🚀 Quick Start

### Install (development mode)

git clone https://github.com/takouzlo/erabytse-sweep.git
cd erabytse-sweep
pip install -e .

Run a dry run
erabytse-sweep --path ~/Downloads --days 60 --dry-run

Begin the ritual
erabytse-sweep --path ./my_old_projects --ritual
A journal file (.erabytse_journal.json) will be created in the target folder.
No file is ever deleted automatically — you decide what happens next. 

📜 License
MIT — but used with intention.

Part of erabytse — a quiet rebellion against digital waste.
Made with care, not with noise.