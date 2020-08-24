% Introduction to Programming
% Matthew X. Curinga

<!--
This syllabus was created for
the Educational Technology Program
at Adelphi University:
http://education.adelphi.edu
copyright 2012 Matthew X. Curinga
http://matt.curinga.com
This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send
a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
We ask, but do not require, that attribution includes a link to our websites (above).
version: 2.1
Based on work available here: https://github.com/mcuringa/adelphi-ed-tech-courses
-->

**Computer Science 0145-602, Fall 2015**

**Keywords:**  computer programming, CS1, python, computational thinking, critical computational literacy, Python

**Description:** This course introduces students to programming and
some core concepts of computer science, using a modern, object oriented
programming language (currently Python). Students learn concepts of
variables, functions, repetition/loops, basic data structures
(arrays, lists, hashtables), and basic object oriented programming.

**Class meetings:** Online, asynchronous (coordinated through Moodle)

**Instructor**

* [Matthew X. Curinga](http://matt.curinga.com), <mcuringa@adelphi.edu>

**Dr. Curinga's Office Hours**

* Monday, 3-5PM
* Wednesday, 3-5PM
* by appointment

Learning Goals
===========================

* understand the types of problems that can be solved using computational techniques
* understand the basic concepts of computation (CPU, RAM, permanent storage, GUIs, file systems, network connections)
* learn core computer programming concepts (abstraction, variables, conditions, functions, repetition, recursion)
* think algorithmically to design and test computer programs
* master the basic syntax and idioms of the Python programming language
* use technical documentation, APIs, and the internet to learn new technical concepts
* develop step-by-step problem solving and debugging practices


Required Text
==========================================================================================

Downey, A. B. (2016). [_Think Python: How to Think Like a Computer Scientist, Version 2.4.0_](http://greenteapress.com/thinkpython2/html/index.html). Green Tea Press.

Readings & Bibliography
==========================================================================================

_This is a selected bibliography of computer science and Python texts and other materials
that you may explore as references or further reading. Many weekly readings will come
from these materials. Specific readings will be posted on Moodle for each week._

Alvarado, C., Dodds, Z., Kuenning, G., & Libeskind-Hadas, R. (2013). [_CS for All_](http://www.cs.hmc.edu/csforall/).
Claremont, CA: Harvey Mudd College.

Barry, P. (2009). _Head first programming: [a learner’s guide to
programming using the Python language]_. Beijing ; Sebastopol,
CA: O’Reilly.

Downey, A. (2012). _Think Python_. Sebastopol, CA: O’Reilly.
[free](http://www.greenteapress.com/thinkpython/html/index.html)
[py v3](http://faculty.stedwards.edu/mikek/python/thinkpython.pdf)

Pilgrim, M. (2009). [_Dive into Python 3_](http://www.diveinto.org/python3/index.html). New York: Apress.

[_The Python Tutorial v.3.3_](http://docs.python.org/3/tutorial/).

Zelle, J. (2010). _Python Programming: An Introduction to Computer
Science_. Franklin, Beedle & Associates Inc.


Required Software/Online Accounts
=================================

- Software
  - [Slack Client](http://slack.com) (recommend desktop and mobile clients)
  - [Atom Editor](https://atom.io/)
  - Firefox or Chrome web browser
- Accounts
  - [repl.it](https://repl.it)
  - [AU Ed Tech Slack channel #code](https://auedtech.slack.com/signup)

Required Hardware
==================
For the more in depth labs and projects, we will be designing and
programming "skills" for the M[yCroft AI voice assistant.](https://mycroft.ai)
MyCroft is like an open source Alexa or Siri. In order to work on your project,
you will need a Raspberry Pi, microphone, and speakers, as well as display, keyboard, and mouse to work with the Pi. You can use any suitable
hardware that you already have from the list below, but we also recommend
certain items if you are purchasing new hardware.

I am posting links to the items on SparkFun and Amazon. You should be able to get most or all of the items locally, at [MicroCenter](https://www.microcenter.com/) (which may be the easiest option).

- Raspberry Pi model 3 or 4, recommended Raspberry Pi 4 (2GB) [SparkFun](https://www.sparkfun.com/products/15446) [Amazon](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27)
- a microphone that works with Raspberry Pi, recommended ReSpeaker 4-Mic Array [SparkFun](https://www.sparkfun.com/products/14645) [Amazon](https://www.amazon.com/seeed-Studio-ReSpeaker-4-Mic-Raspberry/dp/B076SSR1W1/)
- micro hdmi cable [SparkFun](https://www.sparkfun.com/products/15796) [Amazon](https://www.amazon.com/dp/B07VRCK5W1/)
- two (2) 16GB micro SD cards [Amazon](https://www.amazon.com/Micro-Center-Class-Memory-Adapter/dp/B07K81Z6DF/) (these are 32GB, but they're a good deal)

You probably have these items already:

- tv or computer monitor with HDMI input
- USB-C power cord (like a USB-C phone charger)
- USB or Bluetooth Mouse / Keyboard


Class meetings
==========================================================================================

This is a fully online class, which will run on a Tuesday-Tuesday schedule,
meaning new topics will begin each Tuesday, and assignments will be due by end
of day on Monday. There will be a live video session lab held every-other Tuesday.
No new topics will be covered in these labs that aren't also in course materials,
but they will give students the chance to ask questions and receive quick feedback
on practice problems.

Week  Date    Topic                            Read   Due
----  ------  -------------------------------  -----  -------------------
   1  1-Sep   Critical Computational Thinking  TIP 1  -
   2  8-Sep   Variables & Statements           TIP 2  -
   3  15-Sep  Functions                        TIP 3  Quiz 1
   4  22-Sep  Case Study 1: Hello World        -      MyCroft Thesis
   5  29-Sep  Conditionals & Recursion         TIP 5  -
   6  6-Oct   Fruitful Functions               TIP 6  -
   7  13-Oct  Iteration                        TIP 7  Quiz 2
   8  20-Oct  Strings                          TIP 8  -
   9  27-Oct  Case Study 2: Attendance         -      MyCroft Prototype
  10  3-Nov   Lists                            TIP 1  -
  11  10-Nov  Dictionaries                     TIP 1  -
  12  17-Nov  Tuples                           TIP 1  Quiz 3
  13  24-Nov  Files                            TIP 1  -
  14  1-Dec   Case Study 3: Random Groups      -      MyCroft Testing
  15  8-Dec   Project Lab                      -      -
  16  15-Dec  Final Projects Due               -      **Final Project**

* TIP: _Thinking in Python_

Assignments and Grading
==========================================================================================

Assignment     Pct
-------------  -------
Quizzes        60%
Final Project  40%

Lab Exercises
-------------
Most weeks there will be ungraded lab exercises where students can practice
the new materials covered. In general, you should spend about one hour working
on these exercises. If you understand the exercises, you will be on track with
the course. There may be bonus problems that are a little bit more
challenging, which are optional.

Quizzes
-------
Quizzes will consist of 5 questions, similar to the lab exercises. Each question
is worth 4 points, with possible credit available. Roughly:

- 4 points for a complete working solution
- 3 points for a solution that partially works or only doesn't work due
  to minor bugs
- 2 points for a partial solution that has some of the components needed for
  the solution, but overall does not solve the problem
- 0-1 points for non-functional code

Final Project: MyCroft Skill
----------------------------

During the course of the semester we will be learning about software design



#### Marking guide:

There are a total of 20 possible points for this assignment, which will
be evaluated on the following criteria:

1. **Question Quality** (_3 points_)\
   Does the question chosen reflect a problem that a computer program is good
   at analyzing? Is the question interesting or important? Is the answer
   obvious, or is it worthy of analysis?

    - 3 points: the _question can not be easily answered without the aid of
      software_ because it analyzes a large data set, involves
      tedious/repetitive tasks which are prone to error, or requires complex
      calculations. Further, the _question is interesting_—it tells us
      something that is not already established in research or provides
      evidence for something that is incompletely or ambiguously understood
    - 2 points: the question meets one of the two criteria for 3 points,
      but not both
    - 1 point: the question is trivial or obvious after brief human
      analysis, or does not lend itself to generalization/abstract
      conclusions
    - 0 points: the question would be more easily analyzed by human
      rather than computer analysis; trying to write software to
      answer the problem actually makes it more difficult to get a clear
      picture of the problem
2. **Coding fundamentals** (_8 points_)\
   The program demonstrates a grasp of the programming concepts covered
   in this class, including:

    - _variables_
        - data is not "hard coded" and can be easily changed
        by using variables
        - data is separate from functionality
    - _functions_
        - abstraction through function parameters
        - encapsulation through function parameters and return statements;
          use "pure functions" with zero-side effects
    - _design_
        - the program is organized through the use of functions
        - functions "scale" is appropriate to the task and discrete:
          concerns are separated logically, such as one function
          for gather results and another for displaying results
        - functions are written in a way that they are used
          several times in the program
        - code is not repeated
    - _data structures_
        - use python built-in data structures appropriately:
          ``list``, ``dict``, ``tuple``, ``set``
        - use index/slice notation if needed
        - sort data structures

    _Point values:_

    - 6-8 points: creates new functions that perform _new analysis_ not
      available in the ``content.py`` program provided by the instructor. The
      program would easily be able to work on a different data set
      (i.e. different input text files) to provide good results. Functions
      are consistent (in that the parameters expected and results
      returned work well with other functions in the program) and can be
      combined in different ways.
    - 3-5 points: code is clear and organized, but does not add significant
      new functions, some code may have unintended side effects, such
      as modifying list or dictionary data in unexpected ways; other code
      may take parameters, but not use them. Code cannot easily operate
      on other data sets.
    - 0-2 points: repetitive tasks are not factored into functions, but
      exhibit more of a copy-paste approach, functions don't (always)
      return the expected results or contain logic errors; code doesn't
      run due to syntax errors or runtime errors
3. **Risk Taking** (_4 points_)\
   How "adventurous" is this code? Does the student show that they move beyond the
   template given to them? Is there evidence they read online docs or the course text to learn
   addition techniques to approach the problem?

     - 4 points: in several places, the program use advanced features such
       as optional functional parameters, list comprehensions,
       advanced sorting techniques, object oriented programming, or string formatting functions; libraries
       are imported to improve code performance and clarity; content.py
       functions are modified and improved by the student
    -  3 points: some core changes are made to content.py, other advanced
       techniques are evident 1 or 2 times
    -  1-2 points: tentative changes are made to content.py, mostly by
       adding composite functions that combine existing functionality
    -  0 points: only cosmetic changes are made to the initial content.py
       example, such as changing the input text files and the target
       words passed into the ``neighbors`` function
4. **Code Style** (_2 points_)\
   Is the program consistently formatted according to Python conventions?

    - 2 points: consistently follows the spirit of the _Think Python_ and
      PEP 8 style guides.
    - 1 point: follows guide most of the time, shows internal consistency
       for style
    - 0 points: lack of consistency in style makes the program harder to
      read and (potentially) harder to debug and maintain

5. **Results** (_3 points_)\
   The quality of your results include both the information that your program
   produces and the way that it is formatted for the user. When your program
   runs, it should produce some type of report that sheds light on your
   hypothesis. It doesn't matter if your hypothesis was correct or not—after
   your program runs, the user should have more information to evaluate the
   hypothesis.

       - 3 points: results give clear support for or against the
         hypothesis by providing relevant information and are formatted
         in a way that makes them easy to interpret
       - 2 points: results provide some evidence for or against the
         hypothesis. they may not be formatted in a way that makes them
         easy to interpret or they may leave some ambiguity that could
         have been explored further in the code
       - 1 point: some evidence is provided but it is difficult to
         interpret either due to formatting or the output achieved
       - 0 points: results do not shed any light on the question posed

#### Deliverables:

You should turn in all files related to your project in a single
archive (e.g., .zip, .tar, .7z). Project files _must_ contain your
**Python program** and the data/text files you're analyzing.
The program must start with a comment where you identify:

* the question you are investigating (i.e. your hypothesis)
* the method for investigating this question
* the results identified by your code

To create an archive file, Mac users can simply right-click
the project folder from the finder and choose "Compress". This
will create a .zip archive of the project directory. Windows
does not come with a compression utility by default. If you
do not have one installed or are not sure, Adelphi IT
recommends [7-zip, which you can download and use for free.](http://7-zip.org/)

#### Sample project ideas

One of the intentional challenges of this project is for students to generate
their own ideas for projects. It's one thing to answer a quiz question or
to work on homework problems where you know exactly what you are supposed
to do; quite another when you need to decide what the goals for the
program are, too, and what results it should find.

Here are some ideas, though, that might get you started.

1. Compare the ways that U.S. news and foreign news cover a topic:
    a. choose your topic
    b. download US news with a keyword search
    c. download foreign news with same keywords
    d. do a neighbor (n-gram) analysis of word counts near key terms
2. [Stylometry](https://en.wikipedia.org/wiki/Stylometry)\
   Instead of considering the context and content of important keywords,
   stylometry would let us look at the style of a text. By considering
   common words and phrases, we might be able to answer questions such
   as:
   a. is a text written by a man or a woman?
   b. do African Americans have a distinct writing style?
   c. how has writing style changed over time? can we identify when
      a piece was written based on its style?
3. Compare 2 books or 2 authors\
   Create two texts from Gutenberg or another source and pick an area
   to analyze. Classic things to consider are the ways a text deals
   with issues of race, gender, sex, violence, humor, death, god/religion,
   etc.
4. Compare speeches:
   - what are the difference and similarities between speeches
     from WWI, WWII, Vietnam, and today? Has the "security" message changed?
     Has the anti-war/peace message changed?
   - compare the speeches from different political parties? what propaganda
     do they use? how do they use language to shade the issues that are
     most crucial to their supporters?
   - what are the characteristics of a great speech? are the similarities
     between the rhetorical styles of Lincoln, Churchill, King, Malcom X
     and others?
