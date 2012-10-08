#! /usr/bin/python

import subprocess
import os
import os.path
from string import Template
import datetime

def GenerateAllCourses(html, raw):
    courses = [f[:-3] for f in os.listdir("courses") if f.endswith(".md")]
    for c in courses:
        if(IsModified(c)):
            print("rebuilding course: %s" % (c,))
            GenerateCourse(html, raw, c)

def IsModified(course):
    if(not os.path.exists("out/%s.html" % (course,))):
        return True
    srcMod = os.path.getmtime("courses/%s.md" % (course,))
    cssMod = os.path.getmtime("css/adelphi.css")
    customCssMod = 0
    
    if(os.path.exists("css/%s.css" % (course,))):
        customCssMod = os.path.getmtime("css/%s.css" % (course,))
    tmplMod = os.path.getmtime("tmpl/%s.html" % ("adelphi",))
    footerMod = os.path.getmtime("tmpl/%s.html" % ("footer",))

    outMod = os.path.getmtime("out/%s.html" % (course,))
    return (srcMod > outMod) \
           or (cssMod > outMod) \
           or (tmplMod > outMod) \
           or (customCssMod > outMod) \
           or (footerMod > outMod)

def GenerateCourse(html, raw, course):
    pwd = os.getcwd()
    args = dict()
    args["course"] = course
    courseCSS = os.path.join(pwd,"css/%s.css" % (course,))
    args["courseCSS"] = IncludeIfExists(courseCSS, "-H")

    footer = os.path.join(pwd,"tmpl/footer.html")
    args["footer"] = IncludeIfExists(footer, "-A")

    cmd = html.substitute(args)
    subprocess.check_call(cmd,shell=True)

    cmd = raw.substitute(args)
    subprocess.check_call(cmd,shell=True)


def IncludeIfExists(path, arg):
    if(os.path.exists(path)):
        return "%s %s" %(arg, path)
    return ""

def GetTemplate(tmpl=None):
    dt = datetime.datetime.now()

    print(tmpl)

    if tmpl == None:
        return Template("pandoc --toc --section-divs -V date='%s' $$(pwd)/courses/$course.md >raw/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),))

    return Template("pandoc --section-divs -V date='%s' -H $$(pwd)/css/%s.css $courseCSS $footer --template=$$(pwd)/tmpl/%s.html $$(pwd)/courses/$course.md >out/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),tmpl,tmpl))
    
def main():
    html = GetTemplate("adelphi")
    
    assert(html != None)
    raw = GetTemplate()
    GenerateAllCourses(html, raw)

if __name__ == "__main__":
    main()
