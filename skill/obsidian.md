# Obsidian setup

This skill can be connected to an Obsidian vault in a few simple ways.

## Goal

The idea is to search your vault for:

- keywords
- concept clusters
- linked notes and backlinks
- related markdown files

## Recommended design

Use a local vault path like this example:

```bash
/Users/yourname/Library/Mobile Documents/iCloud~md~obsidian/Documents/YourVault
```

Or a path like:

```bash
C:/Users/YourName/Documents/ObsidianVault
```

## What to search for

When a user says a feeling or concept, this skill can:

- search note titles
- search file content
- scan headings and frontmatter
- look for backlinks or related notes
- find nearby words or semantic neighbors

## Example note style

This helps the connector work better if your notes use consistent tags or metadata, for example:

```yaml
---
title: Fear
category: emotion
aliases:
  - anxiety
  - dread
  - static
---
```

## Best practice

Keep the vault organized enough that these searches make sense, even if the structure is messy.

You do not need perfect organization. The point is to make: idea -> note -> connection possible.

## Example use

If the user says "static", the skill can search for:

- static
- noise
- interference
- signal
- pressure
- frequency

Then it can connect the literal and metaphorical meanings.
