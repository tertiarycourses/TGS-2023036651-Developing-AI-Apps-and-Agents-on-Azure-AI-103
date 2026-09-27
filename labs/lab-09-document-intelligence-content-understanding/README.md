# Lab 09 - Document Intelligence and Content Understanding

## Objectives

- Use prebuilt document extraction concepts.
- Plan custom Document Intelligence models.
- Explain composed models.
- Design Content Understanding extraction workflows.

## Scenario

The company processes invoices, contracts, support screenshots, audio notes, and product videos. It wants to extract structured information from multiple content types.

## Steps

### 1. Map Document Scenarios

| Scenario | Capability |
| --- | --- |
| Extract invoice fields | Prebuilt invoice model |
| Extract custom form fields | Custom document model |
| Route different form types | Composed model |
| Extract table data | Layout and table extraction |
| Extract text from images | OCR pipeline |

### 2. Custom Document Model Plan

Document:

```text
Document types
Sample count
Fields to extract
Labels
Training split
Evaluation metric
Publish plan
```

### 3. Content Understanding Plan

Explain extraction from:

- Documents.
- Images.
- Video.
- Audio.

Include summarization, classification, attributes, entities, tables, and images.

### 4. Human Review Rules

Define confidence thresholds and when extracted data requires review.

### 5. Integration Flow

Draw:

```text
Upload content -> extract text/entities/tables -> validate -> store structured data -> search/report
```

### 6. Build a Grounded Extraction Contract

Read `data/maintenance-record.json` and inspect `data/example-extraction.json`. Define an analyzer output with `document_id`, `part_number`, `fault`, `action`, `confidence`, and `source_span` or page region. Copy the example to your own JSON file, correct or change one field, and run `python3 validate.py <your-file.json>`. The validator requires source provenance and human review below 0.80 confidence. Trace the clean structured output into a search index or agent tool without discarding provenance. Record analyzer version, supported modality, latency and cost estimates, privacy policy, and a fallback when the field-accuracy gate fails. This local validator does not claim a live Content Understanding call.

## Validation

You should have scenario mapping, custom model plan, content understanding plan, review rules, and integration flow.

## Checkpoint Questions

1. When should you use a prebuilt model?
2. What is a composed model?
3. Why are confidence scores useful?
4. What content types can Content Understanding process?

## Course Focus

Information extraction solutions need model selection, training data, confidence handling, and integration design.
