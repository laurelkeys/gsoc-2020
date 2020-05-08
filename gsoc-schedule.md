# Project Schedule

*Note: the following dates have been changed, as the [GSoC Timeline](https://developers.google.com/open-source/gsoc/timeline) was updated due to COVID-19.*

## Community Bonding *(May 4 to June 1)*
### 1st week (May 4)
   - Discuss with artists on Discord which effects they want the most
   - Study the way multi-threading is accomplished in `GenericFrameRenderer`
### 2nd week (May 11)
  - Continue to contribute with PRs to get more familiar with the codebase
  - Get familiar with the render pipeline
### 3rd week (May 18)
  - Revise the effects added as stretch goals and their order of implementation to take the obtained feedback into consideration
  - Get more familiar with Qt and the render viewer
### 4th week (May 25)
  - Evaluate what's the best approach to adding effects that could benefit from parelization: whether to use multi-threading, or if they could be applied with shaders (as it is done in Blender's EEVEE with GLSL, for example)

## Phase 1 *(June 1 to June 29)*
### 5th week (June 1)
  - Implement Unity's ["Classic"](https://docs.unity3d.com/Packages/com.unity.postprocessing@2.1/manual/Vignette.html) Vignette
  - Parallelize the effect implementation and get feedback from users
### 6th week (June 8)
  - Abstract and generalize multithreading on post-processing stages, without forcing each stage to have to reimplement it
  - Start implementing Bloom
### 7th week (June 15)
  - Continue working on Bloom and check if the results are satisfactory to decide if more post-processing effects should be added or if it's worth it to attempt recreating UE4's ["Bloom Convolution"](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/Bloom/index.html)
  - Validate the concurrent implementation of effects and fix any bugs so that it's merged
### 8th week (June 22)
  - Finish Bloom implementation
  - Create test scenes for Bloom and add documentation for the customizable settings
  - Fix bugs
  - Start Tonemapping implementation

## Phase 2 *(June 29 to July 27)*
### 9th week (June 29)
  - 🏁 GSoC mentor/student evaluations *(June 29 - July 3)*
  - Continue Tonemapping implementation
### 10th week (July 6)
  - Create test scenes for the different tonemap operators added and add documentation
  - Get preset tonemappers merged into appleseed
  - Start implementing Chromatic Aberration
### 11th week (July 13)
  - Add test scenes and documentation to finish CA effect integration
  - Brainstorm the most friendly way to expose post effects on interactive rendering
### 12th week (July 20)
  - Start coding post effects preview on interactive rendering
  - Fix any remaining bugs on the implemented effects that may emerge

## Phase 3 *(July 27 to August 24)*
### 13th week (July 27)
  - 🏁 GSoC mentor/student evaluations *(July 27 - 31)*
  - Create a test suite for the implementation of post effects on paused interactive renders
  - Decide wheter to implement a few more straightforward effects (e.g. saturation and contrast) or to add a few improvements to the render viewer (as discussed in *#feature-requests* with Esteban)
  - Begin final report
### 14th week (August 3)
  - Final polishes (i.e. testing and minor fixes)
  - Bug fixing
  - Compile the generated test scenes to demonstrate the effects of the new post-processing stages, so that they can easily be added in future release notes
### 15th week (August 10)
  - Create a few eye-candy renders that compile the implemented post-processing effects to illustrate the project's result (e.g. [[4]](https://docs.unity3d.com/Packages/com.unity.postprocessing@2.3/manual/index.html))
  - Finalize the project report
### 16th week (August 17)
  - Project wrap-up

## Project Conclusion *(August 24 to September 9)*
### 17th week (August 24)
  - 🏁 GSoC students submit their code, project summaries, and final evaluations of their mentors *(August 24 - 31)*
### 18th week (August 31)
  - 🏁 GSoC mentors review student code samples and determine if the students have successfully completed their project *(August 31 - September 7)*
### 19th week (September 7)
  - 🏁 GSoC results are announced *(September 8)*