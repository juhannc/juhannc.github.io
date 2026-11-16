---
title: From High-Dimensional Spaces to Verifiable ODD Coverage for Safety-Critical AI-based Systems
collection: publications
category: conferences
permalink: /publication/2026-09-23-From-High-Dimensional-Spaces-to-Verifiable-ODD-Coverage-for-Safety-Critical-AI-based-Systems
bibkey: Stefani2026a
excerpt: A structured ODD coverage method combines parameter grouping, dependency analysis, physical constraints, and criticality-based discretization, reducing a VerticalCAS verification space by roughly 60%.
date: '2026-09-23'
venue: Computer Safety, Reliability, and Security (SAFECOMP)
paperurl: https://doi.org/10.1007/978-3-032-34867-8_10
citation: Thomas Stefani, <b>Johann Maximilian Christensen</b>, Elena Hoemann, Frank Köster, Sven Hallerbach. &quot;From High-Dimensional Spaces to Verifiable ODD Coverage for Safety-Critical AI-based Systems&quot;. <i>Computer Safety, Reliability, and Security (SAFECOMP)</i>, 2026.
---

While Artificial Intelligence (AI) offers transformative potential for operational performance, its deployment in safety-critical domains such as aviation requires strict adherence to rigorous certification standards. Current EASA guidelines mandate demonstrating complete coverage of the AI/ML constituent's Operational Design Domain (ODD)—a requirement that demands proof that no critical gaps exist within defined operational boundaries. However, as systems operate within high-dimensional parameter spaces, existing methods struggle to provide the scalability and formal grounding necessary to satisfy the completeness criterion, and no standardized engineering method exists to bridge the gap between abstract ODD definitions and verifiable evidence. This paper addresses that gap with a structured, multi-step method that integrates parameter grouping, a dependency analysis distinguishing deterministic from stochastic relationships, physically grounded constraint definition, and criticality-based discretization into a single ODD coverage verification process. Applied to a case study on AI-based near mid-air collision avoidance with the VerticalCAS system, the method reduces the verification space by roughly 60% while preserving all safety-relevant combinations and yields an explicit, iterable list of uncovered regions, providing a repeatable process for demonstrating the completeness EASA requires. Designed to scale toward higher-dimensional ODDs, the method advances a Safety-by-Design approach to the certification of future AI-based flight systems.
