% Educational information systems and networks
% Matthew X. Curinga
  Tom Jennings
  Christian Correa
  David Frackman


<div class="row">
<div class="col-6">

### 0858-606, Summer 2021

### Description: From a foundation of computer networks and systems, this course
expands to cover instructional technology infrastructure: file systems, users,
wired and wireless networks, email, web servers, computer labs, and common educational
software services. This course focuses on Free Software; where the source code
is free to use, study, or modify. To explore these topics in this hands on class
all students will be configuring their own Raspberry Pi computers and using them
to complete a software/hardware project.

</div>
<div class="col"><img class="img-fluid" src="https://static.makeuseof.com/wp-content/uploads/2016/09/smart-mirror-raspberry-pi-illustration.png" alt="drawing of a raspberry pi"></div>
</div>

### Keywords: linux, bash, systems, networks, lamp, free software, trouble shooting,
technical project management, rasberry pi, physical computing, debian, ubuntu

Goals & Objectives
==================

This course introduces students to the key concepts in current networked
computing in order to develop a conceptual framework for configuring
and troubleshooting computing systems. Upon completing this course they
will be able to:

- set up a secure, network computing environment
- effectively use the basic tools of GNU/Linux computing environments
- implement techniques for administering group and user permissions
- install and troubleshoot hardware and software infrastructure for
  networked and internet computing
- configure a client/user computer for specific purposes
- configure various server-side applications to support teaching and
  learning
- identify the ethical and legal concerns surrounding educational
  information systems

Class Information
=================

### Instructor:
  ~ Matt Curinga <mcuringa@adelphi.edu>

### Class dates:
  ~ Wednesday, May 26 - Tuesday, June 29

### Live sessions:
- Wednesdays: 4:30pm - 6:20pm
- zoom link on moodle

Course Communications
=====================

This online course will have a mix of synchronous and asynchronous assignments.
The synchronous sessions, "live lab," will be held each Wednesday, via Zoom,
4:30pm to 6:20pm.

