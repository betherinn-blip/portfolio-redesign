# Portfolio redesign

Code, assets and notes for the redesign of [betherinnewman.com](https://www.betherinnewman.com), built on Squarespace 7.1.

This is not a deployable app. The site lives on Squarespace. This repo holds the snippets that get pasted into Squarespace, the images that get uploaded to it, and the notes that explain how it all fits together.

Start with [docs/handoff.md](docs/handoff.md). It has the full context: design direction, Squarespace setup, what works on this plan, the page plan and next steps.

## The concept

A diner table. A guest check is the menu, a napkin is the logo and header, and project photos sit like prints on a gingham tablecloth.

## What is where

| Path | What it is | Where it goes in Squarespace |
| --- | --- | --- |
| `home-guest-check.html` | Homepage snippet (napkin, guest check, draggable prints, stickers) | Embed block on /home-new |
| `check-menu-sitewide.html` | Same napkin and check for project and About pages | Pages panel, Custom Code, Code Injection, Footer |
| `tablecloth-background.css` | Fixed gingham background | Design, Custom CSS |
| `project-pages/see-it-differently.html` | See It Differently project card (only the card scrolls). Template for the other project pages | Embed block on /work-new/britbox-brand-campaign |
| `project-pages/README.md` | Step by step Squarespace setup for a project page | Reference |
| `assets/projects/see-it-differently/` | Web-ready images for that page. Videos are in the project folder `See It Differently/web-ready` | Custom Files uploads |
| `assets/menu/` | Clean check and napkin images the live text sits on | Custom Files uploads |
| `assets/background/` | Gingham tablecloth images | Custom Files uploads |
| `stickers/` | Beth's 10 stickers. Upload the WebP files (Squarespace does not take SVG) | Custom Files uploads |
| `tools/mksitewide.py` | Rebuilds `check-menu-sitewide.html` from the homepage file so both menus match | Run locally |
| `demos/` | Early prototypes and the print list (`items.json`) | Reference only |
| `tests/` | Tiny files used to test what this Squarespace plan allows | Reference only |

## Rules for this repo

1. No em dashes in anything published.
2. File and folder names use hyphens. No commas, no extra spaces.
3. No blank lines in code that gets pasted into Squarespace. Squarespace turns them into hidden spaces that break CSS.

## Keeping the two menus in sync

1. Edit `home-guest-check.html`.
2. Run `python3 tools/mksitewide.py`.
3. Paste the new `check-menu-sitewide.html` into Code Injection, Footer.
