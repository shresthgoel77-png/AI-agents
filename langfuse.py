import os
from langfuse import observe

# Configure Langfuse credentials (can also use self-hosted base url)
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-..."
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-..."
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"  # or your local server


@observe()  # Automatically captures inputs, outputs, and errors
def my_llm_app(query: str):
  # Simulating processing
  return f"Langfuse response for: {query}"


# Running the observed function
result = my_llm_app("Hello Langfuse!")