---
title: "Towards Certifiable AI in Aviation: A Framework for Neural Network Assurance Using Advanced Visualization and Safety Nets"
collection: publications
category: conferences
permalink: /publication/2024-09-29-Towards-Certifiable-AI-in-Aviation
excerpt: "AI's growing role in technology necessitates stringent safety standards, especially in aviation where certification is regulated by strict laws. Ensuring AI system safety requires thorough understanding and proper tools. This work presents a Safety Net, utilizing sparse lookup tables (LUTs) to address neural network failures. By combining LUTs with neural networks, a certifiable system can be created, offering a framework for 100% reliability and effective real-time corrections during operation."
date: 2024-09-29
venue: "2024 IEEE/AIAA 43st Digital Avionics Systems Conference (DASC)"
paperurl: # DOI url
slidesurl: "http://www.chrstnsn.de/files/2024-09-29-DASC-SafetyNet-Handout.pdf"
citation: "<b>Christensen, J. M.</b>, Zaeske, W., Anilkumar Girija, A., Friedrich, S., Stefani, T., Durak, U., K&ouml;ster, F., Kr&uuml;ger, T. and Hallerbach, S. &quot;Towards Certifiable AI in Aviation: A Framework for Neural Network Assurance Using Advanced Visualization and Safety Nets&quot;, in <i>2024 IEEE/AIAA 43st Digital Avionics Systems Conference (DASC)</i>, Sep. 2024."
---
While Artificial Intelligence (AI) has become an important asset in many areas of science and technology, safety is often not treated as important as required for aviation. Neglecting safety is not an option for aviation, where strict laws and regulations govern the certification process of new aircraft. Thus, a solid understanding of the underlying AI-based system is important to certify such systems. To this day, manual inspection by humans is an essential step for certification, however requires proper tooling.

One such tool, called Advisory Viewer, is presented in this work, helping to break down the high-dimensional vector space of neural networks. The tool presented here can visualize decisions derived from assemblies of neural networks for arbitrary 2-dimensional parameter sweeps and provides real-time feedback upon any parameter change. It is designed to better understand the neural networks behind openCAS, an open-source implementation for the Airborne Collision Avoidance System X (ACAS X), the upcoming implementation for collision avoidance in aviation. However, as currently designed, implementing ACAS X is not feasible on current aviation hardware, as the required memory is not available. Here, neural networks and their ability to compress and generalize can be a solution. Therefore, it is of utmost importance that the AI-based system behind ACAS X always produces correct predictions.

Finally, to fix the detected irregularities, this work implements a Safety Net to ensure the correct output for the ACAS X use case. Safety Nets are designed on the idea of sparse lookup tables (LUTs), storing only the points where the neural networks are known to fail. By deploying a system consisting of a Safety Net together with neural network(s), a small, yet potentially certifiable system can be designed and built. This work presents a generic data format for LUTs and recommended algorithms to populate and organize said LUTs for quick access during run-time. Combined, this serves as a generic framework for 100 % assurance of small neural networks, joined by the visualization tooling for the specific use case of openCAS.