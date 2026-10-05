import os

from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("Set the GROQ_API_KEY environment variable before running this script.")

client = Groq(
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant. Answer concisely in short sentences."},
        {"role": "user", "content": "Explain what an AI agent is in one sentence."},
        {"role": "assistant", "content": "An AI agent is simply a LLM connected to tools in a loop."}
    ],
)

print(response.choices[0].message.content)