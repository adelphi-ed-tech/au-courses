% Programming web-based educational media
% Matthew X. Curinga
  Antonios Saravanos

**EDT 603 _Programming web-based educational media_, Spring 2013**

~~~~~~~~~~~~~~~~~~~~~~~~~~{.html}
<!DOCTYPE html>
<html>
  <body>
    <blockquote>
      Anyone who has lost track of time when
      using a computer knows the propensity
      to dream, the urge to make dreams come
      true and the tendency to miss
      lunch.<br>
      <strong>Tim Berners-Lee</strong>
      <em>, inventor of the world wide web</em>
    </blockquote>
  </body>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** In this course students learn techniques of web
programming to develop interactive, educational media. Using the
web programming language and web development technologies (HTML5,
Javascript, CSS), students gain practice in the object oriented
programming and design of interactive software. For their final
project, students will create their own interactive educational website.

**Key words:** computer science, web development, python, interaction
design, django, html, html5, css, javascript, OOP


Required Books
========================================================================

Duckett, J. T. (2011). [_Html & css: design and
build websites (1st ed.)_](http://htmlandcssbook.com/).
Indianapolis, IN: Wiley Pubishing, Inc.

![](http://img1.imagesbn.com/p/9781118008188_p0_v1_s260x420.JPG)

Optional Books
========================================================================

Anderson, T. (Ed.). (2008). [*Theory and practice of online
learning*](http://www.aupress.ca/index.php/books/120146). Edmonton:
AU Press.

Greenfeld, D., & Roy, A. (2013). [_Two scoops of django: best
practices for Django
1.5._](http://twoscoopspress.org/products/two-scoops-of-django-1-5-e-b
ook-bundle)



Bibliography
========================================================================

Castro, Elizabeth. 2010. *Html 5 Visual Quickstart Guide.* Peachpit
Press. ISBN 9780321719614.

Hayward, J. (2011). *Django JavaScript Integration: AJAX and jQuery*.
Packet Publishing. ISBN 1849510342

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. M. (1994). *Design
Patterns: Elements of Reusable Object-Oriented Software* (1st ed.).
Reading Mass.: Addison-Wesley Professional. ISBN 0201633612.

Knuth, Donald. 1997. *The art of computer programming.* Addison-Wesley
Pub. Co. Reading Mass. ISBN 9780201896831.

Moreno, R., & Mayer, R. (2007). Interactive multimodal learning
environments. *Educational Psychology Review*, *19*(3), 309–326.

Moreno, R. (2006). Learning in High-Tech and Multimedia Environments.
*Current Directions in Psychological Science*, *15*(2), 63 -67.

Shneiderman, B. (2000). Universal usability. *Communications of the
ACM*, *43*(5), 84–91.

Shneiderman, B. (2002). Promoting universal usability with multi-layer
interface design. *ACM SIGCAPH Computers and the Physically
Handicapped*, (73-74), 8.

Teague, Jason. 2011. *CSS3: Visual QuickStart Guide.* Peachpit Press.
Berkeley CA. ISBN 9780321719638.

Zelle, John. 2004. *Python programming: an introduction to computer
science.*Franklin Beedle. Wilsonville, OR. ISBN 9781887902991.

Schedule 
========================================================================

Day   Topic                                                       Due
----- ----------------------------------------------------------  ----
1     How the web works, Tools, Document Structure, Media
2     Style & Usability
3     Introducing Javascript                                      Single Page Site
4     Variables and Functions
5     Manipulating DOM                                            Redesign
6     Events
7     Data structures
8     Testing/Refactoring                                         Interactive application


Assignments & Grading
========================================================================

Single Page Website (30%)
-----------------------------------

Students will build a single-page,
informational website on a topic of their choice. Their website
will be composed of HTML, CSS, and (optionally) Javascript. It
will display their fluency with the HTML elements, styling
with CSS, and enhancing user experience with Javascript. The
content of the website is entirely up to the student. They are
encouraged to create a website on something they are already
familiar with and interested in. This is an individual project.

The project will be graded on the following criteria:

1. **Technical design (15 pts):**
    - is html code well formatted and error free?
    - are html elements used appropriately 
      to give semantic structure to the document?
    - are elements combined in ways to make complex layouts?
    - is the document elegant? does it use tags minimally, 
      but in a way that makes it clear for developers to read?
2. **Graphic design (10 pts):**
    - aesthetics
    - usability
    - media (images, video, audio)
    - typography
3. **Information architecture (10 pts):**
    - logical structure of information
    - organization of internal links on page
4. **Impact (5 pts):**
    - does the site deliver an important message?
    - do the design and content (copy) work together?

Single Page Website Redesign (30%)
-----------------------------------
Building on the initial single page websites, students will form pairs or groups
to collaborate to improve and extend their websites.

The new website must:

- be mobile accessible
- include enhanced features using Javascript



Interactive web application (40%)
----------------------------------------

Using Javascript, HTML, and CSS students will design and develop an
ineractive educational website.


Web & Digital Media Toolbox and Resources
=========================================

Software & Tools
-----------------
The first step in becoming a web developer is to get your computer
set up to start writing code and testing it out. At the very least
you will need a ``text editor`` and a ``web browser``. I'm guessing
you have a web browser already.

This short, curated list is the software we will be using.

* Text Editor
    - [Sublime](http://www.sublimetext.com/) (free trial, Mac, Win, Linux)
* Browser
    - [Firefox](http://www.firefox.com), our go-to browser, better with [the firebug extension](https://addons.mozilla.org/en-US/firefox/addon/firebug/)
    - [Safari](http://support.apple.com/kb/dl1531), to get a second look
    - [Chrome](http://www.google.com/chrome/), to test you site in Chrome
    - [Internet Explorer](http://windows.microsoft.com/en-us/internet-explorer/download-ie), you might as well take a look in IE, too, either on your old windows box or in emulation
* Source control
    - [git](http://git-scm.com/downloads)
* FTP/SFTP/SCP Clients
    - [FileZilla](https://filezilla-project.org/download.php?type=client), cross platform
    - [CyberDuck](http://cyberduck.io/), mac
    - [WinSCP](http://winscp.net/eng/index.php), windows
* Windows stuff
    - [PuTTy](http://www.chiark.greenend.org.uk/~sgtatham/putty/), ssh client
    - [Cygwin](https://www.cygwin.com/), create a GNU/linux-like terminal on Windows.
      This is a big install, but worth it if you are going to stick with windows
* Linux
    - Linux is a great platform for programmers and web developers
    - many of the software is written/test on linux
    - many guides assume linux
    - your public website, eventually, will run on linux (in all likeliness)
    - so, check out [Ubuntu](http://www.ubuntu.com/) and maybe give it
      a shot, especially if you have a Windows laptop
* Virtualization
    - want to try linux but can't commit?
    - want to install IE but hate Windows?
    - give [VirtualBox](https://www.virtualbox.org/) a shot
* Media editing
    - [Gimp](http://www.gimp.org/) for photo editing and raster images (instead of photoshop)
    - [Inkscape](http://inkscape.org/) for vector graphics (like SVGs)
    - [Audacity](http://audacity.sourceforge.net/) for editing and creating audio files
    - [LibreOffice Draw](http://www.libreoffice.org/features/draw/) is great for creating charts and diagrams, good for flowcharting and wireframes of software/sites you're working on
    - Color picker: a tool to find the hex or RGB code for colors on your desktop
        - OSX (built-in): [DigitalColor Meter](http://www.techrepublic.com/blog/apple-in-the-enterprise/discover-the-digitalcolor-meter-tool-on-your-mac/)
        - Win: [List of Eyedropper](http://www.hongkiat.com/blog/eyedroppers-color-pickers-for-designers/ "any one of the Windows ones should work")

Books and online resources
--------------------------

### Documentation & Reference websites
- [World Wide Web Consortium](http://w3.org)
- [Mozilla Developer Network](https://developer.mozilla.org/en-US/)
- [jQuery](http://jquery.com/)
- [W3 Schools](http://www.w3schools.com/)
- [Regular Expressions](http://www.regexr.com/)

### Books
- [HTML and CSS: Design and Build Websites](http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118008189.html), our textbook
- [JavaScript & jQuery: Interactive Front-End Web Development Hardcover](http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118871650.html), also J. Duckett, same series
- [Dive into HTML 5](http://diveintohtml5.info/) [free online]
- [The Elements of Typographic Style Applied to the Web](http://webtypography.net/toc/) [free online]
- [Mastering Regular Expressions](http://shop.oreilly.com/product/9780596528126.do)

### Tutorial websites & online learning
- [Code Academcy](http://www.codecademy.com/)
- [P2PU School of webcraft](https://p2pu.org/en/schools/school-of-webcraft/)
- [Treehouse](http://teamtreehouse.com/) [paid]
- [Thinkful](http://www.thinkful.com/)
- [GeekCamp::HTML5 Tutorial](http://www.geekchamp.com/html5-tutorials/1-html5-overview)
- [SkilledUp::Learn Web Design](http://www.skilledup.com/learn-web-design-guide/)

### Design, accessibility, UX
- [A List Apart](http://alistapart.com/topic/html)
- [Smashing Magazine](http://www.smashingmagazine.com/)
- [Adobe Kuler](https://color.adobe.com/create/color-wheel/)
- [Nielsen/Norman Group](http://www.nngroup.com/articles/)
- [United States Section 508](http://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)
  - [https://www.section508.gov/](https://www.section508.gov/)
  - [http://webaim.org/standards/508/checklist](http://webaim.org/standards/508/checklist)
- [Usability.gov](http://www.usability.gov/index.html)
- [Research-Based Web Design & Usability Guidelines](http://www.usability.gov/guidelines/guidelines_book.pdf)
- [hex/html color chart](http://www.december.com/html/spec/color.html)

### Online Tools
- [w3c HTML Validation Service](http://validator.w3.org/#validate_by_uri+with_options)
- [w3c CSS Validation Service](http://jigsaw.w3.org/css-validator/)
- [Pastebin](http://pastebin.com/)
- [HTML Formatter](http://www.freeformatter.com/html-formatter.html)

### Media Resources
- [Creative Commons Search](http://search.creativecommons.org/), for images, music, etc
- [Wikimedia Commons](http://commons.wikimedia.org/wiki/Main_Page), images and other media (including stuff from Wikipedia), curated
- [Open Clip Art](https://openclipart.org/), free vector graphics
- [Creative Commons Music](http://creativecommons.org/music-communities)
- [Fossil Bank](http://fossilbank.wikidot.com/)
- [Colour Lovers Palettes](http://www.colourlovers.com/)
- [DaFonts](http://www.dafont.com/)

