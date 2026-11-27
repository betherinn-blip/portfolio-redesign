# Portfolio redesign handoff (as of Nov 21 2026)

## Who and what
- Beth Erin Newman ("BEN"), Art Director, NYC. Site: betherinnewman.com (Squarespace 7.1).
- Goal: rebuild the portfolio's visual design on Squarespace. Image-led pages, short copy, breadth of work.
- Beth builds it herself. Claude writes code, copy, previews and steps.

## Standing rules
- No em dashes in anything published.
- File and folder names: no commas, no extra spaces, use hyphens.
- Steps and guides: short numbered steps, one action each, plain language.
- Budget: free, $50 max.

## Squarespace setup
- Grandfathered Personal plan (about $138/yr). Keep it. A new site would cost more.
- Works on this plan: Custom CSS, Custom Files uploads, Code Injection (site-wide and per page), Embed block (Code Snippet) runs JavaScript.
- Does not work: JavaScript in the plain Code block. SVG uploads (use WebP or PNG).
- Squarespace turns blank lines in pasted code into hidden spaces that break CSS. Pasted code has no blank lines.
- Build method: hidden Not Linked pages, then swap on launch day.
  - Home New: /home-new (Embed block with home-guest-check.html)
  - Work New: Portfolio page at /work-new. Project sub-pages get their own slugs (See It Differently is /work-new/britbox-brand-campaign)
  - About New: /about-new
- Fix still open: live homepage "View Work" button links to /work-1 (404). Change to /work.

## Design direction
- Concept: diner table. A guest check is the menu, a napkin is the logo and header, and project photos sit like prints on a gingham tablecloth. Inspired by nicomorris.com (Readymag).
- Other references: ckb-consulting.squarespace.com (closest Squarespace model), uncle nats, other-nomads.com (color and light), vacation.inc, lilifrech.xyz, yennmadeit, savannahmcanally, anniehongcreative, filmon.design, lisasaysgah.
- Palette: muted, off black and white, one electric highlight. Hover blue #0001AD. Red marker for NOW AVAILABLE!!
- Type: Rock Salt (handwriting on check), Permanent Marker (NOW AVAILABLE!!), Rubik ExtraBold (name), TT Interphases (napkin address and tagline). TT Interphases is a trial; it currently loads from an unlicensed free host. Buy a TypeType web license (Regular and Bold) or swap to Inter Tight or Figtree before launch.
- Napkin copy reads like a restaurant: BEN'S logo, BETH ERIN NEWMAN, ART DIRECTOR · NEW YORK, N.Y., tagline "Serving brand, campaign & experiential design for culture-driven brands, from identity systems to live events." Text tilted 7.41° to match the logo.
- Figma file: "portfolio-redesign-sandbox" (Desktop 1440x1024, iPhone 402x874). Free Starter plan hits read limits, so export SVG (outline text off) plus PNG instead.

## Homepage (nearly done)
- Left: napkin and check fixed. Right two thirds: draggable prints (option B: can slide under the menu, never off screen, drag to the top edge).
- Check lines are live text over clean images (ben-menu-desktop and ben-menu-phone). Edit words in the CONFIG `hand:` list.
- 6 categories on the check, diner names with codes (Brand Identity, Campaigns, Experiential and Events, Retail and Spatial, Packaging and Print, CRM and Digital).
- Hover a check line: line turns #0001AD with drawn underline. Matching prints straighten, go to color, come to front, get a random sticker. Others stay gray and tilted (no fading). Click locks it, second click clears (also how phones work).
- Hover a print: one random sticker on its top left or right corner, and its category line lights up.
- Stickers: Beth's 10 designs (Sticker_1 to Sticker_10, WebP). 100 to 150px wide, random tilt up to 20°, never two the same at once, softened pop (0.45s).
- Cards fit above the fold, overlapping pile; new projects land on top. Cards 10% smaller. Phone: two tight columns.
- ME, EMAIL, check mark, RESUME: blue tilted ovals on hover. EMAIL opens a new email to hello@betherinnewman.com (subject "Project inquiry"). NOW AVAILABLE!!: red oval, links to Contact. RESUME on the TAX line opens the PDF.
- Background: gingham tablecloth, fixed via body::before in Custom CSS (iPhone-safe). Base color #A3AB72.

