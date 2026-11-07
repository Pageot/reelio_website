---
title: "Play random videos and folders from your library"
navTitle: "Favorites and quick views"
description: "Play a random video or open a random folder from your Reelio library in one click, reshuffle with another click, and keep favorites and recently played at hand."
lead: "The sidebar's quick views pick random videos and folders from your whole library, list what you played last, and gather your favorite clips and folders in one place."
level: beginner
verified: "1.3.0.0"
related: [video-player, sort-and-views, tags]
---

## Play a random video

Click **Random videos** in the sidebar. Reelio draws a random selection of videos from all your libraries and shows them as tiles. Click any tile to play it in your video player (see [Video player](/docs/video-player/)).

The number of videos in the draw is set by **Random videos count** in [Settings](/docs/settings/): 50 by default, adjustable from 10 to 200 in steps of 10.

{{< tip >}}
Click **Random videos** again, even while you are already on it, to draw a fresh set. Coming back to the view with Back also draws a new set.
{{< /tip >}}

Random videos always draws from all your libraries, not from the folder you are viewing.

## Open a random folder

Click **Random folders** to see up to 60 folders picked at random from all your libraries, at any depth. Any subfolder that contains at least one indexed video can come up; the libraries' own root folders are left out. Like Random videos, the folders are reshuffled every time you click the entry. Click a folder tile to open it.

The number of random folders is fixed at 60 and cannot be changed.

## Recently played

**Recently played** lists the videos you launched from Reelio, most recent first, across all libraries. A video is added when its player starts successfully, whether you clicked its tile, pressed Enter on it, or Alt+clicked it in a folder mosaic. Opening a folder does not count.

**Recently played count** in [Settings](/docs/settings/) sets how many videos the list shows: 20 by default, from 5 to 100 in steps of 5.

## Favorites

### Add or remove a favorite

Right-click a video or a folder, on a tile or in a Details row, and choose **Add to favorites**. It is the first entry of the menu. On a favorite, the same entry reads **Remove from favorites**. There is no keyboard shortcut for it.

A favorite tile shows a star at its top-right corner. Click the star to remove the favorite: the click does not play the video or open the folder. Tiles that are not favorites show no star, so use the right-click menu to add one. In the Details view, the star sits right after the name and works the same way.

### The Favorites view

Click **Favorites** in the sidebar to see every favorite folder and video from all your libraries in one list. The list is alphabetical by displayed name (the folder name, or the file name without its extension), with folders and videos mixed. It has no Sort button and ignores the app-wide sort, and it updates as soon as you add or remove a favorite.

A favorite folder is listed only while it still contains indexed videos.

## Sort and view in quick views

Quick views keep their own order (alphabetical for Favorites, most recent first for Recently played, random for the random views) and have no Sort button. They do have the **View** button, and each one remembers its own view. See [Sort and views](/docs/sort-and-views/).

## Failed thumbnails

At the bottom of the sidebar, above Settings, a **Failed thumbnails** entry appears only while at least one video has a failed thumbnail. Its badge shows how many, across all libraries. Click it to see those videos and fix them; see [Failed and corrupted thumbnails](/docs/failed-and-corrupted/).
