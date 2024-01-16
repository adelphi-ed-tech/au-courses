---
layout: base
title: "Adelphi Ed Tech Courses"
author: "Matthew X. Curinga"
---


<div class="d-block text-justify" style="max-width: 600px; hyphens: auto;">

{% capture markdown_content %}
The Adelphi _Master's of Arts in Educational Technology_ is a 32-credit
graduate degree offered as a fully online program, with access to facilities
and faculty at the Garden City and Brooklyn campuses. Students complete **21 credits of required coursework** studying cognition and learning sciences, instructional design, digital media studies, and computer science. They choose elective courses, usually in-depth looks at current themes andtechnologies, for an additional **9 credits of electives**. Students complete the Master's with
a [**2 credit thesis** or thesis project which they design with their thesis advisor](thesis.html).

[See a sample plan of study.](plan-of-study.html)
{% endcapture %}
    
{{ markdown_content | markdownify }}

</div>

<div class="row">
{% for course in site.data.courses %}
    <div class="col-md-4">
        <div class="card">
            {% if course.required %}
                <div class="card-header text-light bg-primary">required</div>
            {% else %}
                <div class="card-header text-light bg-success">elective</div>
            {% endif %}

            <div class="card-body">
                <img class="card-img-top" src="img/{{course.img.src}}" alt="{{course.img.alt}}">
                {% if course.url %}
                    <h5 class="card-title"><a href="{{course.url}}">{{course.course}}</a></h5>
                {% else %}
                    <h5 class="card-title"><strong>{{course.course}}</strong></h5>
                {% endif %}
                <p class="card-text">{{course.desc}}</p>
            </div>
        </div>
    </div>
{% endfor %}
</div>