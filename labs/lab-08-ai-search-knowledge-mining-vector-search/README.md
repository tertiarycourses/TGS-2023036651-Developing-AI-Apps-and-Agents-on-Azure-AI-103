# Lab 08 - Azure AI Search, Knowledge Mining, Vector Search

## Objectives

- Design an Azure AI Search solution.
- Define indexes, data sources, indexers, and skillsets.
- Explain semantic and vector search.
- Plan knowledge store projections.

## Scenario

The company wants searchable support documents, enriched with extracted text, entities, key phrases, and vector embeddings for RAG.

## Steps

### 1. Design an Index

Define fields:

```text
id
title
content
category
source_url
last_updated
security_label
embedding
```

### 2. Plan Data Sources and Indexers

Document:

- Source storage.
- Supported document formats.
- Indexer schedule.
- Change detection.
- Error handling.

### 3. Define a Skillset

Include:

- OCR.
- Language detection.
- Entity extraction.
- Key phrase extraction.
- Custom skill.
- Embedding generation.

### 4. Query Design

Write examples for:

```text
Keyword search
Filter by category
Sort by last updated
Wildcard query
Semantic ranking
Vector search
Hybrid search
```

### 5. Knowledge Store Projections

Explain file, object, and table projections and when enriched output should be stored.

### 6. Ground an Agent on Retrieved Evidence

Use `data/support-docs.json` and `data/judged-queries.json`. Design one BM25 query, one vector query, and one hybrid query with a tenant filter applied before results reach an agent. Save each result ranking as JSON in the shape of `data/example-rankings.json` and run `python3 evaluate.py <your-rankings.json>`. Record a citation to the winning chunk and a no-evidence answer. Compare relevance, p95 latency, and estimated cost for the three modes; label any invented values as illustrative. State how an indexer failure or stale source would be detected. The local scorer checks relevance and tenant isolation; it does not call Azure AI Search or measure live latency.

## Validation

You should have index design, data source/indexer plan, skillset plan, query examples, and knowledge store notes.

## Checkpoint Questions

1. What is an indexer?
2. What is a skillset?
3. What is vector search?
4. Why use semantic ranking?

## Course Focus

Knowledge mining combines source data, enrichment, indexing, querying, and optional vector retrieval for AI applications.
