---
title: "Install Reelio, a video library app for Windows"
navTitle: "Install & first library"
description: "Install Reelio, the video library app for Windows 10 and later, add your first folder, pick the subfolders to scan and let thumbnails generate."
lead: "Reelio comes from the Microsoft Store. Point it at a folder of videos, untick the subfolders you want skipped, and it builds your library while thumbnails generate in the background."
level: beginner
verified: "1.3.0.0"
related: [libraries, free-vs-premium, quality-and-speed]
---

## Requirements

Reelio runs on Windows 10 and later, on x64 and ARM64 PCs. Install it from the Microsoft Store like any other Store app.

## Add your first folder

The first time you open Reelio, there is no library yet, so the Gallery shows a **Welcome to Reelio** panel and the footer invites you to add one. Click **Choose folder…** in the panel, or **Add library** in the toolbar, then pick the folder that holds your videos in the Windows folder picker.

The library takes the name of the folder you picked. A folder that is already a library is refused, with the message "This folder is already in your library."

Before anything else, Reelio reads the folder tree (folders only, no video is opened yet) and shows an "Analyzing folders" message. If the folder cannot be read, for example because the drive or NAS is disconnected, the add stops with an error and nothing is added.

The **Add library** toolbar button is only there while you have no library. To add more folders later, use **Add folder…** in Settings > **Library**. See [Libraries](/docs/libraries/).

## Choose which subfolders to scan

If the folder has subfolders, Reelio opens **Choose folders to scan** before it reads a single video. Every subfolder appears in a tree you can expand, and every box starts ticked.

- Untick a folder to skip it, together with everything inside it.
- A folder with only some of its subfolders unticked shows a partly filled box. Click that box to tick the whole branch again.
- Hidden folders are listed too. Symbolic links and junctions are left out.

Click **Add library** to start the scan. The folders you unticked become the library's exclusions: Reelio never scans them, and their videos do not count toward the [free limit](/docs/free-vs-premium/). You can change them later in Settings, see [Libraries](/docs/libraries/).

**Cancel** stops the whole add: no library is created. If the folder has no subfolders, Reelio skips this step and starts scanning right away.

{{< tip >}}
This is the moment to leave out folders you never browse, such as exports or backups. Unticking them here keeps them out of the scan and out of your 25 free videos.
{{< /tip >}}

## The first scan

The scan runs in the background. In the Gallery, the welcome panel is replaced by a live status: Reelio first counts the videos it finds, then reads their details. The library is saved when the scan finishes, and the footer tells you how many videos were added. While a scan is running, **Add folder…** is disabled.

In the free version, only 25 videos are imported. If the folder holds more, a **Free limit reached** toast tells you how many were left out. See [Free vs Premium](/docs/free-vs-premium/).

If the scan fails, the Gallery shows **Couldn't add this folder** with the error, and a **Choose another folder…** button to try again. Nothing is registered.

## Thumbnails generate in the background

When the scan ends, the grid appears and Reelio starts generating thumbnails on its own. The footer shows the progress: a done / total counter, the folder or file being processed, a progress bar and an estimate of the time left. A button in the footer pauses generation (the footer then shows **Paused**) and resumes it.

When the add finishes, Reelio may show a **Thumbnail generation may be heavy** toast if the library is on a network drive, or if more than 5,000 videos are about to be generated. That count is the videos this add will generate, not the size of the whole library. The toast does not appear when generation already processes one video at a time (Eco, or on battery). **Switch to Eco (recommended)** sets generation to process one video at a time, starting now. See [Thumbnail quality and speed](/docs/quality-and-speed/) and [NAS and external drives](/docs/nas-and-external-drives/).

Once a video has its thumbnail, move your pointer across its tile to preview the clip. See [Hover-scrub previews](/docs/hover-scrub/).
