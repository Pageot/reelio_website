---
title: "Reelio troubleshooting: missing thumbnails and more"
navTitle: "Troubleshooting"
description: "Reelio not working as expected? Fixes for missing thumbnails, folder.jpg not showing, VLC missing from the player list, the 25-video limit and Could not open."
lead: "Find your symptom below. Each answer gives the fix and links to the page that explains the feature in detail."
level: advanced
verified: "1.3.0.0"
related: [failed-and-corrupted, update-and-regenerate, nas-and-external-drives]
---

## My folder.jpg, img folder or same-name image does not show

Reelio looks for these files during a library scan, not live. After you add, rename or remove a `folder.jpg`, an `img` folder or an image named like a video, click **Update thumbnails** in the Gallery or on the folder's page.

If it still does not show:

- Check the image type: only .jpg, .jpeg, .png and .webp work. See [Formats and file names](/docs/formats-and-file-names/).
- A folder only appears in Reelio if it contains at least one video somewhere below it.
- An `img` folder needs at least one supported image inside.
- The top level of a library, shown in the Gallery, never shows an image strip or a header cover.

Images added to an `img` folder Reelio already knows appear the next time you open the folder. See [Folder thumbnails](/docs/folder-thumbnails/), [img folder slideshow](/docs/img-slideshow/) and [Video covers](/docs/video-covers/).

## New videos do not appear in my library

Reelio never scans on its own. Click **Update thumbnails** in the Gallery to scan every library, or on a folder's page to scan only that folder and its subfolders. See [Update and regenerate thumbnails](/docs/update-and-regenerate/).

## Some thumbnails failed to generate

Failed videos are counted in the **Failed thumbnails** entry of the sidebar, and every **Update thumbnails** run tries them again. You can also right-click a video and choose **Try to generate again**. If several videos keep failing, turn off **Hardware-accelerated decoding** in **Settings** (inside the **Power-user settings** group) and try again. See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/).

## VLC, MPC-HC or MPV is missing from the Video player list

Reelio only detects these players at their standard install locations, for example `C:\Program Files\VideoLAN\VLC\vlc.exe` for VLC. A player installed anywhere else is not listed. Open **Settings**, choose **Custom…** in **Video player** and pick the player's .exe file. Reelio looks for players once per session, so if you installed the player while Reelio was open, restart Reelio to see it in the list. See [Video player](/docs/video-player/).

## "Could not open" appears when I click a video

The footer shows **Could not open** followed by the video name when nothing could be started. The usual causes:

- The file is no longer there: it was moved or deleted, or its drive or NAS is disconnected. Reconnect it, or run **Update thumbnails** to bring the library up to date.
- The player cannot start: check that the program chosen in **Video player** still exists, or choose **System default** to open videos with their Windows default app.

See [Video player](/docs/video-player/).

## The tile did not turn vertical after I dropped a portrait cover

The cover shows at once, but the tile changes shape only the next time the page loads. Go to another page and come back. A square image counts as landscape. See [Video covers](/docs/video-covers/) and [Vertical videos](/docs/vertical-videos/).

## I can't add more than 25 videos

The free version holds at most 25 videos in total, across all your libraries. When a scan finds more, only the remaining free slots are filled and a **Free limit reached** notification says how many videos were not imported. Videos already in the library keep working.

To make room, exclude folders you don't need or remove a library. A folder added as a library inside another library counts its videos twice, so remove the inner one. For unlimited videos, get Premium. See [Free vs Premium](/docs/free-vs-premium/) and [Libraries](/docs/libraries/).

## My external drive or NAS was unplugged

Your library is not emptied: a scan of a library that cannot be reached is abandoned before it changes anything. Reconnect the drive, then click **Update thumbnails** to retry any video shown as **File not found**. See [NAS and external drives](/docs/nas-and-external-drives/).

## Every video of a library shows "File not found"

A common cause: **Regenerate all thumbnails** ran while that library's drive was offline. Reconnect the drive and click **Update thumbnails**. See [NAS and external drives](/docs/nas-and-external-drives/).

## A "Cache folder unreachable" banner appears

The drive that holds Reelio's cache folder is disconnected. Reconnect it to resume normal operation. See [Libraries](/docs/libraries/).
