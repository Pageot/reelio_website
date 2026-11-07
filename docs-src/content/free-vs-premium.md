---
title: "Reelio Free vs Premium: the 25-video free limit"
navTitle: "Free vs Premium"
description: "Reelio Free holds up to 25 videos across all libraries. See how the free limit works, what Premium unlocks and how the one-time purchase is restored."
lead: "Reelio Free holds up to 25 videos in total. Premium is a one-time purchase in the Microsoft Store that removes the limit, with no subscription."
level: beginner
verified: "1.3.0.0"
related: [install, libraries, backup-and-move-library]
---

## The 25-video limit

The free version can hold at most 25 videos in total, summed over all your libraries. Only active videos count: videos in excluded folders, in removed libraries, or deleted from Reelio do not.

There is no per-feature paywall: every feature works in the free version, and the limit only decides how many videos Reelio indexes.

{{< note >}}
If one library sits inside another (you added a subfolder of an existing library, or its parent folder), the videos they share are indexed twice and count twice toward the limit. See [Libraries](/docs/libraries/).
{{< /note >}}

## Where to see your count

Reelio shows your count in two places, with different wording:

- In Settings > **Premium**, the **Reelio Free** card shows a counter such as "12 / 25 videos used", a small progress bar and a **Get Premium** button.
- The footer of the Gallery, folder, search, tag and sidebar pages shows a counter such as "Free, 12 / 25 videos", followed by a **Get Premium** link. The counter is hidden while thumbnails are generating, because the footer shows the progress of the batch instead.

## What happens at the limit

### During a scan

When a scan finds more new videos than you have free slots, Reelio fills the remaining slots and leaves the rest out. A **Free limit reached** toast tells you how many videos were not imported. Its **Get Premium** button opens Settings.

The choice is the same on every scan: videos Reelio already knew come back first, then new files, each group in order of their path inside the library. This applies to adding a library, **Update thumbnails**, **Regenerate all thumbnails**, folder rescans and removing an exclusion.

Videos already in your library are never removed. They stay fully usable and are still updated by later scans.

Once you have 25 videos, a banner at the bottom of the Gallery, folder, search, tag and sidebar pages says you have reached the free limit, with a **Get Premium** button.

### When you import a library

Importing a library .zip is all or nothing in the free version. If its videos would take you past 25, the whole import is refused with an **Import failed** toast, and nothing is added. See [Back up and move a library](/docs/backup-and-move-library/).

### Freeing slots

Removing a library, excluding folders or deleting videos lowers the count. The next scan can then import more videos, up to 25.

## Get Premium

The **Get Premium** button in Settings, the footer link and the banner all open the **Reelio Premium** dialog. Click **Get Premium** to open the Microsoft Store purchase window; payment is handled by the Store on your Microsoft account. If the purchase fails or you cancel it, the dialog stays open. **Later** closes it.

Premium is bought once, with no subscription. After a successful purchase, a **Welcome to Reelio Premium** dialog confirms it.

## What changes with Premium

- You can add as many videos as you want, across all your libraries.
- Importing a library .zip has no restriction.
- In Settings, the **Reelio Free** card becomes a **Reelio Premium** card with a check mark.
- The footer counter, its link and the limit banner disappear.

## On another PC or after a reinstall

{{< tip >}}
There is no "restore purchase" button, and you do not need one. At each launch, Reelio asks the Microsoft Store whether the Microsoft account signed in on this PC owns Premium, and unlocks it automatically. The license is also kept on your PC, so Premium keeps working offline.
{{< /tip >}}

## If Premium is no longer found

If the Store reports that you no longer own Premium (after a refund or an account change, for example), Reelio checks again after 5 seconds, then switches back to the free version and shows a **Premium license not found** dialog. **Contact support** opens an email to Reelio's support; **Close** dismisses the dialog.

Videos already in your library stay there and keep working, but adding new ones is again subject to the 25-video limit. Reelio re-checks a license older than 30 days at launch when you are online. Being offline, or getting no clear answer from the Store, never switches you back to Free.
