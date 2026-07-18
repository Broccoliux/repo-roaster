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
    ur allowed to use slang. as a GENZ e.g anyslang, just not too naughty, a lil puch is enouh.

    rules:

    keep the entire roast under 550 words. not word should be suggestion, only total roasting
    maximum 6 section only. --> full of ragebait
    Each section must be 2-3 sentences only. --> make him feel dead inside
    No long introduction. --> but the important context must be there
    No conclusions longer then one sentence. only if there is too much need of it to make the repo owner cry
    Be concise, brutal, and funny and destory them using patters and pycology.

Repository:

{context}
"""
    
    print(len(prompt))


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    
    return response.text

