---
layout: profile
permalink: /
title: "Johann Christensen — Safe AI Engineering"
excerpt: "Research on Safety-by-Design AI, operational design domains, and certifiable aviation systems at the German Aerospace Center."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
<header class="profile-header">
  <p class="profile-eyebrow">Research · Engineering · Aviation</p>
  <h1 id="profile-title">Engineering AI for <br>Safety-Critical Systems.</h1>
  <p class="profile-lead">I’m Johann, an AI expert and researcher developing safe, resilient AI for aviation at the German Aerospace Center (DLR).</p>
  <p>I develop Safety-by-Design approaches that connect AI research with the demands of aviation certification: understanding where a system can operate, verifying its behavior, and building the evidence needed to trust it.</p>
  <nav class="profile-actions" aria-label="Explore my work">
    <a class="profile-button" href="{{ '/publications/' | relative_url }}">Explore Publications <span aria-hidden="true">↗</span></a>
    <a href="{{ '/cv/' | relative_url }}">View My CV <span aria-hidden="true">↗</span></a>
  </nav>
</header>

<section class="profile-section" aria-labelledby="research-focus">
  <h2 id="research-focus">Research Focus</h2>
  <dl class="research-areas">
    <div>
      <dt>Operational Design Domains</dt>
      <dd>Defining the conditions in which AI systems can operate, learning those boundaries from data, and assessing coverage and representativeness.</dd>
    </div>
    <div>
      <dt>Neural-Network Assurance</dt>
      <dd>Combining neural networks with Safety Nets to support reliable collision avoidance and a practical path toward certifiable AI.</dd>
    </div>
    <div>
      <dt>AI Engineering &amp; Human–AI Interaction</dt>
      <dd>Connecting learning assurance with iterative development, and developing guardrails for LLM-based support in air traffic control.</dd>
    </div>
  </dl>
</section>

<section class="profile-section" aria-labelledby="background">
  <h2 id="background">Background</h2>
  <p>I am a research associate at DLR’s Institute for AI Safety and Security and a PhD candidate in Safe AI Engineering at Ruhr University Bochum, supervised by Prof. Frank Köster.</p>
  <p>Previously, I worked as an AI and Robotics Engineer at ZAL Center of Applied Aeronautical Research in Hamburg, developing reinforcement learning systems, robotic simulations, and MLOps workflows for industrial applications.</p>
  <p>I studied Aircraft Systems Engineering at Hamburg University of Technology. My master’s thesis at UC Berkeley’s Hybrid Robotics Lab, supervised by Prof. Koushil Sreenath, explored obstacle avoidance for safety-critical aerial robots. Earlier experience includes Airbus and leading a DLR/ESA-funded REXUS/BEXUS student project.</p>
</section>

<section class="profile-section" aria-labelledby="selected-research">
  <div class="profile-section-heading">
    <h2 id="selected-research">Selected Research</h2>
    <a href="{{ '/publications/' | relative_url }}">All Publications <span aria-hidden="true">↗</span></a>
  </div>
  {% assign selected_keys = 'Christensen2026,Christensen2026a,Christensen2025' | split: ',' %}
  {% for key in selected_keys %}
    {% assign publication = site.publications | where: 'bibkey', key | first %}
    {% if publication %}{% include publication-entry.html publication=publication %}{% endif %}
  {% endfor %}
</section>

<section class="profile-section" aria-labelledby="academic-service">
  <h2 id="academic-service">Academic Service</h2>
  <p>In 2026, I review for IEEE Transactions on Aerospace and Electronic Systems (IEEE TAES), Annals of the New York Academy of Sciences (Wiley), ICML, and NeurIPS. I received an ICML 2026 Silver Reviewer Award.</p>
  <p>My supervised student research includes Mina Randolf’s 2026 master’s thesis on Safety-by-Design for simulation-based dataset creation and AI model development.</p>
  <a href="/cv/#service">Reviewing &amp; Supervision ↗</a>
</section>
