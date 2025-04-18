---
title: Georgia Tech
icon: fas fa-graduation-cap
order: 3
---

{% assign gardening_posts = site.categories.GeorgiaTech %}
{% if gardening_posts %}
  <ul>
    {% for post in gardening_posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span>{{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
{% else %}
  <p>No posts found in the Gardening category.</p>
{% endif %}