# Skills Proposal for Review

**Status:** approved by the user on 17 November 2026, with FlightGear replaced by Isaac Sim/Gym and robotics made explicit. The six categories are implemented in the CV and synchronized in `llms.txt`; the `jc` favicon is included in this update. Optional confirmation-only topics remain excluded.

## Recommended Public Categories and Wording

These six groups balance research specialties, practical engineering, and leadership. Keep spoken languages in their own small row. Tool names are examples of experience, not numerical proficiency ratings.

| Category | Proposed Public Wording |
| --- | --- |
| **AI & Machine Learning** | Supervised learning (neural-network regression and classification), reinforcement learning, model training and evaluation, and LLM integration and guardrails. PyTorch, JAX, TensorRT; experiment tracking with Weights & Biases. |
| **AI Safety & Assurance** | Safety-by-Design, learning assurance, operational design domains (specification, reconstruction, and monitoring), data coverage and representativeness, and scenario-based verification. |
| **Robotics, Control & Simulation** | ROS, PX4, digital twins and robotics simulation, Isaac Sim/Gym, model predictive control, control barrier functions, and constrained optimization. MATLAB/Simulink and C++ for robotics and flight-control integration. |
| **Research Software & MLOps** | Python, NumPy/SciPy, reusable packages and APIs, automated testing and software quality, Git, GitLab CI/CD, GitHub Actions, Docker, and deployment to edge devices. Configuration and reproducibility tooling can be named where useful. |
| **Engineering & Prototyping** | Inventor, SolidWorks, 3D printing, hardware prototyping, integration, and experimental testing. |
| **Research & Project Leadership** | Research proposals and funding acquisition through EU and German programmes and direct industry collaboration; interdisciplinary and interinstitutional projects with budgets up to €5 million; student supervision and research communication. |

**Languages:** retain German (native) and English (fluent, C2, as in the latest Resume).

A shorter alternative is five groups, folding Engineering & Prototyping into Robotics, Control & Simulation. The six-group version gives the aviation/mechanical background its own space and keeps the robotics card manageable. My recommendation is six.

## Highest-Priority Additions

