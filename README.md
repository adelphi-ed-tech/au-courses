# Adelphi University Educational Technology Courses
The goal of this project is to create a space where the course syllabi
for the program in [Educational Technology](http://education.adelphi.edu/ed-tech)
can be easily shared, edited, and remixed.

## Directories and components

### courses
This is where the action is -- the actual syllabi are located in the /courses dir.
They are written in markdown using the [pandoc](http://johnmacfarlane.net/pandoc/) extensions.
These if you are interseted in the course content, this is the place to look, you can pretty
much ignore the rest of the project.

### build.py
This script builds all of the courses into standalone html files.
Basically, it does this:

* look up all the files in /courses
* grab a template from /tmpl
* include the main css for that tmeplate from /css
* optionally include a course-specific css
* execute pandoc to build html files to /out

To run the script, you need Python (probably will work with whatever version you have installed) and pandoc.

The script works for me, but is very rough. For example, there is no way to change the template without editing the script.
Also the only template so far is the Adelphi template, but it would be easy enough to build a plain and a mobile template.

### out
Once you run build, here are your html course syllabi, which should look nice and stylish.
I use rsync to push these to the live website:
http://matt.curinga.com/courses



