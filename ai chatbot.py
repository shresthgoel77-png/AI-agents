from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"
MAX_HISTORY = 6
MAX_NEW_TOKENS = 80

warnings.filterwarnings("ignore")

# -----------------------------
# Device setup
# -----------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")
print("Loading model...\n")

# -----------------------------
# Load tokenizer
# -----------------------------
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Better padding setup
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# -----------------------------
# Load model
# -----------------------------
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

model.eval()

# -----------------------------
# Initial conversation
# -----------------------------
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Reply briefly and clearly in 2-3 lines."
        )
    }
]

print("Chatbot started.")
print("Type 'exit' or 'quit' to stop.\n")

# -----------------------------
# Chat loop
# -----------------------------
while True:

    try:
        user_input = input("> ").strip()

        # Exit conditions
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not user_input:
            continue

        # Store user message
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Keep recent history
        messages = [messages[0]] + messages[-MAX_HISTORY:]

        # -----------------------------
        # Tokenize conversation
        # -----------------------------
        inputs = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        ).to(device)

        # -----------------------------
        # Generate response
        # -----------------------------
        with torch.inference_mode():

            outputs = model.generate(
                inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                repetition_penalty=1.15,
                no_repeat_ngram_size=3,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id
            )

        # -----------------------------
        # Decode only new tokens
        # -----------------------------
        response_tokens = outputs[0][inputs.shape[-1]:]

        response = tokenizer.decode(
            response_tokens,
            skip_special_tokens=True
        ).strip()

        # Fallback response
        if not response:
            response = "I couldn't generate a response."

        # Print response
        print(f"\nBot: {response}\n")

        # Save assistant response
        messages.append({
            "role": "assistant",
            "content": response
        })

    except KeyboardInterrupt:
        print("\nExiting chatbot...")
        break

    except Exception as e:
        print(f"\nError: {e}\n")