## Code files (project files: Job-Hunter/Portfolio/site-code/)
- home-guest-check.html: homepage Embed snippet. Paste image and sticker links into CONFIG.
- check-menu-sitewide.html: Code Injection > Footer. Draws the same napkin and check on /work-new and /about-new pages; current project underlined; napkin links home; Menu button on phones.
- tablecloth-background.css: Custom CSS background rule.
- Images: ben-menu-desktop.webp, ben-menu-phone.webp, stickers/, gingham files.

## Project pages plan (one page at a time)
- Format (modeled on Nico Morris): 120 to 200 words. Label lines, short intro, 3 to 5 "what I made" lines, images, credits footer.
- Order: BritBox pages first.
  1. See It Differently (drafted, waiting for Beth's notes; becomes the template)
  2. BritBox Campaigns (other OOH and multi-channel) NEW
  3. ATX TV Festival (experiential) NEW
  4. Visual Identity Refresh (BritBox)
  5. Taking Back Your Sunday (Taskrabbit, CRM)
  6. The Bureau of Commitment (Vaseline, experiential)
  7. The 99 Store (rebuild around Meaningful Works OOH)
  8. Milk Bar Stores (NYC flagship first, plus Boston, Logan Circle DC)
  9. Milk Bar CRM and Digital NEW (includes 3 holiday and Valentine's social videos)
  10. Milk Bar Packaging and Print (was Campaigns and Packaging; check years, CPG may be 2022 to 2023)
  11. All You Can Treat Tour (Milk Bar)
  - Then optional Odds and Ends (Common Thread Closet, Power Plus Wellness), About and Contact merged, launch day.
- Milk Bar facts Beth confirmed: first project was baking mix packaging; hired for packaging and store marketing, role grew. Worked on Boston and Logan Circle campaigns, all store and marketing print, NYC flagship. Not hers: LA mural, LA cake wall, LA classroom mixer, ice cream pints.
- Reference images (project files): Portfolio/CKB-reference/ and Portfolio/Ursula-reference/ (Ursula Viglietta was her Milk Bar creative director). Excluded images are in _not-using folders.

## Assets on Beth's Mac
- Folder: Documents/Freelance Work/PORTFOLIO SITE ASSETS/***Website redesign (save new images here when Beth says "save").
- Saved project folders: Visual Identity Refresh, All You Can Treat Tour, NYC Flagship, See It Differently.
- Not yet saved (74 files ready in project files, waiting for the Mac to reconnect): The Bureau of Commitment, Campaigns and Packaging, Taking Back Your Sunday, The 99 Store.
- The 31 MB See It Differently film was too big to send; use Beth's original.

## Links
- Live preview of homepage: https://claude.ai/artifact/QZphMLs9duexz3FdLHqEwm
- Project page menu preview: https://claude.ai/artifact/SkhhTwjHRQLrYEB7stUj16
- Simple rebuild plan (pages): https://claude.ai/artifact/LSpw5ksE4KsggVDF6qp4N5
- Build guide: https://claude.ai/artifact/MazjZnUrzSbr2iDuQUQMnH
- Inspiration analysis: https://claude.ai/artifact/KCnfrRDDKrbiWiHK4fNk2k
- Resource guide: https://claude.ai/artifact/PpNW12SEXRVqiSWKMj3vah
- Site copy updates: Job-Hunter/Portfolio/site-copy/

## Next steps
1. Beth reviews the See It Differently draft to lock the page template.
2. Finish saving the remaining 4 asset folders to the Mac.
3. Paste check-menu-sitewide.html into Code Injection and create Work New and About New.
4. Build pages one at a time, in the order above.
5. Sort the TT Interphases license before launch.
