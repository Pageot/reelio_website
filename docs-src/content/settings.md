---
title: "Reelio settings: every option explained"
navTitle: "Settings"
description: "Every Reelio setting in the order of the Settings page: libraries, video player, theme, display defaults, thumbnail quality and speed, settings file and About."
lead: "Open Settings from the bottom of the sidebar. This page lists every setting in the order you see it, with its exact label and a link to the page that explains it."
level: advanced
verified: "1.3.0.0"
related: [libraries, quality-and-speed, video-player]
---

## How settings are saved

There is no Save button. Each change is written as soon as you make it, and an error notification (**Failed to save settings**) appears if the write fails.

{{< note >}}
Not every change applies at once. A new cache folder is used from the next launch, moving the settings file restarts Reelio immediately, and a new thumbnail **Quality** only affects thumbnails generated afterwards.
{{< /note >}}

The page has seven sections, in this order: **Premium**, **Library**, **Playback**, **Display**, **Thumbnails**, **Advanced** and **About**.

## Premium

- **Reelio Free**: in the free version, shows how many of your 25 videos are used, with a **Get Premium** button. Once you own Premium, the **Reelio Premium** card replaces it. See [Free vs Premium](/docs/free-vs-premium/).

## Library

- **Library roots**: your libraries, one card each, with **Add folder…** and, under **More options**, **Import…**. Each card can export or remove its library and holds its exclusions. See [Libraries](/docs/libraries/) and [Back up or move a library](/docs/backup-and-move-library/).
- **Cache folder**: where Reelio stores library indexes and thumbnails, with **Change…** and **Reset to default**. See [Libraries](/docs/libraries/).
- **Export prompt**: only shown after you ticked **Don't ask again, reuse this level for future exports** in the export dialog. **Always ask** brings the compression question back. See [Back up or move a library](/docs/backup-and-move-library/).
- **Restart required**: only shown while a cache folder move is waiting for the next launch.

## Playback

- **Video player**: what plays a video when you click its tile: **System default**, a detected player (**VLC**, **MPC-HC**, **MPV**) or **Custom…** to pick any program. See [Video player](/docs/video-player/).

## Display

- **Theme**: **System** (the default), **Light** or **Dark**. The change applies at once to the window and its dialogs. With **System**, Reelio follows the Windows light or dark mode, and switches when you change it in Windows.
- **Folder tile content**: which videos fill a folder tile's mosaic, **Random** or **Alphabetically first**. See [Folder thumbnails](/docs/folder-thumbnails/).
- **Default sort**: the sort used by the Gallery, folder pages and tag pages. It is the same setting as the toolbar Sort button, so changing one changes the other. Favorites and the other sidebar views keep their own order. See [Sort and views](/docs/sort-and-views/).
- **Default view**: the view used where you never picked one with the View button. Pages already open keep their view until you leave them. See [Sort and views](/docs/sort-and-views/).
- **Default search scope**: **Whole library** or **Current folder**. It is the same value as the scope buttons on the search results page. See [Search](/docs/search/).
- **Recently played count**: how many videos the Recently played view lists, from 5 to 100 (default 20). See [Favorites and quick views](/docs/favorites-and-quick-views/).
- **Random videos count**: how many videos the Random videos view draws, from 10 to 200 (default 50). See [Favorites and quick views](/docs/favorites-and-quick-views/).

## Thumbnails

- **Quality**: **Low**, **Medium**, **High** (the default) or **Ultra**. After a change, Reelio offers to regenerate every thumbnail. See [Thumbnail quality and speed](/docs/quality-and-speed/).
- **Generation speed**: **Eco**, **Balanced** (the default) or **Fast**, how many videos are processed at the same time. See [Thumbnail quality and speed](/docs/quality-and-speed/).
- **Regenerate all thumbnails**: **Run…** rebuilds every thumbnail of every library. See [Update and regenerate thumbnails](/docs/update-and-regenerate/).

## Advanced

Both Advanced settings sit in the **Power-user settings** group, which starts collapsed: click it to show them. **Settings file location** comes first, then **Hardware-accelerated decoding**.

### Settings file location

**Settings file location** shows the folder that holds Reelio's settings file, settings.json. To keep it somewhere else, for example in a folder you back up:

1. Click **Relocate…** and pick a folder.
2. Confirm with **Relocate**.

Reelio copies settings.json to that folder and restarts at once, reopening the same page. The original file stays where it was, unchanged from that moment on. Network paths (`\\server\share`), device paths and system folders are refused with **Relocate failed**.

**Reset to default**, shown only after a relocation, copies your current settings back to the default folder, deletes the relocated copy and restarts Reelio.

If the chosen folder cannot be reached when Reelio starts, it uses the settings file in the default folder and shows **Settings location unreachable**.

This only moves the settings file. Thumbnails and library indexes live in the cache folder, which you move from the **Library** section.

### Hardware-accelerated decoding

**Hardware-accelerated decoding** is on by default. It decodes video on the graphics card when generating thumbnails. Turn it off if some videos fail. See [Thumbnail quality and speed](/docs/quality-and-speed/).

## About

The **Reelio** card shows the version you are running, for example Version 1.3.0.0. Next to **Open-source licenses**, **View** opens a scrollable window with the notices of the third-party software bundled with Reelio, including the FFmpeg licence (LGPL). You can select and copy the text. Click **Close** when done.
