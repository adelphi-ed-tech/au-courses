#! /usr/bin/python3

import subprocess
import os
import os.path
from string import Template
import datetime

def GenerateAllCourses(html, raw, word):
    courses = [f[:-3] for f in os.listdir("courses") if f.endswith(".md")]
    pagesToBuild = []
    for c in courses:
        print("rebuilding course: %s" % (c,))
        GenerateCourse(html, raw, word, c)
        pagesToBuild.append(c)

def GenerateCourse(html, raw, word, course):
    pwd = os.getcwd()
    args = {}
    args["course"] = course
    courseCSS = os.path.join(pwd,"css/%s.css" % (course,))
    args["courseCSS"] = IncludeIfExists(courseCSS, "-H")


    footer = os.path.join(pwd,"tmpl/footer.html")
    args["footer"] = IncludeIfExists(footer, "-A")

    # build standalone HTML versions
    args["out"] = "docs"
    cmd = html.substitute(args)
    subprocess.check_call(cmd,shell=True)

    # # build HTML fragment version
    # args["out"] = "raw"
    # cmd = raw.substitute(args)
    # subprocess.check_call(cmd,shell=True)

    # build MS Word version (due to institutional coercion)
    args["out"] = "word"
    cmd = word.substitute(args)
    try:
        subprocess.check_call(cmd,shell=True)
    except Exception as ex:
        print('failed to generate word doc for {}'.format(course))
        # print(ex)



def IncludeIfExists(path, arg):
    if(os.path.exists(path)):
        return "%s %s" %(arg, path)
    return ""

def GetTemplate(tmpl):
    dt = datetime.datetime.now()
    return Template("pandoc --email-obfuscation=none --toc --highlight-style zenburn -t html5 --section-divs -V date='%s' -H $$(pwd)/css/%s.css $courseCSS $footer --include-after $$(pwd)/tmpl/boot_styles.js --template=$$(pwd)/tmpl/%s.html $$(pwd)/courses/$course.md >$out/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),tmpl,tmpl))

def GetWordTemplate():
    dt = datetime.datetime.now()
    return Template("pandoc --toc --highlight-style zenburn -t docx -V date='%s' $$(pwd)/courses/$course.md -o word/$course.docx" % (dt.strftime("%A, %d. %B %Y %I:%M%p")))


def main():
    html = GetTemplate("adelphi")
    raw = GetTemplate("raw")
    word = GetWordTemplate()
    GenerateAllCourses(html, raw, word)

if __name__ == "__main__":
    main()
