---
layout: design
title: "Intro to Programming"
author:
    - "Matthew X. Curinga"
syllabus_footer: true
header-img: img/programming-carto.png
header-img-alt: "code and a map visual of a demographic map of new york city"
---

<!--
This syllabus was created for
the Educational Technology Program
at Adelphi University:
http://education.adelphi.edu
copyright 2012-2019 Matthew X. Curinga
http://matt.curinga.com
This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send
a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
We ask, but do not require, that attribution includes a link to our websites (above).
version: 3.1
Based on work available here: https://github.com/mcuringa/adelphi-ed-tech-courses
-->

<h1 class="PageTitle text-center">Introduction to Computer Programming:<br>Python Maps</h1>

<blockquote class="border-start border-4 border-start border-dark-subtle ps-2 fs-3 mb-4">
We are looking at a society increasingly dependent on machines, yet
decreasingly capable of making or even using them effectively.<br>
― Douglas Rushkoff, <i>Program or Be Programmed: Ten Commands for a Digital Age</i>
</blockquote>


<div class="row">
<div class="col-md-6">
{% md %}
**Computer Science 0145-602, Fall 2024**

site: {{site.url}}
base: {{base.url}}

**Keywords:**  computer programming, CS1, python, computational thinking, 
critical computational literacy, maps, data visualization

**Description:** This course introduces students to programming and
some core concepts of computer science, using a modern, object oriented
programming language. Students learn concepts of
variables, functions, selection, repetition/loops, basic data structures
(arrays, lists, hashtables), and basic object oriented programming.
{% endmd %}
</div>
<div class="col-md-6">
{% md %}
**Class meetings:** Online, asynchronous (coordinated through the course website)

**Instructor**

