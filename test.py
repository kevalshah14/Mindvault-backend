import os
from markitdown import MarkItDown
from openai import OpenAI

API_KEY = os.getenv('OPENAI_API_KEYs')
BASE_URL = os.getenv('baseURL')
client = OpenAI(api_key=API_KEY)
md = MarkItDown()
result = md.convert("test.pdf")
print(result.text_content)