# Weekly To-Dos

 - [Community Bonding *(May 4 to June 1)*](#community-bonding-may-4-to-june-1)
 - [Phase 1 *(June 1 to June 29)*](#phase-1-june-1-to-june-29)
 - [Phase 2 *(June 29 to July 27)*](#phase-2-june-29-to-july-27) 👈
 - [Phase 3 *(July 27 to August 24)*](#phase-3-july-27-to-august-24)
 - [Project Conclusion *(August 24 to September 9)*](#project-conclusion-august-24-to-september-9)

## Community Bonding *(May 4 to June 1)*
### 1st week (May 4)
  - [x] Setup a repository to organize documents related to GSoC
  - [x] Look into how [`foundation/utility/job`](https://github.com/appleseedhq/appleseed/tree/master/src/appleseed/foundation/utility/job) and [`GenericFrameRenderer`](https://github.com/appleseedhq/appleseed/tree/master/src/appleseed/renderer/kernel/rendering/generic) work
  - [x] Read through GSoC emails and complete any tasks required by Google
  - [x] Schedule a meeting with Kevin to work out the best channel for communication, time zones, any initial feedback on the project proposal, etc.
  - [x] Create a new `.md` listing the main [implementation references](gsoc-proposal.md#Implementation-References) for each effect, as well as the settings/properties/features available for them

### 2nd week (May 11)
  - [x] Refactoring of the Vignette effect implementation (*branch:* [`postfx-jobs`](https://github.com/laurelkeys/appleseed/tree/postfx-jobs), *PR:* [#2865](https://github.com/appleseedhq/appleseed/pull/2865))
  - [x] Explore Nuke's [C++ API](https://learn.foundry.com/nuke/developers/121/ndkreference/)
  - [ ] Read the [OpenFX programming guide](https://openfx.readthedocs.io/en/master/)

### 3rd week (May 18)
  - [x] Add Vignette test scenes
  - [x] Setup environment for quickly testing rendered images
  - [x] Fix bugs in Vignette refactoring (*branch:* [`postfx-jobs`](https://github.com/laurelkeys/appleseed/tree/postfx-jobs), *PR:* [#2865](https://github.com/appleseedhq/appleseed/pull/2865))
  - [x] Biweekly meeting

### 4th week (May 25)
  - [x] Start working on the Bloom effect (*branch:* [`bloom/unopt`](https://github.com/laurelkeys/appleseed/tree/bloom/unopt))

## Phase 1 *(June 1 to June 29)*
### 5th week (June 1)
  - [x] Create test scenes for Bloom (*branch:* [`bloom/unopt`](https://github.com/laurelkeys/appleseed/tree/bloom/unopt))
  - [x] Improve Bloom performance (replaced [Kawase](http://www.daionet.gr.jp/~masa/archives/GDC2003_DSTEAL.ppt) bloom with [KinoBloom](https://github.com/keijiro/KinoBloom))

### 6th week (June 8)
  - [x] Fix image artifacts in Bloom (*branch:* [`bloom/unopt`](https://github.com/laurelkeys/appleseed/tree/bloom/unopt))
  - [x] Decide which blurring method is going to be used
  - [x] Start wrapping up Bloom (*first draft PR:* [#2872](https://github.com/appleseedhq/appleseed/pull/2872))
  - [x] Create scripts for quickly generating and rendering test scenes

### 7th week (June 15)
  - [x] Simplify multithreaded effect appliers (*PR:* [#2865](https://github.com/appleseedhq/appleseed/pull/2865))
  - [x] Add profiling (*branch:* [`bloom/opt`](https://github.com/laurelkeys/appleseed/tree/bloom/opt))
  - [x] Improve Bloom performance (more than halved stage time)
  - [x] Biweekly meeting
  - [x] Merge Vignette refactoring (*PR:* [#2865](https://github.com/appleseedhq/appleseed/pull/2865))

### 8th week (June 22)
  - [x] Update Bloom test scenes
  - [x] Finish implementing Bloom (*branch:* [`bloom/opt`](https://github.com/laurelkeys/appleseed/tree/bloom/opt))
  - [x] Submit Bloom (*PR:* [#2875](https://github.com/appleseedhq/appleseed/pull/2875))

## Phase 2 *(June 29 to July 27)*
### 9th week (June 29)
  - 🏁 GSoC mentor/student evaluations *(June 29 - July 3)*
  - [x] Fix false colors being applied twice (*PR:* [#2877](https://github.com/appleseedhq/appleseed/pull/2877))
  - [x] Fix false colors bug with final render (*PR:* [#2880](https://github.com/appleseedhq/appleseed/pull/2880))
  - [x] Preview post-processing effects when rendering is stopped (*branch:* [`fxs/preview`](https://github.com/laurelkeys/appleseed/tree/fxs/preview))
  - [x] Start Tone Mapping implementation (*branch:* [`tonemap`](https://github.com/laurelkeys/appleseed/tree/tonemap))

### 10th week (July 6) 👈
  - [ ] Continue Tone Mapping implementation (*branch:* [`tonemap`](https://github.com/laurelkeys/appleseed/tree/tonemap))
  - [ ] Read more on tone mapping / HDRi / gamma / color management / etc.
  - [x] Biweekly meeting

### 11th week (July 13)
### 12th week (July 20)

## Phase 3 *(July 27 to August 24)*

## Project Conclusion *(August 24 to September 9)*
