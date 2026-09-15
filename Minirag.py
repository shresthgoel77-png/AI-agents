import faiss
import numpy as np
# Fixed typo: SentenceTransformer (with an 'r')
from sentence_transformers import SentenceTransformer

documents = [
    "Python is a popular programming language used for AI and web development.",
    "RAG stands for Retrieval-Augmented Generation. It combines retrieval and generation.",
    "FAISS is a library developed by Facebook for efficient similarity search.",
    "Embeddings convert text into numerical vectors so computers can compare meanings.",
    "Vector databases store embeddings and allow semantic search.",
]

# Fixed typo: SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")


# Fixed the indentation and logic inside chunk_text
 def chunk_text(text, chunk_size=50):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i : i + chunk_size]
        chunks.append(chunk)  # Fixed: appended 'chunk', not 'chunks'
    return chunks  # Fixed: return statement must sit outside the loop


# Fixed indentation: Pulled this block out of the function definition
chunked_documents = []
for doc in documents:
    chunks = chunk_text(doc)
    chunked_documents.extend(chunks)

# Create FAISS index
embeddings = model.encode(chunked_documents)
embeddings_matrix = np.array(embeddings).astype("float32")
dimension = embeddings_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings_matrix)

# Fixed typo: 'True' must be capitalized
while True:
    query = input("\nPlease enter your query: ")
    if not query.strip():
        print("Please do not enter a blank query")
        continue
    if query.lower() == "exit":
        print("Bye bye brotha")
        break

    # FIXED INDENTATION: The search logic must live inside the while loop,
    # otherwise it will never execute.
    query_embeddings = model.encode([query])  # Wrap query in a list for 2D array
    query_embeddings = np.array(query_embeddings).astype("float32")

    top_k = 3
    distances, indices = index.search(query_embeddings, top_k)
    retrieved_docs = [chunked_documents[i] for i in indices[0]]

    print("\nThe retrieved documents are:")
    # Fixed typo: corrected the syntax of the enumerate loop
    for i, doc in enumerate(retrieved_docs, start=1):
        print(f"{i}. {doc}")