* [Matthew X. Curinga](http://matt.curinga.com), <mcuringa@adelphi.edu>

**Dr. Curinga's Office Hours by appointment**

* Wednesday, 4:30-5:30PM

{% endmd %}
</div>
</div>


<div class="row">
<div class="col-md-6">
{% md %}

Learning Goals
==============

* understand the types of problems that can be solved using computational techniques
* understand the basic concepts of computation (CPU, RAM, permanent storage, GUIs, file systems, network connections)
* learn core computer programming concepts (abstraction, variables, conditions, functions, repetition, recursion)
* think algorithmically to design and test computer programs
* master the basic syntax and idioms of the Python programming language
* use technical documentation, APIs, and the internet to learn new technical concepts
* develop step-by-step problem solving and debugging practices

Required Software/Online Accounts
=================================
1. [Google Colab](https://colab.research.google.com/). This is a 
   free, online programming environment which you will access through your Adelphi email.
2. [Join our Slack](https://auedtech.slack.com/) with your mail.adelphi.edu email.
   - install the desktop client so that you can easily share code and screenshots
   - install the mobile client so that you can stay tuned for messages about the class
   - join the `#code` channel for discussions related to this class
   - DM the instructor at `@mxc` to get in touch
3. [Chat GPT](https://chat.openai.com/). Since it's release, I have used ChatGPT as a 
   resource for my own software development projects. I think it will be very beneficial 
   for you, too. Create an account at <https://chat.openai.com/auth/login> to get started. 
   You can use your AU email, but that's not required.
4. **Screenshot software.** To get help, you might need to share a screenshot (more often you will 
   copy-paste code or error messages). Don't take pictures of your laptop with you phone. 
   Take a screenshot. If you need help setting this up or getting recommendations, ask on `#code`
   on slack.

Required Books
===============
_None. All course readings, videos, etc will be provided online._

{% endmd %}
</div>
<div class="col-md-6">
{% md %}
References
==========
**Programming references**

1. [Python Documentation](https://docs.python.org/3/): official documentation for the Python programming language
2. [Pandas Documentation](https://pandas.pydata.org/docs/): the Pandas data analysis library
3. [Matplotlib Documentation](https://matplotlib.org/stable/contents.html): we'll use Matplotlib for plots and graphs
4. [Seaborn Documentation](https://seaborn.pydata.org/): Seaborn gives us more control of the appearance of our charts
5. [GeoPandas Documentation](https://geopandas.org/): we'll use GeoPandas to read geospatial data and make maps
6. [Plotly Documentation](https://plotly.com/python/): we'll use Plotly to make interactive charts and graphs
7. [Folium Documentation](https://python-visualization.github.io/folium/): Folium controls some of the map features in GeoPandas
8. [HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML): we'll need a little bit of HTML for our legends and pop-ups
9. [Named HTML colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)

**Other documentation**

1. [Slack Help Center](https://slack.com/help)
2. [Google Colab Help](https://colab.research.google.com/notebooks/intro.ipynb)
3. [ChatGPT Documentation](https://beta.openai.com/docs/)
4. [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)
5. [Markdown in Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html): learn how to use Markdown in Jupyter Notebooks

**Tutorials for basic or advanced topics**

1. [Python Essential Training](https://www.linkedin.com/learning/python-essential-training-2)
2. [Pandas Essential Training](https://www.linkedin.com/learning/pandas-essential-training-24082178/)
3. [Khan Academy: descriptive statistics](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)
4. [Python Statistics Basic Training](https://www.linkedin.com/learning/python-statistics-essential-training-19258005)

{% endmd %}
</div>
</div>

Generative AI / ChatGPT Policy
==============================
Since the introduction of GPT-3, programmers have been using
generative AI as an integral part of their work. Some are
predicting [the end of programming](https://cacm.acm.org/opinion/the-end-of-programming/),
but I think it's just another iteration in the tools that computer scientists and software
engineers have at their disposal to create software more quickly and efficiently.
In particular, it can help us learn new things and reduce the risk of trying
something new.

The general rule for this course is that **generative AI can be used for learning**,
but it is a violation of Adelphi's academic honesty policy and
**considered cheating** if you submit work that was generated by AI as your own.

Specifically:

- lab exercises cannot be written by AI 
  (i.e. if you upload the question to ChatGPT and then post its answer, you will risk receiving 0 points)
- you may always ask it about the API, to produce examples (e.g., _show me how to make a bar graph in `Matplotlib_`)
- you may submit your code to AI for suggestions, feedback, and debugging
- you can use AI as a companion in your project code, either to write "routine" code, 
  or help do something new (e.g., _how can I make a map with a legend in `GeoPandas`?_)
- if you incorporate significant AI code in your project, you must document it in comments
  and be prepared to explain it in your final presentation

Please note: it is not that hard for me to spot code you didn't 
write (whether from a friend, AI, a "cheating" website, etc).


Assignments and Grading
=======================

<div class="row">
<div class="col-md-6">
{% md %}

| Assignment         | Points |
|--------------------|--------|
| Labs (10 total)    | 30     |
| Midterm project    | 25     |
| Final project      | 25     |
| Participation      | 20     |

### Participation (15%)

You will complete three self-evaluations of your participation in the course
by completing a Google Form. Your self-eval will be averaged with the instructor's
evaluation at the end of the semester.

Because this is a self-evaluation, you will have to set your own criteria for
how you evaluate your participation. Here are some things that I will be looking
for:

- do you set aside time to work on the course each week?
- do you complete labs on time?
- do you ask for help when you are stuck?
- do you help others on slack or over email?
- do you share your work, relevant ideas, and resources?
- do you find time to study or work with other students?
- do you complete assignments on time?
- **do not** abandon your teammates
- do not turn in work written by AI or other students

### Labs (50%)

There will be 10 programming "labs" during the course of the semester.
Each lab will provide a few challenges based on the goals and examples
of the week. You will

- _0 points_: for not turning in any work
- _1-2 points_: for a basic attempt, but code isn't working or has fundamental flaws
- _3 points_: solution works and demonstrates mastery of relevant concepts

Some labs may have bonus problems. You should always try to do the
bonus problems. They are focused more on problems solving and
core "CS" concepts than the project-based exercises. If you submit
a nice bonus solution, you may earn an extra point towards your lab
score (but the total can't exceed 30 points).

Labs are due by midnight on Tuesday of the week they are assigned. To turn
in your lab:

1. Save a copy of the weekly lab to your Colab.
2. Rename it with your last name and the lab number, e.g. `curinga-lab1.ipynb`
3. Share the document with the instructor <mcuringa@adelphi.edu>
{% endmd %}
</div>

<div class="col-md-6">
{% md %}

### Midterm: census data analysis (25%)

The midterm will be a pair project that you complete **with your assigned partner**
(see [the roster](https://docs.google.com/spreadsheets/d/1vlRZEpIeROtgi_jB3PX2tyfch1QHsqLYVY_48jEz3H4/edit?usp=sharing)).

For this project you will create your own analysis of the US Census
data that we have been working with. You will investigate a question
that you think can be explored with the data available to us, and
you will use the methods of statistical and spatial analysis to
create a report that includes python code, written analysis,
interactive maps, data tables, and graphs.

Specifically, your Colab Notebook must have:

- all of the code used to create your analysis
- an introduction, headers, written discussion as markdown blocks
- at least one interactive map with points and pop-ups
- at least one table of data
- at least one graph or chart
- markdown text blocks that provide a narrative analysis of the data
  and relevant descriptions of the methods

<h4 class="linkable">Project evaluation criteria</h4>

1. **Content/question:** is the question interesting and important?
   Does the data help us understand it in a new way? Is it analyzed
   in a compelling way?
2. **Programming:** is the code well written and efficient?
   Does it demonstrate mastery of the concepts covered in the course to this point?
   Specifically, you should use variable to make your program more flexible and
   easier to read. Variables should be well named. You shouldn't have any unused 
   code, commented out code, or redundant statements.
3. **Risk:** does the project take a risk? Does it try to do something new or
   different? Low-risk projects very closely resemble the examples and labs;
   high-risk projects try to do something new or different, even if it doesn't
   work exactly right.
4. **Visualization & presentation:** is the map easy to read and easy to use? Can
   the user use the map to explore the data? Is the text edited (no typos, clear prose)?
   Is text formatted in HTML and markdown as needed? Are data tables well formatted
   and have appropriate column headers? Are the charts and graphs selected a good match
   for the data presented? Does the project make good use of color and size to convey
   quantitative information?

_Both team members will receive the same grade for the project. This means
that both members should be prepared to explain any aspect of the project
during the instructor meeting and to demonstrate their ability to write
new code._

### Final project (25%)
The final project will follow the same format as the midterm project,
except everyone will work alone and turn in their own work. The final
can use either census data (from the first half of the term) or school
data from the second half of the term. You must also integrate at least
one data source that is not provided by the instructor.

_The final project will be evaluated on the [same criteria as the midterm](#project_evaluation_criteria)._

{% endmd %}
</div>
</div>

Class Sessions
==============
We're going to operate this async course on a Wednesday to Wednesday schedule.
That means that each Wednesday, will start a new module, and the lab
for that week will be due by end of day on the following Tuesday.
Modules will generally start with an audio introduction to the materials
and a link to a Google Colab notebook. The notebook will contain
all links to all other readings and videos, as well as sample code
and lab exercises.

| Week | Date         | Topic                      | Due (end of week)     |
|------|--------------|----------------------------|-----------------------|
| 1    | 08/28 - 09/03| Data(frames) & Variables   | Lab 1                 |
| 2    | 09/04 - 09/10| Data and tables            | Lab 2                 |
| 3    | 09/11 - 09/17| Mapping points             | Lab 3 |
| 4    | 09/18 - 09/24| Formatting map points      | Lab 4, Eval 1         |
| 5    | 09/25 - 10/01| Merging and grouping data  | Lab 5                 |
| 6    | 10/02 - 10/08| Charts & Graphs            | Lab 6                 |
| 7    | 10/09 - 10/15| Project 1 Studio           | _project work_        |
| 8    | 10/16 - 10/22| Midterm meetings           | Project 1             |
| 9    | 10/23 - 10/29| Exploring data             | Lab 7, Eval 2         |
| 10   | 10/30 - 11/05| Mapping shapes             | Lab 8                 |
| 11   | 11/06 - 11/12| Open                       | Lab 9                 |
| 12   | 11/13 - 11/19| Open                       | Lab 10                |
| 13   | 11/20 - 11/26| Open                       | _project work_        |
| 14   | 11/27 - 12/03| Final project studio       | _project work_        |
| 15   | 12/04 - 12/10| Beta testing               | _project work_        |
| 16   | 12/11 - 12/17| Final meetings             | Final Project, Eval 3 |


Weekly Modules
==============

<div class="row">
<div class="col-md-6">
{% md %}

Module 1: Data(frames) & Variables
----------------------------------
This week we want to get up and running with the
tools of the class and the basics of writing code in
Python and Colab.

**Listen to the Welcome Message:**
<audio controls>
    <source src="audio/csc-602/week1.mp3">
</audio>



[**Lab 1**](https://colab.research.google.com/drive/1Sq15myWHj3Q8etcuK7tMx-TK_ewVObH3) (due Tuesday)

**Goals:**

- install Slack
- run code in Colab
- review syllabus and course expectations
- view results/output
- use variables to store data
- use basic operators to make calculations
- explore data in a `pandas` `DataFrame`

**Topics:**

- baic syntax
- using Jupiter notebooks and Colab
- introduction to DataFrames and pandas

**Do:**
                                  
- Listen to the Welcome Message (above) 
- [Join our Slack](https://auedtech.slack.com/)
- Post on the `#code` channel in Slack:
  - your name
  - area of study
  - why you are taking this course and programming background (if any)
- share lab 1 with the instructor


Module 2: Data and tables
----------------------------------

This week we're going to look at how to manipulate data 
in a `DataFrame` and how to format it in tables. We
will continue working with census data regarding
populations in urban areas.


[**Lab 2**](#colab link)

**Goals:**

- use comparison operators to filter data
- use math operators to calculate new columns
- format data to make more readable tables
- gain a deeper understanding of how variables and data work
  in Jupyter Notebook / Colab

**Topics:**

- calculate new columns in a `DataFrame` with math operators
- `.copy()` a `DataFrame`
- display a sub-selection of columns in a table
- filter/query a `DataFrame` to find specific rows
- work with String data to improve table display
- change column names
- calculate basic statistics (sum, mean, etc) on columns

**Do:**

- Post on the `#code` channel in Slack:
  - a screenshot of a table your created in Colab
  - an interesting "finding" from your analysis of the data
- share lab 2 with the instructor


Module 3: Mapping points
------------------------

We're going to start working with geospatial data
and maps this week. Specifically, we will look at
how to create maps of our US City census data.

[**Lab 3**](#colab link)

**Goals:**

- understand core concepts of geospatial data
- create a map of points
- create mouse-over titles and pop-ups for points
- create a map of points with different colors
- create a map of points with different sizes

**Topics:**


**Do:**

- **choose a partner for the midterm project (aka project 1)**

Module 4: Formatting map points
-------------------------------

We're going to continue mapping points, but this
week we will learn more details about creating
the themes of our "base layer" maps, mapping
multiple sets of points onto a single map, and
creating more complex pop-ups with formatting.

[**Lab 4**](#colab link) (due Tuesday)

**Goals:**

- understand core concepts of geospatial data
- create a map of points
- write **functions** to use with `.apply()`
  - create mouse-over titles and pop-ups for points
  - create a map of points with different colors
  - create a map of points with different sizes

**Topics:**

**Do:**

Module 5: Merging and grouping data
-----------------------------------

We're going to start working with more complex
data this week, including looking at ways to
combine data from different sources and techniques
for grouping data to create new insights.

[**Lab 5**](#colab link) (due Tuesday)

**Goals:**

- load multiple data sets
- understand how to merge data on shared keys
  - understand the difference between inner, outer, left, and right joins
- group data to create new insights
  - use `.groupby()` and aggregate functions

**Topics:**

**Do:**

Module 6: Charts & Graphs
-------------------------

We're going to make all the basic charts this week:

- bar charts
- line charts
- scatter plots
- grouped bar charts

[**Lab 6**](#colab link) (due Tuesday)

**Goals:**

- understand how charts work to convey quantitative information
- choose the right chart for the right data
- use `matplotlib` to create charts
- control the appearance of charts


**Topics:**

**Do:**

Module 7: Project 1 studio
--------------------------
This week you will work with your partner to
complete the midterm project. There will be
no new labs this week, but we will hold
our weekly online session to work on projects.


Module 8: Midterm meetings
--------------------------
This week, you and your partner will schedule a 30 minute
meeting with the instructor. In this meeting, you will 
have 15 minutes to explain and demonstrate the key aspects
of your code, followed by a 5 minute discussion.

The instructor will ask you to write some new code for your project,
which you will have 10 minutes to work on, individually, and then
present.

**Goals:**

- demonstrate mastery of topics and concepts 
  covered in the first half of the course
- identify areas of weakness and strength
- offer feedback to the instructor

**Do:**

- share your project code with the instructor
- schedule a zoom meeting with the instructor [link TBD](#tbd)

{% endmd %}
</div>
<div class="col-md-6 border-start border-3 border-dark">
{% md %}
Module 9: Exploring data
------------------------
This week you will be presented with several new data sets
available through the `nycschools` library. This package
provides data on all the schools in New York City, combined
from public data sets. Your task will be to use the API
to load data and to explore it in an open-ended manner.

_You will apply your project 1 skills in a new context._

**Goals:**

- experience working with new data and discovering
  features of that data
- choose your own analysis and visualizations

**Topics:**

**Do:**

Module 10: Mapping shapes
------------------------
So far, we have only placed _points_ on our maps. This week
we will plot polygons (shapes) from geospatial data files.
We will learn how to draw boundaries from data, add labels,
control the styles, and use color maps to create data-driven
**choropleth** maps.

[**Lab 8**](#colab link) (due Tuesday)

**Goals:**

- experience working with new data and discovering
  features of that data
- choose your own analysis and visualizations

**Topics:**

**Do:**


Module 11, 12, 13: Stats, data cleaning, spatial queries?
---------------------------------------------------------
These three weeks are left intentionally blank. It's
tough to have a student-directed learning experience
if everything is planned before we have met. There
are many topics to cover, so we will choose which ones
to focus on based on interest and the types of projects
students are pursuing.

We may want to take a deeper dive into statistical analysis.
We might want to add multiple layers and controls to the
maps. Maybe we want to collect data from more sources, including
live data streams, "scraped" data that isn't ready immediately
ready for analysis (and must be cleaned), or text data that
requires some natural language processing. We might also
want to focus on making highly polished visuals, making
interactive graphs or integrating more advanced HTML/CSS
into our work. Almost certainly we will do further spatial
analysis, learning how to find where shapes overlap and border,
which points are contained within which shapes, etc.

In short, there are many possibilities and studying
any of them will help us gain a deeper understanding
of computer science, software engineering, and computer
programming.

**Goals:**


**Topics:**

**Do:**



Module 14: Final studio 
------------------------
This week will focus on getting your
final project in shape for the beta test
in week 15.


Module 15: Beta testing
-----------------------
This week you will share your progress with the class in order
to receive feedback, ask for help, and learn from each other.

**Goals:**

- get feedback on project
- find bugs and areas of confusion


**Do:**

Module 16: Final meetings
-------------------------
You will schedule your final one-on-one meeting with the
instructor to demo your final project and solve some
computing problems to show what you learned during the semester.

{% endmd %}
</div>
</div>