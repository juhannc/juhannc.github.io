---
title: "Advancing the AI-Based Realization of ACAS X Towards Real-World Application"
collection: publications
category: conferences
permalink: /publication/2024-10-28-Advancing-the-AI-Based-Realization-of-ACASX
excerpt: "AI is increasingly applied in safety-critical domains like automotive and robotics, but its deployment in aviation remains limited due to stringent safety requirements. This work explores AI's potential in aviation through the Airborne Collision Avoidance Systems X (ACAS X), including ACAS X<sub>A</sub> for vertical advisories and ACAS X<sub>U</sub> for horizontal advisories. Implementations of both variants for FlightGear demonstrate their effectiveness in avoiding near mid-air collisions (NMACs). An Operational Design Domain is defined for safety considerations, and simulation tests validate the successful use of advisory predictions for collision avoidance."
date: 2024-10-28
venue: "36th IEEE International Conference on Tools with Artificial Intelligence (ICTAI)"
paperurl: "https://doi.org/10.1109/ICTAI62512.2024.00017"
slidesurl: "http://www.chrstnsn.de/files/2024-10-28-pyCASX-Handout.pdf"
citation: "<b>Christensen, J. M.</b>, Anilkumar Girija, A., Stefani, T., Durak, U., Hoemann, E., K&ouml;ster, F., Kr&uuml;ger, T. and Hallerbach, S. &quot;Advancing the AI-Based Realization of ACAS X Towards Real-World Application&quot;, in <i>36th IEEE International Conference on Tools with Artificial Intelligence (ICTAI)</i>, Oct. 2024."
---
In recent years, artificial intelligence (AI) has been applied to a wide range of safety-critical domains, such as automotive, robotics, and aviation.
Especially the automotive and robotics domains have seen a rapid increase in the number of AI-based systems that are being deployed in real-world applications.
However, real-world applications in the aviation domain are still sparse, given the challenges of AI engineering in combination with strict safety requirements.

A first possible application of AI in the aviation domain might be the future collision avoidance system Airborne Collision Avoidance Systems X (ACAS X).
The goal of collision avoidance systems is to issue advisories to the pilot to avoid near mid-air collisions (NMACs).
The two important variants of ACAS X for this work are ACAS X<sub>A</sub>, providing vertical advisories and meant as a drop-in replacement for current systems in commercial air flight, and ACAS X<sub>U</sub>, providing horizontal advisories for the ever-growing unmanned aircraft systems market.
This work brings both variants closer to real-world deployment by implementing a vertical collision avoidance system, based upon ACAS X<sub>A</sub>, and a horizontal collision avoidance system, based upon ACAS X<sub>U</sub>, for the research flight simulator FlightGear.
Using advisories given by this implementation, this work furthermore provides an auto-avoid function that can command an airplane in FlightGear to safely avoid NMACs.

Finally, this work will show that the ACAS X implementation can avoid collisions in a simulated environment.
For this task, an Operational Design Domain will be defined serving as a basis for safety considerations and evaluating the implementation of the ACAS X.
In the end, simulation-based testing will be used separately for VCAS and HCAS showing the successful utilization of advisory predictions as autopilot inputs.

Summarizing, this work not only presents an open-source implementation of ACAS X<sub>A</sub> and ACAS X<sub>U</sub> for FlightGear but also shows how the generated advisories can be used to successfully avoid NMACs.