1. **Supervised learning, regression, and classification.** Direct first-author evidence in the ICAS 2026 Safety Nets paper, §5: Q-value regression using MSE versus advisory classification using cross entropy, plus systematic architecture/activation/encoding experiments. This is deliberate compression of a fully known finite function, not a claim of generalization outside the evaluated domain. [Paper](https://doi.org/10.71945/icas2026_0210).
2. **A dedicated AI Safety & Assurance category.** ODD methods, learning assurance, coverage, and verification recur across the papers and current DLR role. [AI engineering framework](https://doi.org/10.3390/aerospace12060482), [learning assurance framework](https://doi.org/10.3390/aerospace13020200). Several concepts already appear elsewhere on the site but are missing from the Skills tab.
3. **Simulation-based data generation, data quality, and coverage assessment.** The scenario-generation paper explicitly attributes the main Python implementation to Johann. [Paper](https://doi.org/10.1007/s13272-024-00772-4). Depending on emphasis, add this wording to AI Safety & Assurance or Robotics, Control & Simulation.
4. **Scientific Python: NumPy and SciPy.** Supported by numerical geometry and advisory software, plus merged robot transformation code from the old ZAL account. [fanucpy contribution](https://github.com/torayeff/fanucpy/pull/31).
5. **Software engineering: testing, typing, packaging, and API integration.** Authored package templates and tests, plus merged simulator HTTP-client implementation. [Package template](https://github.com/juhannc/python-package), [timeoutd tests](https://github.com/juhannc/timeoutd/blob/main/tests/test_timeoutd.py), [FlightGear HTTP client](https://github.com/julianneswinoga/flightgear-python/pull/9). These are stronger public claims than a generic list of programming languages.
6. **Containers and reproducible experiments.** Docker/Buildx and multiarchitecture builds are demonstrated in original workflows; W&B integration is a merged contribution. [Container build](https://github.com/juhannc/prek/blob/main/Dockerfile), [merged Podman build repair](https://github.com/unifi-utilities/unifi-common/pull/332), [W&B integration](https://github.com/Toni-SM/skrl/pull/31).
7. **Constrained optimization, digital twins, and simulator integration.** The master's thesis provides direct control/optimization and experimental aerial-robotics evidence; Resume.tex explicitly describes the UR10e digital twin. [Master's thesis](https://doi.org/10.48550/arxiv.2011.08178).
8. **Project acquisition and research leadership.** Already explicit in the current Resume/CV and confirmed by the user; bringing it into Skills makes this professional capability visible alongside technical tools.

## Optional Additions to Prioritize or Confirm

| Candidate | What Is Supported / What Needs Your Decision |
| --- | --- |
| **Computer Vision & Object Detection** | There is clear project-supervision experience, particularly Mina Randolf's YOLO/synthetic-data thesis. The student's contribution statement assigns implementation and validation to her. Confirm your own hands-on experience before listing broad object-detection expertise. [Thesis](https://elib.dlr.de/224824/). |
| **OOD Detection, Kernel Methods & Statistical Calibration** | Strong method evidence in autoSAFE, including kernel-based ODD reconstruction and calibration. Worth naming for research audiences, but could overload a general CV card. |
| **LLM Integration & Guardrails** | Current Resume.tex explicitly states guardrail work; the ATC paper provides research context. This supports applied integration, not unqualified LLM pretraining/fine-tuning/RAG expertise. [Paper](https://doi.org/10.1109/DASC66011.2025.11257297). |
| **ONNX / ONNX Runtime** | Code and conversion tooling exist in pycasx, but its alternative inference backends are documented as experimental. List tool experience only if useful; no production-maturity claim. |
| **Hydra, Sphinx, Linux/Shell** | Practical evidence exists. Useful supporting tools, probably secondary to the conceptual skills above. |
| **Embedded Systems / CANopen / Trajectory Interfaces** | Real historical code and contribution evidence. Some relevant PRs remain unmerged; do not imply upstream adoption or current embedded specialization. |
| **PyQt GUI Development** | Demonstrated in a personal project; useful if application development is a priority. [Example](https://github.com/juhannc/beerpong/blob/main/beerpong/gui/gui.py). |

## Deliberate Omissions

- Keep reinforcement learning broad; do not restore the specific algorithm names previously removed at the user's request.
- Do not revive TensorFlow/Keras or Java solely from older/commented-out CV material. They may be historical skills, but need a relevance/currentness decision.
- Do not infer Rust expertise from a coauthored paper's Rust implementation without individual attribution.
- Do not infer competence from unmodified forks, repository language percentages, package dependencies alone, or ownership of upstream mirrors.
- Do not describe the unfinished, closed-unmerged MBMPO work as a completed implementation.
- Do not turn EUROCAE participation or safety-method research into claims of certification authority, certified products, or guarantees beyond the systems and assumptions studied.

## Review Coverage and Limits

**Documents:** Resume.tex, CV.tex and matching PDFs, plus directly relevant older CV versions. Main direct sources: Resume.tex lines 144–161 (Safety-by-Design, ODDs, LLM guardrails, digital twin, MLOps, funding and leadership); CV.tex lines 119–138 (research and coordination). Latest Resume is used where older documents differ. Private identifiers, addresses, and correspondence are excluded.

**Publications:** all 21 canonical entries: 18 authored research/thesis/preprint entries and three supervised theses. For 20 available local full texts, the audit inspected methods, implementation, results, and contribution passages; this was not a sequential reading of every page. Erdogan2027 had metadata only, so no technical skill was inferred from it. Coauthorship and supervision do not establish personal implementation of every method.

**GitHub:** inventoried 47 public repositories under `juhannc` and two under `zal-jlange`; 34 are forks. Inspected 12 relevant repository trees, representative source/manifests/tests, and 58 authored public PR results. This is an evidence-focused review of relevant work, not a line-by-line audit of every repository. Direct examples from each account include merged W&B/FlightGear contributions and merged fanucpy work by `zal-jlange`.

## Approved Implementation

The user accepted the six categories and requested Isaac Sim/Gym in place of FlightGear, plus explicit robotics wording. The public CV and `llms.txt` now reflect these choices. The favicon uses an outlined `jc` monogram matching the sidebar, with SVG, PNG, ICO, and Apple touch variants. Optional confirmation-only skills remain excluded; historical contribution evidence above is retained for provenance.
