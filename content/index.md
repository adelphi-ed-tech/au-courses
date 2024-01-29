---
layout: home
title: "Adelphi Ed Tech Courses"
author: "Matthew X. Curinga"
---

<div class="row mt-4 p-4">
{% for course in site.data.courses %}
    <div class="col-md-2 rounded mb-4 shadow">
        <img class="rounded-top d-block img-fluid" src="img/{{course.img.src}}" alt="{{course.img.alt}}">
        {% if course.url %}
            <strong class="d-block text-center py-1"><a class="link-underline link-underline-opacity-0" href="{{course.url}}">{{course.course}}</a></strong>
        {% else %}
            <strong class="d-block text-center py-1">{{course.course}}</strong>
        {% endif %}
    </div>
{% endfor %}
</div>

