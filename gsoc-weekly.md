# Weekly To-Dos

 - [Community Bonding *(May 4 to June 1)*](#community-bonding-may-4-to-june-1)
 - [Phase 1 *(June 1 to June 29)*](#phase-1-june-1-to-june-29)
 - [Phase 2 *(June 29 to July 27)*](#phase-2-june-29-to-july-27)
 - [Phase 3 *(July 27 to August 24)*](#phase-3-july-27-to-august-24) 👈
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

### 10th week (July 6)
  - [x] Continue Tone Mapping implementation (*bra  nch:* [`tonemap`](https://github.com/laurelkeys/appleseed/tree/tonemap))
  - [x] Read more on tone mapping / HDRi / gamma / color management / etc.
  - [x] Biweekly meeting
  - [x] Address the first reviews of Bloom (*PR:* [#2875](https://github.com/appleseedhq/appleseed/pull/2875))
  - [x] Further explain the two bugs found in `.studio` (*PRs:* [#2877](https://github.com/appleseedhq/appleseed/pull/2877), [#2880](https://github.com/appleseedhq/appleseed/pull/2880))

### 11th week (July 13)
  - [x] Create a post on the [appleseed Users Forum](https://forum.appleseedhq.net/) about Bloom ([*link here*](https://forum.appleseedhq.net/t/bloom-as-a-new-post-processing-effect/1027/2))
  - [x] Update Bloom after more reviews (*PR:* [#2875](https://github.com/appleseedhq/appleseed/pull/2875))
  - [x] Continue work on Tone Mapping (*branch:* [`tonemap`](https://github.com/laurelkeys/appleseed/tree/tonemap))
  - [ ] Create test scenes for Tone Mapping

### 12th week (July 20)
  - [x] Wrap up Tone Mapping to focus on creating a PR (*branch:* [`tonemap`](https://github.com/laurelkeys/appleseed/tree/tonemap))
  - [x] Share a new "test build" with Tone Mapping

## Phase 3 *(July 27 to August 24)*
### 13th week (July 27)
  - 🏁 GSoC mentor/student evaluations *(July 27 - 31)*
  - [x] Biweekly meeting
  - [x] Create a PR for Tone Mapping (*PR:* [#2884](https://github.com/appleseedhq/appleseed/pull/2884))
  - [x] Work on improving the user experience when testing post-processing stages (*branch:* [`fxs/reload`](https://github.com/laurelkeys/appleseed/tree/fxs/reload))

### 14th week (August 3)
  - [x] Preview effects as their parameters are changed in `.studio` (*PR:* [`#2885`](https://github.com/appleseedhq/appleseed/pull/2885))
  - [x] Start implementing Chromatic Aberration (*branch:* [`chromatic-aberration`](https://github.com/laurelkeys/appleseed/tree/chromatic-aberration))

### 15th week (August 10)
  - [x] Add test scenes and documentation to Chromatic Aberration (*branch:* [`chromatic-aberration`](https://github.com/laurelkeys/appleseed/tree/chromatic-aberration))
  - [x] Finish implementing Chromatic Aberration (*PR:* [`#2887`](https://github.com/appleseedhq/appleseed/pull/2887))
  - [x] Final polishes (i.e. testing and minor fixes)
  - [x] Work on the final project report

### 16th week (August 17) 👈
  - [x] Final polishes (i.e. testing and minor fixes)
  - [x] Work on the final project report
  - [ ] Create an "eye-candy" scene

## Project Conclusion *(August 24 to September 9)*
### Final week (August 24)
  - 🏁 GSoC students submit their code, project summaries, and final evaluations of their mentors *(August 24 - 31)*
  - [ ] Submit the final evaluation
  - [ ] Submit the final report

### Conclusion
  - 🏁 GSoC mentors review student code samples and determine if the students have successfully completed their project *(August 31 - September 7)*
  - 🏁 GSoC results are announced *(September 8)*