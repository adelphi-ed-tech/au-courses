---
layout: com301
title: "COM 301: Week 6"
author:
- "John Drew"
- "Matthew X. Curinga"
- "Suraj Uttamchandani"
sidenav: "com301-nav.html"
---

Week 6: Case Study III: Climate Change
======================================


<h2><i class="bi bi-book text-primary"></i> Seminar: Monday, Feb 26</h2>

**Goals:**

- Discuss the role of maps, visualizations, 

### Readings due:
- Popovich, N., Rojanasakul, M., & Plumer, B. (2022, December 13).
  [The Climate Impact of Your Neighborhood, Mapped](https://www.nytimes.com/interactive/2022/12/13/climate/climate-footprint-map-neighborhood.html). _The New York Times_. 
- Andreoni, M. (2024, January 9). [A New Era in Global Heat](https://www.nytimes.com/2024/01/09/climate/a-new-era-in-global-heat.html). _The New York Times_.


- - - -

<h2><i class="bi bi-filetype-html text-primary"></i> Lab: Wednesday, Feb 29</h2>

**Goals:**

- learn how to use custom web fonts
- use the "inspect" tool in the browser to debug and modify code
- use ChatGPT to learn HTML, CSS, etc
- create a Pinterest board for your final project

**Agenda**

1. Editing `index.html` (adding fonts, using chat-gpt for animations)
2. Using the inspector
3. Programming lab (work on your project)
4. [Pinterest](https://pinterest.com) and project ideation
   1. Create an account on pinterest
   2. Create a board with one of your ideas for the final project
   3. Add 3 pins to the board that are related to your idea
      - they are _about_ the topic
      - they _inspire_ your design

**Resources**

0. [Example Code: Brooklyn Map Revised](https://codesandbox.io/p/sandbox/adelphi-brooklyn-revised-msswsn?file=%2Findex.html%3A40%2C8)
1. [MDN Web Fonts](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts)
2. [CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations)


### Quick Guide: using a custom font
[See this in action on codesandbox](https://codesandbox.io/p/sandbox/adelphi-brooklyn-revised-msswsn)

1. Download a free font from dafont, google fonts, font squirrel, etc
2. Unzip the .zip folder on your computer (e.g. your Downloads folder)
3. Create a `fonts` folder on your web proejct
4. Upload the font file (.otf, .ttf, etc -- there are many font types) to your fonts folder by dragging it from your computer into the `fonts` folder. Just the font file, not the .zip file.
5. Create a new file in the fonts folder called `fonts.css`
6. In `fonts.css` add the following code. The property `font-family` is the name you will use in your CSS to call the font. The `src` is the path to the font file. In my example, I'm using _superchage_ as the font name.
```css
   @font-face {
     font-family: 'supercharge';
     src: url('supercharge.ttf');
   }
``` 
7. In your `index.html` file, link to the `fonts.css` file in the head of the document. 
```html
   <link rel="stylesheet" href="/fonts/fonts.css">
```
8. Use the new font in your `styles.css` file. For example, this code changes the
   title in the legend.
```css
.Legend h3 {
  font-family: "supercharge";
  text-align: center;
  font-weight: bold;
}
```

