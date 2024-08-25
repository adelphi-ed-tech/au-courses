---
layout: design
title: "Intro to Programming"
author:
    - "Matthew X. Curinga"
syllabus_footer: true
header-img: /img/programming-carto.png
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

**Keywords:**  computer programming, CS1, python, computational thinking, critical computational literacy, maps, data visualization

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


Assignments and Grading
=======================

<div class="row">
<div class="col-md-6">
{% md %}

| Assignment         | Points |Due date|
|--------------------|--------|--------|
| Labs (10 total)    | 30     |ongoing |
| Midterm project    | 25     |Oct 17  |
| Final project      | 25     |Dec 12  |
| Participation      | 20     |ongoing |

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
- **do not** abandon your teammates
- do not turn in work written by AI or other students

### Labs (50%)


There will be 10 programming "labs" during the course of the semester.
Each lab will provide a few challenges based on the goals and examples
of the week. You will

- _0 points_: for not turning in any work
- _1-2 points_: for a basic attempt, but code isn't working or has fundamental flaws
- _3 points_: solution works and demonstrates mastery of relevant concepts

Labs are due by midnight on Tuesday of the week they are assigned. To turn
in your lab:

1. Save a copy of the weekly lab to your Colab.
2. Rename it with your last name and the lab number, e.g. `curinga-lab1.ipynb`
3. Share the document with the instructor <mcuringa@adelphi.edu>
{% endmd %}
</div>

<div class="col-md-6">
{% md %}

### Midterm

The midterm will be a pair project that you complete **with your assigned partner**
(see [the roster](#roster)).

### Final project (25%)

For the final project you will work in a team of 2-3 people to create your own
data analysis and visualization using a data set that is available for
download or as a live open data set such as the [NYC Open Data](https://opendata.cityofnewyork.us/).



Of course, you may incorporate other data sets as you see fit.


**The final solution will be scored using the following guide:**



**Solution (7 points)**

How well does the program written solve the problem? Does the project seriously
engage with the data? Does it use compute analysis to provide interesting
insights? Is the data presented in a meaningful and usable way?

Your team's ability to design a solution to the problem is evaluated by this measure.


**Elegance & Robustness (8 points)**

This area evaluates the quality of the computer code produced by the team. An
_elegant_ program provides a parsimonious solution that is both efficient and
clear. A _robust_ program is flexible and able to change. In the case of data
analysis, it would be easy to modify if the input data changed or the output
requirements are updated. It wouldn't "break" if it encountered unexpected data,
and would continue to operate even if the amount of data were increased
dramatically. Often, both elegance and robustness are achieved through
_refactoring_: the process of reflecting on code and revising it after an initial
working solution is achieved.

**Risk Taking (5 points)**

Learning should be an adventure. One of the most exciting things about writing
software is the sense of new possibilities and discovery. The "risk taking"
aspect of your team's grade will reflect the chances that you take with your
project. Even if your solution isn't quite what you hoped for, or your code
isn't as elegant as you'd like, it's important that you take chances and try new
things. To do well in this section, you might want to shoot for an ambitious, or
complex analysis; or integrate some Javascript libraries or techniques that haven't been
explicitly covered in the course.

**Code Style (5 points)**

Your code should be well formatted and easy to read. Your functions and
variables (aka "identifiers") should have clear, meaningful names. Comments
should be used sparingly, but appropriately to guide the human reader through
your code.

_All project members will receive the same grade._

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
| 3    | 09/11 - 09/17| Mapping points             | Lab 3, choose partner |
| 4    | 09/18 - 09/24| Formatting map points      | Lab 4, Eval 1         |
| 5    | 09/25 - 10/01| Merging and grouping data  | Lab 5                 |
| 6    | 10/02 - 10/08| Charts & Graphs            | Lab 6                 |
| 7    | 10/09 - 10/15| Project 1 Sprint           | _project work_        |
| 8    | 10/16 - 10/22| Midterm meetings           | Project 1             |
| 9    | 10/23 - 10/29| Lists                      | Lab 7, Eval 2         |
| 10   | 10/30 - 11/05| Files                      | Lab 8                 |
| 11   | 11/06 - 11/12| Dictionaries               | Lab 9                 |
| 12   | 11/13 - 11/19| Exceptions                 | Lab 10                |
| 13   | 11/20 - 11/26| Recursion                  | _project work_        |
| 14   | 11/27 - 12/03| Objects and Classes        | _project work_        |
| 15   | 12/04 - 12/10| Portfolio work             | _project work_        |
| 16   | 12/11 - 12/17| Final 1:1 presentations    | Final Project, Eval 3 |

<div class="row">
<div class="col-md-6">
{%md %}

Module 1: Data(frames) & Variables
----------------------------------


This week we want to get up and running with the
tools of the class and the basics of writing code in
Python and Colab.

[**Lab 1**](#colab link) (due Tuesday)

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

- Watch to the Welcome Message
- Join Slack (find the link in your Adelphi email)
- Post on the `#code` channel in Slack:
  - your name
  - area of study
  - why you are taking this course and programming background (if any)
  - which of the "fears of programming" resonate with you
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

Module 7: Midterm meetings
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
Module 8: Exploring data
------------------------
This week you will be presented with several new data sets.
You will choose one and will conduct your own novel analysis,
using the techniques we have learned so far.

**Goals:**

- experience working with new data and discovering
  features of that data
- choose your own analysis and visualizations

**Topics:**

**Do:**

{% endmd %}
</div>
</div>