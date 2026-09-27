# Lab 07 — Generative Text Analysis and Translation

**Course:** Developing AI Apps and Agents on Azure (AI-103) · **Domain:** Text analysis (10–15%)

## Objectives

- Extract entities, topic, sentiment, summary, and structured JSON from customer text.
- Detect sensitive content and distinguish source evidence from generated claims.
- Compare Azure Translator with an LLM translation flow for a support workflow.

## Scenario

A service team receives multilingual synthetic messages. It needs a typed triage record for a support agent, with human review when the message is ambiguous or contains sensitive data.

## Materials

- `data/messages.json`: three synthetic messages with expected review signals.
- `data/sample-analysis.json`: simulated model output for a repeatable local exercise; **not** a live Azure result.
- Python 3 standard library for validation.
- Optional: trainer-approved Microsoft Foundry text model and Azure Translator in the training region.

## Steps

### 1. Define the output contract

Read the three messages. Design a JSON record with `message_id`, `topic`, `sentiment`, `entities`, `summary`, `sensitive_content`, `evidence_span`, `language`, and `review_required`. Define allowed values and a no-evidence rule. Make the evidence span an exact substring of the source message.

### 2. Evaluate the sample

Open `data/sample-analysis.json` and compare every record with its source. Identify any missing entity, unsupported summary, false sentiment, or sensitive identifier that should be redacted. Write the corrected records to `analysis.json` in the same folder. Run `python3 validate.py analysis.json`; fix each reported error and save the PASS output.

### 3. Design the Foundry prompt

Write a prompt that requests only the typed JSON fields, keeps each message separate, cites an exact evidence span, avoids ungrounded claims, and sets `review_required` when uncertain or sensitive. Record model deployment/version, temperature, input, response, request ID, and latency if the trainer provides a live deployment. Label `data/sample-analysis.json` as **synthetic simulation** at all times.

### 4. Compare translation paths

For the non-English message, compare two paths: Azure Translator followed by text analysis, and an LLM-powered translation and extraction flow. Define tests for preserved named entities, tone, domain terms, language identification, cost, latency, and privacy. Do not silently replace the original message with a translation; retain both for audit.

### 5. Add agent integration

Draw the path: message → language detection → sensitive-content gate → typed analysis → schema validation → human review if needed → agent tool. State why the agent must not act on unvalidated JSON or leak identifiers into logs.

## Validation

Submit `analysis.json`, the validator PASS output, prompt, translation comparison, and agent data-flow. Each record must have a source-bound evidence span, correct sensitive-content decision, and no invented entity. Live service evidence is optional and must be labeled separately.

## Troubleshooting

- JSON parse failure: remove commentary outside the JSON object and verify types.
- Evidence span mismatch: copy the exact source substring; do not paraphrase it.
- Ambiguous sentiment: set a review rule and explain the uncertainty.
- Translation changes an entity: retain the original and route the case for review.

## Cleanup

Remove only your own temporary training deployments after the trainer confirms evidence capture. Keep synthetic source and corrected records.

## Reference

[Microsoft AI-103 study guide — text analysis](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103#implement-text-analysis-solutions-1015)
