---
layout: resume
title: "CV"
permalink: /cv/
excerpt: "Johann Christensen — Safe AI Engineering, aviation safety, and robotics."
redirect_from:
  - /resume
  - /cv-json/
  - /resume-json
---
<header class="resume-header">
  <div>
    <p class="resume-eyebrow">Curriculum vitae</p>
    <h1 id="resume-title">Johann Christensen</h1>
    <p class="resume-tagline">Expert for Safe AI Engineering <span aria-hidden="true">/</span> PhD Candidate</p>
    <p class="resume-intro">Developing resilient AI systems for aviation, with a focus on Safety-by-Design, operational design domains, and the path to certification.</p>
    <nav class="resume-contact" aria-label="Contact and research profiles">
      <a href="mailto:johannchristensen@outlook.de">Email</a>
      <a href="https://github.com/juhannc">GitHub</a>
      <a href="https://orcid.org/0000-0001-9871-122X">ORCID</a>
      <a href="{{ site.author.googlescholar }}">Google Scholar</a>
    </nav>
  </div>
  <a class="resume-download" href="{{ '/files/CV.pdf' | relative_url }}" download>Download resume <span>PDF ↗</span></a>
</header>

<div class="resume-grid">
  <div class="resume-primary">
    <section aria-labelledby="experience">
      <h2 id="experience">Experience</h2>
      <article class="resume-entry">
        <p class="resume-date">October 2023 – Present <span>Germany</span></p>
        <h3>Research Associate</h3>
        <p class="resume-organization">German Aerospace Center (DLR)</p>
        <ul>
          <li>Developing resilient, safety-critical AI systems for aviation and advancing Safety-by-Design frameworks for AI certification.</li>
          <li>Defining operational design domains (ODDs) and developing ODD-aware training methods for limited data scenarios.</li>
          <li>Developing guardrails for LLMs used as air traffic controllers.</li>
          <li>Contributing to EUROCAE WG-114 on Artificial Intelligence.</li>
          <li>Managing projects with funding of up to €5 million and acquiring national and European funding.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">October 2019 – August 2023 <span>Hamburg, Germany</span></p>
        <h3>AI and Robotics Engineer</h3>
        <p class="resume-organization">ZAL Center of Applied Aeronautical Research</p>
        <ul>
          <li>Developed reinforcement learning systems for industrial applications, with a focus on PPO and SAC.</li>
          <li>Built robots in simulation and hardware, including a ROS-based digital twin of a UR10e.</li>
          <li>Built an MLOps pipeline to accelerate model training and automate CI/CD for deployment to edge devices.</li>
          <li>Acquired a total of €8 million in research funding and managed government-funded projects.</li>
        </ul>
      </article>
    </section>

    <section aria-labelledby="selected-publications">
      <div class="resume-section-heading">
        <h2 id="selected-publications">Selected publications</h2>
        <a href="{{ '/publications/' | relative_url }}">All publications ↗</a>
      </div>
      {% assign selected_keys = 'Christensen2026,Christensen2025,Berro2025,Christensen2024' | split: ',' %}
      <ol class="resume-publications">
        {% for key in selected_keys %}
          {% assign publication = site.publications | where: 'bibkey', key | first %}
          {% if publication %}
          <li>
            <h3><a href="{{ publication.url | relative_url }}">{{ publication.title }}</a></h3>
            <p>{{ publication.venue }} · {{ publication.date | date: '%Y' }}{% if publication.publication_status %} · {{ publication.publication_status }}{% endif %}</p>
          </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>
  </div>

  <div class="resume-secondary">
    <section class="resume-award" aria-labelledby="award">
      <p class="resume-eyebrow">Recognition</p>
      <h2 id="award">Best of Session Paper Award</h2>
      <p>Digital Avionics Systems Conference (DASC), 2024</p>
    </section>

    <section aria-labelledby="education">
      <h2 id="education">Education</h2>
      <article class="resume-entry">
        <p class="resume-date">October 2024 – 2027 (expected)</p>
        <h3>PhD (Dr.-Ing.) in Safe AI Engineering</h3>
        <p class="resume-organization">Ruhr University Bochum</p>
        <p>Working title: On the Development of Safety-by-Design AI-Based Systems in Safety-Critical Applications</p>
        <p class="resume-detail">Supervisor: Prof. Frank Köster</p>
      </article>
      <article class="resume-entry">
        <p class="resume-date">October 2017 – September 2019</p>
        <h3>M.Sc. in Aircraft Systems Engineering</h3>
        <p class="resume-organization">Hamburg University of Technology (TUHH)</p>
      </article>
      <article class="resume-entry">
        <p class="resume-date">October 2018 – September 2019</p>
        <h3>Master’s thesis · UC Berkeley</h3>
        <p>Obstacle Avoidance-Driven Controller for Safety-Critical Aerial Robots</p>
        <p class="resume-detail">Supervisor: Prof. Koushil Sreenath</p>
      </article>
    </section>

    <section aria-labelledby="expertise">
      <h2 id="expertise">Technical skills</h2>
      <dl class="resume-skills">
        <div><dt>Python</dt><dd>Proficient</dd></div>
        <div><dt>PyTorch</dt><dd>Advanced</dd></div>
        <div><dt>MLOps</dt><dd>Advanced</dd></div>
        <div><dt>CI/CD</dt><dd>Advanced</dd></div>
      </dl>
    </section>

    <section aria-labelledby="languages">
      <h2 id="languages">Languages</h2>
      <dl class="resume-skills">
        <div><dt>German</dt><dd>Native</dd></div>
        <div><dt>English</dt><dd>Fluent · C2</dd></div>
      </dl>
    </section>
  </div>
</div>
