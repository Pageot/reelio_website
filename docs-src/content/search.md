---
title: "Search video files by name in Reelio"
navTitle: "Search"
description: "Search video files by name across your Reelio libraries on Windows: live results, folder and file suggestions, words in any order, and search within one folder."
lead: "Type a few letters in the search box and Reelio lists the matching folders and videos as you type, across all your libraries or inside the folder you are browsing."
level: beginner
verified: "1.3.0.0"
related: [tabs-and-navigation, sort-and-views, tags]
---

## Start a search

The search box sits at the top of the sidebar, above the Gallery entry, with the placeholder **Search videos**. It finds folders as well as videos.

Type a first letter or digit and the **Search** results page opens in the active tab. Results refresh as you type, so you rarely need to press Enter, although Enter (or the magnifier icon) runs the search too.

Press Ctrl+F from anywhere in the window to put the cursor in the search box. Ctrl+F also selects the text already there, so what you type replaces the old query.

{{< note >}}
Typing letters while you browse a page does not go to the search box: it jumps to the first item whose name starts with those letters. Use Ctrl+F or click the box to search. See [Keyboard and mouse](/docs/keyboard-and-mouse/).
{{< /note >}}

### Suggestions

While you type, a list under the box offers up to 8 names, folders and videos mixed: up to 3 folder names at the top, then video file names (without their extension). Suggestions follow the current scope, described below. Click a suggestion, or pick it with the arrow keys and press Enter, to put that name in the box and run the search.

## How matching works

Reelio splits your query into words and looks for items where every word matches the start of a word in the name, in any order. Spaces and punctuation separate words.

{{< tip >}}
Word order does not matter: "beach sun" finds "Sunny/beach day.mp4". Each word only needs to match the beginning of a word, so "sun" finds "Sunny" but "unny" does not.
{{< /tip >}}

Matching ignores case and accents in both directions: "ete" finds "été", and "été" finds "Ete". A query with no letter or digit at all shows **Type at least one letter or digit.**

## What Reelio searches

A video is matched on its path inside the library: every folder name between the library's root folder and the file, plus the file name and its extension. The name of the library's root folder itself is not searched.

Folders are matched on their own name only. They are listed before the videos, up to 50 folders, followed by up to 200 videos. Click a folder result to open it, like any folder tile.

{{< tip >}}
Because folder names and extensions count, you can type "mp4" to list your .mp4 files, or a folder name to list the videos stored anywhere under that folder. Tags are not searched: to see every video with a tag, click the tag in the sidebar. See [Tags](/docs/tags/).
{{< /tip >}}

Technical details such as codec or resolution are not searched either. Search results always use Medium tiles and have no Sort or View button; see [Sort and views](/docs/sort-and-views/).

## Search inside one folder

When you start a search from a folder page, a **Scope:** row appears above the results with two buttons:

- **Library**: search every library.
- **In &lt;folder name&gt;**: search only that folder and all its subfolders.

The scope folder is the one you were viewing when you started typing. The row is hidden for searches started from the Gallery or anywhere other than a folder page. Clicking the other button runs the current query again with the new scope.

{{< tip >}}
To find a clip in one project, open the project's folder first, then start typing and click **In &lt;folder name&gt;**. Reelio keeps that choice for your next searches.
{{< /tip >}}

Reelio remembers the scope you pick. It is the same setting as **Default search scope** in [Settings](/docs/settings/), with the choices **Whole library** (the default) and **Current folder**. With **Current folder** saved, a search started outside a folder still covers every library.

## Leave a search and come back

A search is a step in the tab's history, like opening a folder. Click a folder result or a sidebar entry and the search ends and the box empties. Press Back later and the results return with your full query and its scope.

Empty the search box while the results are showing (delete the text or use the box's clear button) and the tab goes back to where you started the search, or to the Gallery if there is nowhere to go back to.

Each tab keeps its own search. When you switch tabs, the search box shows that tab's query, or is empty. See [Tabs and navigation](/docs/tabs-and-navigation/).

## Shortcuts

{{< keys >}}
Ctrl+F | Put the cursor in the search box and select its text
Enter | Run the search
Up / Down then Enter | Pick a suggestion from the list
{{< /keys >}}
