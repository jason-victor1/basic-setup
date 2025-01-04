from openai_module import generate_text_basic

prompt = "Explain the concept of AI agents in one sentence."

response = generate_text_basic(prompt, model="gpt-4o")

print(response)
