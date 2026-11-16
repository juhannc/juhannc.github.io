---
layout: profile
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---
<header class="profile-header">
  <p class="profile-eyebrow">Find Your Way</p>
  <h1 id="profile-title">Sitemap</h1>
  <p class="profile-lead">Research, experience, and publications in one place.</p>
</header>

<section class="profile-section" aria-labelledby="main-pages">
  <h2 id="main-pages">Main Pages</h2>
  <ul class="sitemap-links">
    <li><a href="{{ '/' | relative_url }}">Homepage</a> — research interests and background.</li>
    {% for link in site.data.navigation.main %}
    <li><a href="{{ link.url | relative_url }}">{{ link.title }}</a></li>
    {% endfor %}
  </ul>
</section>

<section class="profile-section" aria-labelledby="resources">
  <h2 id="resources">Downloads &amp; Machine-Readable Information</h2>
  <ul class="sitemap-links">
    <li><a href="{{ '/files/Johann_Christensen_Resume.pdf' | relative_url }}">Resume PDF</a></li>
    <li><a href="{{ '/llms.txt' | relative_url }}">Profile for LLMs (llms.txt)</a></li>
    <li><a href="{{ '/sitemap.xml' | relative_url }}">XML Sitemap</a></li>
  </ul>
</section>

{% assign publications = site.publications | sort: 'date' | reverse %}
{% for category in site.publication_category %}
  {% assign entries = publications | where: 'category', category[0] %}
  {% if entries.size > 0 %}
  <section class="profile-section" aria-labelledby="sitemap-{{ category[0] }}">
    <h2 id="sitemap-{{ category[0] }}">{{ category[1].title }}</h2>
    <ul class="sitemap-links">
      {% for publication in entries %}
      <li>
        <a href="{{ publication.url | relative_url }}">{{ publication.title }}</a>
        <span class="sitemap-meta">{{ publication.date | date: '%Y' }}{% if publication.publication_status %} · {{ publication.publication_status }}{% endif %}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
{% endfor %}
