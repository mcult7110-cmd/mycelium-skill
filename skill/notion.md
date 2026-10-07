# Notion wiring

This is how the skill connects to Notion.

## Why

Notion is another layer of memory. It can hold:

- research notes
- personal writing
- project concepts
- database records
- long-form thought objects

## Required config

Set these in `.env`:

```bash
NOTION_API_KEY=secret_xxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=1234567890abcdef1234567890abcdef
```

## Useful API call

The script can use the Notion search API:

```http
POST https://api.notion.com/v1/search
```

with a body like:

```json
{
  "query": "static",
  "filter": {
    "property": "object",
    "value": "page"
  }
}
```

## What to pull back

The script should return:

- page title
- page URL
- relevant properties/tags
- a snippet of the page content if available

## Best practice

Notion is not a replacement for your vault. It is a second memory web. The real power comes from combining them.

If Obsidian says one thing and Notion implies another, that tension may be the actual connection the user needs.

## This is a thought network

Do not treat it like a normal search system.

Treat it like a memory map shaped by weirdness, association, and hidden relevance.
