Adelphi University Educational Technology Courses
=================================================
The goal of this project is to create a space where the course syllabi
for the program in [Educational Technology](http://education.adelphi.edu/ed-tech)
can be easily shared, edited, and remixed.

[See the course syllabuses online here.](https://adelphi-ed-tech.github.io/au-courses/)

Directories and components
--------------------------

### courses
This is where the action is -- the actual syllabuses are located in the /content
dir. They are written in markdown using the
[pandoc](http://johnmacfarlane.net/pandoc/) extensions. If you are interested in
the course content, this is the place to look, you can pretty much ignore the
rest of the project.

### build.py
This script builds all of the courses into standalone html files.
Basically, it does this:

* look up all the files in /courses
* grab a template from /tmpl
* include the main css for that tmeplate from /css
* optionally include a course-specific css
* execute pandoc to build html files to /out

To run the script, you need Python (probably will work with whatever version you
have installed) and pandoc.

The script works for me, but is very rough. For example, there is no way to
change the template without editing the script. Also the only template so far is
the Adelphi template, but it would be easy enough to build a plain and a mobile
template.

### docs
Once you run build, here are your html course syllabi, which should look nice
and stylish. Courses are built to the `docs` dir and pushed live when committed
to github pages. If you want to include images or other external resources in
your markdown, you should put it in `docs` and reference it as a relative path.


### raw
The HTML for the courses is built here, without any "containing" html. The raw
output is used to push to Wordpress, Blogger, etc. where the framework already
has its own template.
