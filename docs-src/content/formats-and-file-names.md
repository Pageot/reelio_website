---
title: "Supported video formats and special file names"
navTitle: "Formats & file names"
description: "Which video formats Reelio shows thumbnails for (MXF, MTS, M2TS, VOB, MKV and more), which image types work as covers, and the folder.jpg and img names."
lead: "Reelio indexes 20 video extensions and reads covers from four image types. Three file and folder names have a special meaning; everything else is just a file."
level: advanced
verified: "1.3.0.0"
related: [folder-thumbnails, video-covers, img-slideshow]
---

## Video formats

Reelio indexes exactly these 20 extensions and generates thumbnails and hover-scrub frames for them:

| Family | Extensions |
|---|---|
| MP4 and QuickTime | .mp4, .m4v, .mov |
| Matroska and WebM | .mkv, .webm |
| Windows Media and AVI | .avi, .wmv, .asf |
| MPEG and DVD | .mpg, .mpeg, .vob |
| MPEG transport streams | .ts, .mts, .m2ts |
| Professional (MXF) | .mxf |
| Mobile | .3gp |
| Other | .flv, .ogv, .rm, .rmvb |

Files with any other extension are not indexed and never appear in Reelio. With the **System default** player, Reelio only opens files with one of these extensions. See [Video player](/docs/video-player/).

Extensions are matched whatever their letter case: .MP4, .MTS or .MXF work the same as lowercase.

## Image formats

Covers, folder images, `img` strips and same-name images all accept the same four types: .jpg, .jpeg, .png and .webp, in any letter case.

Other image types are not recognised for any of these roles: .gif, .bmp, .tif and .tiff, .heic, .avif and .jfif. Convert such an image to JPG, PNG or WebP first.

## Special file and folder names

Reelio recognises exactly three names when it scans a library:

| Name | Where | What it does | Details |
|---|---|---|---|
| `folder.jpg`, `folder.jpeg`, `folder.png` or `folder.webp` | Directly inside a folder | Becomes that folder's cover. If several exist, the first in this order wins: .jpg, .jpeg, .png, .webp | [Folder thumbnails](/docs/folder-thumbnails/) |
| A subfolder named `img` | Directly inside a folder | Shows its images as a scrolling strip at the top of the folder's page | [img folder slideshow](/docs/img-slideshow/) |
| An image with the same name as a video | Next to the video | Becomes that video's cover, for example `holiday.jpg` for `holiday.mp4` | [Video covers](/docs/video-covers/) |

For a same-name image, only the last extension of the video is dropped: `my.clip.mp4` pairs with `my.clip.jpg`, not with `my.jpg`.

These names are found during a library scan, not live. After you add, rename or remove one, click **Update thumbnails** so Reelio picks it up. Images added to an `img` folder that Reelio already knows show up the next time you open the folder, without a scan. See [Update and regenerate thumbnails](/docs/update-and-regenerate/).

{{< note >}}
On a standard Windows drive, `Folder.JPG` or `IMG` work too, because Windows ignores letter case in names. On a NAS share, or a folder where case sensitivity is turned on, use lowercase names (`folder.jpg`, `img`) to be safe.
{{< /note >}}

The top level of a library, shown in the Gallery, has no image strip and no header cover, even if the library folder itself contains `img` or `folder.jpg`.

## No other special names

Reelio recognises no other special name. Hidden and system files and folders are scanned like any other. Folder junctions and symbolic links are not followed.

The `img` folder is still a normal folder: if you put videos inside it, they are indexed and `img` appears as an ordinary subfolder. A folder that holds only images, with no video anywhere below it, never appears as a folder tile.
