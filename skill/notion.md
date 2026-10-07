# Notion setup

This skill can also read from a Notion workspace and bring in notes, databases, or pages as additional knowledge sources.

## Goal

Use Notion to search for pages or databases that relate to the user's current concept.

Examples:

- a database of research notes
- a page with personal memories
- a collection of ideas or tags
- a writing archive

## Required values

You will usually need:

- `NOTION_API_KEY`
- `NOTION_DATABASE_ID`

## How to get the API key

1. Open Notion
2. Go to Settings and Members
3. Choose Integrations
4. Create a new integration
5. Copy the internal integration secret
6. Add it to your `.env` file

## How to get a database ID

A database ID is usually the long block of characters in a Notion database URL.

Example URL:

```text
https://www.notion.so/yourworkspace/1234567890abcdef1234567890abcdef?v=...
```

The `1234567890abcdef1234567890abcdef` part is the database ID.

## Example `.env` settings

```bash
NOTION_API_KEY=secret_xxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=1234567890abcdef1234567890abcdef
```

## Best practice

Use Notion as another layer of memory, not the only source. The real power comes when you merge:

- Obsidian notes
- Notion pages
- external web search
- user intuition

## Example use

If the user says "energy", the skill can look for pages with tags like:

- energy
- frequency
- vibration
- power
- memory
- system

Then it can compare those with notes in Obsidian and return connections that are not obvious at first glance.
