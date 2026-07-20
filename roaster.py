
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

print("API KEY:", os.getenv("GEMINI_API_KEY"))

client = genai.Client(
    api_key= os.getenv("GEMINI_API_KEY")
)

def roast_repo(context):
    prompt = f"""


Roast this GitHub repository in a funny way.

Repository:


{context}
"""
    
    print(len(prompt))


    response = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=prompt
    )    
    
    for chunk in response:
        if chunk.text:
            yield chunk.text