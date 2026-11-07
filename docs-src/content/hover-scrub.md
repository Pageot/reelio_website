---
title: "Preview videos on hover with hover-scrub"
navTitle: "Hover-scrub previews"
description: "Preview a video in Reelio without opening it: move your pointer across its tile to flip through key frames. Short clips get 2 frames, long ones 8."
lead: "Move your pointer across a video tile and Reelio flips through key frames of the clip, so you can see what is inside without opening a player."
level: beginner
verified: "1.3.0.0"
related: [video-covers, folder-thumbnails, quality-and-speed]
media:
  type: demo
  demo: scrub
---

The tile above is a demo that behaves like a video tile in Reelio. Move your pointer across it, or drag a finger on a touch screen, then pick another clip length to see how the number of frames changes.

## How it works

Point at a video tile and move left or right. Reelio splits the tile into as many equal zones as the clip has frames, and the zone under the pointer picks the frame: the left edge shows the first frame, the right edge shows the last one. Frames switch instantly, with no fade, so one sweep across the tile shows you the whole clip.

Reelio extracts these frames once, when it generates the video's thumbnail. Nothing needs to be clicked or opened to preview a clip.

## How many frames you get

The number of frames depends on the length of the video:

| Clip length | Frames |
|---|---|
| Under 30 seconds | 2 |
| 30 seconds to under 2 minutes | 3 |
| 2 minutes or longer | 8 |

A clip of exactly 30 seconds gets 3 frames, and a clip of exactly 2 minutes gets 8. The frames are spread evenly through the clip.

## When the pointer leaves the tile

Move the pointer off the tile and it goes back to its resting image. For a video without a cover, that resting image is a frame from the middle of the clip, not the first frame of the scrub.

## Videos with a custom cover

A cover you dropped on a tile, or an image with the same name as the video, only replaces the resting image. As soon as you hover, the tile shows frames of the video again, and the cover comes back when the pointer leaves. See [Video covers](/docs/video-covers/) to set one.

## Where hover-scrub works

Hover-scrub works on video tiles in the **Extra large**, **Large** and **Medium** views. In the **Details** view, the small thumbnail at the start of each row does not scrub. Folder tiles do not scrub either: they show a cover or a mosaic of the videos inside.

{{< tip >}}
In a folder mosaic, hold **Alt** and click a cell to play that video directly, without opening the folder. Holding Alt while you move over the mosaic highlights the cell that Alt+click would play. See [Folder thumbnails](/docs/folder-thumbnails/).
{{< /tip >}}

## When there is nothing to scrub

Scrubbing starts once the video's thumbnail has been generated, so a video added a moment ago may not scrub yet. A video whose thumbnail failed, or that you marked as corrupted, has no frames to scrub. See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/).

## Related shortcuts

{{< keys >}}
Alt+Click | Play the video under the pointer in a folder mosaic
Alt+Hover | Highlight the mosaic cell that Alt+click would play
{{< /keys >}}
