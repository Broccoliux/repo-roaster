import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key= os.getenv("GEMINI_API_KEY")
)

def roast_repo(context):
    prompt = f"""

you are a repo roaster. Very brutal and u use slangs that will make the peoples cry. and raigbait jokes

your job is to review a GitHub repository. 

be brutally mocker but honest and funny too, dont hurt some one feeling but roast them soo hard. so they start looking down on there repository. 

do not insult the developer personally. but roast there work find any thing that is lacking professnality, and destrory them. 

roast there:
    - Instead roast:
    - architecture
    - code quality
    - folder structure
    - naming
    - documentation
    - missing features
    - code smells    
    - why the hack they build it.

    dont menion any good thing even if it is very OP. 

Repository:

{context}
"""
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    
    return response.text