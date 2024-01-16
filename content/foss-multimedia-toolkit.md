---
layout: syllabus
title: "FOSS Multimedia Toolkit"
author: ""
---

FOSS Multimedia Toolkit
=======================
For many years I have used GNU/Linux computers as my main/sole computers. I mostly stay in the [Debian](https://www.debian.org/)/[Ubuntu](https://ubuntu.com/) line of distros because they are well documented and well supported. Lately I have been using [Pop!_OS](https://pop.system76.com/) on a lot of my computers. I started using Linux because I was aligned with the [freedom message](https://fsfe.org/freesoftware/) and it was the best platform for software development, especially if your software was going to run on a Linux server. For a while now, though, it's been a great general purpose desktop platform that's easy to maintain and trouble shoot, especially as a lot of "work" has migrated to web-based platforms (Chrome runs fine on Linux, if you're wondering).

As I'm teaching the [2023 Multimedia Studio on Generative AI](https://adelphi-ed-tech.github.io/au-courses/multimedia-studio.html), I've decided to put together this list of tools that I use for multimedia production. I'm not a professional multimedia producer -- I'm a profession researcher of how people learn from multimedia and other software systems. So, I don't warrant that this is the best or definitive list by any means.


Screenshots
-----------
Of all of the tools and techniques on this list, I put making screenshots at the top. Like most people, I use screenshots daily -- from my phone and computer(s). A lot of the other multimedia here begins with a screenshot. If you can help it at all, please don't send me photos of your computer screen. Take a screen shot! 

Since [Mozilla added screenshots to Firefox](https://support.mozilla.org/en-US/kb/take-screenshots-firefox), I use Firefox for most of my screenshot taking. It's quick, copies to the clipboard, and automatically clips to the underlying HTML elements.

If I need a shot outside of Firefox, I use [Flameshot](https://flameshot.org/) which has most of the features you want (delays, annotations, etc).

[Peek](https://github.com/phw/peek) enables quick screen recordings that you can save (among other formats) as animated GIFs. I use Peek when I want to show something that requires short, simple steps (like a menu option).

Occasionally, there has been a task where I want to automate screenshots. For this, I write a simple `bash` or `python` script that uses the command line tool, [scrot](https://www.tecmint.com/take-screenshots-in-linux-using-scrot/).

Editing Photos
--------------
[GIMP](https://www.gimp.org/) is the FOSS image editor, an [alternative to Photoshop](https://alternativeto.net/software/adobe-photoshop/). This is a go-to application for me and always finds a spot on my launcher. I mostly use it to scale and crop photos, add transparency to images, or [crop thumbnails into a circle](https://www.gimp.org/tutorials/CircleImage/). If I care about a photo (I'm going to print it or put it up online or use it in a presentation), I will do post processing and color correction in GIMP. I'll also use it to remove something from an image, "shop" someone into a photo, etc. I only recently learned about how awesome the stamping tool can be.

When I need to automate or batch image manipulation, [Image Magick](https://imagemagick.org/) is usually where I turn first. ([Released in 1987](https://en.wikipedia.org/wiki/ImageMagick)) it's been available on every linux machine I've ever used. I would probably be better served by becoming more expert in [Python image processing](https://pythongeeks.org/image-processing-in-python/), so maybe I'll chart my progress in a separate post.

- [GIMP Tutorials](https://www.gimp.org/tutorials/)
- [LinkedIn Learning GIMP](https://www.linkedin.com/learning/search?keywords=gimp&u=56671577)

Screen Recording
----------------
It's fair to say that I teach computer programming online via screen recordings, and for the past several years I have relied on [OBS: Open Broadcaster Studio](https://obsproject.com). OBS is full featured, allowing me to easily switch scenes between a full screen recording, a "talking head" recording from my webcam, or a picture-in-picture with me in the corner (at various sizes). The dual-monitor support makes it particularly nice to use. Less important for me, but essential for others, it supports live streaming. It's configuration seems a little tricky at first, but it's worth the effort.

Video Editing
-------------
For other people, video editing might be first on the list. I don't happen to incorporate a lot of live action in my multimedia teaching. If I were teaching cooking or microelectronics, my workflow would be very different and my first tool would be the video editor. Still, every multimedia author needs to have a solid grasp of a good video editor. For me, this has been an area where the FOSS ecosystem falls short. I have tried pretty much every [FOSS editor](https://itsfoss.com/open-source-video-editors/) and have spent particular time with OpenShot, Flowblade, and Kdenlive. Of these, I have had the most success with OpenShot, however in my experience these editors have been unstable and/or missing key features such as precise editing while being able to see audio waves. For the past couple of years, I have settled on the non-free [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/edit). The free beer version has been stable and has all of the features that I need.

While sometimes I can do a short OBS screen cast in one shot and post it directly, I usually post process a video in a video editor. At the very least, I like to take out dead space, add and add a title at the start. If it's "important" I will:

- edit together several short screen recordings
- reduce dead space, add transitions, and/or speed up the video in segments where I'm typing and not speaking (if you're typing a lot of code or demonstrating some other aspect of software, remember to keep quiet so that you can edit it later)
- separate the audio and do noise reduction in Audacity
- add sound/music to signal transitions and focus attention
- add titles and text annotations
- add still images (sometimes with labels) that I will discuss
- mix in other videos (and add narration or text/image glosses)

Vector Graphics
---------------
[Vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) are small and scale without any loss. They are great for creating illustrations and working with text. If you need to, you can also mix in raster graphics (e.g. photos). I use vector drawing programs to create diagrams, info graphics, or for any work that requires a lot of text and images (because working with text in GIMP isn't great).

[Inkscape](https://inkscape.org/) is the FOSS alternative to Adobe Illustrator and like GIMP, it's a very full featured, stable program. Recently, I have been using it a lot to "trace" aspects of images to create a hand drawn effect. Everyone should know the basics of drawing with curves, putting text on a path, and working with gradients (this also goes for your image editor).

If my document requires paragraphs of text or is more of a flow diagram than an illustration, I will do the text in [LibreOffice Draw](https://www.libreoffice.org/discover/draw/) (or for flow diagrams, the entire drawing in LibreOffice).

Audio Editing
-------------
Making a podcast? Can't stop saying "um"? Have a fan in the background? Want to mix some beats together? Of all of the software on this list, [Audacity](https://www.audacityteam.org/) is the one that I think is better for most people than any paid, proprietary competitor. I use Audacity directly to record audio if I don't need video, to quickly transcode an audio file (e.g .wav to .mp3), for the great noise reduction filter, and to equalize different audio tracks. Install Audacity -- it's easy to learn and invaluable once you are accustomed to it.

Where's Blender?
----------------
[Blender](https://www.blender.org/) is a heavy hitter in the FOSS multimedia world. Unfortunately, my Blender skills are negligible, so it's not very useful _to me._ Blender lets you create 3D models, animations, VFX, motion graphics, etc. I would like to learn it to, at least, make simple 2D animations. Maybe next year.

foo