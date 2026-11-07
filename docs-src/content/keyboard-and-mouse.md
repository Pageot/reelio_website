---
title: "Reelio keyboard shortcuts and mouse gestures"
navTitle: "Keyboard & mouse"
description: "All Reelio keyboard shortcuts and mouse gestures: tabs, Alt+Up, Ctrl+F search, type-ahead to jump to a video by its first letters, arrow keys and Enter."
lead: "Every shortcut Reelio has, grouped by where you use it, plus the mouse gestures that are easy to miss."
level: advanced
verified: "1.3.0.0"
related: [tabs-and-navigation, search, hover-scrub]
---

## Window shortcuts

These work from anywhere in the main window, but not while a dialog is open.

### Tabs

{{< keys >}}
Ctrl+T | Open a new tab on the Gallery
Ctrl+W or Ctrl+F4 | Close the current tab (closing the last tab closes the window)
Ctrl+Tab | Go to the next tab (from the last tab, back to the first)
Ctrl+Shift+Tab | Go to the previous tab
Ctrl+1 to Ctrl+8 | Go to the tab at that position, counted from the left
Ctrl+9 | Go to the last tab
{{< /keys >}}

Use the digit keys above the letters: Ctrl with a numeric keypad digit does nothing. See [Tabs and navigation](/docs/tabs-and-navigation/).

### Navigation

{{< keys >}}
Alt+Up | Open the parent folder (from a top-level folder, the Gallery)
{{< /keys >}}

Alt+Up works on folder pages, like the **Up** button. Back and Forward have no keyboard shortcut (Alt+Left and Backspace do nothing): use the mouse side buttons.

### Search

{{< keys >}}
Ctrl+F | Put the cursor in the search box and select its text, so typing replaces the old query
Enter | Run the search typed in the box
Up / Down then Enter | Pick a name from the suggestion list
{{< /keys >}}

Enter and the arrow keys do this only while the cursor is in the search box. See [Search](/docs/search/).

## Jump to a video by typing its name

On any page with a grid (the Gallery, folders, search results, tags and the sidebar views), just start typing. Reelio highlights the first item whose name starts with what you typed: the file name without its extension for a video, the folder name for a folder.

{{< tip >}}
Type quickly to spell more of the name: letters typed less than a second apart add up, so "bea" jumps to the first name starting with "bea". After a one-second pause, the next letter starts a new search. Press the same letter again to step to the next item starting with that letter. Then press Enter to play the video or open the folder.
{{< /tip >}}

Case and accents are ignored, and the search wraps around to the top. A character that matches nothing is ignored; spaces inside a name count. Typing works wherever the focus is, except inside a text field such as the search box: letters typed on a grid page never go to the search box, so use Ctrl+F to search.

## Move around the grid with the keyboard

{{< keys >}}
A to Z / 0 to 9 | Jump to the first item whose name starts with what you type
Left / Right | Previous or next item, continuing across row ends (tile views)
Up / Down | Row above or below, in the same column (tile views)
Up / Down | Previous or next row (Details view)
Enter | Play the highlighted video or open the highlighted folder
Esc | Clear the highlight and end the letter search
{{< /keys >}}

The first arrow press highlights the first item visible on screen. Movement stops at the first and last items, and the view scrolls to keep the highlight visible. In the **Details** view, Left and Right do nothing.

The highlight is the same accent ring as a mouse hover. It goes away when you press Esc, click in the grid, leave the page or switch tabs.

Home, End, Page Up, Page Down, Delete, F2, F5 and the Menu key have no Reelio action in the grid.

## Confirmation dialogs

{{< keys >}}
Enter or Esc | Cancel a confirmation dialog, such as **Delete video?**
{{< /keys >}}

The default button is **Cancel**: click the action button to confirm.

## Mouse gestures

| Gesture | What it does | Details |
|---|---|---|
| Click a video or a folder (tile or Details row) | Plays the video, or opens the folder | [Video player](/docs/video-player/) |
| Move the pointer across a video tile | Flips through frames of the video | [Hover-scrub previews](/docs/hover-scrub/) |
| Mouse Back and Forward side buttons | Go back or forward in the current tab | [Tabs and navigation](/docs/tabs-and-navigation/) |
| Hold Alt and click a cell of a folder mosaic | Plays that video without opening the folder (holding Alt while you move highlights the cell first) | [Folder thumbnails](/docs/folder-thumbnails/) |
| Click the star on a favorite | Removes it from favorites (**Remove from favorites**) | [Favorites and quick views](/docs/favorites-and-quick-views/) |
| Click **Random videos** again in the sidebar | Draws a new random selection | [Favorites and quick views](/docs/favorites-and-quick-views/) |
| Drop an image file from File Explorer on a tile | Sets it as the cover (**Set as cover**) | [Video covers](/docs/video-covers/) |
| Drag a video onto a tag in the sidebar | Adds that tag (**Add tag**); folders cannot be dragged | [Tags](/docs/tags/) |
| Drag a video out of Reelio | Drops it as a regular file on File Explorer or another app, such as a video editor | [Drag into your editor](/docs/drag-into-your-editor/) |
| Right-click a video or a folder | Opens its menu (folders have no **Show in folder** and no delete) | [Video player](/docs/video-player/) |
| Right-click a sidebar entry | **Open in new tab** | [Tabs and navigation](/docs/tabs-and-navigation/) |
| Drag a tab left or right | Reorders the tabs | [Tabs and navigation](/docs/tabs-and-navigation/) |
| Click a column header in the Details view | Sorts by that column; click again to reverse | [Sort and views](/docs/sort-and-views/) |
