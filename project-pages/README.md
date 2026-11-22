# Project pages

Each project page is one Embed block holding a project card. The napkin and guest check come from `check-menu-sitewide.html` (Code Injection, Footer) and the gingham from `tablecloth-background.css` (Custom CSS). Those stay still. Only the card scrolls, sliding up under the napkin.

On a desktop (1200px and wider) the card keeps the Figma frame 38:2 layout. It starts at x 760, y 328 of the 1440 x 1024 frame, so the napkin covers less than 10% of it, and it scales to fit the space to the right (up to its Figma size of 898). Under 1200px the same card stacks in reading order. Under 860px it goes full width and the menu becomes the Menu button.

## Build the See It Differently page

### Before you start (one time)

1. Paste `check-menu-sitewide.html` into Settings, Developer Tools, Code Injection, Footer. Paste your menu image links into its CONFIG.
2. Paste `tablecloth-background.css` into Design, Custom CSS.

### Upload the images

1. Open Design, Custom CSS.
2. Click Manage Custom Files.
3. Upload every `.webp`, `.png` and `.woff2` file from `See It Differently/web-ready`. The scallops and sparkles are already built into the code, so skip the `sid-scallop`, `sid-sparkle` and `sid-arrow` files.

### Upload the videos

1. Open any page in the editor and add a Text block.
2. Type a word and highlight it.
3. Click the link icon, then File, then upload `sid-film.mp4`.
4. Copy the link it gives you (it starts with `/s/`).
5. Repeat for `sid-ooh-moynihan.mp4`, `sid-genre-spot.mp4`, `sid-cutdown-crown.mp4`, `sid-cutdown-mug.mp4` and `sid-cutdown-gloves.mp4`.
6. Delete the Text block. The files stay uploaded.

### Make the page

1. Open your Work New portfolio page.
2. Open the See It Differently project, or add one with the URL slug `brand-identity-systems`.
3. Delete any blocks inside it.
4. Add one Embed block and choose Code Snippet.
5. Paste all of `see-it-differently.html`.
6. In the CONFIG near the bottom, replace each `PASTE-LINK ...` with the link for that file.
7. Save, then view the page outside the editor.

### Check it

1. Scroll. Only the card moves.
2. Click X close. It returns to the menu.
3. Open the page on your phone. The card stacks and the Menu button opens the check.

## Notes

- Inside the Squarespace editor the card shows inside its block so you can still click it. The real layout shows on the live page.
- If Squarespace refuses the film file as too big, upload it to Vimeo or YouTube and paste that link instead. Both work.
- Fonts: the title, labels and Play use SignPainter, and the body uses TT Interphases. Before launch, check the licenses: SignPainter came with macOS, which does not allow use on a website, and TT Interphases is a trial. Swap the file links in CONFIG once you have licensed files.
- Words are in the HTML. Edit them where you read them.
