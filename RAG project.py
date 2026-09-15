import numpy as np
import openai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
print("yoooooooo whats up brotha")
model = SentenceTransformer("all-MiniLM-L6-v2")
paragraphs = [
    "All full-time employees accrue 1.5 days of paid vacation per month, totaling 18 days annually. Vacation requests must be submitted to managers via the HR portal at least two weeks in advance.",
    "The company provides a monthly stipend of up to $50 for mobile phone expenses. To qualify, employees must submit their itemized phone bills through the expense management system by the 5th of each month.",
    "Core business hours are from 9:00 AM to 5:00 PM, Monday through Friday. All employees are expected to be available online or in the building during these hours, with a flexible 1-hour window for lunch.",
    "Employees receive 10 fully paid sick days per calendar year. If an illness extends beyond three consecutive business days, a formal note from a licensed medical professional is required by HR.",
    "Under our hybrid model, team members are eligible for flexible arrangements. Employees can work remotely up to 3 days per week, provided they coordinate their in-office days with their direct supervisor.",
]

paragraph_embeddings = model.encode(paragraphs)
while True :
    user_query = input("please enter your query")
    
    if not user_query.strip():
        print("the query entered by the user is null")
        continue
    if user_query.lower() == "exit" :
        print("by brotha")
        break 
    query_embedding = model.encode(user_query)
    similarity = cosine_similarity(query_embedding, paragraph_embeddings)[0]
    best_match_idx = np.argmax(similarities)
    retrieved_context = paragraphs[best_match_idx]
    augmented_prompt = f"""
You are a precise HR assistant. Answer the user's question using ONLY the provided context.
If the answer is not in the context, say "I don't know".
Context:
"{retrieved_context}"

Question:
"{user_query}"


"""

print(f"\n🔍 System ne Paragraph {best_match_idx + 1} retrieve kiya!")
print(augmented_prompt)

respone = openai.ChatCompletion.create(
        model="gpt-4o",
    messages=[{"role": "user", "content": augmented_prompt}]
)
final_answer = response.choices[0].message.content
print(f"🤖 AI ka Answer: {final_answer}")
    b
