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


def ModTimeIfExists(path):
    if os.path.exists(path):
        return os.path.getmtime(path)
    return 0

def IsModified(course):
    """check to see if any relevant course materials have been modified
       since this course was last built."""
    rawMod = ModTimeIfExists("raw/%s.html" % (course,))
    outMod = ModTimeIfExists("out/%s.html" % (course,))

    lastBuilt = min(rawMod,outMod)

    if(lastBuilt == 0):
        return True

    # if any of these have changed since the last build, rebuild
    srcMod = ModTimeIfExists("courses/%s.md" % (course,))
    cssMod = ModTimeIfExists("css/adelphi.css")
    customCssMod = ModTimeIfExists("css/%s.css" % (course,))
    tmplMod = ModTimeIfExists("tmpl/%s.html" % ("adelphi",))
    rawTmplMod = ModTimeIfExists("tmpl/%s.html" % ("raw",))
    footerMod = ModTimeIfExists("tmpl/%s.html" % ("footer",))
    
    assert srcMod > 0
    assert tmplMod > 0
    assert rawTmplMod > 0
    
    #if the source files are 0, then we don't have them
    changes = [d for d in [srcMod,cssMod,customCssMod,tmplMod,rawTmplMod,footerMod] if d > 0]
    
    mostRecentChange = max(changes)

    return mostRecentChange > lastBuilt
    
def GenerateCourse(html, raw, course):
    pwd = os.getcwd()
    args = dict()
    args["course"] = course
    courseCSS = os.path.join(pwd,"css/%s.css" % (course,))
    args["courseCSS"] = IncludeIfExists(courseCSS, "-H")

    footer = os.path.join(pwd,"tmpl/footer.html")
    args["footer"] = IncludeIfExists(footer, "-A")
    args["out"] = "out"

    cmd = html.substitute(args)
    subprocess.check_call(cmd,shell=True)

    args["out"] = "raw"
    cmd = raw.substitute(args)
    subprocess.check_call(cmd,shell=True)


def IncludeIfExists(path, arg):
    if(os.path.exists(path)):
        return "%s %s" %(arg, path)
    return ""

def GetTemplate(tmpl):
    dt = datetime.datetime.now()

    return Template("pandoc --toc --section-divs -V date='%s' -H $$(pwd)/css/%s.css $courseCSS $footer --template=$$(pwd)/tmpl/%s.html $$(pwd)/courses/$course.md >$out/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),tmpl,tmpl))
    
def main():
    html = GetTemplate("adelphi")
    raw = GetTemplate("raw")
    GenerateAllCourses(html, raw)

if __name__ == "__main__":
    main()
