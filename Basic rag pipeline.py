from dotenv import load_dotenv
import os
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

# 1. Load keys (OpenAI for embeddings, Pinecone for database)
load_dotenv()

# 2. Initialize the Pinecone client
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index_name = "my-test-index"

# Create a serverless index if it doesn't already exist
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536, # Must match OpenAI's embedding size
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# 3. Define the raw data you want to save
docs = [
    Document(page_content="Artificial Intelligence agents can execute complex workflows."),
    Document(page_content="Pinecone is a cloud-native vector database optimized for similarity search.")
]

# 4. Choose an Embedding Model (converts text to numbers)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 5. Save (Upsert) the data into Pinecone via LangChain
vector_store = PineconeVectorStore.from_documents(
    documents=docs,
    embedding=embeddings,
    index_name=index_name
)

print("Data successfully embedded and saved to Pinecone!")
