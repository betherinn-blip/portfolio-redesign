# Project pages

Each project page is one Embed block holding a project card. The napkin and guest check come from `check-menu-sitewide.html` (Code Injection, Footer) and the gingham from `tablecloth-background.css` (Custom CSS). Those stay still. Only the card scrolls, sliding up under the napkin.

On a desktop (1200px and wider) the card keeps the Figma frame 38:2 layout. It starts at x 760, y 328 of the 1440 x 1024 frame, so the napkin covers less than 10% of it, and it scales to fit the space to the right (up to its Figma size of 898). Under 1200px the same card stacks in reading order. Under 860px it goes full width and the menu becomes the Menu button.

## Build the See It Differently page

### Before you start (one time)

1. Paste `check-menu-sitewide.html` into Code Injection, Footer. To find it, open the Pages panel and scroll to the bottom to Custom Code, then Code Injection. The menu image links are already in its CONFIG.
2. Paste `tablecloth-background.css` into Design, Custom CSS.

### Photos and videos

You do not upload these to Squarespace. They live in this repo under `assets/projects/<project>/` and load from the repo's GitHub Pages site (`https://betherinn-blip.github.io/portfolio-redesign/`). The `media` line in CONFIG points at the project's folder, and each photo or video line is just a file name. Claude adds the files and fills in CONFIG.

### Make the page

1. Open your Work New portfolio page.
2. Open the See It Differently project, or add one with the URL slug `britbox-brand-campaign`.
3. Delete any blocks inside it.
4. Add one Embed block and choose Code Snippet.
5. Open `see-it-differently.html` on GitHub, click Copy raw file, and paste it into the snippet.
6. Save, then view the page outside the editor.

### Check it

1. Scroll. Only the card moves.
2. Click X close. It returns to the menu.
3. Open the page on your phone. The card stacks and the Menu button opens the check.

## Notes

- Inside the Squarespace editor the card shows inside its block so you can still click it. The real layout shows on the live page.
- If Squarespace refuses the film file as too big, upload it to Vimeo or YouTube and paste that link instead. Both work.
- Fonts: the title, labels and Play use SignPainter, and the body uses TT Interphases. Before launch, check the licenses: SignPainter came with macOS, which does not allow use on a website, and TT Interphases is a trial. Swap the file links in CONFIG once you have licensed files.
- Words are in the HTML. Edit them where you read them.
## Build the Visual Identity Refresh page

Same steps as See It Differently, with these changes:

1. In Work New, open (or add) the Visual Identity Refresh project with the URL slug `britbox-visual-identity`. That is the link the homepage print already uses.
2. Paste `visual-identity-refresh.html` into its one Embed block.

Its photos and videos are in `assets/projects/visual-identity-refresh/`. None of its videos have sound, so they all loop like GIFs with no Sound on button.

## Side-scrolling galleries

The two photo frames above the four squares can each hold several photos. Visitors swipe, scroll sideways or use the arrows, and a counter shows which photo is showing (for example 2 / 5). The frame keeps its size, so the layout does not change. Claude sets these up: inside the frame, the photos sit in a `<div class="sid-track">`, and each one has a name in CONFIG. A frame with one photo shows no arrows.
## Build the NYC Flagship page (Milk Bar)

Same steps as the other project pages:

1. In Work New, open (or add) the NYC Flagship project. The homepage print links to `/work-new/retail-environmental-design` for now. If you choose a different slug, Claude updates the homepage link.
2. Paste `nyc-flagship.html` into its one Embed block.

Photos and the cake display video are in `assets/projects/nyc-flagship/`. The three frames under the credits are side-scrolling galleries: counters, the ballroom and the neon signs.
## Build the All You Can Treat Tour page (Milk Bar)

1. In Work New, open (or add) the All You Can Treat Tour project page. Set its URL slug to `milkbar-treat-tour` (page settings, URL Slug), so the address is `/work-new/milkbar-treat-tour`. The homepage print already links there.
2. Paste `all-you-can-treat-tour.html` into its one Embed block.

Photos and the tour email loop are in `assets/projects/all-you-can-treat-tour/`. Two frames are side-scrolling galleries: the truck and trike, and the ship-a-treat station and merch tent.
