#! /usr/bin/python

import subprocess
import os
import os.path
from string import Template
import datetime

def GenerateAllCourses(tmpl):
    courses = [f[:-3] for f in os.listdir("courses") if f.endswith(".md")]
    for c in courses:
        GenerateCourse(tmpl,c)

def GenerateCourse(tmpl,course):
        pwd = os.getcwd()
        args = dict()
        args["course"] = course
        courseCSS = os.path.join(pwd,"css/%s.css" % (course,))
        args["courseCSS"] = IncludeIfExists(courseCSS, "-H")

        footer = os.path.join(pwd,"tmpl/footer.html")
        args["footer"] = IncludeIfExists(footer, "-A")
        
        cmd = tmpl.substitute(args)
        subprocess.check_call(cmd,shell=True)

def IncludeIfExists(path, arg):
    if(os.path.exists(path)):
        return "%s %s" %(arg, path)
    return ""

def SetTemplate(templateName):
    dt = datetime.datetime.now()
    pan = Template("pandoc --toc --section-divs -V date='%s' -H $$(pwd)/css/%s.css $courseCSS $footer --template=$$(pwd)/tmpl/%s.html $$(pwd)/courses/$course.md >out/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),templateName,templateName))
    return pan

def main():
    pan = SetTemplate("adelphi")
    GenerateAllCourses(pan)

if __name__ == "__main__":
    main()
