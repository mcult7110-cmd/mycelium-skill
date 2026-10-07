# Mycelium Connector

This is the full feral knowledge-connector skill for your personal sandbox.

The Mycelium Connector does not believe in clean categories. It searches everything and follows the weirdest meaningful link.

It is built to:

- scan an Obsidian vault
- query Notion pages/databases
- search for literal, metaphorical, and wild connections
- return an anchor when the brain is spinning
- keep the chaotic, cross-pollinating energy of the original persona

## What is in this repo

- `README.md` — human-facing overview
- `skill.md` — the actual persona/instructions for the skill
- `skill/skill.yaml` — metadata manifest
- `skill/main.py` — local tool connector script
- `skill/obsidian.md` — Obsidian wiring notes
- `skill/notion.md` — Notion wiring notes
- `.env.example` — local config template
- `requirements.txt` — Python dependencies
- `.gitignore` — local env protection

## Core behavior

The skill follows this protocol:

1. Identify the stuck word, feeling, or concept.
2. Search hidden memory layers:
   - Obsidian notes
   - Notion pages
   - optional web search later
3. Return three threads:
   - The Literal
   - The Metaphorical
   - The Wild
4. Give the user a fresh angle or anchor instead of getting trapped in looped thinking.

## Quick start

1. Copy `.env.example` to `.env`
2. Fill in your vault path and Notion values
3. Install Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Run the connector:

```bash
python skill/main.py --prompt "static"
```

5. Or test a user feeling:

```bash
python skill/main.py --prompt "fear"
```

## What the script does

The script will:

- scan your Obsidian vault for matching notes
- query Notion for relevant pages
- synthesize a response with 3 threads
- show the most relevant anchor for the user

## This is the feral version

The system is intentionally not polite about categories.

It is allowed to say:

- this is not random, it is the hidden link
- this is not irrelevant, it is the missing connection
- this may look strange until the pattern shows up

That is the point.

## License

This is a personal sandbox skill repo. Use it as you want.
