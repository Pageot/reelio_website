---
title: "Reelio tabs, history and navigation shortcuts"
navTitle: "Tabs and navigation"
description: "Work in several Reelio tabs at once: open, close and reorder tabs, jump with Ctrl+1 to Ctrl+9, go back with mouse side buttons and up a folder with Alt+Up."
lead: "Each Reelio tab is a separate place in your library with its own history. Open as many as you need, switch between them from the keyboard, and move up and down your folders without losing your way."
level: beginner
verified: "1.3.0.0"
related: [search, keyboard-and-mouse, favorites-and-quick-views]
---

## Open, close and switch tabs

The tabs sit in the window's title bar. Click the + button at the end of the tab strip, or press Ctrl+T from anywhere in the window, to open a new tab. It appears at the right end of the strip, becomes the active tab and opens on the Gallery.

Every tab has a close (x) button. Ctrl+W and Ctrl+F4 close the active tab. When you close the active tab, the tab to its left becomes active. Closing the last remaining tab closes the Reelio window, like in a web browser.

Ctrl+Tab moves to the next tab and Ctrl+Shift+Tab to the previous one. Both wrap around: next from the last tab goes back to the first.

To reorder tabs, drag one left or right within the strip. A tab cannot be dragged out of the strip into a new window.

{{< tip >}}
Press Ctrl+1 to Ctrl+8 to jump straight to the tab at that position, counted from the left. Ctrl+9 always goes to the last tab, however many you have open. Use the digit keys on the top row of the keyboard: the numeric keypad does not work for these.
{{< /tip >}}

## Open a sidebar entry in a new tab

Right-click an entry in the sidebar and choose **Open in new tab**. The destination opens in a new tab at the right end of the strip. This works on **Gallery**, **Random videos**, **Random folders**, **Recently played**, **Favorites**, each individual tag under **Tags**, **Failed thumbnails** (when it is shown) and **Settings**. It is not offered on the **Tags** group header or on **Add tag…**, and video and folder tiles have no such entry.

Sidebar clicks, folder clicks and searches always act on the active tab only.

## Tabs are not saved between sessions

Reelio always starts with a single Gallery tab: open tabs are not restored. The one exception is when Reelio restarts itself from [Settings](/docs/settings/), for instance after you move the thumbnail cache or the settings file. It then reopens with one tab, on the page the active tab was showing. If that page was a search, it opens on the Gallery instead.

## Back and Forward

Each tab keeps its own history. Back returns to the previous page of the active tab, and Forward takes you again to a page you went back from. If you go back and then open a different page, the pages you could have gone forward to are dropped, as in a web browser.

{{< tip >}}
The Back and Forward side buttons of your mouse work anywhere in the main window, even with the pointer over a tile. A side-button press over a tile never plays the video or opens the folder, so you can use them freely while browsing.
{{< /tip >}}

There is no keyboard shortcut for Back and Forward: Alt+Left, Alt+Right and Backspace do not go back or forward.

## Go up one folder

The **Up** button sits right of the Forward button. On a folder page it opens the parent folder in the same tab; from a top-level folder it opens the Gallery. It is disabled on every other page (Gallery, search results, sidebar views, tags and Settings).

Up is different from Back: it follows the folder tree, not your history. If you reached a folder from a search, a tag or a random view, Back returns to that search or view, while Up opens the folder that contains the one you are in.

{{< tip >}}
Alt+Up does the same as the **Up** button, as in File Explorer. It only acts on a folder page.
{{< /tip >}}

## The breadcrumb

Right of the Back, Forward and Up buttons, the breadcrumb shows where the active tab is. On a folder page it starts with **Gallery**, followed by one segment for each folder of the path inside the library (the library's own root folder is not shown). Click a folder segment to open that folder in the same tab, or click **Gallery** to go back to the Gallery.

On any other page, the breadcrumb simply names the page, for example **Settings** or **Tag: &lt;name&gt;**, and clicking it does nothing.

## Shortcuts

These shortcuts work from anywhere in the main window, but not while a dialog is open. For the full list, see [Keyboard and mouse](/docs/keyboard-and-mouse/).

{{< keys >}}
Ctrl+T | Open a new tab on the Gallery
Ctrl+W or Ctrl+F4 | Close the current tab
Ctrl+Tab | Go to the next tab
Ctrl+Shift+Tab | Go to the previous tab
Ctrl+1 to Ctrl+8 | Go to the tab at that position
Ctrl+9 | Go to the last tab
Alt+Up | Open the parent folder
Mouse_Back_button | Go back in the current tab
Mouse_Forward_button | Go forward in the current tab
{{< /keys >}}
