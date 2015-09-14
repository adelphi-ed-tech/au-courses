#! /usr/bin/python3

import subprocess
import os
import os.path
from string import Template
import datetime

try:
    from wordpress_xmlrpc import Client
    from wordpress_xmlrpc.methods import posts
    from wordpress_xmlrpc import WordPressPage
    pushToWordPress = True
    
    # you need to create your own settings.py, or just enter these vars here
    from settings import url, user, pw
except:
    print("no wordpress support")
    pushToWordPress = False

def GenerateAllCourses(html, raw, word):
    courses = [f[:-3] for f in os.listdir("courses") if f.endswith(".md")]
    pagesToBuild = []
    for c in courses:
        if(IsModified(c)):
            print("rebuilding course: %s" % (c,))
            GenerateCourse(html, raw, word, c)
            pagesToBuild.append(c)
    PushToWeb(pagesToBuild)

def ModTimeIfExists(path):
    if os.path.exists(path):
        return os.path.getmtime(path)
    return 0

def IsModified(course):
    """check to see if any relevant course materials have been modified
       since this course was last built."""
    rawMod = ModTimeIfExists("raw/{}.html".format(course))
    outMod = ModTimeIfExists("out/{}.html".format(course))
    wordMod = ModTimeIfExists("word/{}.docx".format(course))

    lastBuilt = min(rawMod, outMod, wordMod)

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
    
def GenerateCourse(html, raw, word, course):
    pwd = os.getcwd()
    args = {}
    args["course"] = course
    courseCSS = os.path.join(pwd,"css/%s.css" % (course,))
    args["courseCSS"] = IncludeIfExists(courseCSS, "-H")


    footer = os.path.join(pwd,"tmpl/footer.html")
    args["footer"] = IncludeIfExists(footer, "-A")

    # build standalone HTML versions
    args["out"] = "out"
    cmd = html.substitute(args)
    subprocess.check_call(cmd,shell=True)

    # # build HTML fragment version
    # args["out"] = "raw"
    # cmd = raw.substitute(args)
    # subprocess.check_call(cmd,shell=True)

    # build MS Word version (due to institutional coercion)
    args["out"] = "word"
    cmd = word.substitute(args)
    print(cmd)

    try:
        subprocess.check_call(cmd,shell=True)
    except Exception as ex:
        pass
        # print('failed to generate word doc for {}'.format(course))
        # print(ex)



def GetWebPages():
    # the most stable way to access WordPress is to
    # hardcode the post IDs in here
    ids = [817,819,822,841,834,836,839,807,812,1156,1131,847,1428]
    pages = dict()
    client = Client(url,user,pw)
    for postId in ids:
        page = client.call(posts.GetPost(postId))
        pages[page.slug] = page

    return pages

def PushToWeb(courses):
    if not pushToWordPress:
        return
    client = Client(url,user,pw)
    pages = GetWebPages()

    for course in courses:
        print("pushing to web", course)
        try:
            page = pages[course]
            f = open("raw/%s.html" % (course,),"r")
            page.content = f.read()
            f.close()
        except IOError as ioe:
            print("** no raw file found for",course)
            print(ioe)
            continue
        except KeyError as keyx:
            print("** no course found on blog",course)
            print(keyx)
            continue

        result = client.call(posts.EditPost(page.id, page))
        if result:
            print("Successfully updated ", page.slug)
        else:
            print("******Warning********: could not update ", page.slug)

def IncludeIfExists(path, arg):
    if(os.path.exists(path)):
        return "%s %s" %(arg, path)
    return ""

def GetTemplate(tmpl):
    dt = datetime.datetime.now()
    return Template("pandoc --email-obfuscation=none -S --toc --highlight-style zenburn -t html5 --section-divs -V date='%s' -H $$(pwd)/css/%s.css $courseCSS $footer --template=$$(pwd)/tmpl/%s.html $$(pwd)/courses/$course.md >$out/$course.html" % (dt.strftime("%A, %d. %B %Y %I:%M%p"),tmpl,tmpl))

def GetWordTemplate():
    dt = datetime.datetime.now()
    return Template("pandoc -S --toc --highlight-style zenburn -t docx -V date='%s' $$(pwd)/courses/$course.md -o word/$course.docx" % (dt.strftime("%A, %d. %B %Y %I:%M%p")))

    
def main():
    html = GetTemplate("adelphi")
    print(html)
    raw = GetTemplate("raw")
    word = GetWordTemplate()
    GenerateAllCourses(html, raw, word)

if __name__ == "__main__":
    main()
