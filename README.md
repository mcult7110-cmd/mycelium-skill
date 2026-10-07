# Mycelium Connector

A simple GitHub skill scaffold for a cross-pollinating knowledge connector that links thoughts across Obsidian, Notion, and the web.

This project is meant to help your sandbox harness pull in a personal knowledge pattern that feels like:

- a note search engine
- a concept mapper
- a spinning-brain prompt system
- a way to connect weird ideas without getting lost

## What this repo contains

- `README.md` — repo overview and setup
- `skill.md` — the main skill description for your harness
- `skill/skill.yaml` — metadata for the skill
- `skill/obsidian.md` — Obsidian instructions
- `skill/notion.md` — Notion instructions
- `.env.example` — environment variables for vault and Notion access

## Core behavior

This skill is built around the Mycelium Connector pattern:

- ignore category boundaries
- search across everything
- look for surprising links
- return three threads:
  - literal
  - metaphorical
  - wild

## Quick setup

1. Copy `.env.example` to `.env`
2. Fill in your Obsidian vault path
3. Add your Notion API key and database ID
4. Keep the repository public or private depending on your harness
5. Use this repo as the source for your GitHub skill

## Example user prompt

- "I keep spiraling on fear"
- "I need a link between zero point and government coverups"
- "Find the weirdest connection between memory and energy"

Expected output style:

- The Literal: a note, fact, or page match
- The Metaphorical: an emotional or personal echo
- The Wild: a totally unexpected connection that still might matter

## Notes

This is a scaffold, not a finished production app. It is intentionally lightweight so a beginner can understand it and extend it later.

If you want, you can later turn this into:

- a local CLI tool
- a GitHub Copilot skill wrapper
- a Python script that reads notes and queries Notion
- a webhook-based bridge between your vault and a database
