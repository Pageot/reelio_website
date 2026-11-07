---
title: "Change a video thumbnail on Windows with Reelio"
navTitle: "Video covers"
description: "Change a video thumbnail on Windows: drop a JPG, PNG or WebP image on a video in Reelio, or keep a same-name image next to the file. Reset it anytime."
lead: "Give any video the still image you want: drop an image on its tile, or keep an image with the same name next to the video file."
level: beginner
verified: "1.3.0.0"
related: [folder-thumbnails, hover-scrub, vertical-videos]
---

Reelio gives a video a cover in one of two ways: an image you drop on it (a custom cover), or an image with the same name sitting next to the video file (an associated image). Folders can have covers too, see [Folder thumbnails](/docs/folder-thumbnails/).

## Drop an image on a video

Drag an image file from File Explorer and drop it on a video tile. The image becomes that video's cover at once. This works in every grid: folder pages, search results, tag pages and sidebar views. In the **Details** view, drop the image on the video's row.

- Accepted formats: .jpg, .jpeg, .png and .webp, whatever the case of the extension.
- If you drop several files, Reelio uses the first image and ignores the other files and any folders.
- Reelio keeps its own copy of the image, so you can move or delete the original right after the drop.
- Drag the file from File Explorer. An image dragged straight out of a web browser may not arrive as a file and is then not accepted.
- Only image files from outside Reelio work: you cannot drop one Reelio video tile on another to reuse its picture.

If nothing you dropped is a JPG, PNG or WebP image, or the image cannot be read, a **Could not set cover** dialog explains why. Click **OK**: nothing changes.

{{< tip >}}
A portrait image gives the video a narrow vertical tile, but the tile changes shape only the next time the page loads (go to another page and back). Until then, the new cover is cropped to fill the tile's current shape. See [Vertical videos](/docs/vertical-videos/).
{{< /tip >}}

## Reset a cover

Right-click the video (its tile, or its row in the **Details** view) and choose **Reset thumbnail**, the last item of the menu. The item only appears when the video has a dropped cover. The cover is removed immediately, with no confirmation.

After a reset, the video shows its associated image if it has one, otherwise its generated thumbnail.

## Use a same-name image

Put an image in the same folder as the video, with the same base name: `holiday.jpg` next to `holiday.mp4`. Reelio then shows that image instead of the generated thumbnail. This is handy when your footage already comes with stills or poster frames.

- Formats: .jpg, .jpeg, .png and .webp. If several exist for one video, Reelio takes the first it finds in this order: .jpg, .jpeg, .png, .webp.
- On standard Windows drives the match ignores letter case, so `Holiday.JPG` goes with `holiday.mp4`. On a NAS share, use exactly the same name to be safe.
- A portrait image gives the video a vertical tile, even if the video itself is landscape, and the other way around.
- The image also stands for the video in its parent folders' mosaics.

{{< tip >}}
The base name is the file name without its *last* extension only: `my.clip.mp4` goes with `my.clip.jpg`, not with `my.jpg`.
{{< /tip >}}

{{< tip >}}
Same-name images are picked up by a library scan, not live. After you add, rename or remove one, click **Update thumbnails** in the toolbar so Reelio sees the change. See [Update and regenerate thumbnails](/docs/update-and-regenerate/).
{{< /tip >}}

To stop using a same-name image, delete or rename it, then run **Update thumbnails**.

## Which image a video shows

When several images could apply, Reelio picks one in this order:

1. The custom cover you dropped.
2. The same-name image next to the file.
3. The thumbnail Reelio generated from the video.

Whatever the cover, hovering the tile still shows frames of the video, and the cover comes back when the pointer leaves. See [Hover-scrub previews](/docs/hover-scrub/).

{{< note >}}
A dropped cover is used on the video's own tile and row only. In a folder's mosaic, the video's cell shows its same-name image or its generated thumbnail, never the dropped cover.
{{< /note >}}
