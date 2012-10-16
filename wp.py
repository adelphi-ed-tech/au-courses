#!/usr/bin/python3

# wp.py
# push the published courses to a WordPress site

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts

from wordpress_xmlrpc import WordPressPage

# you need to create your own settings.py, or just enter these vars here
from settings import url, user, pw

client = Client(url,user,pw)
pages = client.call(posts.GetPosts({'post_type': 'page'}, results_class=WordPressPage))

courses = [c for c in pages if c.title.lower().startswith("edt") or c.title.lower().startswith("csc")]


for course in courses:
    print("attempting update of post: ({}) {}".format(course.id,course.slug))

    try:
        f = open("raw/%s.html" % (course.slug,),"r")
        course.content = f.read()
        f.close()
    except IOError as ioe:
        print("** no raw file found for",course)
        print(ioe)
        continue

    result = client.call(posts.EditPost(course.id, course))
    print(result)
    if result:
        print("Successfully updated ", course.slug)
    else:
        print("******Warning********: could not update ", course.slug)


