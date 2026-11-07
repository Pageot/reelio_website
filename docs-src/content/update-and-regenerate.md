---
title: "New videos not showing in the library? Update thumbnails"
navTitle: "Update and regenerate"
description: "New videos not showing in your Reelio library? Click Update thumbnails to scan for new files, or use Regenerate all thumbnails to rebuild every one."
lead: "Reelio does not watch your folders. When you copy, rename or delete videos on disk, click Update thumbnails and the library catches up."
level: beginner
verified: "1.3.0.0"
related: [quality-and-speed, failed-and-corrupted, nas-and-external-drives]
---

Reelio reads your folders when you add a library, then works from its own index. Videos you add, rename or delete later appear in the library after a scan, and the scan starts when you click **Update thumbnails**. The same goes for cover images you add next to your videos, such as a `folder.jpg` (see [Video covers](/docs/video-covers/) and [Folder thumbnails](/docs/folder-thumbnails/)).

## Update thumbnails in the Gallery

Click **Update thumbnails** at the top right of the Gallery toolbar. Reelio then:

1. Scans every library on disk: it adds new videos, updates changed ones and removes the ones no longer on disk.
2. Generates a thumbnail for every video that has none, and tries again the videos whose thumbnail failed or whose file was not found.

Existing thumbnails are kept as they are, and videos you marked as corrupted are skipped (see [Failed and corrupted thumbnails](/docs/failed-and-corrupted/)). The button is disabled until you have added a library. Some messages in the app call this action a refresh.

## Update thumbnails in a folder

The same button on a folder page works only on that folder and all its subfolders. The parent folder and the folders next to it are not scanned and get no new thumbnails. Use it when you changed the content of one folder.

On a tag page, the **Update thumbnails** button only reloads the list of tagged items. It does not scan your drives and does not generate any thumbnail.

## One update at a time

Only one scan or generation runs at a time in the whole app. While one is running in any tab, including **Regenerate all thumbnails** and the first generation after adding a library, the **Update thumbnails** buttons are disabled and their tooltip explains why. They also stay disabled while a generation is paused: resume it and let it finish first. The button icon spins while an update runs.

## Follow the progress

While Reelio scans, the footer of the Gallery and folder pages shows what it is doing. While thumbnails generate, the footer shows a counter (videos done out of the total, per library when there are several), the name of the file being processed, a progress bar, an estimate of the time left once a few videos are done, and a **Pause / Resume** button.

Pause holds the generation: videos already being processed finish, and no new one starts until you resume. **Paused** then replaces the time estimate. An update cannot be cancelled from the footer; you can only pause it.

While a video waits for its thumbnail, its tile shows a placeholder that shakes while the video is being processed, and each cell of a folder mosaic fills in as soon as its video is done.

When the run ends, the footer shows a summary and a notification gives the number of thumbnails generated (no notification appears when nothing was generated or failed). If some failed, the notification adds the failed count and a **View failed** button. Without failures, it closes by itself after 6 seconds.

## Regenerate all thumbnails

Use this after changing the thumbnail quality (see [Quality and speed](/docs/quality-and-speed/)), or when you want every thumbnail rebuilt from scratch.

1. Open **Settings** > **Thumbnails**.
2. On the **Regenerate all thumbnails** card, click **Run…**.
3. Confirm with **Regenerate**. **Cancel** is the default button.

Reelio first clears the thumbnail of every video in every library, so all tiles go back to the placeholder at once. Then, library by library, it scans the library on disk and rebuilds every thumbnail, including videos that failed, were not found or were marked as corrupted. It also rebuilds the cached folder covers and associated images at the current quality. An **Update thumbnails** run in progress is cancelled, and new ones are refused until it ends.

Progress shows under the card and in the Gallery and folder footers, with the same **Pause / Resume** button. A **Cancel** button next to **Run…** stops the whole regeneration.

{{< note >}}
Connect all your drives before you run **Regenerate all thumbnails**. If a library's drive or network share is offline, its scan is skipped but its thumbnails are still cleared, and every video of that library ends up marked **File not found**. To recover, reconnect the drive and click **Update thumbnails**: it tries those videos again.
{{< /note >}}
