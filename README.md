# event-driven-image-annotation
An event-driven image annotation and retreival system

REDIS pub-sub for topics and messages (can use any messaging and bus system)

Suggested Services: 
- Upload
- Inference
- Document DB
- Embedding
- CLI 

# REDIS 
- Free version which includes 1 database, 30 connections, 100 ops/sec, 30MB RAM, other capabilities 
- Name: edia-database-bnd #14278090
- Database version: 8.4 
- Cloud vendor: Amazon Web Services (AWS)
- Region: us-east-1

## Project Overview (taken and slightly modified from slides): 
- This project combines modular systems, pub-sub, document databases, and vector search into one system.
- Workflow is asynchronous: submission, inference, storage, indexing, and retrieval do not need one blocking call. 
- Annotations are variable and nested, so justify a document model instead of forcing fixed tables.
- Embeddings add a new capability: similarity search over images or objects, not just metadata lookup.
- An event generator makes unit testing concrete through contracts, mocking, deterministic replay, and fault injection.

### Mission: 
- Visual Object retrieval system that searches using natural language and gets objects
- Use cases
    - User can upload images, then run via an AI system which detects objects and provides embedding for those objects.
    - User searches for something and retrieves objects that match



