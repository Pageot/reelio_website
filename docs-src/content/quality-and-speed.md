---
title: "Thumbnail generation slow or using too much CPU"
navTitle: "Quality and speed"
description: "Thumbnail generation slow or CPU usage too high? Pick Eco, Balanced or Fast in Reelio, and set thumbnail quality from Low (224x126) to Ultra (640x360)."
lead: "Two settings decide how Reelio builds thumbnails: Generation speed sets how many videos are processed at the same time, and Quality sets the size of each thumbnail."
level: advanced
verified: "1.3.0.0"
related: [update-and-regenerate, nas-and-external-drives, failed-and-corrupted]
---

Generating a thumbnail means decoding part of each video, so a large first run keeps your processor and your drives busy. If your PC feels slow while thumbnails generate, or the run takes too long on a fast machine, change **Generation speed** in **Settings** > **Thumbnails**. If the thumbnails look soft or take too much disk space, change **Quality** on the same page.

## Generation speed

**Generation speed** has three choices. It sets how many videos Reelio processes at the same time:

| Setting | Videos processed at once |
|---|---|
| **Eco** | 1 |
| **Balanced** (default) | Half your processor threads, at least 2 |
| **Fast** | All your processor threads but one, at least 2 |

The count uses processor threads (Windows calls them logical processors), not physical cores. On a processor with 8 cores and 16 threads, **Balanced** runs 8 videos at once and **Fast** runs 15.

- Pick **Eco** for a library on a NAS or network drive, a very large library, or a laptop on battery.
- Keep **Balanced** if you want to keep working while thumbnails generate.
- Pick **Fast** on a powerful machine with the videos on a fast local SSD.

You can change the speed while thumbnails are generating. It applies at once: the run continues with the videos not done yet at the new speed, the counter keeps going, and a paused run stays paused. During **Regenerate all thumbnails**, only the library being processed restarts, from the videos it has not done yet.

{{< tip >}}
On a laptop running on battery, Reelio processes one video at a time whatever speed you chose. Plug the laptop in and your chosen speed comes back, even in the middle of a run. Your setting is not changed, and nothing on screen shows the switch. PCs without a battery are never affected.
{{< /tip >}}

## The Eco suggestion

Before a generation starts, Reelio may suggest Eco with a notification titled **Thumbnail generation may be heavy**. It can appear when the library is on a network drive (a `\\server\share` path, or a drive letter Windows reports as a network drive), or when more than 5,000 videos are about to be generated. It does not appear when generation already runs one video at a time.

Click **Switch to Eco (recommended)** to save **Eco** as your speed in Settings and restart the current run at one video at a time. Videos that were being processed at that moment are done again; the counter keeps going. The notification closes by itself after 16 seconds. See [NAS and external drives](/docs/nas-and-external-drives/) for libraries stored on a network.

## Thumbnail quality

**Quality** sets the size of the still thumbnail and of each [hover-scrub](/docs/hover-scrub/) frame. All thumbnails are WebP images.

| Quality | Thumbnail | Hover-scrub frames |
|---|---|---|
| **Low** | 224x126 | 128x72 |
| **Medium** | 320x180 | 160x90 |
| **High** (default) | 480x270 | 256x144 |
| **Ultra** | 640x360 | 320x180 |

Higher levels look sharper on high-resolution screens and take more disk space. **Ultra** uses the same compression as **High**, at a larger size.

When you pick another quality, Reelio asks **Regenerate thumbnails now?**, because existing thumbnails keep their old size until they are rebuilt (the question is skipped while **Regenerate all thumbnails** is already running). **Regenerate** starts [Regenerate all thumbnails](/docs/update-and-regenerate/) right away, without a second confirmation. **Later** keeps the new setting for thumbnails generated from now on. Changing the quality does not restart a generation that is already running.

## No black bands

Each thumbnail is scaled to fill its whole box and cropped from the center, so Reelio never adds black bands around a video. Landscape and square videos get a 16:9 thumbnail. Portrait videos get the same box turned to 9:16 (270x480 at **High**), so they keep a vertical thumbnail. See [Vertical videos](/docs/vertical-videos/).

## Hardware-accelerated decoding

In **Settings** > **Advanced**, expand **Power-user settings** to find **Hardware-accelerated decoding**. It is on by default. H.264, HEVC, VP9 and AV1 videos are then decoded on the graphics card; other codecs always decode on the processor.

If decoding on the graphics card fails for a video, Reelio tries that video once more on the processor automatically. After 3 such failures in the same run, the rest of the run skips the graphics card. If some videos still fail to generate, turn the switch off: every video is then decoded on the processor.

## Order and time limit

Videos are generated in the order the Gallery shows them, videos in subfolders first, so thumbnails fill the grid from top to bottom. Each video gets at most 5 minutes; a video that takes longer is marked as failed, and is not retried on the processor. See [Failed and corrupted thumbnails](/docs/failed-and-corrupted/).
