"""
RAG (Retrieval-Augmented Generation) — COMPLETE MINI REVISION CODE
Covers:
1. Documents
2. Chunking
3. Embeddings
4. Vector Database
5. Similarity Search
6. Retriever
7. Prompt Augmentation
8. Generator / LLM
9. Re-ranking idea
10. Hybrid Search idea
11. Metadata filtering
12. Multi-query retrieval
13. Context compression
14. Hallucination reduction
15. Conversation memory
16. Evaluation ideas


Install:
pip install sentence-transformers faiss-cpu transformers torch

This is a SIMPLE + SMALL + COMPLETE RAG FLOW.
"""

# =========================
# 1. IMPORTS
# =========================
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from transformers import pipeline


# =========================
# 2. DOCUMENTS
# =========================
documents = [
    "RAG combines retrieval with generation.",
    "Embeddings convert text into vectors.",
    "Vector databases store embeddings efficiently.",
    "Chunking splits large documents into smaller parts.",
    "Similarity search finds relevant chunks.",
    "Hybrid search combines keyword and vector search.",
    "Re-ranking improves retrieval quality.",
    "Metadata filtering restricts retrieval results.",
    "Context compression removes irrelevant information.",
    "Multi-query retrieval improves recall.",
]


# =========================
# 3. CHUNKING
# =========================
# Real systems split huge PDFs/books into chunks.
# Here every sentence is already a chunk.
chunks = documents


# =========================
# 4. EMBEDDING MODEL
# =========================
# Converts text -> vectors
embedder = SentenceTransformer("all-MiniLM-L6-v2")

chunk_embeddings = embedder.encode(chunks)


# =========================
# 5. VECTOR DATABASE (FAISS)
# =========================
dimension = chunk_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(chunk_embeddings))


# =========================
# 6. RETRIEVER
# =========================
def retrieve(query, top_k=3, metadata_filter=None):
    """
    Retrieval step:
    - Query embedding
    - Similarity search
    - Optional metadata filtering idea
    """

    # ---- Multi Query Retrieval Idea ----
    queries = [
        query,
        query + " explained",
        query + " definition",
    ]

    all_results = []

    for q in queries:

        query_embedding = embedder.encode([q])

        distances, indices = index.search(
            np.array(query_embedding),
            top_k
        )

        for i in indices[0]:
            all_results.append(chunks[i])

    # ---- Remove duplicates ----
    all_results = list(dict.fromkeys(all_results))

    # ---- Metadata Filtering Idea ----
    # Example:
    # if metadata_filter:
    #     all_results = [
    #         r for r in all_results
    #         if metadata_filter in r
    #     ]

    # ---- Context Compression Idea ----
    # Keep only shortest useful chunks
    compressed = sorted(all_results, key=len)[:top_k]

    return compressed


# =========================
# 7. RE-RANKING IDEA
# =========================
def rerank(query, retrieved_chunks):
    """
    Real systems use cross-encoders.
    Here we simulate re-ranking using overlap score.
    """

    scores = []

    for chunk in retrieved_chunks:

        score = len(
            set(query.lower().split()) &
            set(chunk.lower().split())
        )

        scores.append((score, chunk))

    scores.sort(reverse=True)

    return [chunk for _, chunk in scores]


# =========================
# 8. GENERATOR (LLM)
# =========================
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100
)


# =========================
# 9. MEMORY (Conversation History)
# =========================
chat_history = []


# =========================
# 10. COMPLETE RAG PIPELINE
# =========================
def rag(query):

    # ---- Retrieve ----
    retrieved_chunks = retrieve(query)

    # ---- Re-rank ----
    reranked_chunks = rerank(query, retrieved_chunks)

    # ---- Build Context ----
    context = "\n".join(reranked_chunks)

    # ---- Prompt Augmentation ----
    prompt = f"""
    Use ONLY the provided context.
    If answer is not present, say:
    "I don't know."

    Context:
    {context}

    Chat History:
    {chat_history}

    Question:
    {query}

    Answer:
    """

    # ---- Generate ----
    response = generator(prompt)[0]["generated_text"]

    # ---- Store Memory ----
    chat_history.append({
        "question": query,
        "answer": response
    })

    return {
        "query": query,
        "retrieved_chunks": retrieved_chunks,
        "reranked_chunks": reranked_chunks,
        "final_answer": response
    }


# =========================
# 11. TEST
# =========================
result = rag("What is vector database in RAG?")

print("\nQUESTION:")
print(result["query"])

print("\nRETRIEVED:")
for r in result["retrieved_chunks"]:
    print("-", r)

print("\nRERANKED:")
for r in result["reranked_chunks"]:
    print("-", r)

print("\nFINAL ANSWER:")
print(result["final_answer"])


# ==========================================================
# FULL RAG CONCEPT MAP (VERY IMPORTANT FOR REVISION)
# ==========================================================

"""
USER QUERY
    ↓
QUERY UNDERSTANDING
    ↓
QUERY EMBEDDING
    ↓
VECTOR SEARCH / HYBRID SEARCH
    ↓
TOP-K RETRIEVAL
    ↓
RE-RANKING
    ↓
METADATA FILTERING
    ↓
CONTEXT COMPRESSION
    ↓
PROMPT AUGMENTATION
    ↓
LLM GENERATION
    ↓
FINAL ANSWER

----------------------------------

CORE RAG TOPICS:

1. Chunking
   - fixed
   - semantic
   - recursive
   - overlap chunking

2. Embeddings
   - dense vectors
   - semantic meaning

3. Vector DB
   - FAISS
   - Chroma
   - Pinecone
   - Weaviate
   - Milvus

4. Retrieval
   - similarity search
   - cosine similarity
   - top-k retrieval

5. Advanced Retrieval
   - hybrid search
   - self-query retrieval
   - parent-child retrieval
   - multi-query retrieval

6. Re-ranking
   - cross encoder
   - reranker models

7. Context Handling
   - compression
   - deduplication
   - token optimization

8. Prompt Engineering
   - grounded prompts
   - instruction prompts

9. Hallucination Reduction
   - use only context
   - citations
   - confidence thresholds

10. Memory
   - chat history
   - long-term memory

11. Evaluation
   - retrieval accuracy
   - faithfulness
   - answer relevance
   - latency

12. Production RAG
   - caching
   - streaming
   - async retrieval
   - observability
   - guardrails
"""
