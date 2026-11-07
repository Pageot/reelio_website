---
title: "Back up or move your video library to a new PC"
navTitle: "Backup & move to a new PC"
description: "Move your video library to a new PC or keep a backup: export a Reelio library to a .zip with its tags, favorites and thumbnails, then import it on the other PC."
lead: "Export a library to a .zip file to keep a backup, or to carry its tags, favorites and thumbnails to another PC, then import it there next to your videos."
level: advanced
verified: "1.3.0.0"
related: [libraries, free-vs-premium, install]
---

Export and import both live in **Settings**, in the **Library** section. An export covers one library, so a PC with several libraries gives several .zip files.

## What a library export contains

The archive holds the library's index (its videos with their tags, favorites and details) and its thumbnails, plus a small description file that Reelio checks on import.

It does not hold:

- the video files: copy them yourself, or reconnect the drive or NAS that holds them;
- the library's exclusions: set them again after the import, see [Libraries](/docs/libraries/);
- the cached cover images: folder covers and same-name images are read again from the source folders after the import;
- custom covers you dropped on tiles: they are lost and must be dropped again, see [Video covers](/docs/video-covers/);
- your app settings, such as the video player or the theme.

{{< note >}}
Because exclusions and dropped covers are not exported, an imported library can look different at first: excluded folders are scanned again, and tiles with a dropped cover go back to their image or generated thumbnail.
{{< /note >}}

## Export a library

1. On the library's card, click the export icon (**Export this library to a .zip**).
2. The **Export compression** dialog asks how hard to compress the archive. There are four levels: the quickest export with the largest file (the default), a balanced level, the smallest file with the slowest export, and no compression at all (fastest to read back). Thumbnails are already compressed, so the stronger levels save little space. Reelio remembers your last choice.
3. Click **Export**. A Save dialog opens in your Documents folder, with the file type **Reelio library archive** and a name made of the library name and today's date.

A notification confirms the export, or shows **Export failed** if something went wrong.

### Skip the compression question

Tick **Don't ask again, reuse this level for future exports** in the dialog. Later exports then use the saved level without asking. To get the question back, click **Always ask** on the **Export prompt** card, which appears in the **Library** section once you have ticked that box. The notification **Export prompt restored** confirms it.

## Import a library

1. Next to **Add folder…**, click the **More options** button (three vertical dots), then **Import…**.
2. Pick the .zip file exported by Reelio.
3. Pick the folder that holds the library's videos on this PC.

An **Importing library…** row shows the progress. The library takes its name from the archive, then Reelio rescans the folder and starts generating thumbnails in the background. A notification confirms the import with the library name and folder.

- Only archives exported by Reelio are accepted. Anything else is refused with **Import failed**.
- If the folder you picked already is a library, the import is skipped with **Import skipped**.
- If the rescan fails, the library is still imported, with an **Import scan warning**.
- On a NAS, Reelio may suggest the Eco speed afterwards. See [NAS and external drives](/docs/nas-and-external-drives/).

{{< note >}}
In the free version, an import is all or nothing: if the archive's videos would take your total above 25, the whole import is refused with **Import would exceed the free limit (25 videos). Get Premium to import this library.** A normal folder scan, by contrast, adds videos up to the limit. See [Free vs Premium](/docs/free-vs-premium/).
{{< /note >}}

## Move your library to a new PC

1. On the old PC, export each library.
2. Copy the video files to the new PC, or connect the drive or NAS that holds them.
3. Install Reelio on the new PC (see [Install Reelio](/docs/install/)) and launch it once.
4. Import each .zip, picking the folder that now holds its videos.
5. Set your exclusions again, drop your custom covers again, and choose your settings.

{{< tip >}}
Premium follows your Microsoft account. At each launch, Reelio asks the Microsoft Store in the background whether your account owns Premium and unlocks it automatically: there is no restore button to find. After that, Premium keeps working offline. Before importing a library of more than 25 videos, launch Reelio once on the new PC and check that **Settings** shows the **Reelio Premium** card.
{{< /tip >}}

{{< note >}}
An archive contains the paths of your videos inside the library, your tags and your favorites. Keep that in mind before you share one.
{{< /note >}}
