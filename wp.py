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
    f = open("raw/%s.html" % (course.slug,),"r")
    course.content = f.read()
    f.close()

    print("attempting update of post: ({}) {}".format(course.id,course.slug))
    result = client.call(posts.EditPost(course.id, course))
    result = True
    if result:
        print("Successfully updated ", course.slug)
    else:
        print("******Warning********: could not update ", course.slug)


