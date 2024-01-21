---
layout: bold
title: "Adelphi Ed Tech Courses"
author: "Matthew X. Curinga"
---

<div class="IndexHeader">
    {% include top-nav.html %}
    <div class="TitleText d-block text-center mx-auto text-light" style="max-width: 800px;">
        Adelphi University Master's of Arts in Educational Technology
    </div>
    <div class="d-block text-center mx-auto text-light pb-2" style="max-width: 800px; font-size: 32px">
        <strong>100% online</strong><br>
        <strong>7 core courses ~ 3 electives ~ 1 thesis</strong>
    </div>
</div>

<div class="row mx-4">
{% for course in site.data.courses %}
    <div class="col-md-2 rounded p-0 m-4 shadow">
        <img class="rounded-top d-block img-fluid" src="img/{{course.img.src}}" alt="{{course.img.alt}}">
        {% if course.url %}
            <strong class="d-block text-center py-1"><a class="link-underline link-underline-opacity-0" href="{{course.url}}">{{course.course}}</a></strong>
        {% else %}
            <strong class="d-block text-center py-1">{{course.course}}</strong>
        {% endif %}
    </div>
{% endfor %}
</div>

