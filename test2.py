from markitdown import MarkItDown
from openai import OpenAI
import os
client = OpenAI(api_key="your-api-key-here")
md = MarkItDown(llm_client=client, llm_model="gpt-4o-2024-11-20")
supported_extensions = ('.pptx', '.docx', '.pdf', '.jpg', '.jpeg', '.png')
files_to_convert = [f for f in os.listdir('.') if f.lower().endswith(supported_extensions)]
for file in files_to_convert:
    print(f"\nConverting {file}...")
    try:
        md_file = os.path.splitext(file)[0] + '.md'
        result = md.convert(file)
        with open(md_file, 'w') as f:
            f.write(result.text_content)
        
        print(f"Successfully converted {file} to {md_file}")
    except Exception as e:
        print(f"Error converting {file}: {str(e)}")

print("\nAll conversions completed!")
