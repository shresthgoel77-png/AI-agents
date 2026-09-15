test =[{
    "prompt = What is the capital of uk"
    "expected = london"
},
{
    "prompt = what is the value of t=2+2"

    "expected = 4"
}
]

# 2. Simulate the LLM Generation
def mock_llm_model(prompt):
  # In a real app, this would call OpenAI, Anthropic, or a local model API
  model_responses = {
      "What is the capital of France?": (
          "The capital of France is Paris, a major European city."
      ),
      "What is 2 + 2?": (
          "The answer is 5."
      ),  # Intentional error for testing
  }
  return model_responses.get(prompt, "")

  # 3. Define the Scorer (Checks if the expected answer is present)
def evaluate_response(response, expected):
  return expected.lower() in response.lower()   