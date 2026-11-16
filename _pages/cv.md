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
          <li>Leading interinstitutional and interdisciplinary projects with funding of up to €5 million, and acquiring funding with public and industrial partners.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">October 2019 – August 2023 <span>Hamburg, Germany</span></p>
        <h3>AI and Robotics Engineer</h3>
        <p class="resume-organization">ZAL Center of Applied Aeronautical Research</p>
        <ul>
          <li>Developed reinforcement learning systems for industrial applications, with a focus on PPO and SAC.</li>
          <li>Built robots in simulation and hardware, including a ROS-based digital twin of a UR10e.</li>
          <li>Built an MLOps pipeline to accelerate model training and automate CI/CD for deployment to edge devices; administered the robotics simulation server and local GitLab instance.</li>
          <li>Acquired a total of €8 million in research funding and managed government-funded projects.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">November 2018 – April 2019 <span>Berkeley, CA, USA</span></p>
        <h3>Visiting Research Scholar</h3>
        <p class="resume-organization">Hybrid Robotics Lab · University of California, Berkeley</p>
        <ul>
          <li>Researched autonomous quadrotor flight control and obstacle avoidance under Prof. Koushil Sreenath.</li>
          <li>Combined model predictive control with control barrier functions to improve predictive obstacle avoidance, with experimental validation on aerial robots.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">December 2016 – June 2018 <span>Hamburg, Germany</span></p>
        <h3>Working Student · Cabin R&amp;D</h3>
        <p class="resume-organization">Airbus · Cabin Supply Modules A350</p>
        <ul>
          <li>Supported project management for aircraft cabin R&amp;D, particularly galley developments.</li>
          <li>Managed a project to develop an alternative to conventional honeycomb panels, coordinating management, suppliers, and teams across Airbus.</li>
          <li>Coordinated project deliverables and supported the development through Technology Readiness Level 6.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">September 2016 – January 2018 <span>Germany &amp; Sweden</span></p>
        <h3>Team Leader · HAMBURG Experiment</h3>
        <p class="resume-organization">REXUS/BEXUS student programme · DLR &amp; ESA</p>
        <ul>
          <li>Led the student experiment, with responsibility for project coordination, hardware and software development, integration, and testing.</li>
          <li>Organized the campaign in Kiruna, Sweden, where the experiment was tested and flown on a balloon reaching approximately 25,000 metres.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">January – April 2016 <span>Hamburg, Germany</span></p>
        <h3>Bachelor’s Research · Autonomous Diving Cell</h3>
        <p class="resume-organization">Institute of Mechanics and Ocean Engineering · TUHH</p>
        <ul>
          <li>Designed and built an autonomous diving cell using variable volume to control buoyancy.</li>
          <li>Investigated PID and sliding-mode depth control; the work led to a publication on adaptive control of a micro diving agent.</li>
        </ul>
      </article>
      <article class="resume-entry">
        <p class="resume-date">October 2015 – February 2016 <span>Hamburg, Germany</span></p>
        <h3>Engineering Intern · Design to Mass Properties</h3>
        <p class="resume-organization">Airbus</p>
        <ul>
          <li>Contributed to mass calculations and weighing activities, from individual components to aircraft.</li>
          <li>Developed the foundations of a data tool to track changes in component and assembly masses.</li>
        </ul>
      </article>
    </section>

    <section aria-labelledby="teaching">
      <h2 id="teaching">Teaching &amp; mentoring</h2>
      <article class="resume-entry">
        <p class="resume-date">October 2013 – September 2015</p>
        <h3>Mechanics Tutor</h3>
        <p class="resume-organization">Institute of Mechanics and Ocean Engineering · TUHH</p>
        <p>Supported groups of up to 20 students with mechanics assignments.</p>
      </article>
      <article class="resume-entry">
        <p class="resume-date">October 2014 – March 2015</p>
        <h3>Mechanical Design Project Tutor</h3>
        <p class="resume-organization">Institute of Production Management and Technology · TUHH</p>
        <p>Mentored teams of up to six students and assessed their design projects.</p>
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
        <p class="resume-date">February 2021 – August 2023</p>
        <h3>Doctoral Research · Reinforcement Learning</h3>
        <p class="resume-organization">Hamburg University of Technology (TUHH) · External research</p>
        <p>Researched reinforcement learning for mechatronic systems, using linear parameter-varying models to accelerate training.</p>
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
      <article class="resume-entry">
        <p class="resume-date">October 2012 – September 2016</p>
        <h3>B.Sc. in Mechanical Engineering</h3>
        <p class="resume-organization">Hamburg University of Technology (TUHH)</p>
        <p>Focus on Aircraft Systems Engineering.</p>
      </article>
    </section>

    <section aria-labelledby="expertise">
      <h2 id="expertise">Technical skills</h2>
      <dl class="resume-skill-groups">
        <div><dt>AI &amp; machine learning</dt><dd>Python, PyTorch, reinforcement learning (PPO, SAC), MLOps, and neural-network assurance.</dd></div>
        <div><dt>Robotics &amp; control</dt><dd>ROS, PX4, C++ for robotics and flight-control integration, MATLAB/Simulink, model predictive control, and control barrier functions.</dd></div>
        <div><dt>Software &amp; deployment</dt><dd>Git, GitLab CI/CD, GitHub Actions, TensorRT, and deployment of trained models to edge devices.</dd></div>
        <div><dt>Mechanical engineering</dt><dd>Inventor, SolidWorks, hardware prototyping, integration, and experimental testing.</dd></div>
      </dl>
    </section>

    <section aria-labelledby="project-leadership">
      <h2 id="project-leadership">Project leadership</h2>
      <p>Research proposals and funding acquisition; interdisciplinary project management; coordination with industrial partners and suppliers; conference presentations; and student mentoring.</p>
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
