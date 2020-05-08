# [New Post-Processing Stages](https://github.com/appleseedhq/appleseed/wiki/List-of-Project-Ideas-for-GSoC-2020#new-post-processing-stages) Project Proposal


## Contact Information

Tiago Chaves
- Email:   [tiagoloureirochaves@gmail.com](mailto:tiagoloureirochaves@gmail.com)
- GitHub:  [laurelkeys](https://github.com/laurelkeys)
- Discord: laurelkeys#6751


## Synopsis

This project aims to equip the post-processing pipeline with a good amount of new artistic effects, to allow users to tweak the overall look and feel of their scenes without having to leave appleseed.

The four main effects which will be added are **Bloom**, **Tonemapping**, **Chromatic Aberration** and **Vignetting**, which do not take place during rendering, but rather, are composited on top of the resulting image.

Post-processing applies full image filters and transformations to the rendered scenes, which can drastically improve their visual quality with little computation time. Currently, this is only possible with final renders in appleseed, however, bringing this feature to paused interactive renders is another goal of this project, as this is a more artist friendly approach to testing different customizable values of effects.



## Benefits

At the end of this project, appleseed will have over 4 new post-processing stages, tripling its current amount, and introducing effects specifically aimed at enriching the artistic quality of renders. The proposed additions are: bloom, tonemapping, chromatic aberration and vignetting; with more effects being implemented as stretch goals (such as bokeh and depth of field).

Besides that, the effects will also be available on interactive rendering (while it is paused), as currently you'd need to configure low sample final renders to quickly test them, which isn't an optimal solution for fast comparisons. With this feature, users will be able to preview the effects of different values for customizable options on top of the same (high quality) render in much shorter time, without the added delay of having to start a new final render for each visualization.

This brings the ability to accelerate project workflow when using appleseed in two ways: **1)** as it enables users to do more of their work inside appleseed itself, without having to resort to other DCC tools to apply treatments to a render; but also **2)** because some common effects can be well performed by fast 2D filters (e.g. bloom/glare, DoF and bokeh) leveraging image processing techniques, with unnoticeable differences when compared to actually simulating camera and lights properties, which take a whole render time to view.


## Deliverables

1. New post-processing stages:
   - **Bloom**
   - **Tonemapping**
   - **Chromatic Aberration**
   - **Vignetting**
   - & more
2. Enable previewing effects when interactive rendering is paused (i.e. after `Ctrl-F5` and `Shift-F5`)
3. Multiple test scenes to show off the new post-processing effects


## Project Details

### Main Goals

