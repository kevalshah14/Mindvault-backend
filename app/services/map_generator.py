
import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.getenv('apiKey'),
    base_url="https://api.featherless.ai/v1",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    (
        "human",
        "I love programming."
    ),
]
ai_msg = llm.invoke(messages)
print(ai_msg)