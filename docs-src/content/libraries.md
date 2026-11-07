---
title: "Manage video libraries and exclude folders from scans"
navTitle: "Libraries & exclusions"
description: "Add several video libraries to Reelio, exclude folders from the library scan, remove a library safely, and move the thumbnail cache to another drive."
lead: "A library is a folder that Reelio scans for videos. You can add several, keep some subfolders out of the scan, and choose the drive where Reelio stores its thumbnails."
level: advanced
verified: "1.3.0.0"
related: [install, nas-and-external-drives, backup-and-move-library]
---

Everything on this page happens in **Settings**, in the **Library** section. Open **Settings** from the bottom of the sidebar.

## Add another library

The **Library roots** card lists every library as a card, with its name and full path. Click **Add folder…** to add one more.

The steps are the same as for your first library: pick a folder, untick the subfolders you want to skip, and Reelio scans it, then generates thumbnails in the background. See [Install Reelio](/docs/install/) for each step. While a scan is running, **Add folder…** is disabled.

You can add as many libraries as you like. The Gallery merges them into one page, so you browse them together. Picking a folder that already is a library is refused with an **Already added** notification.

{{< note >}}
Reelio does not stop you from adding a folder that sits inside an existing library, or a folder that contains one. Its videos are then indexed twice, and in the free version they count twice toward the 25-video limit. See [Free vs Premium](/docs/free-vs-premium/).
{{< /note >}}

## Exclude folders from the scan

Each library card has a collapsible **Exclusions** section, with the number of excluded folders in its title. Expand it to see the excluded subfolders, shown relative to the library.

- To bring one folder back, click the X next to it (**Remove this exclusion**).
- To change several at once, click **Manage exclusions…**. Reelio reads the folder tree from disk (the button shows **Reading folders…** meanwhile) and opens the **Manage exclusions** dialog, with your current exclusions already unticked. Untick the folders to skip, tick the ones to scan again, then click **Save**.

If the library has no subfolder, Reelio tells you so with **No subfolders to exclude**. An exclusion whose folder is no longer on disk is kept.

## What an exclusion does

An excluded folder, and everything inside it, is skipped by every scan. The folder name matches whatever its letter case.

When you add or remove an exclusion, Reelio rescans only that folder, in the background, right away:

- Videos in a newly excluded folder disappear from every view. They stop counting toward the free 25-video limit, and Reelio never generates thumbnails for them.
- When you remove the exclusion, the videos come back.

{{< tip >}}
An exclusion is easy to undo for about a week. Hidden videos keep their tags and favorites for about 7 days, so if you remove the exclusion within that time they come back as they were. A scan that runs after that deletes them for good, and re-including the folder later adds them back as new videos, without tags.
{{< /tip >}}

## Remove a library

Click the trash icon on the library card (**Remove this library**), then confirm with **Remove** in the **Remove library?** dialog.

Removing a library:

- removes it from Reelio, and the free-tier video count is recomputed;
- deletes everything Reelio stored for it: the index of its videos with their tags, favorites and details, the thumbnails, the cached cover images including custom covers you dropped, and the views remembered for its folders;
- never touches the video files on disk.

There is no undo. If you want to keep tags and favorites, export the library first: see [Back up or move a library](/docs/backup-and-move-library/).

## Move the thumbnail cache to another drive

The **Cache folder** card shows where Reelio stores library indexes and thumbnails. By default this is a folder in your Windows user profile. To use another drive:

1. Click **Change…** and pick a folder.
2. Confirm with **Queue change**. Nothing moves yet.
3. A **Restart required** bar appears. Click **Apply now** to restart Reelio straight away: after you confirm, Reelio closes, moves the cache, and reopens on the same page. Or keep working: the cache moves the next time you launch Reelio. **Cancel pending change** drops the move.

Picking the current folder gives **No change**. A folder inside the current cache folder, or one that contains it, is refused as **Invalid folder**.

To go back, click **Reset to default**. It only appears while a custom folder is in use, and it queues a move back to the default location for the next launch.

The cache move does not move your settings file. See [Settings](/docs/settings/) for that.

## If the cache drive is disconnected

Reelio checks every 7 seconds that the cache folder is still there. If its drive is disconnected, a **Cache folder unreachable** banner asks you to reconnect it. You can dismiss the banner; it then stays hidden for the rest of that disconnection. For libraries stored on a NAS or a removable drive, see [NAS and external drives](/docs/nas-and-external-drives/).
