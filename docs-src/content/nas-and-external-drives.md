---
title: "Video library on a NAS or external drive"
navTitle: "NAS & external drives"
description: "Keep your video library on a NAS or external drive: Reelio stores thumbnails and covers on your PC, and an unplugged drive never empties your library."
lead: "Reelio works with videos on a network share or a removable drive. Thumbnails and cover images live on your PC, and your library stays intact while the drive is offline."
level: advanced
verified: "1.3.0.0"
related: [libraries, quality-and-speed, failed-and-corrupted]
---

## Add a library from a NAS

Add a network share or a folder on an external drive like any other folder: see [Libraries](/docs/libraries/). If Reelio cannot read the folders of a network share while you add it from **Settings**, it stops and shows **Couldn't reach the library**, asking you to check that the NAS or drive is connected.

## Use Eco speed for network drives

Before a generation starts, Reelio may suggest the Eco speed when the library is on a network drive (a `\\server\share` path, or a mapped drive letter that Windows reports as a network drive), or when more than 5,000 videos are about to be generated.

The notification reads **Thumbnail generation may be heavy**. Its **Switch to Eco (recommended)** button saves Eco as your generation speed and applies it to the generation already running. The notification closes by itself after 16 seconds, and is not shown when generation already runs one video at a time (Eco selected, or a laptop on battery).

{{< note >}}
The suggestion does not always appear, and a NAS that Windows presents as a local disk (for example through iSCSI) is not detected as a network drive. If your library is on a NAS, pick **Eco** yourself in **Settings** under **Generation speed**. See [Thumbnail quality and speed](/docs/quality-and-speed/).
{{< /note >}}

## Covers are read from the NAS once

Video thumbnails and hover-scrub frames are stored in Reelio's cache folder on your PC. Reelio also keeps a local copy of three kinds of images:

- folder cover images (`folder.jpg` and the like),
- images with the same name as a video,
- custom covers you dropped on a tile (for these, the local copy is the only copy Reelio keeps).

A background pass reads each image once, scales it down and saves a local WebP copy. Until that copy exists, the tile shows the original from the NAS, then switches to the local copy as soon as it is written. A copy is made again only if the source file's name or modified time changes.

This pass is silent and gentle: no progress in the footer, no notification, and at most 2 images at a time, 1 on battery or when the generation speed is Eco. It runs after adding or importing a library, after **Update thumbnails** and folder rescans, and at every launch. **Regenerate all thumbnails** makes every copy again.

If a local copy is missing or cannot be read, Reelio shows the original image instead. Removing a library deletes all its cached images, custom covers included.

The images of a folder's `img` subfolder are not cached: Reelio reads them from the folder each time you open it, so that strip needs the drive. See [img folder slideshow](/docs/img-slideshow/).

## Unplugging a drive does not empty your library

Reelio never scans on its own. Every scan follows something you do: adding or importing a library, **Update thumbnails**, **Regenerate all thumbnails**, changing exclusions, or **Rescan folder**.

{{< tip >}}
If a scan runs while the drive is unplugged or the NAS is offline, Reelio sees that the library or folder cannot be reached and abandons the scan before changing anything. After **Update thumbnails**, the status simply reads **Refreshed, 0 added, 0 updated, 0 removed.** Your videos, tags and favorites stay where they were.
{{< /tip >}}

While the drive is away, you can still browse the library, since thumbnails are on your PC. Playing a video needs the file, so a click shows **Could not open** in the footer until the drive is back. See [Troubleshooting](/docs/troubleshooting/).

## When files really are gone

When the folder can be reached but some files were deleted or moved, the next scan removes them from the library. Reelio keeps the removed entries for 7 days: if the files come back within that time, they reappear.

If a video's file is missing at the moment its thumbnail is generated (moved, renamed, or on a drive that is offline), its tile shows **File not found** and counts as a failed thumbnail. Reconnect the drive and click **Update thumbnails**: it retries these videos.

To clean up one folder, right-click a **File not found** video and choose **Rescan folder**. Reelio rescans that video's folder and its subfolders only, removing entries whose files are gone and adding replacement files. If the folder cannot be opened, nothing is removed and Reelio shows **Folder not reachable**. See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/).

{{< note >}}
Connect all your drives before you run **Regenerate all thumbnails**. With a drive offline, every video of that library ends up as **File not found**. To recover, reconnect the drive and click **Update thumbnails**.
{{< /note >}}

## If the cache itself is on an external drive

If you moved Reelio's cache folder to a removable drive and it is disconnected, a **Cache folder unreachable** banner asks you to reconnect it. See [Libraries](/docs/libraries/).

A library export does not include the cached images. See [Back up or move a library](/docs/backup-and-move-library/).
