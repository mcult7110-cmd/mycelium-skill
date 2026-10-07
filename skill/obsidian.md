# Obsidian wiring

This is how the skill connects to your Obsidian vault.

## Why

Your notes are one of the memory layers. This skill treats them as a living knowledge web, not a folder of dead files.

## What to search

The script searches:

- file names
- file contents
- headings
- yaml frontmatter
- tag values
- backlink-like references

## What counts as a hit

A file counts as relevant if it contains the current concept or a close semantic neighbor such as:

- fear
- static
- pressure
- signal
- memory
- interference
- anomaly
- pattern
- energy

## Vault path

Set your path in `.env`:

```bash
OBSIDIAN_VAULT_PATH=/Users/yourname/Library/Mobile Documents/iCloud~md~obsidian/Documents/YourVault
```

Or on Windows:

```bash
OBSIDIAN_VAULT_PATH=C:/Users/YourName/Documents/ObsidianVault
```

## Search behavior

The connector should prefer:

- the exact words the user said
- near-neighbor words in the same cluster
- notes with strong title matches
- notes that talk about emotional, conceptual, or symbolic meaning

## Best practice

Your notes do not need to be perfect, but they should have a few recurring anchors. That makes the network stronger.

You want:

- recurring names or themes
- repeated tags
- links between pages
- a few clear concepts with messy edges

This is not a clean database. It is a living web.
