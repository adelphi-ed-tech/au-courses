import subprocess
import os
import os.path
from string import Template
import datetime


def Deploy():
    pass

def GenerateAllCourses(tmpl):
    courses = [f[:-3] for f in os.listdir("courses") if f.endswith(".md")]
    for c in courses:
        GenerateCourse(tmpl,c)

def GenerateCourse(tmpl,course):
        args = dict()
        args["course"] = course
        args["courseCSS"] = "-H $$(pwd)/css/%s.css" % (course,)
        if(not os.path.exists("css/%s.css" % (course,))):
            args["courseCSS"] = ""
        cmd = tmpl.substitute(args)
        subprocess.check_call(cmd,shell=True)

def SetTemplate(templateName):
    dt = datetime.datetime.now()
    pan = Template("pandoc --section-divs -V date='%s' -H $$(pwd)/css/%s.css $courseCSS --template=$$(pwd)/tmpl/%s.html $$(pwd)/courses/$course.md >out/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),templateName,templateName))
    return pan

def main():
    pan = SetTemplate("adelphi")
    GenerateAllCourses(pan)


if __name__ == "__main__":
    main()
