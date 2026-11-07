---
title: "Folder thumbnails: video mosaics and folder.jpg covers"
navTitle: "Folder thumbnails"
description: "Show video thumbnails on folder tiles in Reelio: a mosaic of the videos inside, a folder.jpg cover, or an image you drop. See which one wins and when."
lead: "Every folder tile in Reelio shows either a picture you chose or a mosaic of the videos inside it, so you can tell folders apart at a glance."
level: beginner
verified: "1.3.0.0"
related: [video-covers, vertical-videos, hover-scrub]
---

## What a folder tile shows

Reelio picks the picture of a folder tile in this order:

1. An image you dropped on the folder (a custom cover).
2. An image named `folder` inside the folder, such as `folder.jpg`.
3. A mosaic of the videos in the folder.

## The video mosaic

Without a cover, a folder tile shows a grid of 2 by 2 slots. A landscape video fills a whole slot, and two portrait videos share one slot side by side, so a mosaic shows up to 8 videos. Slots with nothing to show stay empty.

The videos come from the whole folder, including all its subfolders, not only the videos sitting directly inside it.

Each cell shows the video's same-name image if it has one (see [Video covers](/docs/video-covers/)), otherwise its generated thumbnail. A video still waiting for its thumbnail shows a placeholder, and a video whose thumbnail failed leaves its cell empty.

### Random or alphabetical

Choose which videos fill the mosaic in Settings > **Display** > **Folder tile content**:

- **Random** (the default): a new random pick each time the page loads.
- **Alphabetically first**: the first videos by their path inside the folder, ignoring case. This is plain text order, so `clip10` comes before `clip2`, and a video in a subfolder named `A` comes before a file named `B`.

### Play a video straight from the mosaic

{{< tip >}}
Hold **Alt** and click a cell of the mosaic to play that video in your video player, without opening the folder. Holding Alt while you move over the mosaic highlights the cell that Alt+click would play. A plain click anywhere on the tile still opens the folder.
{{< /tip >}}

Only cells that show a picture react to Alt+click. On an empty or loading cell, or on a folder with a cover, Alt+click opens the folder. Alt is read when the pointer enters a cell, so if you press it with the mouse still, move to another cell to see the highlight.

The mosaic appears in the **Extra large**, **Large** and **Medium** views. In the **Details** view, a folder row shows its cover as a small thumbnail (a dropped cover or `folder.*`), or a folder icon, never a mosaic.

## Use folder.jpg as a cover

Put an image named `folder` directly inside the folder, with the extension .jpg, .jpeg, .png or .webp. It replaces the mosaic: the tile shows only that image.

- If several exist, the first one wins in this order: `folder.jpg`, `folder.jpeg`, `folder.png`, `folder.webp`.
- Use lowercase names. Other casings, such as `Folder.JPG`, work on standard Windows drives, but a NAS share may need the exact lowercase name.
- A portrait image (taller than wide) gives the folder a narrow vertical tile, half a cell wide, which can share its cell with another vertical tile. A square image counts as landscape. See [Vertical videos](/docs/vertical-videos/).

{{< tip >}}
Reelio looks for `folder.*` during a library scan, not live. After you add, rename or remove one, click **Update thumbnails** in the toolbar to see the change.
{{< /tip >}}

{{< note >}}
A folder only appears in Reelio if it contains at least one indexed video somewhere below it. A folder with only a `folder.jpg` and no videos is not shown.
{{< /note >}}

## Drop an image on a folder

You can also drag an image file from File Explorer and drop it on a folder tile, or on its row in the **Details** view. It works exactly like a [video cover](/docs/video-covers/), with the same formats and messages, and it wins over `folder.*`.

To remove it, right-click the folder and choose **Reset thumbnail**. The folder then shows its `folder.*` image if it has one, otherwise its mosaic.

## Related shortcuts

{{< keys >}}
Alt+Click | Play the video under the pointer in a folder mosaic
Alt+Hover | Highlight the mosaic cell that Alt+click would play
{{< /keys >}}
