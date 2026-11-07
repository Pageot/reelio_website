---
title: "Show reference images with a footage folder"
navTitle: "Image strip (img folder)"
description: "Keep reference images with your footage: put them in an img subfolder and Reelio shows them in a scrolling strip at the top of the folder page."
lead: "Put stills, mood boards or reference shots in a subfolder named img, and Reelio shows them in a scrolling strip at the top of that folder's page."
level: beginner
verified: "1.3.0.0"
related: [folder-thumbnails, formats-and-file-names, update-and-regenerate]
---

## Set it up

1. Inside the folder that holds your footage, create a subfolder named `img`. Use lowercase: other casings work on standard Windows drives, but a NAS share may need the exact lowercase name. Other names, such as `images` or `covers`, are not recognized.
2. Put your images in it, as .jpg, .jpeg, .png or .webp files (any case for the extension). Images in subfolders of `img` are not read.
3. Click **Update thumbnails** in the toolbar, so Reelio notices the new `img` folder.

{{< tip >}}
Reelio detects a new `img` folder during a library scan, so run **Update thumbnails** once after you create it. From then on, Reelio reads the images each time you open the folder: images you add to an existing `img` folder show up on your next visit, with no scan needed.
{{< /tip >}}

The `img` folder must contain at least one supported image for the strip to appear.

## Where the strip appears

The strip sits at the top of the folder's page, above the folder name, and scrolls up and down with the rest of the page. It shows in every view, including **Details**.

{{< note >}}
The library's top-level page (the Gallery) never shows a strip, even if the library folder itself contains an `img` folder. Put `img` in a folder below it.
{{< /note >}}

## Which images, in which order

The strip shows up to 40 images. Reelio sorts them by file name the way File Explorer does: letter case is ignored and numbers compare by value, so `img_2` comes before `img_10`. If the folder holds more than 40 images, only the first 40 in that order appear.

To control the order, number your files, for example `shot_1`, `shot_2`, `shot_10`.

## Browse the strip

When the images are wider than the strip, it scrolls continuously to the left on its own and loops without a visible seam. When all the images fit in the width, the strip stays still, shows each image once and has no arrows.

On a strip that scrolls:

- Point at the strip to pause it. A left and a right arrow appear. Move the pointer away to hide them and resume scrolling from where it stopped.
- Click an arrow to move the strip by its own width. Quick clicks add up, and the strip wraps around endlessly.
- Drag with the mouse (hold the left button and move) to scroll it by hand, in either direction. Releasing after a drag does not open an image. With touch or a pen, the same gesture scrolls the page instead.

On any strip, click an image to open it in the Windows default app for that file type. If no app is set or the file is gone, nothing happens.

## Related shortcuts

{{< keys >}}
Hover | Pause the strip and show its arrows
Click | Open the image in its default Windows app
Drag | Scroll the strip by hand (mouse only)
{{< /keys >}}