1. Implement the following post-processing stages:
   - **Vignetting**
     - Although simple, vignetting is a really commonly used effect. Thus, it could be tackled first, as a way to focus more on the integration of a new post effect in appleseed rather than on the effect implementation itself. That way, further effects integration will be much quicker.
     - An initial implementation has already been proposed (and merged) in [PR#2807](https://github.com/appleseedhq/appleseed/pull/2807), however, it is quite limited (with a single customizable parameter). There are two goals when reimplementing this effect:
       - Add a more complete implementation, as the one [used in Unity's Post-Processing Stack v2](https://docs.unity3d.com/Packages/com.unity.postprocessing@2.3/manual/Vignette.html);
       - Make the implementation multi-threaded, as many other effects can benefit from it.
   - **Bloom**
     - Use a sum of gaussian filters [applied to downsamplings](https://github.com/blender/blender/blob/master/source/blender/draw/engines/eevee/eevee_bloom.c#L216) of the rendered image (such as [Kawase's Bloom](http://developer.amd.com/wordpress/media/2012/10/Oat-ScenePostprocessing.pdf)).
     - There are many different reference implementations for this, but the one used in Blender's EEVEE follows [KinoBloom](https://github.com/keijiro/KinoBloom) (by the same author of the submitted vignette effect).
   - **Tonemapping**
       - One of the benefits of making the vignette implementation multi-threaded is that GLSL code can be easily ported. Thus, adding the 7 tonemap operators from this [ShaderToy](https://www.shadertoy.com/view/WdjSW3) reference could be a good (and fast) starting point, but further modifications and the addition of customization options should be considered after an initial feedback from artists.
   - **Chromatic Aberration** (CA)
       - Provide support for red/blue and green/purple fringing, following [Unity's implementation](https://docs.unity3d.com/Manual/PostProcessing-ChromaticAberration.html) of CA.

2. Make post-processing effects available in paused (`Ctrl-F5`) interactive rendering.


### Stretch Goals

Add more post-processing stages*, such as: **Glare**, **FFT Bloom**\*, **Saturation**, **Contrast** and **Sharpening**. These stages are subject to changes upon discussions with artists using appleseed, to better suit their needs and suggestions.

\* Attempt recreating [UE4's FFT Convolution implementation](https://www.youtube.com/watch?v=SkJgopq-JQA), instead of the classic Sum of Gaussians approach, for increased realism.

**Note:** Color LUTs have been suggested more than once in *#feature-requests* on Discord, however, as explained by Esteban, they should be integrated into the current render viewer's color management system instead of being added as an independent post-processing step. Nevertheless, since it is offered by many non-real time renderers (e.g. Corona, V-Ray, Redshift, Arnold, RenderMan), work could be initiated towards adopting the [Cube specification](https://wwwimages2.adobe.com/content/dam/acom/en/products/speedgrade/cc/pdfs/cube-lut-specification-1.0.pdf) for LUT files, or [OCIO look transforms](https://opencolorio.org/userguide/looks.html), in the final weeks of GSoC if the community finds it more valuable than adding more effects (other than the main four).

### Post-Processing in Other Rendering and Game Engines

As mentioned on Discord, the Corona Renderer offers one of the largest amounts of post effects [[1]](https://corona-renderer.com/features/workflow-tweaks) amongst non-real time renderers. Blender also provides many image processing filters through its Compositing Filter Nodes [[2]](https://docs.blender.org/manual/en/latest/compositing/types/filter/index.html), and in EEVEE's Render Settings [[3]](https://docs.blender.org/manual/en/latest/render/eevee/render_settings/index.html).

Furthermore, both Unity and Unreal Engine (UE4) have post-processing stacks which share many effects in common [[4]](https://docs.unity3d.com/Manual/PostProcessingOverview.html), [[5]](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/index.html).

From the aforementioned examples, the following effects are included in 3 or more of them: bloom, chromatic aberration (CA), depth of field (DoF), tonemapping, screen space ambient occlusion (SSAO) and vignetting. While most non-real time renderers offer some sort of tonemaping and color grading, a few other noteworthy renderers that implement bloom are [LuxCore](https://wiki.luxcorerender.org/ImagePipeline#Effects), [V-Ray](https://docs.chaosgroup.com/display/VRAY3MAX/V-Ray+Frame+Buffer+%7C+VFB) and [Redshift](https://docs.redshift3d.com/display/RSDOCS/PostFX?product=3dsmax).

Thus, besides **bloom** and **tonemapping** which were suggested in the project idea, other effects have been proposed (e.g. **vignetting** and **chromatic aberration**) in an effort to best equip appleseed with a subset from the most common render post-processes.


## Project Schedule

As I am nearing the final stretch of my BSc, I don't have many classes left, so I will have a good amount of time to invest in GSoC. Also, (assuming things don't change because of COVID-19), I won't have any classes in July, so I can work completely on this project.

Here is an overview of the 19 weeks of GSoC's timespan, with more details about each week and an estimate of the project schedule below:

### Community Bonding *(April 27 to May 18)*
#### 1st week (April 27)
   - Discuss with artists on Discord which effects they want the most
   - Study the way multi-threading is accomplished in `GenericFrameRenderer`
#### 2nd week (May 4)
  - Continue to contribute with PRs to get more familiar with the codebase
  - Get familiar with the render pipeline
#### 3rd week (May 4)
  - Revise the effects added as stretch goals and their order of implementation to take the obtained feedback into consideration
  - Get more familiar with Qt and the render viewer
#### 4th week (May 11)
  - Evaluate what's the best approach to adding effects that could benefit from parelization: whether to use multi-threading, or if they could be applied with shaders (as it is done in Blender's EEVEE with GLSL, for example)

### Phase 1 *(May 18 to June 15)*
#### 5th week (May 18)
  - Implement Unity's ["Classic"](https://docs.unity3d.com/Packages/com.unity.postprocessing@2.1/manual/Vignette.html) Vignette
  - Parallelize the effect implementation and get feedback from users
#### 6th week (May 25)
  - Abstract and generalize multithreading on post-processing stages, without forcing each stage to have to reimplement it
  - Start implementing Bloom
#### 7th week (June 1)
  - Continue working on Bloom and check if the results are satisfactory to decide if more post-processing effects should be added or if it's worth it to attempt recreating UE4's ["Bloom Convolution"](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/Bloom/index.html)
  - Validate the concurrent implementation of effects and fix any bugs so that it's merged
#### 8th week (June 8)
  - Finish Bloom implementation
  - Create test scenes for Bloom and add documentation for the customizable settings
  - Fix bugs
  - Start Tonemapping implementation

### Phase 2 *(June 15 to July 13)*
#### 9th week (June 15)
  - 🏁 GSoC mentor/student evaluations *(June 15 - 19)*
  - Continue Tonemapping implementation
#### 10th week (June 22)
  - Create test scenes for the different tonemap operators added and add documentation
  - Get preset tonemappers merged into appleseed
  - Start implementing Chromatic Aberration
#### 11th week (June 29)
  - Add test scenes and documentation to finish CA effect integration
  - Brainstorm the most friendly way to expose post effects on interactive rendering
#### 12th week (July 6)
  - Start coding post effects preview on interactive rendering
  - Fix any remaining bugs on the implemented effects that may emerge

### Phase 3 *(July 13 to August 10)*
#### 13th week (July 13)
  - 🏁 GSoC mentor/student evaluations *(July 13 - 17)*
  - Create a test suite for the implementation of post effects on paused interactive renders
  - Decide wheter to implement a few more straightforward effects (e.g. saturation and contrast) or to add a few improvements to the render viewer (as discussed in *#feature-requests* with Esteban)
  - Begin final report
#### 14th week (July 20)
  - Final polishes (i.e. testing and minor fixes)
  - Bug fixing
  - Compile the generated test scenes to demonstrate the effects of the new post-processing stages, so that they can easily be added in future release notes
#### 15th week (July 27)
  - Create a few eye-candy renders that compile the implemented post-processing effects to illustrate the project's result (e.g. [[4]](https://docs.unity3d.com/Packages/com.unity.postprocessing@2.3/manual/index.html))
  - Finalize the project report
#### 16th week (August 3)
  - Project wrap-up

### Project Conclusion *(August 10 to August 25)*
#### 17th week (August 10)
  - 🏁 GSoC students submit their code, project summaries, and final evaluations of their mentors *(August 10 - 17)*
#### 18th week (August 17)
  - 🏁 GSoC mentors review student code samples and determine if the students have successfully completed their project *(August 17 - 24)*
#### 19th week (August 24)
  - 🏁 GSoC results are announced *(August 25)*


## Bio

Hi! I'm Tiago, a 4th year BSc Computer Engineering student at the [University of Campinas (Unicamp)](https://ic.unicamp.br/en/), in Brazil. I am particularly interested by the intersections of art with technology, so as I progressed in my graduation I have focused more and more on the fields of Image Processing, Artificial Intelligence and Computer Graphics.

I've been programming for 7 years now, using mostly in Python, C and C++ for personal/university projects, and Kotlin and Java professionally. But it was in the last year that I really immersed myself in computer graphics, after finding the work of some amazing people, to name two in particular:
- Peter Shirley, as his ["Ray Tracing in One Weekend" book series](https://raytracing.github.io/) was my first contact with many of the underlyings of renderers, so from then on I've started to research much more about its inner workings.
- [Inigo Quilez](https://www.iquilezles.org/), for the "magic" he accomplishes using math to generate artistic images, and how he's able to intertwine the two topics in a way that is simply fascinating.

I am looking forward to continue to contribute to open source projects after GSoC, and would love to use the opportunity to learn a lot more about appleseed. As mentioned, the list of possible post-processing effects that could be implemented is long, so I chose this particular project as it sets the ground for some exciting further work (such as implementing real-time visualization of effects in interactive rendering 🤗).

> Links to past contributions: issue [#494](https://github.com/appleseedhq/blenderseed/issues/494) and pull requests [#2785](https://github.com/appleseedhq/appleseed/pull/2785), [#2791](https://github.com/appleseedhq/appleseed/pull/2791), [#2806](https://github.com/appleseedhq/appleseed/pull/2806), [#2807](https://github.com/appleseedhq/appleseed/pull/2807).


## References

[Post-Processing in Other Rendering and Game Engines](#post-processing-in-other-rendering-and-game-engines)

- [1] "Extensive Post-Processing, Inside the VFB" — https://corona-renderer.com/features/workflow-tweaks
- [2] "Compositing » Filter Nodes" — https://docs.blender.org/manual/en/latest/compositing/types/filter/index.html
- [3] "Eevee » Render Settings" — https://docs.blender.org/manual/en/latest/render/eevee/render_settings/index.html
- [4] "Post-processing" — https://docs.unity3d.com/Manual/PostProcessingOverview.html
- [5] "Post Process Effects" — https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/index.html


## Implementation References

### Bloom
  - https://github.com/jeremyfix/FFTConvolution
  - https://learnopengl.com/Advanced-Lighting/Bloom
  - https://catlikecoding.com/unity/tutorials/advanced-rendering/bloom/
  - https://natron.readthedocs.io/en/rb-2.3/plugins/net.sf.cimg.CImgBloom.html
  - http://rastergrid.com/blog/2010/09/efficient-gaussian-blur-with-linear-sampling/
  - https://devtalk.blender.org/t/eevee-needs-to-have-physically-based-defaults/4700/9
  - https://github.com/LuxCoreRender/LuxCore/blob/master/src/slg/film/imagepipeline/plugins/bloom.cpp
  - https://software.intel.com/en-us/blogs/2014/07/15/an-investigation-of-fast-real-time-gpu-based-image-blur-algorithms
### Tonemapping
  - https://www.shadertoy.com/view/WdjSW3
  - https://www.shadertoy.com/view/lslGzl
  - https://github.com/johnhable/fw-public
  - https://learnopengl.com/Advanced-Lighting/HDR
  - https://docs.substance3d.com/spdoc/tone-mapping-162005358.html
  - https://mynameismjp.wordpress.com/2010/04/30/a-closer-look-at-tone-mapping/
  - http://filmicworlds.com/blog/filmic-tonemapping-with-piecewise-power-curves/
  - http://advances.realtimerendering.com/other/2016/naughty_dog/NaughtyDog_TechArt_Final.pdf
### Chromatic Aberration
  - https://www.shadertoy.com/view/XssGz8
  - https://www.shadertoy.com/view/MtXXDr
  - https://github.com/keijiro/KinoFringe
### General
  - https://github.com/keijiro/Kino
  - https://github.com/NatronGitHub/Natron
  - https://github.com/crosire/reshade-shaders
  - https://github.com/vanruesc/postprocessing
  - https://github.com/Unity-Technologies/PostProcessing
  - https://github.com/JoachimCoenen/Cat-PostProcessing/
  - https://john-chapman.github.io/2017/11/05/pseudo-lens-flare.html
  - https://mynameismjp.wordpress.com/2011/04/19/bokeh-ii-the-sequel/
  - https://github.com/google/filament/blob/master/shaders/src/dithering.fs
  - https://pixelmischiefblog.wordpress.com/2016/11/25/bokeh-depth-of-field/
  - https://www.adriancourreges.com/blog/2018/12/02/ue4-optimized-post-effects/
  - https://github.com/LuxCoreRender/LuxCore/tree/master/src/slg/film/imagepipeline/plugins
  - Blender's EEVEE and Cycles, as it is an (open-source) industry standard
