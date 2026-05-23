from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

# Hide warning messages
warnings.filterwarnings("ignore")

# Model name from Hugging Face
model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"

print("Loading model...")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set padding token
tokenizer.pad_token = tokenizer.unk_token

# Load language model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",
    torch_dtype=torch.float32
)

# Initial system prompt
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Give short and concise answers in 2-3 lines."
        )
    }
]

print("Chatbot started. Type 'exit' to quit.\n")

# Chat loop
while True:

    # Take user input
    user_input = input("> ")

    # Exit condition
    if user_input.lower() == "exit":
        break

    # Store user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Keep only recent conversation history
    messages = [messages[0]] + messages[-10:]

    # Convert conversation into model tokens
    tokenized = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
        max_length=512
    )

    # Generate AI response
    with torch.inference_mode():

        outputs = model.generate(
            tokenized["input_ids"],
            attention_mask=tokenized["attention_mask"],
            max_new_tokens=60,
            temperature=0.5,
            top_p=0.8,
            do_sample=True,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.pad_token_id
        )

    # Decode generated tokens into readable text
    response = tokenizer.decode(
        outputs[0][tokenized["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    # Print bot response
    print(f"Bot: {response}\n")

    # Save assistant response into memory
    messages.append({
        "role": "assistant",
        "content": response
    })