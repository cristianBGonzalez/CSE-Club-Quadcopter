---
layout: page
title: Hello World!
tagline: Working on a quadrotor
---
{% include JB/setup %}

#CSE Quadrotor Project CSUSB

Hello and welcome to our website for the CSE Club Quadorotor project in California Sate University, San Bernardino. This website is mainly made so that group members that are involved in the project will be able to obtain information they need and to post updates. We will tag information "general" for parts of the project that pertain to all members. However, since there might be different subgroups, those groups will have different tags on their posts.

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## Infromation
<ul>
  <li>For more information on the CSE Club please go to the official <a href="www.cse-club.com">CSE Club</a> website.</li> 
  <li>The <a href="http://github.com/egonzalezjr555/CSE-Club-Quadcopter">repository page</a>.</li>
</ul>