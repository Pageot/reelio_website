---
title: "Sort videos by resolution, duration or size"
navTitle: "Sort and views"
description: "Sort videos in Reelio by name, date added, duration, file size, modified date or resolution, and switch between large tiles and a Details list with columns."
lead: "Use the Sort button to order your clips by resolution, duration, size or date, and the View button to switch between big tiles and a Details list that shows each clip's resolution, codec and frame rate."
level: beginner
verified: "1.3.0.0"
related: [vertical-videos, favorites-and-quick-views, search]
---

## Sort your videos

Click **Sort** at the left of the toolbar and pick a key. The Sort button is on the Gallery, on every folder page and on every tag page. Sidebar views and search results do not have it (see below).

| Key | Sorts by | Default direction |
|---|---|---|
| **Name** | The path inside the library, which within one folder is the file name with its extension | A to Z |
| **Date added** | When Reelio indexed the file | Newest first |
| **Duration** | Length of the video | Longest first |
| **File size** | Size on disk | Largest first |
| **Modified** | The file's last-modified date on disk | Most recent first |
| **Resolution** | Pixel count (width times height) | Highest first |

Picking a key always applies its default direction, even if it is already the active key. To reverse the order, open the menu again and choose **Ascending** or **Descending** below the separator.

Videos whose duration or resolution is unknown are always listed last, in both directions.

{{< note >}}
Name sorting compares characters one by one, it is not "natural" number order: "10.mp4" comes before "2.mp4". Pad numbers with zeros (02, 10) if you want them in counting order.
{{< /note >}}

## One sort for the whole app

There is one sort for all of Reelio. It is saved, survives a restart, and applies to the Gallery, every folder page and every tag page in every tab. Changing it from any of these pages reorders all of them. **Default sort** in [Settings](/docs/settings/) is the same setting as the Sort button.

Sidebar views keep their own order and ignore the sort:

- **Favorites**: alphabetical, folders and videos mixed.
- **Recently played**: most recently played first.
- **Random videos** and **Random folders**: random.
- **Failed thumbnails**: by path, A to Z.

Search results keep the order of the search itself. See [Favorites and quick views](/docs/favorites-and-quick-views/) and [Search](/docs/search/).

## How folders are ordered

Folders are always listed before videos. Their order follows the sort only for three keys:

- **Name**: A to Z or Z to A, following the direction.
- **File size**: by the folder's total size, subfolders included.
- **Duration**: by the folder's total duration, subfolders included.

With **Date added**, **Modified** or **Resolution**, folders stay in A to Z order whatever the direction.

## Choose a view

Click **View** in the toolbar and pick **Extra large**, **Large**, **Medium** or **Details**. The View button is on the Gallery, folder pages, tag pages and all sidebar views. Search results always use Medium tiles.

Reelio remembers the view separately for each place: the Gallery, each folder, each tag and each sidebar view. A second tab showing the same place follows the change. Places you never set use **Default view** from [Settings](/docs/settings/), which is **Medium** unless you change it. Changing the default does not affect pages already open until you leave them.

In the tile views, two vertical videos in a row share one cell. See [Vertical videos](/docs/vertical-videos/).

## The Details view

**Details** shows one row per item under a column header: **Name**, **Duration**, **Size**, **Resolution** and **Modified**. There is no Date added column.

Each video row shows a small thumbnail, the file name, a star after the name if it is a favorite, and a second line with the codec and frame rate. Each folder row shows the folder cover or a folder icon, the number of videos it contains, and its total duration and size. All three count the subfolders too. Resolution and Modified stay blank for folders.

Rows behave like tiles: a single click plays the video or opens the folder, a right-click opens the same menu, and video rows can be dragged onto a tag or into another app (see [Drag into your editor](/docs/drag-into-your-editor/)). Folder rows cannot be dragged.

{{< tip >}}
Click a column header to sort by that column. Click it again to reverse the direction. A chevron on the active column shows the direction (up for ascending, down for descending). This changes the same app-wide sort as the **Sort** button. On sidebar views the header does not sort.
{{< /tip >}}
