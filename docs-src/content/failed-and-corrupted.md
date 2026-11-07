---
title: "Video thumbnails that failed to generate"
navTitle: "Failed and corrupted"
description: "Video thumbnails failed to generate in Reelio? Find them in one view, retry them, mark broken files as corrupted, or rescan the folder of a moved file."
lead: "When Reelio cannot build a video's thumbnail, it keeps track of it. You can list every failed video, try again, or mark files that will never work as corrupted."
level: beginner
verified: "1.3.0.0"
related: [update-and-regenerate, quality-and-speed, troubleshooting]
---

## Why a thumbnail fails

A video is marked as failed when FFmpeg cannot read it or produces no image, when its duration cannot be read, when it takes longer than the 5-minute limit per video, or when its thumbnail file has gone missing from the cache. Reelio remembers the failure across restarts, and every **Update thumbnails** run tries failed videos again automatically (see [Update and regenerate thumbnails](/docs/update-and-regenerate/)).

Before giving up, Reelio tries to rescue a damaged file by looking for a single readable frame at several points of the video. If one works, the video gets a still thumbnail with no [hover-scrub](/docs/hover-scrub/) preview, and it counts as generated, not failed. This rescue is not attempted after a video hits the time limit.

If the video file itself is gone when Reelio tries to generate it (moved, renamed, replaced by another format, or on a drive that is offline), the tile shows **File not found** instead. The section on **Rescan folder** below explains how to fix it.

## Find your failed thumbnails

There are three ways to open the **Failed thumbnails** view:

- The **Failed thumbnails** entry near the bottom of the sidebar, just above Settings, with a badge showing the count. It only appears while the count is above zero.
- The "N failed" link, with a red warning icon, in the footer of the Gallery and folder pages. It is hidden while a generation runs.
- The **View failed** button in the notification shown when a generation ends with failures. That notification stays until you click it or close it.

The count adds up all your libraries and includes failed videos and **File not found** videos. Videos marked as corrupted, and videos in excluded folders, are not counted.

The view lists all these videos, sorted by path. When nothing is left, it shows **No failed thumbnails.** and the sidebar entry disappears.

## Try again on one video

A failed video with no image to show displays **Retry** over its thumbnail area. Click it to generate that video again. If a generation is already working on that library, the retry is not started and a notification explains why: that generation retries failed videos anyway.

The **Retry** overlay does not appear when the tile shows a custom cover or an associated image. In that case, and for **File not found** or corrupted videos, right-click the tile and choose **Try to generate again**. If the new attempt fails, the video is marked as failed again and comes back in the count.

## Mark a video as corrupted

For a file that will never work, right-click it and choose **Mark as corrupted** to take it out of the failed count, the badge and the view. **Update thumbnails** no longer retries it. This option is not offered on **File not found** videos.

A corrupted video shows a neutral placeholder reading **Corrupted video** and **No thumbnail could be generated**. It is not clickable. If you dropped a custom cover on it, the cover shows instead (see [Video covers](/docs/video-covers/)). To try again later, use **Try to generate again**, or run **Regenerate all thumbnails**, which also retries corrupted videos.

To clear the whole list at once, click **Mark all as corrupted** in the toolbar of the **Failed thumbnails** view. After you confirm, every failed video of all libraries is marked as corrupted. **File not found** videos are not marked and stay in the view. This button is refused while a generation is running.

## File not found and Rescan folder

When **Retry** or **Try to generate again** finds that the file is missing, a notification titled **Video file not found** offers **Rescan folder**. It closes after 16 seconds, so the same command is also in the right-click menu of every **File not found** video.

**Rescan folder** removes the missing entry, then scans the video's folder including all its subfolders: other missing entries there are removed too, replacement files are added, and missing thumbnails are generated (existing ones are kept). It never scans the whole library: for a video at the root of the library, it only removes the entry, or regenerates it if the file is back. Removed entries are kept for 7 days and come back if the files reappear. The rescan is refused while a generation or a library scan is running.

If the folder cannot be opened, for example because the drive is unplugged or the network share is offline, nothing is removed and Reelio shows **Folder not reachable**. Reconnect the drive and try again.

{{< tip >}}
An unplugged drive never empties your library. Any scan of a library or folder that cannot be found stops before changing anything. See [NAS and external drives](/docs/nas-and-external-drives/).
{{< /tip >}}

## Excluded folders

Videos inside a folder you excluded are never generated, so they never appear in the failed count or the view. See [Libraries](/docs/libraries/) to manage exclusions.
