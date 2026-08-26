<div align="center">

# Microsoft Certified Azure AI Engineer Associate (AI-102) Training

[![Course Code](https://img.shields.io/badge/Course-TGS--2023036651-0078D4)](https://www.tertiarycourses.com.sg/wsq-microsoft-certified-azure-ai-engineer-associate-ai-102-training.html)
[![Courseware](https://img.shields.io/badge/Courseware-v2.0-107C10)](courseware/QA-REPORT-v2.0.md)
[![Microsoft Azure](https://img.shields.io/badge/Microsoft-Azure_AI-0078D4?logo=microsoftazure)](https://learn.microsoft.com/azure/ai-services/)
[![Labs](https://img.shields.io/badge/Hands--on_Labs-10-00A4EF)](labs/README.md)

**Mechanism-led Azure AI engineering courseware with detailed, self-contained hands-on labs.**

[Register for the course](https://www.tertiarycourses.com.sg/wsq-microsoft-certified-azure-ai-engineer-associate-ai-102-training.html) · [Open the labs](labs/README.md) · [Review QA evidence](courseware/QA-REPORT-v2.0.md)

</div>

## About the Course

This two-day WSQ course develops the ability to analyse, evaluate, and improve Azure AI solutions using Microsoft Foundry, Azure AI services, governed engineering decisions, and observable evidence. The v2.0 package contains a highly visual 126-slide editable trainer deck, an aligned Learner Guide and Lesson Plan, and ten individual lab folders.

> Microsoft retired the AI-102 certification exam on 30 June 2026. This approved WSQ course title and code remain unchanged; learners pursuing the current Microsoft certification pathway should also review the [AI-103 study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-103).

## Learning Outcomes

- Analyse algorithms in Microsoft Azure AI applications and establish their correlation with efficiency.
- Identify and evaluate the strengths and limitations of Microsoft Azure AI applications.
- Assess feasibility and improvements when applying Azure AI to product and maintenance processes.
- Support engineering conclusions with architecture, configuration, runtime, metric, failure-control, and acceptance evidence.

## Courseware

| Resource | Description |
| --- | --- |
| [Trainer slides (PPTX)](courseware/Microsoft%20Certified%20Azure%20AI%20Engineer%20Associate%20AI-102%20Training-v2.0.pptx) | Editable 126-slide deck with native charts, diagrams, transitions, and generated concept visuals. |
| [Trainer slides (PDF)](courseware/Microsoft%20Certified%20Azure%20AI%20Engineer%20Associate%20AI-102%20Training-v2.0.pdf) | Learner-viewable rendering of the trainer deck. |
| [Learner Guide](courseware/LG-Microsoft%20Certified%20Azure%20AI%20Engineer%20Associate%20AI-102%20Training.pdf) | Detailed click paths, commands, expected results, diagnostics, and evidence checks. |
| [Lesson Plan](courseware/LP-Microsoft%20Certified%20Azure%20AI%20Engineer%20Associate%20AI-102%20Training.pdf) | Two-day schedule aligned to the actual slide map, labs, and assessments. |
| [Labs index](labs/README.md) | Entry point for all ten self-contained hands-on labs. |
| [QA report](courseware/QA-REPORT-v2.0.md) | Structural, alignment, privacy, and technical-anchor checks. |

Assessment candidate papers and answer keys are managed through the course LMS and are intentionally excluded from this public repository.

## Learning Architecture

```text
Business requirement
        │
        ▼
Plan and govern ──► Build with Microsoft Foundry and Azure AI services
        │                              │
        │                              ▼
        └──────────────────────► Observe runtime evidence
                                       │
                                       ▼
                         Evaluate quality, safety, latency, and cost
                                       │
                                       ▼
                           Release, monitor, improve, or roll back
```

## Lab Catalogue

| Lab | Engineering focus |
| --- | --- |
| [01](labs/lab-01-plan-manage-secure-azure-ai-solution/README.md) | Plan, manage, monitor, and secure an Azure AI solution |
| [02](labs/lab-02-responsible-ai-content-safety-governance/README.md) | Responsible AI, Content Safety, and governance |
| [03](labs/lab-03-generative-ai-foundry-openai-prompt-flow-rag/README.md) | Generative AI, Microsoft Foundry, Azure OpenAI, prompt flow, and RAG |
| [04](labs/lab-04-agentic-ai-foundry-agent-service/README.md) | Agentic AI, Foundry Agent Service, and multi-agent concepts |
| [05](labs/lab-05-computer-vision-custom-vision-video/README.md) | Computer Vision, Custom Vision, and video insights |
| [06](labs/lab-06-nlp-language-speech-translation/README.md) | NLP, language, speech, and translation |
| [07](labs/lab-07-custom-language-question-answering/README.md) | Custom language models and question answering |
| [08](labs/lab-08-ai-search-knowledge-mining-vector-search/README.md) | Azure AI Search, knowledge mining, and vector search |
| [09](labs/lab-09-document-intelligence-content-understanding/README.md) | Document Intelligence and Content Understanding |
| [10](labs/lab-10-ai102-capstone-course-review/README.md) | AI-102 capstone, evidence review, and improvement plan |

Every lab contains its own scenario, objectives, detailed procedure, validation criteria, evidence checklist, and troubleshooting guidance.

## Repository Structure

```text
.
├── courseware/             # Current trainer PPTX/PDF, LG, LP, slide map, and QA evidence
├── labs/                   # Ten independent learner lab folders
├── scripts/                # Reproducible courseware build and QA scripts
└── assessment/             # Private and git-ignored; distributed only through the LMS
```

## Build and Verify

```bash
python3 scripts/build_ai102_courseware.py
python3 scripts/qa_ai102_courseware.py
```

The build scripts require Python 3 and the document/presentation dependencies used by the Tertiary Infotech courseware toolchain. Do not commit `.env` files, credentials, private assessment materials, or generated answer keys.

## Current Technical References

- [AI-102 study guide and retirement notice](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-102)
- [AI-103 study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-103)
- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure AI services documentation](https://learn.microsoft.com/azure/ai-services/)
- [Azure AI Search documentation](https://learn.microsoft.com/azure/search/)

## Developed By

[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/) · UEN 201200600W

<div align="center">

Ready to build governed Azure AI solutions? [Register for TGS-2023036651](https://www.tertiarycourses.com.sg/wsq-microsoft-certified-azure-ai-engineer-associate-ai-102-training.html).

</div>
