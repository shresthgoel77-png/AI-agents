import os
from langsmith import traceable

# 1. Configure LangSmith Environment Variables
# (Normally you set these in your terminal or a .env file)
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = "your_lsv2_api_key_here"  # Replace with your key
os.environ["LANGSMITH_PROJECT"] = "my-first-project"


# 2. Use the @traceable decorator to monitor this function
@traceable
def process_user_query(query: str):
  # Simulate a multi-step AI process
  formatted_prompt = f"System: Answer the user.\nUser: {query}"

  # Pretend this is an LLM call step
  response = fake_llm_call(formatted_prompt)

  return response


def fake_llm_call(prompt):
  # Simulating processing delay and output
  return f"Processed response for: '{prompt}'"


# 3. Run your function
if __name__ == "__main__":
  print("Running tracked function...")
  result = process_user_query("What is Human-in-the-Loop?")
  print(f"Result: {result}")