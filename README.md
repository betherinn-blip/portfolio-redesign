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
| `about-me.html` | About and contact card (photo, bio, resume, LinkedIn and Email me buttons). Moves the page's Squarespace Form block into the card | Embed block on /about-new, plus a Form block on the same page |
| `assets/about/` | About page photo | Loads from GitHub Pages, no upload needed |
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

## About page

1. In the Pages panel, find your current Connect page. Click the three dots next to it, then Duplicate. This copies your contact form, with its email settings.
2. Open the copy's settings. Name it About New, set the URL slug to `about-new`, and move it under Not Linked.
3. On the copy, delete every block except the Form block.
4. Add one Embed block (Code Snippet) above the form. Paste `about-me.html` into it. Save.
5. View the page outside the editor. The form now sits inside the card, under "Pull up a chair". Send yourself a test message.

## Contact email

All site email goes to **hello@betherinnewman.com**. It is free Squarespace domain email forwarding (Domains panel, Email Forwarding) into Beth's portfolio Gmail, and Gmail sends replies as hello@ too. The EMAIL line on the guest check and the Email me button on the About page open a new email to hello@ with the subject "Project inquiry". Do not put the Gmail address in this repo; it is public.

Launch day: in `about-me.html` set `homePath` to "/", and in the menu links change "/about-new" to "/about".
