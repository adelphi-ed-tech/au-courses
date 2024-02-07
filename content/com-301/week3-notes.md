---
layout: com301
title: "COM 301: Map Point Notes"
author:
    - "John Drew"
    - "Matthew X. Curinga"
    - "Suraj Uttamchandani"
sidenav: "com301-nav.html"
---

Notes: Map Points & CSS
=======================

Adding a Marker to the map
-----------------------------
1. Create a new "HTML snippet" in the ``points`` folder on your website. Either copy an existing example or create a new .html file with the following template:
    ```html
    <div class="MapPoint" data-lat="40.7128" data-lon="-74.0060">
        <h2>New York City</h2>
        <p>Here is a description of New York City</p>
    </div>
    ```
2. Look up the longitude and latitude on Google Maps or other mapping software. Copy the coordinates into the `data-lat` and `data-lon` attributes.
3. Include the marker in the map by editing `config.js`:
   add the name of the new snippet file (without the path or .html extension)
   to the ``points`` array.

Naming Things
-------------
Naming things is actually an important part of computer programming. There are formal rules that govern what things can be named, but it's also important to
use consistent names that describe what the thing is.

Things we will be naming:

- html files
- css files
- images and other media
- css classes
- (later) JavaScript variables and functions

General guidelines for naming things for our projects:

- start names with a letter
- don't put any spaces in names -- use an underscore `_` or use "camelCase" 
- assume everything is case sensitive (so `myFile.html` is different from `MyFile.html`)
- specifically for css classes:
  - use camelCase (not underscores between words)
  - start the class with a capital letter if it describes a specific element like `MapPoint`
  - start the class with a lowercase letter if it describes a general style like `pageHeader` or `fancyBorder`

CSS Selectors
-------------
CSS selectors are used to match HTML elements to styles
that control their appearance.

**Tag based selectors:** match all elements of a given type (_all_ the links, headers, etc)
```css
p {
    color: red;
}
```
This makes the text of all paragraphs `<p>` red.

**Class based selectors:** match all elements with a given class. `class` is an html attribute of all tags.
```css
.MapPoint {
    background-color: lavender;
}
```
This makes the background of all elements with the class `MapPoint` lavender. Your HTML would look like this:
```html
<div class="MapPoint" data-lat="40.7128" data-lon="-74.0060">
    <h2>New York City</h2>
    <p>Here is a description of New York City</p>
</div>
```

- **id based selectors:** match a single element with a given id
    ```css
    #pageHeader {
        background-color: lightblue;
    }
    ```
    This makes the background of the element with the id `myElement` light blue.
    ```html
    <header class="pageHeader" data-lat="40.7128" data-lon="-74.0060">
        <h1>Home Page</h1>
        <p>Header description</p>
    </header>
    ```
    In our code, we will not use many id based selectors for CSS. We will use them for JavaScript to identify a specific element on the page.
- **combining selectors:** you can combine selectors to match elements that have both a tag and a class, or a tag and an id.
    ```css
    .MapPoint h1 {
        color: blue;
    }
    ```
    This will make the text for all `<h1>` tags _inside_ a `.MapPoint` class blue. `<h1>` tags outside of `.MapPoint` will not be affected.

Box Model
---------
It's useful to think of every HTML tag as a "box" on the page, even though we cannot see the borders of that box. This is how the web browser arranges the elements. Today we are concerned primarily with two types of boxes: block-level and inline-level. Block boxes take up the whole line. Inline boxes shrink to the size of the content they contain and can be arranged side by side. Box model is controlled by the `display` property in CSS, but all elements have a default display property. For example, the headers (h1..h6)
and containers (div, section, main, etc.) are block-level by default. Span, img, and a (`<a>`) are inline-level by default.

### width and height:
you can set the width and height of a box in CSS. This is useful for making sure that your boxes are the right size.
```css
.MapPoint {
    width: 200px;
    height: 200px;
}
```
This will make all `.MapPoint` boxes 200 pixels wide and 200 pixels tall. When measuring things in CSS we can use exact measurements with pixels, or relative measurements. Relative measurements are useful because they can change size based on the size of the screen or the size of the text. For example, you can use percentages, or the `em` unit. `em` is a unit of measurement that is based on the size of the text. If you set the `font-size` of the body to 16px, then 1em is 16px. If you set the `font-size` of the body to 20px, then 1em is 20px. This is useful for making sure that your boxes are the right size no matter what size the text is.

**percentage:** e.g. ``width: 50%`` will make the box half the width of its container (not necessarily the whole screen)

**min and max**: in addition to `width` and `height` you can specify the minimum and maximum size of a box. This is useful for making sure that your boxes are the right size no matter what size the screen is.
```css

.MapPoint {
    min-width: 100px;
    max-width: 300px;
}
``` 
This will make sure that the `.MapPoint` boxes are at least 100 pixels wide, and at most 300 pixels wide. If the screen is smaller than 100 pixels, the box will be 100 pixels wide (and scroll). If the screen is larger than 300 pixels, the box will be 300 pixels wide. If the screen is between 100 and 300 pixels, the box will be the size of the screen.

### margin and padding
The margin is the space between boxes. You can set the margin on all sides with the `margin` property, or specifically set the margin on one side with `margin-top`, `margin-bottom`, `margin-left`, and `margin-right`.
    ```css
    h1 {
        margin: 10px;
    }
    h2 {
        margin-top: 20px;
        margin-bottom: 10px;
    }
    ```
**padding:** padding refers to the space between the box and its inner content. Padding works just like margin.

### borders

Boxes have borders that you can set to a specific width, color, and style. You can also specify rounded corners with the `border-radius` property. [Read the docs to see how border works.](https://developer.mozilla.org/en-US/docs/Web/CSS/border)

**centering blocks with margin:** you can center a block-level element by setting the left and right margin to `auto`. This will make the box take up the whole width of the screen, and center it. This is useful for making sure that your boxes are the right size no matter what size the screen is.
```css
.MapPoint {
    width: 200px;
    margin: 0 auto;
}
```
This will make all `.MapPoint` boxes 200 pixels wide and centered on the screen. If the screen is smaller than 200 pixels, the box will be 200 pixels wide (and scroll). If the screen is larger than 200 pixels, the box will be 200 pixels wide and centered. _If you don't specify the `width` of your block level element, it will not appear centered because it will take up the whole screen._ For more advanced centering and layout
there is a very flexible system called ["flexbox"](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox).

Backgrounds
-----------
Each box can have its own background.  It's easy to
set a colored background. This CSS makes a black
background with white text:
```css
.MapPoint h1 {
    background-color: black;
    color: white;
}
```

You can also use an image as a background. This
is a little bit trickier because you need to know the "path" to the image. For now, we will assume
that you put the image in the same folder on your
website that has your .css stylesheet. In this example, the image is called "campus.png":
```css
.MapPoint {
    background-image: url('campus.png');
}
```

Note that background images automatically "repeat". There are
many different ways to control the background image in CSS. You can control the size, position, and repetition of the image. [Read the docs to see how background works.](https://developer.mozilla.org/en-US/docs/Web/CSS/background).

`background-repeat: no-repeat;` disables repeating. `background-size: cover;` makes the image cover the whole box. `background-size: fit;` makes the image fit inside the container.

If you want a background for just one of your
MapPoints, you can add a new class to your HTML
like this: `<div class="MapPoint campus" data-lat="40.7128" data-lon="-74.0060">`. Then you can set the background for just that class in your CSS:
```css
.MapPoint .campus {
    background-image: url('campus.png');
    background-size: cover;
}
``` 
