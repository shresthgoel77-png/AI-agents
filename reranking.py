# Our mock database of documents
documents = [
    {"id": 1, "text": "Python is a great programming language for AI."},
    {"id": 2, "text": "Java and Python are popular languages."},
    {"id": 3, "text": "Error code 404 means page not found on a server."},
    {"id": 4, "text": "To fix error 404, check your URL and routing configuration."},
]

query = "how to fix error 404"


# ==========================================
# STEP 1: HYBRID SEARCH (Broad Retrieval)
# ==========================================
def keyword_score(q, text):
  """Simulates BM25 keyword matching."""
  return (
      sum(1 for word in q.lower().split() if word in text.lower())
      / len(q.split())
      * 0.5
  )


def vector_score(q, text):
  """Simulates Semantic / Vector embedding similarity."""
  # Mocking semantic match: higher if words overlap conceptually
  common_words = set(q.lower().split()).intersection(set(text.lower().split()))
  return len(common_words) * 0.3


print("=== STEP 1: HYBRID SEARCH (Retrieving Top Candidates) ===")
retrieved_pool = []
for doc in documents:
  kw = keyword_score(query, doc["text"])
  vec = vector_score(query, doc["text"])

  # Combine Keyword + Vector into a single Hybrid Score
  hybrid_score = kw + vec
  retrieved_pool.append(
      {"id": doc["id"], "text": doc["text"], "score": hybrid_score}
  )

# Sort and take top 3 results for the reranker
retrieved_pool = sorted(retrieved_pool, key=lambda x: x["score"], reverse=True)[
    :3
]

for d in retrieved_pool:
  print(f"Doc {d['id']} | Hybrid Score: {d['score']:.2f} | Text: {d['text']}")


# ==========================================
# STEP 2: RERANKING (Deep Precision Check)
# ==========================================
def cross_encoder_reranker(q, text):
  """Simulates an AI Reranker (Cross-Encoder) doing deep analysis."""
  # Rerankers look at contextual phrasing and precision
  if "fix" in text.lower() and "404" in text.lower():
    return 0.98  # Highly relevant actionable answer
  elif "404" in text.lower():
    return 0.50  # Mentions the topic, but doesn't solve it
  else:
    return 0.05  # Irrelevant


print("\n=== STEP 2: RERANKED RESULTS (Final Best Match) ===")
reranked_pool = []
for doc in retrieved_pool:
  rerank_score = cross_encoder_reranker(query, doc["text"])
  reranked_pool.append(
      {"id": doc["id"], "text": doc["text"], "score": rerank_score}
  )

# Sort by the new strict rerank score
reranked_pool = sorted(reranked_pool, key=lambda x: x["score"], reverse=True)

for d in reranked_pool:
  print(f"Doc {d['id']} | Rerank Score: {d['score']:.2f} | Text: {d['text']}")