---
title: "Color tag video files on Windows"
navTitle: "Tags"
description: "Color tag video files on Windows, MP4 and MKV included: Reelio adds colored tags to videos and folders, then lists every tagged item on one page."
lead: "Give any video or folder one or more colored tags, then click a tag in the sidebar to see everything that carries it, across all your libraries."
level: beginner
verified: "1.3.0.0"
related: [favorites-and-quick-views, sort-and-views, libraries]
---

File Explorer does not offer colored tags for files. Reelio keeps its own tags in its library index, not inside the files, so you can tag an MP4, an MKV or any other format Reelio indexes in the same way, and the video files themselves are never touched. See [Formats and file names](/docs/formats-and-file-names/) for the list of formats.

## Add a tag to a video or folder

Right-click a video or a folder, on a tile or on a row of the **Details** view, and open **Tags**. The submenu lists every tag of all your libraries in alphabetical order, each with its color dot. A check mark shows the tags already on that item. Click a tag to add it. An item can carry several tags.

To create a tag and assign it in one step, click **New tag…** at the bottom of the same submenu, name it, pick a color and click **Create**.

{{< tip >}}
Drag a video tile (or a video row in the Details view) onto a tag in the sidebar. The tag entry highlights and the drag shows **Add tag**: drop to assign the tag. This works for videos only, because folders cannot be dragged. It also works when the video belongs to another library than the one where the tag was first created.
{{< /tip >}}

You can also create a tag without assigning it: in the sidebar, expand **Tags** and click **Add tag…** at the end of the list. After **Create**, Reelio opens the new tag's page, which is empty until you tag something.

## Name and color

The **New tag** dialog has a **Name** field and a **Color** row. Spaces at the start and end of the name are removed, and the **Create** button stays disabled while the name is blank.

For the color, pick one of the 7 preset swatches, or the empty circle on the left for no color (its tooltip reads **No color**). **Custom…** opens a color picker for any other color. A new tag starts with no color. The color shows as a dot next to the tag in the sidebar and in the **Tags** submenu; a tag without a color shows a plain tag icon.

Tag names are unique, whatever the letter case. If you create a tag with a name that already exists, Reelio does not make a second one: it reuses the existing tag (keeping its original spelling), applies the color you picked (if you picked one), and assigns or opens it.

## Remove a tag from an item

Right-click the video or folder, open **Tags** and click the checked tag. The check mark goes away and the tag is removed from that item only.

## Browse a tag

In the sidebar, click **Tags** to expand it. Each tag appears with a count in brackets, for example "B-roll (12)": the number of tagged videos plus tagged folders, across all libraries.

Click a tag to open its page. It shows the tagged folders first, then the tagged videos, from all your libraries, each group in the current sort order. The **Sort** and **View** buttons work as on any folder page (see [Sort and views](/docs/sort-and-views/)).

Only items that carry the tag themselves appear. If you tag a folder, the folder shows up, but the videos inside it are not listed one by one. A tagged folder that no longer contains any indexed video is not shown.

The **Update thumbnails** button on a tag page only reloads the list of tagged items. It does not scan your drives or generate thumbnails; see [Update and regenerate thumbnails](/docs/update-and-regenerate/) for that.

## Rename, recolor or delete a tag

On a tag page, click **Rename** to open the **Rename tag** dialog, filled in with the current name and color. Change either one and click **Rename**. The change applies in every library. Renaming to a name another tag already uses is refused, but changing only the letter case is allowed.

Click **Delete** to remove the tag. Reelio asks **Delete tag?** first, with **Cancel** as the default button. Confirming removes the tag from every video and every folder in all libraries, then takes you back to the Gallery. Your files are not touched.

{{< note >}}
The delete confirmation only mentions videos, but tagged folders lose the tag too.
{{< /note >}}

## Tags across several libraries

If you have several libraries, tags with the same name (whatever the letter case) are treated as one tag: the counts add up, and one page lists the items of all libraries. Creating a tag creates it in every library. When the libraries disagree on the color, the color comes from the first library, in the order shown in Settings, that has one. See [Libraries](/docs/libraries/) to add more libraries.
