---
layout: com301
title: "COM 301: Map Markers Lab"
author:
    - "John Drew"
    - "Matthew X. Curinga"
    - "Suraj Uttamchandani"
sidenav: "com301-nav.html"
---

Week 4 Lab Activities
=====================
To get started on these activities, for [the Adelphi Brooklyn map sandbox](https://codesandbox.io/p/sandbox/smoosh-glade-z6qnp5).


Appetizers
----------
_Everyone should do, or be so confident that you can skip, these exercises._

1. **New `points.js`.** Move some of the points from project 1 to the new
   mapping system introduced this week. Add tooltip tiles to these points.
2. **Plot circles.** Following the map code/video, plot circles with 3 different
   colors and radii on a map.
3. **Borders.** Use the `border-` css properties to make an interesting effect. Bonus, add in the `box-shadow` property.
4. **Images & paths.** Choose an image to be a background in _one_ of your point
   pop-ups. Scale the image to the right size on your computer. Upload it to
   the `img` dir on your web project. Add a css class to your pop-up and
   and edit your `styles.css` to set the background image.


Mains
-----
_Most students should be working through these problems._

5. **Audio upload.** 
    - Record an audio narrative for one of your pop-ups.
    - Make a new folder called `media` in the root of your web project.
    - Upload the as an mp3 audio file (this format is widely supported).
    - Use the `<audio>` tag to create an audio player on one of your pop-ups.
6. **Custom icon.** Find some icon images online. Create **two custom icons**
   in `points.js`. Add them to your map. 
7. **Make an icon.** Create your own icon image and use it on your map. 
8. **Legend.** Add a legend to your map that includes colors and the custom icons
   you created.
9. **Circle properties.** Our `circle` in `points` use the `radius` and `color` properties. 
   There are many other properties that can be set.
   [See the list of options here](https://leafletjs.com/reference.html#path)
   and play around with things like the opacity, changing the border (stroke) color
   from the fill color, using fill or line patterns, etc.

After Dinner
------------
_Try one of these for more of a challenge._

10. **Bar chart.** Use colored `<div>`s to create a bar chart in one of your pop-ups
   that shows the demographics of your school. Hint: horizontal bar charts are a little bit easier.
11. **Icon variations.** Leaflet allows us to create named variations
    of a single icon (the way we have multiple colored circles). This way they all use the
    same size, anchor, etc. [See the tutorial here](https://leafletjs.com/examples/custom-icons/)
    and create a variation of one of your icons. If you create your icon as an SVG
    (in Illustrator or Inkscape), it's easier to change the fill and stroke colors.
12. **Edit `index.html`**. The map is embedded on a regular web page. Edit `index.html`
    to add a header/title, sidebar, or place the map in the context of a longer narrative
    with other images, text, videos, etc (like in the articles we have been looking at).
13. **Hack Leaflet css.** Sometimes we don't have good documentation for the system we're using.
    Since servers send all of their content to our browser, we can use the browser to inspect
    the code to understand how it works. Use your browser's developer tools to "inspect" 
    (try right-clicking) a map pop-up and figure out how to change the css of the pop-up. For 
    example, using the Leaflet CSS class names, you might add styles to your css to override 
    the width, padding, border-radius, background color, or opacity.