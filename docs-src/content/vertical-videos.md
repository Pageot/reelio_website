---
title: "Vertical video thumbnails on Windows, no black bars"
navTitle: "Vertical videos"
description: "Reelio gives vertical video thumbnails on Windows their own 9:16 shape with no black bars, and fits two portrait clips side by side in one grid cell."
lead: "Phone footage, Reels and other portrait clips keep a vertical thumbnail in Reelio, and two of them can share one cell of the grid."
level: beginner
verified: "1.3.0.0"
related: [video-covers, folder-thumbnails, sort-and-views]
---

## Vertical thumbnails without black bars

Reelio scales every thumbnail up until it covers the whole frame, then crops the center, so it never adds black bars around a video. The frame follows the video:

| Source | Thumbnail shape |
|---|---|
| Portrait (taller than wide) | 9:16, for example 270x480 at the default **High** quality |
| Landscape or square | 16:9 |

So a clip shot on a phone held upright gets a tall thumbnail, not a small picture in the middle of a wide black box. To change the size of thumbnails, see [Thumbnail quality and speed](/docs/quality-and-speed/).

## Two vertical videos share one cell

In the **Extra large**, **Large** and **Medium** views, a vertical tile is half a cell wide, and two vertical tiles in a row share one cell side by side.

{{< tip >}}
Pairing follows the order of the list strictly: a vertical tile followed by a horizontal one (or by nothing) leaves the other half of its cell empty. Changing the sort order changes which vertical videos end up side by side. See [Sort and views](/docs/sort-and-views/).
{{< /tip >}}

The **Details** view shows one row per item, so there is no pairing there.

## What makes a tile vertical

A tile is vertical when its picture is taller than wide. A square picture counts as landscape. The picture can come from:

- The video itself: a portrait video gets a vertical tile.
- A same-name image next to the video: its shape wins over the video's. A portrait image makes a landscape video's tile vertical, and the other way around. Hovering still shows frames of the video, cropped to fill that tile.
- A cover you dropped on the tile: its shape wins too. Reelio reads the image size right away, respecting the rotation stored by phone cameras.

{{< note >}}
After you drop a cover whose shape differs from the tile, the tile keeps its old shape until you go to another page and come back. Until then, the cover is cropped to fill the current tile. See [Video covers](/docs/video-covers/).
{{< /note >}}

## Vertical folder tiles

A folder whose cover is portrait gets a vertical tile too. Put a portrait `folder.jpg` (or .jpeg, .png, .webp) in the folder, and its tile becomes half a cell wide and can pair with another vertical tile in the same cell. See [Folder thumbnails](/docs/folder-thumbnails/).

## Vertical videos in folder mosaics

A folder without a cover shows a mosaic of 2 by 2 slots. A landscape video fills a whole slot, while two portrait videos share one slot side by side, so a mosaic shows up to 8 videos. A video's same-name image decides the shape of its cell, just as it does for the tile.
