---
title: "Leveraging Large Language Models as an Interface to Conflict Resolution for Human-AI Alignment in Air Traffic Control"
collection: publications
category: conferences
permalink: /publication/2025-09-14-Leveraging-Large-Language-Models
excerpt: "Forecasted increases in aircraft traffic will strain air traffic control, prompting research into Single Controller Operations (SCOs). Conflict Resolution (CR) has been identified as a key automatable task. However, existing CR solvers that use fixed optimization functions cannot accommodate dynamic air traffic controller preferences. This work proposes an LLM-based algorithm that filters and ranks CR solutions using natural language policies to better align with controller preferences. Testing on synthetic datasets demonstrates success in most cases, although analysis reveals limitations of LLMs that warrant consideration in future development."
date: 2025-09-14
venue: "2025 AIAA DATC/IEEE 44th Digital Avionics Systems Conference (DASC)"
paperurl: "https://10.1109/DASC66011.2025.11257297"
slidesurl: # URL to slides pdf
citation: "Berro, C., Deligiannaki, F., Stefani, T., <b>Christensen, J. M.</b>, Gerdes, I. and K&ouml;ster. F. &quot;Leveraging Large Language Models as an Interface to Conflict Resolution for Human-AI Alignment in Air Traffic Control&quot;, in <i>2025 AIAA DATC/IEEE 44th Digital Avionics Systems Conference (DASC)</i>, Sep. 2025."
---
A steep aircraft increase is forecasted in the near future, putting additional strain on en-route air traffic control.
To meet the safety and efficiency goals, contemporary research explores the Single Controller Operations (SCOs) concept to replace traditional positioning of two Air Traffic Controllers (ATCOs) per sector.
During workshops with ATCOs addressing SCOs, Conflict Resolution (CR) has been identified as one important task that can be supported by automation.
Although existing work on CR solvers shows promising results, solvers based on fixed optimization functions are incompatible with the dynamic evolving preferences of ATCOs.
This work proposes two additional steps that filter and rank CR solutions based on a set of rules in natural language-forming a flexible policy-to better align with ATCO preferences in automation-supported CR.
Inspired from related work on LLM-driven agents, an algorithm using LLMs to filter and sort CR solutions for alignment with natural language policies is presented.
The algorithm is tested on a synthetic dataset of policies and solutions for several minimal filtering and sorting scenarios.
The experiments show success in solving the task in most cases and a correct understanding of the task by the LLM.
Nevertheless, the analysis of failure cases highlights several limitations of LLMs that must be considered in future research and development of similar systems.
