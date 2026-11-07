---
title: "Open videos in VLC, MPV or your own player"
navTitle: "Video player"
description: "Open videos from your Reelio library in VLC, MPV, MPC-HC or any player you choose, instead of the Windows default app, with a single click on a tile."
lead: "Reelio does not play videos itself: one click on a tile opens the clip in the player you choose, whether that is the Windows default app, VLC, MPV, MPC-HC or any other program."
level: beginner
verified: "1.3.0.0"
related: [settings, favorites-and-quick-views, troubleshooting]
---

## Click to play

A single left click on a video tile, or on a video row in the Details view, plays the video. A single click on a folder opens it. There is no double-click action. This works the same on every page: the Gallery, folders, search results, tags and the sidebar views.

{{< tip >}}
On a folder tile that shows a mosaic of thumbnails, hold Alt and click one of them to play that video without opening the folder. See [Folder thumbnails](/docs/folder-thumbnails/).
{{< /tip >}}

## Choose your video player

Open [Settings](/docs/settings/), go to **Playback** and pick a program in the **Video player** list. The list contains:

- **System default** (the default): opens the file with the app Windows uses for its file type.
- **VLC**, **MPC-HC** and **MPV**: each one appears only if Reelio found it at its standard install location (see the table below).
- **Custom…**: lets you pick any other program.

Any choice other than **System default** runs that program with the video's full path, so the player opens the clip directly.

### Where Reelio looks for VLC, MPC-HC and MPV

Reelio checks only these locations:

| Player | Locations checked |
|---|---|
| VLC | `C:\Program Files\VideoLAN\VLC\vlc.exe` or `C:\Program Files (x86)\VideoLAN\VLC\vlc.exe` |
| MPC-HC | `C:\Program Files\MPC-HC\mpc-hc64.exe` or `C:\Program Files (x86)\MPC-HC\mpc-hc.exe` |
| MPV | `C:\Program Files\mpv\mpv.exe` or `%LOCALAPPDATA%\mpv\mpv.exe` |

A player installed anywhere else is not listed. Pick it with **Custom…** instead.

### Use any other player

Choose **Custom…** and a file picker opens, limited to .exe files. Select the player's program file. The list then shows **Custom, &lt;exe name&gt;** with the name of the file you picked. If you cancel the picker, the previous choice stays.

{{< note >}}
If you install a player while Reelio is running and it does not appear in the list, restart Reelio so it can detect it.
{{< /note >}}

## Right-click menus

Right-click a tile or a Details row to see what you can do with that video or folder. Some entries appear only in certain situations.

| Entry | Videos | Folders | What it does |
|---|---|---|---|
| **Add to favorites** / **Remove from favorites** | Yes | Yes | Adds or removes the favorite. See [Favorites and quick views](/docs/favorites-and-quick-views/). |
| **Tags** | Yes | Yes | Adds or removes tags. See [Tags](/docs/tags/). |
| **Show in folder** | Yes | No | Opens File Explorer on the video's folder, with the file selected. |
| **Delete video…** | Yes | No | Moves the file to the Recycle Bin (see below). |
| **Try to generate again** | When the thumbnail failed, is marked as corrupted, or the file is missing | No | Retries the thumbnail. See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/). |
| **Rescan folder** | When the file is missing | No | Rescans the video's folder. See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/). |
| **Mark as corrupted** | When the thumbnail failed | No | See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/). |
| **Reset thumbnail** | When it has a custom cover | When it has a custom cover | Removes the custom cover. See [Video covers](/docs/video-covers/) and [Folder thumbnails](/docs/folder-thumbnails/). |

## Delete a video

Choose **Delete video…** in a video's right-click menu. Reelio asks **Delete video?** and explains that the file will be moved to the Recycle Bin and removed from the library. Click **Delete** to confirm, or **Cancel** (the default button) to keep it. Once confirmed, the file goes to the Recycle Bin and its tile disappears from every page. If the deletion fails, Reelio shows **Could not delete video**.

## When a video does not open

If the file no longer exists or the player cannot be started, nothing opens and the status bar at the bottom of the page reads **Could not open &lt;name&gt;.** See [Troubleshooting](/docs/troubleshooting/).

## Recently played

Every video that opens successfully in your player is added to **Recently played** in the sidebar, whether you clicked its tile, pressed Enter on it, or Alt+clicked it in a folder mosaic. See [Favorites and quick views](/docs/favorites-and-quick-views/).
