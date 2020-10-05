% Introduction to Programming
% Matthew X. Curinga

<!--
This syllabus was created for
the Educational Technology Program
at Adelphi University:
https://adelphi.edu
copyright 2012-2020 Matthew X. Curinga
http://matt.curinga.com
This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send
a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
We ask, but do not require, that attribution includes a link to our websites (above).
version: 2.1
Based on work available here: https://github.com/mcuringa/adelphi-ed-tech-courses
-->

**Computer Science 0145-602, Fall 2020**

**Keywords:**  computer programming, CS1, python, computational thinking, critical computational literacy, Mycroft, virtual assistant

**Description:** This course introduces students to programming and
core concepts of computer science, using a modern, object oriented
programming language (currently Python). Students learn concepts of
variables, functions, repetition/loops, basic data structures
(arrays, lists, dictionaries), and basic object oriented programming.

<img src="img/python-logo.png" class="d-block img-fluid" alt="Python intertwined snakes and text on white field">

**Class meetings:** Online, asynchronous (coordinated through Moodle)

**Instructor**

* [Matthew X. Curinga](http://matt.curinga.com), <mcuringa@adelphi.edu>

**Dr. Curinga's Office Hours by appointment**

* Wednesday, 4:30-5:30PM
* Thursday, 4-5PM

Learning Goals
===========================

* understand the types of problems that can be solved using computational techniques
* understand the basic concepts of computation (CPU, RAM, permanent storage, GUIs, file systems, network connections)
* learn core computer programming concepts (abstraction, variables, conditions, functions, repetition, recursion)
* think algorithmically to design and test computer programs
* master the basic syntax and idioms of the Python programming language
* use technical documentation, APIs, and the internet to learn new technical concepts
* develop step-by-step problem solving and debugging practices


Computer Science Tutoring, Fall 2020
====================================
The Math & CS department offers student-led computer science tutoring on
weekdays via Zoom. The tutors are experienced computer science students. They
may not be expert in Python or the specific problems of our class, but can
certainly help you break down problems and understand key concepts.

Here's the Fall schedule. You don't need an appointment, just join the zoom
link for the tutor during their tutoring hours.

Day          Time                 Tutor    Zoom Link
-----------  -------------------  -------  -------------------------------------------------
Monday       4:00 to 6:00 PM      Aianne   <https://adelphiuniversity.zoom.us/j/95098505891>
Tuesday      4:30 to 6:30 PM      Jasur    <https://adelphiuniversity.zoom.us/j/94652074966>
Wednesday    4:00 to 6:00 PM      Matt     <https://adelphiuniversity.zoom.us/j/93998972403>
Thursday     3:00 to 5:00 PM      Kaitlyn  <https://adelphiuniversity.zoom.us/j/97958835405>
Friday       11:00 AM to 1:00 PM  Tia      <https://adelphiuniversity.zoom.us/j/4259506444>


Required Text
=============

Downey, A. B. (2016). [_Think Python: How to Think Like a Computer Scientist, Version 2.4.0_](http://greenteapress.com/thinkpython2/html/index.html). Green Tea Press.

Required Software/Online Accounts
=================================

- Software
  - [Slack Client](http://slack.com) (_must install_ desktop and mobile clients, using the web client is not sufficient)
  - Firefox or Chrome web browser
- Accounts
  - [repl.it](https://repl.it)
  - [AU Ed Tech Slack channel #code](https://auedtech.slack.com/signup)

Required Hardware
==================
For the final project (see below) we will be designing and
programming "skills" for the [Mycroft AI voice assistant.](https://mycroft.ai)
Mycroft is like an open source Alexa or Siri. In order to work on your project,
you will need a Raspberry Pi, microphone, and speakers, as well as display,
keyboard, and mouse to work with the Pi. You can use any suitable
hardware that you already have from the list below, but we also recommend
certain items if you are purchasing new hardware.

I am posting links to the items on SparkFun and Amazon. You should be able to
get most or all of the items locally, at [MicroCenter](https://www.microcenter.com/)
(which may be the easiest option). You _must_ have a working Raspberry Pi
setup by week 4 (Sep 22). If you have any trouble acquiring equipment, please
let me know as soon as possible.

- Raspberry Pi model 3 or 4, recommended Raspberry Pi 4 (2GB) [SparkFun](https://www.sparkfun.com/products/15446) [Amazon](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27)
- a microphone that works with Raspberry Pi, recommended ReSpeaker 4-Mic Array [SparkFun](https://www.sparkfun.com/products/14645) [Amazon](https://www.amazon.com/seeed-Studio-ReSpeaker-4-Mic-Raspberry/dp/B076SSR1W1/)
- micro hdmi cable [SparkFun](https://www.sparkfun.com/products/15796) [Amazon](https://www.amazon.com/dp/B07VRCK5W1/)
- two (2) 16GB micro SD cards [Amazon](https://www.amazon.com/Micro-Center-Class-Memory-Adapter/dp/B07K81Z6DF/) (these are 32GB, but they're a good deal)

You probably have _some_ these items already. Please gather or purchase each item on the list.

- micro SD card reader: these are built into many modern laptop and some desktops,
  but any card reader/writer that works with your computer (USB 2, USB 3, USB-C)
  will work. You should be able to find one for less than $10 on Amazon or in a local store (Staples, Best Buy, Microcenter).
  [here's one on amazon](https://www.amazon.com/dp/B06ZYXR7DL)
- USB-C power cord (like a USB-C phone charger) [SparkFun](https://www.sparkfun.com/products/15448) Amazon [[RPI official](https://www.amazon.com/Raspberry-Model-Official-SC0218-Accessory/dp/B07W8XHMJZ/)]
- TV or computer monitor with HDMI input (you **cannot** use your laptops display for this)
- USB Keyboard (a wireless keybaord with a dongle will work, but not a bluetooth keyboard) [[I use this one](https://www.microcenter.com/product/376891/K400_Wireless_Touch_Keyboard), but if you can just borrow a keyboard for a day, that should be fine]
- if your monitor doesn't have speakers you will need computer speakers or (wired) headphones

Class meetings
==============

This is a fully asynchronous online class, which will run on a Tuesday-Tuesday schedule,
meaning new topics will begin each Tuesday, and assignments will be due by end
of day on Monday. There are no set meeting times, and there will not be
Zoom or other video class sessions. You will be able to flexibly schedule your
time within the week for each topic. Assignments will be submitted via Moodle
and the coding website <https://repl.it>

### Weekly topics

Week  Date    Topic                        Read   Due
----  ------  ---------------------------- -----  -------------------
   1   Sep 1  The way of the program       TIP 1  -
   2   Sep 8  Variables & Statements       TIP 2  -
   3  Sep 15  Functions                    TIP 3  Quiz 1
   4  Sep 22  Case Study 1: Hello World    -      Mycroft Concept
   5  Sep 29  Conditionals & Recursion     TIP 5  -
   6   Oct 6  Fruitful Functions           TIP 6  -
   7  Oct 13  Iteration                    TIP 7  Quiz 2
   8  Oct 20  Strings                      TIP 8  -
   9  Oct 27  Case Study 2: Attendance     -      Mycroft Prototype
  10   Nov 3  Lists                        TIP 10 -
  11  Nov 10  Dictionaries                 TIP 11 -
  12  Nov 17  Tuples                       TIP 11 Quiz 3
  13  Nov 24  Files                        TIP 12 -
  14   Dec 1  Case Study 3: Random Groups  -      Mycroft UX Testing
  15   Dec 8  Working Session              -      -
  16  Dec 15  Final Projects Due           -      **Final Project**

TIP: _Thinking in Python_

### Live labs

In addition to the required weekly assignments, there will be several "live"
labs on Wednesdays (either at 4:30-5:30 or 6:30-7:30). Lab times and meeting
links will be posted on Moodle. These live **sessions are optional**,  but will
offer additional help and hands-on demonstration of course concepts. If the
health situation allows it, some of these later sessions may be shifted to flex
(oline/in-person) sessions held at the Manhattan Center.

The tentative schedule for live sessions:

- 9/16: quiz 1 review*
- 9/30: setting up "picroft"*
- 10/14: quiz 2 review*
- 10/28: mycroft programming*
- 11/18: quiz 3 review*
- 12/9: final project work session*


Assignments and Grading
=======================

Assignment     Pct
-------------  ----
Quizzes        60%
Final Project  40%

Lab Exercises
-------------
Most weeks there will be ungraded lab exercises where students can practice
the new materials covered. In general, you should spend about one hour working
on these exercises. If you understand the exercises, you will be on track with
the course. There may be bonus problems that are a little bit more
challenging, which are optional. You are encouraged to work on the exercises
with other students and friends.

Quizzes
-------
Quizzes will consist of 5 questions, similar to the lab exercises. Each question
is worth 4 points, with possible credit available.

- _0-1 points_: for not turning in any work, or code that does not address the problem
- _1 point_: for a basic attempt, but code isn't working or has fundamental flaws
- _3 points_ (mostly) solution demonstrates mastery of relevant concepts, but doesn't work in all cases or fails due to minor errors
- _4 points_: solution works, demonstrates mastery of concepts, and is well formatted and clearly written

Quizzes will be timed, taken through Moodle. You can use the textbook, course examples,
and any documentation or internet resources you find. **You may not ask other people for help.**
While programming is a highly collaborative practice, these quizzes are meant
to assess _your_ work and understanding.


Final Project: Mycroft Skill
----------------------------
During the course of the semester we will be learning about the software design
process, and have the opportunity to write a larger program. This is a group
project, and you should work in a group of 2-4 students.

[Mycroft](https://mycroft-ai.gitbook.io/docs/about-mycroft-ai/why-use-mycroft)
is a free open source software voice assistant. It is not as advanced as better
known products from big tech companies: Siri, Alexa, Cortana, Google Assistant.
However, it works very well and is much easier to get started programming with.
Also, since the project is designed to protect users and their data, it is a
good fit for classrooms and students.

Working with your team, you will design a new Mycroft "skill." Skills are the
"apps" of the Mycroft system. You activate them with a spoken phrase and
Mycroft can ask follow up questions or speak a response. Mycroft can also
affect other changes, if it's connected properly, such as changing lights,
playing audio or video, or controlling motors or sensors connected to your
Raspberry Pi. See [What can a Skill do?](https://mycroft-ai.gitbook.io/docs/skill-development/voice-user-interface-design-guidelines/what-can-a-skill-do)
from the Mycroft developers guide in order to get a better sense of what you
might make.

For this project, you will conceive of a novel Mycroft skill, refine the skill
by talking to people who are in the target audience, and code the skill through
an iterative process of developing, testing, and improving.

### Final Project Grading:

There are a total of 40 possible points for this assignment, which will
be evaluated on the following criteria:

1. **Design** (_5 points_)\
   How well is the skill designed? Does it solve a real problem or need in the world?
   Has the team spoken to enough real users to understand the problem? How usable
   is the skill? Is it easy to learn and understand? Has it been validated
   and revised through user testing?

2. **Coding fundamentals** (_15 points_)\
   The program demonstrates a grasp of the programming concepts covered
   in this class, including:

    - _variables_
        - data is not "hard coded" and can be easily changed
        by using variables, soliciting user input, and/or reading from files
        - data is separate from functionality
    - _functions_
        - abstraction through function parameters
        - encapsulation through function parameters and return statements;
          use "pure functions" with zero-side effects when possible
        - composition and re-use of code
    - _design_
        - the program is organized through the use of functions
        - functions' "scale" is appropriate to the task and discrete:
          concerns are separated logically, such as one function
          for gathering results and another for outputting results
        - functions are written in a way that they are used
          several times in the program
        - code is not repeated
    - _data structures_
        - use python built-in data structures appropriately:
          `list`, `dict`, `tuple`, `set`, etc
        - use index/slice notation if needed
        - sort data structures
        - map, filter data as needed

3. **Risk Taking** (_5 points_)\
   How "adventurous" is this code? Does the team show that they move beyond the
   template given to them? Do they come up with a really novel and desirable project?
   "Riskier" project push beyond the material strictly covered in class and demonstrate
   the teams' ability to learn new things and push their horizons.

4. **Code Style** (_2 points_)\
   Is the program consistently formatted according to Python conventions?

    - 2 points: consistently follows the spirit of the _Think Python_ and
      PEP 8 style guides.
    - 1 point: follows guide most of the time, shows internal consistency
       for style
    - 0 points: lack of consistency in style makes the program harder to
      read and (potentially) harder to debug and maintain

5. **Usability & Usefulness** (_3 points_)\
   The usability is different from the design, in that it incorporates things
   such as the usefulness of the results provided, speed and accuracy of the software,
   and the total experience of working with the skill.

### Deliverables:

1. **Code Files and Resources**\
   You should turn in all files related to your project in a single
   archive (e.g., .zip, .tar, .7z). Project files _must_ contain your
   **Python program** and any data and media files that are required.

   To create an archive file, Mac users can simply right-click
   the project folder from the finder and choose "Compress". This
   will create a .zip archive of the project directory. Windows
   does not come with a compression utility by default. If you
   do not have one installed or are not sure, Adelphi IT
   recommends [7-zip, which you can download and use for free.](http://7-zip.org/)
2. **Video Demo**\
   You should provide a narrated screencast or video of 4-5 minutes that demonstrates
   your skill, running on your Raspberry Pi. Your group can decide who to divide the work.
   Upload the video to YouTube and provide the link when you submit your assignment to Moodle.
