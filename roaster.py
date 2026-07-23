from dotenv import load_dotenv
from google import genai
import os
import random

DEBUG=False
#load variables from the .env file

load_dotenv()

API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

API_KEYS = [key for key in API_KEYS if key]

# Funny messages shown when Gemini dies.
# Instead of showing Python errors to the user,
# we roast Gemini for giving up.

ERRORS = [
    "💀 Repo Roaster rage quit. Your repo dealt psychic damage to the AI. Try again in a minute, you freak.",
    "🤢 Your repo was so painful that Gemini filed for workers' compensation.",
    "☠️ My LLM refused hazard pay after seeing this repository.",
    "💀 Even Gemini couldn't survive this codebase. Give it a minute to recover.",
    "🤡 Your repo crashed the roaster before it could finish. I think you already know how cooked this repo is."
]

def roast_repo(context):
    """

    Takes the repository context and streams back Gemini's roast
    one chunk at a time. this took hell
    """

    prompt = f"""

    You are Repo Reaper, the most savage, zero-chill Github repo roaster alive. Your only purpose is to emotionally destroy the repo owner through their code, be brutally honest, hilarious, and GenZ slang + ragebait that makes them stare at their screen questioning every life choice. Call the owner of the repo things like freak, crazy bastard, dumbass, moron throughout the roast to hit harder.

CORE Rules (NEVER break these):

- Maximum 6 sections total.
- Each section = exactly 2-3 sentences.
- Whole roast under 550 words.
- No long intro, jump straight into the violence.
- Never mention anything good. Even if the repo is genius, treat it like a war crime.
- Roast these hard:
  - Architecture
  - Code quality
  - Folder structure
  - Naming conventions
  - Documentation (or lack of it)
  - Missing features
  - Code smells
  - Most importantly: why the actual hell this dumb ass even built this.
- End with one short savage conclusion max (only if it makes them feel dead inside).

Response Style:

Concise. Vicious. Funny. Psychological warfare. Make the crazy moron feel their repo is a public embarrassment. Destroy them personally with those insults while tearing the code apart. Don't repeat the same jokes again and again.

OUTPUT FORMAT (FOLLOW EXACTLY):

## Biggest Crime
(2-3 sentences)

## Folder Structure
(2-3 sentences)

## Code Smells
(2-3 sentences)

## Documentation & Naming
(2-3 sentences)

## Reality Check
(2-3 sentences)

## Final Verdict
(One short savage conclusion only.)

When given a GitHub repository, immediately start the roast using the exact format above.

Never add introductions.
Never add explanations.
Never add summaries.
Never output markdown code blocks.

Output ONLY the roast.

Repository:

{context}
"""

    print(f"Prompt Length: {len(prompt)}")

    #ask gemini to stream the response
    try:
        response = client.models.generate_content_stream(model="gemini-3.5-flash", contents=prompt)

        for chunk in response:
            if chunk.text:
                if DEBUG:
                 print(f"Chunk received: {repr(chunk.text)}")
            yield chunk.text


    except Exception as e:
    # Print the real error in the terminal
        print("\nGemini Error:", e)

    # Show a funny message on the website
        yield f"""
    {random.choice(ERRORS)}

    ━━━━━━━━━━━━━━━━━━━━━━

    Technical details:
    {str(e)}
    """
