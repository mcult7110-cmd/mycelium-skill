# Mycelium Connector

This is a GitHub skill scaffold for a personal knowledge connector that links ideas across Obsidian, Notion, and the wider web.

## Purpose

The Mycelium Connector is designed to help when your brain feels stuck or overloaded. It behaves like a cross-pollinating thought engine.

Instead of asking only one narrow question, it searches broadly for:

- literal matches
- metaphorical echoes
- weird but meaningful connections

## Trigger ideas

Use this skill when the user says things like:

- "I feel stuck"
- "I keep circling this thought"
- "Find the hidden connection"
- "What is this feeling really about?"
- "Search the whole network for this concept"

## Core protocol

The skill follows a simple loop:

1. Identify the noise word or feeling
2. Search all available sources
3. Return 3 threads:
   - The Literal
   - The Metaphorical
   - The Wild
4. Push the concept in a new direction instead of stopping at the first answer

## Obsidian integration

This skill should read from a local Obsidian vault and search notes by keyword, concept, and backlink structure.

See `skill/obsidian.md` for more details.

## Notion integration

The skill should also be able to query Notion pages or databases to look for related concepts, tags, and linked notes.

See `skill/notion.md` for more details.

## Environment values

Copy `.env.example` to `.env` and fill in your keys and local paths.

## Minimal config example

- `OBSIDIAN_VAULT_PATH`
- `NOTION_API_KEY`
- `NOTION_DATABASE_ID`
- `WEB_SEARCH_ENABLED`

## Important note

This file is intentionally simple and beginner-friendly. It is meant to be the human-readable anchor for your skill while you build out the technical plumbing later.