Participants in this course must actively participate in our suite of online
communications tools, including Slack (<https://auedtech.slack.com>),
Adelphi email, and the course website.

You _must_ check your Adelphi email and the `#raspberrypi` channel on Slack **at least
once a day.** It is highly recommended that you install the Slack mobile client
and an email client on your mobile phone so that you receive "push notifications"
of course announcements.

The best place to post general course questions and any content-related questions
is the `#raspberrypi` Slack channel. The instructor, as well
as other students and alums, monitor this channel and often provide immediate support.
You are encouraged to contact the instructors at any time via email or direct
message on Slack.

### Online tools:

- ### Moodle: will be used to post the syllabus and links to weekly readings, videos, and discussions.
- ### Slack: will be our main channel for online communications.
  Please [Join our Slack team with your Adelphi email](https://auedtech.slack.com/signup).
  If you run into trouble or have a question, post it here to our channel, `#raspberrypi`,
  or send a message to `@mxc`. During the weeks of the class, we recommend running
  the Slack app for you phone.
- ### Trello: is project management software that you will use to track/plan
  your two projects, and to share your progress with the course instructors.
  Create a [Trello Account](https://trello.com/signup) before the first week of
  class, and (optionally) [install the mobile app](https://trello.com/platforms).        
- ### mail.adelphi.edu email: we will use your official adelphi student email
  for class email communications. Please check this email regularly.

### Getting remote help:

Because of the hands on nature of working with computers and Raspberry Pi, you
will have to use a variety of tools to get help. Your first stop for help should
be #raspberrypi on Slack. You are most likely to get quick help if you post here
because anyone in the channel (instructors, other students, other faculty, ed tech alums)
can lend a hand.

For more complicated problems, you will need to be able to:

- [post formatted code in slack](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages)
- [take a screenshot from your RPI](https://wiki.debian.org/ScreenShots#Using_Gnome)
- [create a google hangout/meeting with screensharing](https://support.google.com/meet/answer/7290345?co=GENIE.Platform%3DDesktop&hl=en)
- enable remote access to instructors to your RPI via `ssh` -- at the end of the
  first week, you should have `ssh` enabled on your Pi. To enable remote access
  you will probably have to enable Network Address Translation (NAT) on your wifi router.
  If you are on public wifi (e.g. school, library, coffee shop), you probably won't
  be able to enable remote access. NAT is not hard to configure, but it's specific
  to the wifi router that you're using. You will have to search
  "configure network address translation" along with your router make and model.
- [connect to your RPI with VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)
  (once you're comfortable with NAT, you can also configure NAT for VNC if needed)


Required Books
==============
_None_

Required Materials
==================

Desktop/Laptop
--------------
You must have access to a desktop computer running Linux, Windows, or MacOS to
participate in this course. You will use this computer to participate in the
course online and to configure and connect or your RPI. You can use a phone
or tablet for some online elements of the course, however you will not be able
to complete course assignments without access to a computer where you are able
to install software.

In addition to the computer, you must have a webcam, headphones, and microphone
to participate in live video chat and to record your screencasts.

Raspberry Pi
------------

Every student _must_ purchase a Raspberry Pi (RPI) computer and accessories
for use in this course. You will keep your own hardware. If you already own a
Raspberry Pi, of course you can use it for this course. You can pick up these
items in person at a local [MicroCenter](https://www.microcenter.com/) ([view items in wishlist](https://account.microcenter.com/PublicWishList.aspx?WishListID=4Yt4PUuytCb2roLGPinnTH5Itg3JsOKt&Email=SXkm0QpXuD%2b%2fxxyZcAguSK2mIABUJbA7)) or purchase them online.

Required hardware:

- Raspberry Pi model 4 (2GB model recommended): [[SparkFun](https://www.sparkfun.com/products/15446)] [[Amazon](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27)] [[AdaFruit](https://www.adafruit.com/product/4295)]
- 16GB (or larger) Micro SD Card (at least 2 recommended)
- micro hdmi cable [[SparkFun](https://www.sparkfun.com/products/15796)] [[Amazon](https://www.amazon.com/dp/B07VRCK5W1/)] [[AdaFruit](https://www.adafruit.com/product/4302)]
- 5.1V 3A USB-C wall charger [[SparkFun](https://www.sparkfun.com/products/15448)] [[Amazon](https://www.amazon.com/Raspberry-Model-Official-SC0218-Accessory/dp/B07W8XHMJZ/)] [[AdaFruit](https://www.adafruit.com/product/4298)]
- micro SD card reader: these are built into many modern laptop and some desktops, but any card reader/writer that works with your computer (USB 2, USB 3, USB-C) will work. You should be able to find one for less than $10 on [Amazon](https://www.amazon.com/dp/B08BBX4YM1/) or in a local store (Staples, Best Buy, Microcenter).

You will need (but can re-use existing):

- USB Keyboard and Mouse [[wireless](https://www.amazon.com/dp/B014EUQOGK/)] [[wired](https://www.microcenter.com/product/485045/inland-ic-210-premium-mouse-keyboard-combo)]
- Computer Monitor or TV with HDMI input

_You must have all of the required hardware ### before the first week of class._

If you purchased everything except the monitor it would cost $80-$90.

In addition to these core materials, you will also need to purchase/acquire
materials to complete your final project (see below).
Costs may range from $20-$80.

Books & Resources
=================
- [Raspberry Pi Foundation](https://www.raspberrypi.org/)
- Crowley, C. 2017. [_Raspberry Pi: The Unofficial Tutorial_](http://cdn.makeuseof.com/wp-content/uploads/2017/07/Raspberry-Pi-The-Unofficial-Tutorial.pdf)
- [Make: Magazine](https://makezine.com/)
- [Explaining Computers Series](https://www.youtube.com/user/explainingcomputers/videos) (Youtube)

Schedule
========

Week  Date          Topic            
----  ------------  -------------------------------------
   1  Wed, May 26   Computers & Operating Systems
   2  Wed, Jun 2    The Command Line
   3  Wed, Jun 9    Users, Groups, Files, & Permissions
   4  Wed, Jun 16   Networks
   5  Wed, Jun 23   Ethics
   6  Tues, Jun 29  DIY Project Due

A detailed calendar of due dates and course deadlines is available online at.
[You can subscribe to and view the calendar online at this link.](https://calendar.google.com/calendar/u/0?cid=Y19rN3IzMTU4ODRsYWcyMzE4cnYwaWJiNDZiOEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)

Grades & Assignments
====================

Assignment                  Pct  Due
--------------------------  ---  -------
Participation               20%  ongoing
RPI Client or Server Setup  40%  6/15
DIY Project                 40%  6/29


Participation
------------------
Because this is a short summer course (3 credits in 6 weeks), you should budget
10-15 hours each week for course work. Wednesday live lab sessions are required,
but you will also spend significant time working through course materials at your
own pace.

Your participation grade will consider preparation for live labs, timely
management of your Trello projects, and participation in Slack and Moodle
discussions. Smaller (ungraded) weekly assignments will also be considered for
your participation grade.

RPI Client or Server Setup
--------------------------
For our first project you will configure your Raspberry Pi for a specific
educational scenario: a general computer for 4th grade classroom computer
station, a setup to teach computer programming for kids, a development server
for the Canvas LMS, a workstation configured with assistive technology to support
users with different physical needs, a web server to host static HTML/Javascript projects,
a managed computer lab setup, etc. Whatever scenario you choose, your installation
should be precisely tailored to meet the needs of your target users.

You will present your project as a narrated screencast. In addition to demonstrating the
software, you will upload a report which details:

- a description of the target audience and how you envision they would use the RPI
- the process you used to find, test, and configure the RPI
- key features of the software installed
- advantages, disadvantages, and other implications of your design

You will be evaluated on:

- demonstration of your understanding of RPI hardware and software
- suitability of your solution for your stated audience/problem
- risk/complexity of the task undertaken
- reflection on the process

_Submission Guidelines_

To submit this project, you will upload a narrated screencast video of your
project to YouTube (you can sign in with your Adelphi email account). If you do
not want the video to be public, change the permissions so that it is an
"unlisted" video. Only people with the link will be able to see it. Create a new
thread in the discussion forum with a title for your project. Post the link to
your video here, along with any supporting documentation (screenshots, code,
config files).

Begin the video with a description of who the target users are of this setup and
what your goals are for them. Next, show your project from the user's
perspective, showing how it meets the needs  of the use cases that guided you in
designing the project. Next, you can, if appropriate, give a brief tour of the
configuration files and scripts that make your project possible. Your video
should be 5-10 minutes long.

Please take time to watch your classmate's videos and post comments, questions,
and suggestions.

_This is an individual project._

DIY Project
-----------
One of the key technical tasks of an educational technologist or instructional
designer is to research and evaluate possible solutions to a problem and then
implement a plan to test a possible solution. Real world problems often require
the combination of several systems in a new way, suffer from incomplete or
inaccurate documentation, and are hindered by time or resources/financial
constraints.

With this in mind, you will choose an RPI project that you find interesting and
engaging to pursue for your final project. You will be responsible for
gathering/purchasing the materials to complete the project.

You will be evaluated on:

- skill with RPI hardware
- skill with RPI software
- creativity of the project chosen
- risk/scope of the project
- reflection on the process

This is a _paired project._ You and a partner of your choice will work on the
same project. You will share a Trello and set goals together, however you will
both complete the project independently and will receive an individual grade.
Your partner will serve as a resource for planning and troubleshooting problems
that arise during the course of the project.

With the instructors' permission, you may work on this project individually.

Here are a few raspberry pi project ideas that will give you a sense of the size and
scope of what you can do for your final project.

1. **MyCroft Open Source personal assistant**<br>
   <https://mycroft.ai><br>
   MyCroft is a Free Software alternative to systems such as Alexa and Google Assistant.
   While it runs on a regular desktop computer, it was designed to work on a RPI.
   You can download a pre-configured SD Card image to get started with "PiCroft".
   For this project, you will download and configure MyCroft for your Pi; create
   and connect to your online account, configure and test the microphone and audio
   output, and customize the features and functionality of your RPI assistant.
   Start at the [mycroft site](https://mycroft.ai) for all of the information you need to get started.
2. **RetroPi Arcade Console**<br>
   <https://retropie.org.uk/><br>
   <img src="https://i0.wp.com/www.hanahaki.com/wp-content/uploads/2018/06/arcade-bartop-raspberry-pi-retropie-mame-2018-diy-tutorial-guide.png?fit=735%2C458&ssl=1" alt="old school arcade games made with retropi" class="img-fluid d-block">
   Do you think that Fortnite has nothing on the original Streetfighter? That
   Assassin's Creed pales in the glow of Golden Eye? Or do you just want to play
   the Super Mario Bros, the greatest video game of all time? Turn your RPI into
   a video game emulator that can play the classics made for Artari, Nintendo NES, Sega,
   and more. Once you've got the general system up and running, you can add some
   custom controllers and make it an upright arcade.  
3. **Raspberry Pi Light Show**<br>
   <https://www.raspberrypi.org/blog/christmas-lights/> & <https://opensource.com/life/15/2/music-light-show-with-raspberry-pi><br>
   <img src="https://media.giphy.com/media/Kci9K2E4fsvaqymZvO/giphy.gif" alt="very flash xmas light show" class="img-fluid d-block">
   Want to turn your classroom into a disco or put your neighbors to shame this
   Halloween or Christmas? Even if you don't, you should
   [check out this sick RPI Christmas display](https://www.youtube.com/watch?embed=0&v=90oZ52M4IC0).
4. **Mini Creature Home**<br>
   <https://allenheard.wordpress.com/2013/11/06/making-a-mini-beast-habitat-raspberry-pi-style/><br>
   Create an ant or snail home, complete with a live webcam. This project should
   give you lots of ideas if your looking for STEAM projects for younger kids.
5. **MagicMirror**<br>
   <https://magicmirror.builders/><br>
   The magic mirror or smart mirror is an RPI favorite: put a reflective coating
   or 2-way mirrored plexiglass over an old monitor or TV, hook it up to your Pi, and
   throw up you daily calendar, the bus schedule, weather, news, poetry, etc.
6. **Digital (Pi)cture Frame**<br>
   <https://www.makeuseof.com/tag/showerthoughts-earthporn-make-inspiring-raspberry-pi-photo-frame/><br>
   If the _mirror_ seems like it might be too much, how about a digital picture frame?

These are just a few of the many possible projects. You may conceive of your
own project, or check out some of these other ideas:

- [circuit specialists](https://www.circuitspecialists.com/blog/best-raspberry-pi-projects/)
- [tom's hardware](https://www.tomshardware.com/features/best-raspberry-pi-projects)
- [it's foss](https://itsfoss.com/raspberry-pi-projects/)


_Submission Guidelines_

To submit this project, you will upload a narrated screencast video of your
project to YouTube (you can sign in with your Adelphi email account). If you do
not want the video to be public, change the permissions so that it is an
"unlisted" video. Only people with the link will be able to see it. Create a new
thread in the discussion forum with a title for your project. Post the link to
your video here, along with any supporting documentation (screenshots, code,
config files).

Begin the video with a description of who the target users are of this setup and
what your goals are for them. Next, show your project from the user's
perspective, showing how it meets the needs  of the use cases that guided you in
designing the project. Next, you can, if appropriate, give a brief tour of the
configuration files and scripts that make your project possible. Your video
should be 5-10 minutes long.

Class Sessions
===============

Week 0: Before Class Begins
---------------------------
Before our first week of class our goal is to gather all of the materials needed and prepare our computers for participation in this course.

### To Do:
1. Order your Raspberry Pi and related equipment
   ([syllabus: required materials](https://matt.curinga.com/adelphi-ed-tech-courses/school-networks.html#required-materials))
2. [Join Slack](https://auedtech.slack.com) and install the desktop
   and mobile apps ([slack support](https://get.slack.help/hc/en-us))
3. Create an account on [Trello](https://trello.com) and install the
   mobile app ([Trello Support](https://help.trello.com/))

Week 1: Computers & Operating Systems
-------------------------------------
This week we will learn about core computer hardware, and the key software
(Operating Systems) that drive computers. We'll also learn about the specific
hardware of our RPIs and install an operating system so we can take them out
for a test drive. By the end of the week you should have a bootable Raspberry Pi
that is housed in a homemade case of your design. You should be able to log into
your computer with a working display (monitor) and keyboard/mouse. You will
also make sure that it connects to the internet.

### Week 1 Guiding Questions:

1. How does a modern computer work?
2. What makes a computer a _computer_?
3. How is a computer an abstraction of many parts and processes?

### Watch & Read:

1. [Computer Hardware](https://www.youtube.com/watch?embed=0&v=ExxFxD4OSZ0) (Computer parts Explained) [7:48]
2. [RPI Hardware](https://www.youtube.com/watch?embed=0&v=SgR_5Ai64nM) (Urban Penguin) [2:01]
3. [_Unofficial Raspberry Pi Manual_](https://www.makeuseof.com/tag/great-things-small-package-your-unofficial-raspberry-pi-manual/)
  [ [pdf](http://cdn.makeuseof.com/wp-content/uploads/2017/07/Raspberry-Pi-The-Unofficial-Tutorial.pdf) ] Sections 1-3
4. [What is an OS?](https://www.youtube.com/watch?embed=0&v=26QPDBe-NB8) (Crash Course Computer Science) [13:35]
5. Klint Finley. (April 24, 2019) [The WIRED Guide to Open Source Software](https://www.wired.com/story/wired-guide-open-source-software/). _WIRED_.

### To Do:

_Complete all the videos/readings before the first live session on Wednesday._

1. Complete all of the readings _before_ our first class meeting.
2. Install Raspberry Pi OS on your RPI. [[instructions](https://www.raspberrypi.org/software/)]
3. Make a case for your RPI and post a picture on Slack (see _Unofficial Manual_ Section 3.1)
4. Get to know your new computer by connecting it to your network, installing software, etc.
5. After your Pi is up and running, the first thing you want to enable is a remote connection via `ssh`. [Follow this guide to enabling `ssh`](https://www.raspberrypi.org/documentation/remote-access/ssh/).

### Live Lab Agenda

1. Welcome & Introductions
2. Kahoot competition: review of videos/readings
3. Breakout Rooms
   A. Room A: Installing Raspberry Pi OS and Booting your Pi for the first time
   B. Room B: Configure ssh, make a case
4. Getting ready for next week: terminal basics

Week 2: The Command Line
------------------------
This week we will learn how to interact with our computer using the command line
(aka terminal). The command line interface (CLI) offers an alternative to the
graphical user interface (GUI) we are more familiar with. Wile the terminal
hearkens back to the early days of computing, its still very much alive for
systems administrators, software developers, and others. In particular, complex
tasks can be accomplished with a few lines of text, remote computers can be
easily accessed, and all manner of tasks can be automated (and scheduled).
Specifically, after gaining fluency with the command line, you will be able to
log into your RPI from your regular laptop or desktop computer in order to
configure and control it. To get started on the command line we'll check out
Terminus, a game developed at MIT to introduce the players to the command line.

In addition to jumping into the command line, by the end of the week you will
have customized your RPI by installing software packages through `apt` and the
GUI. You will also choose your topic for the first project and set up a Trello
with a Board for your project and milestones for each week until it's due.

### Week 2 Guiding Questions:
1. How is a command line interface different from the more familiar graphical user interface?
2. What is gained from a CLI? What is lost?

### Watch, Play, & Read:
1. Read [What is Free Software?](https://www.gnu.org/philosophy/free-sw.en.html)
2. Watch [Keyboards & Command Line Interfaces: Crash Course Computer Science #22](https://www.youtube.com/watch?embed=0&v=4RPtJ9UyHS0)[11:23] Hackers are fast typists.
2. Play [Terminus](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html) for at least an hour. Post on Slack how far you get.
3. Read [Chapter 5: Getting to grips with the GUI in _Unofficial Tutorial_](https://www.makeuseof.com/tag/great-things-small-package-your-unofficial-raspberry-pi-manual/#5-getting-to-grips-with-the-gui)

### To Do:
1. Update the software on your RPI with `apt` (hint `sudo apt update` then `sudo apt dist-upgrade`)
2. Install VNC and [connect to your RPI from your computer](https://www.raspberrypi.org/documentation/remote-access/vnc/)
3. Install at least 2 programs on your RPI using `apt` or the graphical software package manager.
   See [5 Ways To Install Software On Raspberry Pi](https://www.makeuseof.com/tag/three-ways-to-install-software-on-raspberry-pi/).
4. Post in the FOSS Apps Discussion which apps you installed and a brief review of them.
5. Create a Trello Board for your project and invite the course instructors as
   collaborators.

### Live Lab Agenda

1. Welcome, questions
2. Command line Quizlet
3. Breakout rooms:
   A. Installing and connecting to VNC
   B. Managing your Pi server through `ssh`
4. Project ideas and Trello Updates

Week 3: Users, Groups, Files, & Permissions
-------------------------------------------
As you're working on finishing up your first RPI project, we'll take a deeper
look at how files, permissions and security works on RPI and in linux/unix operating
systems generally. To better understand how to work with files, we'll take a look
at file archives (multiple files and directories combined in a single file) and
compression (reducing the size of a file). Because your programs all run as a
"user" (either root or their own user), it's important to understand files and
permissions to troubleshoot problems.

### Week 3 Guiding Questions:
1. How do you secure digital resources?
2. Is the unix approach of users and groups sufficient for all security needs?

### Watch & Read:
1. Watch [Files & File Systems: Crash Course Computer Science #20](https://www.youtube.com/watch?embed=0&v=KN8YgJnShPM) [12:02]
2. Watch [Compression: Crash Course Computer Science #21](https://www.youtube.com/watch?embed=0&v=OtDxDvCpPL4) [12:47]
3. Read [Understanding Basic File Permissions and ownership in Linux](https://www.thegeekdiary.com/understanding-basic-file-permissions-and-ownership-in-linux/)
4. Watch [Linux Terminal 201: How To Use tar, gzip, bzip2, and zip - HakTip 156](https://www.youtube.com/watch?embed=0&v=f8-7lhs4ky0) [11:32]
5. Docs [Linux users](https://www.raspberrypi.org/documentation/linux/usage/users.md)
4. Docs [How To Extract Zip, Gz, Tar, Bz2, 7z, Xz and Rar File in Linux](https://tecadmin.net/extract-archive-file-linux/)

### To Do:
- finish RPI Client or Server Setup project by the end of the week

Week 4: Networks
----------------
How does the internet work? What happens after you hit enter on a search term
on [Duck Duck Go](https://duckduckgo.com/spread)? How does Spotify get music
to your phone to your wireless earbuds? A deeper understanding of different
networking hardware, software, and protocols will help us better understand
the networked software we're installing, configuring, and troubleshooting.

### Week 4 Guiding Questions:
1. How does the internet work as a collection of networks?
2. How does a multi-layered model allow for abstraction between different layers?

### Watch:
1. [How the Internet Works in 5 Minutes](https://www.youtube.com/watch?embed=0&v=7_LPdttKXPc) [4:48]
2. [The Internet: IP Addresses & DNS](https://www.youtube.com/watch?embed=0&v=5o8CwafCxnU) [6:44]
3. [The Internet: Wires, Cables & Wifi](https://www.youtube.com/watch?embed=0&v=ZhEf7e4kopM&list=PLzdnOPI1iJNfMRZm5DDxco3UdsFegvuB7&index=2) [6:41]
4. [The Internet: Packets, Routing & Reliability](https://www.youtube.com/watch?embed=0&v=AYdF7b3nMto&list=PLzdnOPI1iJNfMRZm5DDxco3UdsFegvuB7&index=4) [6:25]

### To Do:
1. Post (with a partner) a written report on one of the network topics (see full instructions below).
2. Choose a topic and a partner for your final project. Create a Trello board
   for it and share it with your partner and the instructors.

### Networking Topic Report Instructions
For a more in-depth look at networking, you will work with a partner to write
a mini report on a related topic. Please: a) choose a partner, and b) choose a
topic from the list below. If you have an idea for a different topic, you may
write about that with approval from the instructors. By the end of the week,
please post your report directly into our _Networking Topics_ forum. Your report
should be roughly 500-800 words. It should give an overview of the topic,
summary of how it works, and discussion of how it's used and why it is (or
isn't) important. Read through the other posts, and ask any follow-up questions.
The instructor and topic authors will do their best to answer your questions.

Possible topics:

 1. Bluetooth
 2. Mesh network
 3. Near Field Communication (NFC)
 4. HTTPS/SSL
 5. 4g/5g/6g
 6. BitTorrent
 7. Dark Web
 8. Radio-frequency identification (RFID)
 9. Bluetooth Beacons

Week 5: Ethics
-------------------------------------
[As Spider-Man learned](https://www.marvel.com/comics/issue/17610/spider-man_with_great_power._2008_1),
with great power comes great responsibility. We trust the people who run our
networks to keep our information safe, and to not violate our trust while they
do it. Along the way, they may face some hard choices, usually weighing the benefits
of individuals versus the group. We'll take a look at some of the ethical concerns
in "big tech", and also investigate how these same concerns appear in the context
of schools and other educational institutions.

### Week 5 Guiding Questions:

1. How do school systems balance student privacy and autonomy, with safety and learning efficiency?
2. What are the key ethical concerns of embedding corporate interests (and technology) into public spaces like schools?

### Read:
1. **Monitoring Student Social Media**
  - Karen Turner. April 22, 2016. [Schools are helping police spy on kids’ social media activity](https://www.washingtonpost.com/news/the-switch/wp/2016/04/22/schools-are-helping-police-spy-on-kids-social-media-activity/). _The Washington Post_.
  - Aaron Leibowitz. September 6, 2018. [Could Monitoring Students on Social Media Stop the Next School Shooting?](https://www.nytimes.com/2018/09/06/us/social-media-monitoring-school-shootings.html). _The New York Times_.
  - Tom Simonite. August 20, 2018. [Schools Are Mining Students' Social Media Posts for Signs of Trouble](https://www.wired.com/story/algorithms-monitor-student-social-media-posts/). _Wired_.
2. **Student Data**
  - [Student Privacy](https://www.eff.org/issues/student-privacy). _Electronic Frontier Foundation_.
  - Natasha Singer. May 13, 2017. [How Google Took Over the Classroom](https://www.nytimes.com/2017/05/13/technology/google-education-chromebooks-schools.html). _The New York Times_.
  - Gennie Gebhart. March 28, 2017. [Privacy By Practice, Not Just By Policy: A System Administrator Advocating for Student Privacy](https://www.eff.org/deeplinks/2017/03/privacy-practice-not-just-policy-system-administrator-advocating-student-privacy). _Electronic Frontier Foundation_.

### To Do:
1. Complete ethics readings and come to class prepared to discuss and debate.
2. Update your Trello project with the work you've completed this week. Identify any issues and get help as needed.

Week 6: Final Project Due
-------------------------
This is a working week where our full attention is focused on producing great
final projects.

### To Do:

- turn in your final project and have a great summer!
