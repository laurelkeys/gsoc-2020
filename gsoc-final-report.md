# Google Summer of Code 2020 - appleseed - Final Report

## New Post-Processing Stages
This year I was really excited to have been selected by [appleseed](https://appleseedhq.net/) – an open source rendering engine designed for animation and visual effects – to participate in [Google Summer of Code 2020](https://summerofcode.withgoogle.com/projects/#5361208732942336) (GSoC).

[My project focused on](https://github.com/laurelkeys/gsoc-2020/blob/master/gsoc-proposal.md#synopsis) extending appleseed's stack of post-processing stages – which previously consisted of only two: a Render Stamp, to add text information, and a Color Map stage for visualizing relative luminance – with a good number of high-quality post-processing effects, aimed towards artists. Post effects are image filters and transforms frequently used by artists to make their renders more realistic or stylized.

I set out to implement four new image effects as post-processing stages – [Vignette](https://en.wikipedia.org/wiki/Vignetting), [Bloom](https://en.wikipedia.org/wiki/Bloom_(shader_effect)), [Tone Map](https://en.wikipedia.org/wiki/Tone_mapping), and [Chromatic Aberration](https://en.wikipedia.org/wiki/Chromatic_aberration) – alongside improvements to [appleseed.studio](https://appleseedhq.net/docs/appleseed.studio.html), appleseed's standalone GUI lookdev application.

For further details, you can check out my [original proposal](gsoc-gsoc-proposal.md), as well as my [weekly progress reports](gsoc-weekly.md).

![](misc/images/finalreport/studio%20interactive%20preview%20demo.gif)
*Showcase of the interactive preview of effect changes, inside appleseed.studio*

## Summary
Pior to the beginning of GSoC, I started working on some small issues to get to know the project, and interacting with the community made me excited to work on appleseed. This led to my first notable contribution at the end of March, [introducing a new vignette effect](https://github.com/appleseedhq/appleseed/pull/2807) (although the implementation was quite straight-forward and not optimized).

| Original [Coffe Maker](https://benedikt-bitterli.me/resources/) scene | Moderate vignetting | Intense vignetting |
| :---: | :---: | :---: |
| ![](misc/images/finalreport/vignette%20(none)%20-%20coffee.png) | ![](misc/images/finalreport/vignette%20(moderate)%20-%20coffee.png) | ![](misc/images/finalreport/vignette%20(intense)%20-%20coffee.png) |

Since I had already made some contributions to appleseed, during the [Community Bonding period](https://google.github.io/gsocguides/student/how-gsoc-works) I focused on writing a [new abstraction layer for post-processing stages](https://github.com/appleseedhq/appleseed/pull/2865), on top of which I would refactor the vignette effect I had implemented, and also build the new, more complex, effects.

My aim with it was twofold:

1. To make it really simple to separate the actual *effect algorithm* – i.e. what / how to process the image – from its execution schedule, and from exposing parameters to the user

2. To seamlessly handle concurrency – for effects that allow it – by leaveraging appleseed's job system to run the effect on smaller portions of the image, in parallel, given the number of available threads.

I successfully finished it at the end of May, and after some really insightful suggestions from [François Beaune](https://github.com/dictoon) and [Kevin Mason](https://github.com/oktomus) to improve its simplicity, we [got it merged in early June](https://github.com/appleseedhq/appleseed/pull/2865).

Thereon, I implemented the remaining effects using this "[compression layer](https://caseymuratori.com/blog_0015)" I created, starting with [bloom](https://github.com/appleseedhq/appleseed/pull/2875) – which was the most challenging one, and required a lot of testing, comparisons between different implementation trade-offs, and profiling (all of which you can [read more about on a post I made to the appleseed Users Forum](https://forum.appleseedhq.net/t/bloom-as-a-new-post-processing-effect/1027)) – and then, moving on to [tone mapping](https://github.com/appleseedhq/appleseed/pull/2884) and [chromatic aberration](https://github.com/appleseedhq/appleseed/pull/2887).

![](misc/images/finalreport/bloom%20-%20as%20sphere.png)
*Rendering with (bottom-left) and without (top-right) the bloom effect*

Along the way, I also came across [some](https://github.com/appleseedhq/appleseed/pull/2877) [bugs](https://github.com/appleseedhq/appleseed/pull/2880) on appleseed.studio – while testing the post effects – and worked on [enhancing effects preview to improve the user experience](https://github.com/appleseedhq/appleseed/pull/2885) (which was only possible after a rendering finished, adding delays to the artistic process of iteratively testing changes).

These changes, however, are still pending review. Though, once a new release of appleseed ships with these brand-new effects, artists should be able to quickly preview what their scenes would look like in post – without having to leave appleseed.studio – and to easily tweak stage parameters while seeing the changes they make live.

## The Code

### Overview

> 🟣 *Merged:* [#2791](https://github.com/appleseedhq/appleseed/pull/2791)\*, [#2785](https://github.com/appleseedhq/appleseed/pull/2785)\*, [#2807](https://github.com/appleseedhq/appleseed/pull/2807)\*, [#2806](https://github.com/appleseedhq/appleseed/pull/2806)\*, [#2855](https://github.com/appleseedhq/appleseed/pull/2855)\*, [#2865](https://github.com/appleseedhq/appleseed/pull/2865)
>
> 🟢 *Open:* [#2875](https://github.com/appleseedhq/appleseed/pull/2875), [#2877](https://github.com/appleseedhq/appleseed/pull/2877), [#2880](https://github.com/appleseedhq/appleseed/pull/2880), [#2884](https://github.com/appleseedhq/appleseed/pull/2884), [#2887](https://github.com/appleseedhq/appleseed/pull/2887)
>
> ⚫ *Draft:* [#2885](https://github.com/appleseedhq/appleseed/pull/2885)
>
> \* contributions before the official GSoC start date

<details>
<summary>Full Pull Requests Timeline (<i>click to expand</i>)</summary>
<ul>
    <li>March*</li>
    <ul>
        <li>[🟣 <a href="https://github.com/appleseedhq/appleseed/pull/2791">#2791</a>] Add Google AI's Turbo rainbow colormap</li>
        <li>[🟣 <a href="https://github.com/appleseedhq/appleseed/pull/2785">#2785</a>] Tile highlights are now colored</li>
        <li>[🟣 <a href="https://github.com/appleseedhq/appleseed/pull/2807">#2807</a>] Add Vignette post-processing stage</li>
        <li>[🟣 <a href="https://github.com/appleseedhq/appleseed/pull/2806">#2806</a>] Ignore incandescence color in black-body mode</li>
    </ul>
    <li>April*</li>
    <ul>
        <li>[🟣 <a href="https://github.com/appleseedhq/appleseed/pull/2855">#2855</a>] Fix double slider regression</li>
    </ul>
    <li>June</li>
    <ul>
        <li>[🟣 <a href="https://github.com/appleseedhq/appleseed/pull/2865">#2865</a>] Refactor the vignette post-processing stage</li>
        <li>[🟢 <a href="https://github.com/appleseedhq/appleseed/pull/2875">#2875</a>] Add Bloom post-processing stage</li>
        <li>[🟢 <a href="https://github.com/appleseedhq/appleseed/pull/2877">#2877</a>] Fix Shift+F5 causing False Colors to be applied twice</li>
    </ul>
    <li>July</li>
    <ul>
        <li>[🟢 <a href="https://github.com/appleseedhq/appleseed/pull/2880">#2880</a>] Fix false colors not being applied to all tiles on a final render</li>
        <li>[🟢 <a href="https://github.com/appleseedhq/appleseed/pull/2884">#2884</a>] Add Tone Map post-processing stage</li>
    </ul>
    <li>August</li>
    <ul>
        <li>[⚫ <a href="https://github.com/appleseedhq/appleseed/pull/2885">#2885</a>] Preview post-processing stage changes in appleseed.studio</li>
        <li>[🟢 <a href="https://github.com/appleseedhq/appleseed/pull/2887">#2887</a>] Add Chromatic Aberration post-processing stage</li>
    </ul>
</ul>
</details>

### Results

As mentioned, the vignette effect is already [merged into master](https://github.com/appleseedhq/appleseed/commit/229d8ea9d40147eddadf8bc60e604ab5b54743c2) (together with its improved implementation, which takes advantage of multi-threading).

[Bloom](https://github.com/appleseedhq/appleseed/pull/2875) and two fixes to appleseed.studio I made ([#2877](https://github.com/appleseedhq/appleseed/pull/2877), [#2880](https://github.com/appleseedhq/appleseed/pull/2880)) have already received a first, overall, review.

Unfortunately, development around appleseed has slowed down a bit after the pandemic, so the pull requests for [tone mapping](https://github.com/appleseedhq/appleseed/pull/2884) and [chromatic aberration](https://github.com/appleseedhq/appleseed/pull/2887) have not yet started to be reviewed.

Hence, my changes for interactively updating appleseed.studio's viewport as effect parameters are modified – and previewing how the complete stack of post rendering stages make the render look like, when a rendering is paused / stopped – are still in [draft](https://github.com/appleseedhq/appleseed/pull/2885), since getting the user experience right first requires users to experience the effects, so it should still undergo changes as other effects get merged into master.

![](misc/images/finalreport/tone%20map%20-%20starship%20(shrinked).png)
*Modified [Spaceship](https://benedikt-bitterli.me/resources/) scene, with details showing the original (left) and tone mapped images (right, with decreasing exposure values)*

## Future Work

As pretty much everything in software, there are always ways in which things could be improved.

Below I list my three picks for "cherries on the cake" that could follow up on the work that has been done:

### 1. GPU accelerated effects
One of the main ways we can improve the creative process for artists is to provide an [immediate connection](https://www.youtube.com/watch?v=EGqwXt90ZqA&feature=youtu.be&t=105) with what they are creating.

Therefore, by running the effects on the GPU we can get huge speed boosts, which would enable them to be previewed in real-time on [interactive rendering](https://vimeo.com/127622613). The simplest way to do this would probably be to convert the effects to GLSL code – what should be straight-forward, given the logical division made to run them in parallel – another thing that might be worth looking into is [Halide](https://halide-lang.org/), a DSL on top of C++ for high-performance image processing.

### 2. Extended tone mapping
Tone mapping is an often requested effect – since physically-based renderings work in High Dynamic Range ([HDR](https://en.wikipedia.org/wiki/High-dynamic-range_imaging)), but most monitors can only display RGB values on the [0, 255] range, so we need to map the HDR color values into this Low Dynamic Range (LDR).

Here are some ways of making it even more useful inside appleseed.studio, decreasing the need for third-party DCC tools:
* Add tone curves for real cameras, as well as "user-defined looks", with [LUT](https://www.studiobinder.com/blog/what-is-lut/)s
* Include a plotting widget in appleseed.studio's `Attribute Editor` for visualizing the tone mapping operator curve, and previewing changes to it
* Let the user choose between tone mapping:
  * Only luminance values (available for [Reinhard curves](https://www.cs.utah.edu/~reinhard/cdrom/tonemap.pdf))
  * Each RGB channel separately (default for all other operators)
  * Operating with [`max(R, G, B)`](https://gpuopen.com/learn/optimized-reversible-tonemapper-for-resolve/) or `average(R, G, B)` values

![](misc/images/finalreport/tone%20map%20-%20comparison.gif)
*Tone mapping operators comparison (on [The Breakfast Room](https://benedikt-bitterli.me/resources/) scene)*

### 3. UX (miscellaneous) improvements
Keeping with the theme of fluidity and ease of use, here are some ideas to improve the user experience when experimenting with post effects in appleseed.studio:
* Allow previewing effects in downsized scales (for faster processing and greater responsiveness)
* Choose to toggle multiple post-processing stages on/off when a rendering isn't running
* Give the option of saving (unfinished) renderings with the previewed effects
* Add hints when the mouse is over stage settings, explaining what they do
* Store effects in a separate layer, for non-destructive editing

![](misc/images/finalreport/studio%20ui%20(shrinked).png)
*appleseed.studio `Attribute Editor`, used for changing post-processing stage parameters*

## Conclusion & Final Words

I learned a lot during GSoC, not only technically, but also in the ways of approaching challenging problems, communicating ideas and deciding when to shift focus. I am super thrilled to see everything I worked on for the past few months be included in a future release, and hope to continue contributing to appleseed.

I would like to say a **huge thank you** to the community around appleseed, as there are so many knowledgeable people who have always been super kind, and helped me a lot.

Lastly, a special thank you to my mentor, [Kevin Masson](https://github.com/oktomus), for the many advices, and for pushing me to not be afraid to *do the hard things first*. This is something I will take with me going forward.

