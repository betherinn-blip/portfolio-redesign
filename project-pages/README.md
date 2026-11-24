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
## Build the ATX TV Festival page (BritBox)

1. In Work New, add the ATX TV Festival project page. Set its URL slug to `britbox-atx-tv-festival` (page settings, URL Slug), unless Beth picks another.
2. Paste `atx-tv-festival.html` into its one Embed block.

Photos, the three activation videos and the AI portraits are in `assets/projects/atx-tv-festival/`. The three tall videos have sound, so each has a Sound on button. Three frames are side-scrolling galleries: the box (2 photos), the line and lounge (3), and the entrance, talent and tote (3). The homepage print uses atx-home-thumb.webp (the guest in the box photo).
## Build the BritBox out of home page

1. In Work New, add the BritBox out of home project page. Set its URL slug to `britbox-out-of-home` (page settings, URL Slug), unless Beth picks another. The homepage print links there.
2. Paste `britbox-ooh.html` into its one Embed block.

Photos are in `assets/projects/britbox-ooh/`: Beth's "edits" folder of OOH picks, her LA Sherwood billboard, "Why Didn't They Ask Evans?" photos from David Vogler's portfolio (Beth OK'd), and the four squares from the South Africa mall campaign (ZA Mall Placements folder). Four frames are side-scrolling galleries: billboards, wild postings, taxis, and walls and Citi Bike docks. No videos on this page.
## Build The 99 Store page

1. In Work New, open (or add) The 99 Store project page. Its URL slug is `multichannel` (page settings, URL Slug), so the address is `/work-new/multichannel`. The homepage print already links there.
2. Paste `the-99-store.html` into its one Embed block.

Photos and videos are in `assets/projects/the-99-store/` (Beth's Meaningful Works folder). None of the videos have sound, so they all loop like GIFs: the three Instagram stories and the four holiday digital cards in the squares (the 3:4 cards sit on their own background color to fill the square). Four frames are side-scrolling galleries: train wraps, transit kiosks, light rail car cards, and app posters, Banana Day stories and the SoFi fireworks. The homepage print uses n99-home-thumb.webp (the train on the platform).
## Build the Milk Bar packaging and print page

1. In Work New, open (or add) the Milk Bar packaging and print project page. Its URL slug is `product-packaging-print`, the one the homepage print already links to.
2. Paste `milk-bar-packaging.html` into its one Embed block.

Photos are in `assets/projects/milk-bar-packaging/`, taken from Beth's live site. None of the LA pieces that weren't Beth's are used. Four frames are side-scrolling galleries: the spring catalogue, the boxes and wraps, the gift card, ad, poster and menu, and the seasonal posters. The four squares are the cookie mix tins.
