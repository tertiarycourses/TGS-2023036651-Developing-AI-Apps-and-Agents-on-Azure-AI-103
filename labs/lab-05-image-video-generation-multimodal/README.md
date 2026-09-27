# Lab 05 — Image and Video Generation, Multimodal Understanding

**Course:** Developing AI Apps and Agents on Azure (AI-103) · **Domain:** Computer vision (10–15%)

## Objectives

- Choose image generation, video generation, image editing, or multimodal understanding for a product need.
- Evaluate generated media against the source brief, safety rules, accessibility, and visual evidence.
- Define a production workflow with model version, moderation, human approval, and provenance.

## Scenario

A retailer wants a synthetic product campaign image and accessible descriptions. Its support agent must also answer questions about a customer-submitted product photo. Work only with the synthetic brief and review records in this folder.

## Materials

- `data/product-brief.json`: product attributes, permitted claims, and brand rules.
- `data/sample-output.json`: simulated model output for a repeatable review. It is **not** evidence of a live Foundry call.
- Python 3 standard library for the local check.
- Optional: an approved Microsoft Foundry project with an image model and a multimodal model available in the training region.

## Steps

### 1. Select the workflow

Read `data/product-brief.json`. Write a decision table with four rows: image generation, image editing, video generation, and visual question answering. For each, state the input, output, model capability, safety gate, and whether this scenario needs it. Distinguish creating new media from interpreting existing media.

### 2. Design generation evidence

Draft an image prompt that uses only the approved product attributes. Record the model/deployment and version, prompt, safety policy, and expected output format. Define a rejection rule for an unsupported performance claim, missing product attribute, incorrect logo, or unsafe content. If video is proposed, add storyboard, duration, reference-media rights, watermark, and frame-level review controls.

### 3. Review a synthetic response

Open `data/sample-output.json`. Compare its caption, alt text, answer, and claims with the brief. Create `review.json` containing:

```json
{"model_version":"sample-only","approved":false,"unsupported_claims":[],"missing_attributes":[],"alt_text_issue":"","human_reviewer":"training reviewer"}
```

Populate the arrays and decision from the evidence. Run `python3 validate.py review.json`; it checks the review schema and the required decision rationale. Save the validation output.

### 4. Optional live Foundry extension

If the trainer has supplied approved deployments, generate a synthetic product concept image, then ask a multimodal model for a caption, accessible alt text, and an answer grounded in that image. Record the model and deployment versions, prompt, response, safety result, latency, and request ID. Compare the live result with the same brief. Label it **live** only when the service call and response are captured. Do not upload real customer images or publish generated media without the human gate.

### 5. Architecture and failure review

Draw the path: brief or uploaded media → content validation → model deployment → moderation → visual/claim evaluator → human review → approved asset or rejection. Add the indirect prompt-injection risk from text embedded in an image. State a control for each failure and a rollback path for a changed model version.

## Validation

A complete submission has the decision table, prompt and model record, `review.json`, passing local validation, architecture, and one rejected output with a cited reason. Live Foundry evidence is optional and must be labeled separately.

## Troubleshooting

- Missing model in region: use the provided sample; record the deployment constraint.
- JSON check fails: compare required keys and value types in `validate.py`.
- Model answer invents a property: reject it and quote the unsupported claim in the review.
- Visual content may be unsafe: stop distribution and route to human review.

## Cleanup

Remove only resources created in your own lab resource group after the trainer confirms evidence is saved. Keep the synthetic review files.

## Reference

[Microsoft AI-103 study guide — computer vision](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103#implement-computer-vision-solutions-1015)
