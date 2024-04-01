---
layout: com301
title: "COM 301: Week 6"
author:
- "John Drew"
- "Matthew X. Curinga"
- "Suraj Uttamchandani"
sidenav: "com301-nav.html"
---

Week 11: Choropleth Maps
========================
A [choropleth map](https://infogram.com/blog/what-is-a-choropleth-map/) uses colors to show statistical differences
between regions on a map. Building on the geojson shapes we used last
last week, we will consider if choropleths can be useful in your project.


Goals:
------
- Understand when, why, and how to use choropleth maps
- Consider choropleths relevant to your final project
- Design a choropeth that _might_ be useful for your final project

Agenda:
-------
1. What is a choropleth map?
2. Explore choropleths (below)
3. Choropleth census data example
4. Group work/studio

Activity:
---------
1. With your team, find some choropleths that are related to your project:
   either that contain relevant data or demonstrate a relevant design.
2. Pin (at least) 3 of these examples to your Pinterest board
3. Sketch or create a written description of a choropleth that would be related to your project. **You do not need to use this in your final project, it is just an activity to encourage you to consider a choropleth.**

Resources
----------
1. [What is a Choropleth Map?](https://infogram.com/blog/what-is-a-choropleth-map/)
2. [Python Shapes(last week)](https://colab.research.google.com/drive/1SZb02DmN6V8OGQYH2YQuvp1P5Oq3xlep?usp=sharing)
2. [Python Census Choropleth](https://colab.research.google.com/drive/1w6qHdedpXXnxPWNoYu4qGoR3edApD_Hy?usp=sharing)
3. [Color maps](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choropleth Cheat Sheet
----------------------
The basic steps to making a choropleth.

1. Prepare a geojson file with the shapes of the regions you want to color.
2. Make sure that data has a numerical field (column) that will tell you what color
   to shade the region.
3. (Optional) if the field doesn't exist, open your data in Google Colab and either merge or
   calculate the field.
4. Using Python (Colab), add a new column/field to your geojson called "color" using one of the standard
   color maps. (See example code). Remember, for Leaflet, we want our colors to be hex codes.
5. Save your updated geojson file. Download it.
6. Add the geojson to your Leaflet project. Use a `style function` to shade the regions based on the
   "color" column of your data. (See example code).
