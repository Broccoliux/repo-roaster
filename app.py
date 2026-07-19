from flask import Flask, render_template, request, jsonify
from github import fetch_repo_data, build_repo_context
from roaster import roast_repo

import time
import random

app = Flask(__name__)

# funny error messages shown to the user if Gemini fails

ERRORS = [
    "💀 Repo Roaster rage quit. Your repo dealt psychic damage to the AI. Try again in a minute, you freak.",
    "🤢 Your repo was so painful that Repo Roaster filed for workers' compensation.",
    "☠️ My LLM refused hazard pay after seeing this repository.",
    "💀 Even my LLM couldn't survive this codebase. Give it a minute to recover.",
    "🤡 Your repo crashed the roaster before it could finish. I think you already know how cooked this repo is."
]

# home page

@app.route("/")
def home():
    return render_template


# roasting end point

@app.route("/roast", methods=["POST"])
def roast():

    # get JSON send by JS\
    data = request.get_json()
    repo_url = data.get("url", "")

    # fetchs the repo info

    start = time.time()
    repo = fetch_repo_data(repo_url)

    print("Repo:", time.time() - start)

    if repo is None:
        return jsonify({
            "success": False,
            "message": "Repository not found."
        }), 404

    # build context for Gemini

    start = time.time()
 
    context = build_repo_context(repo_url)
    print("Context:", time.time() - start)

    # genration roast

    start = time.time()

    try:
        roast = roast_repo(context)

    except Exception as e:
        
        # Print the real  error in the terminal for debugging

        print("Gemini Error:", e)

        # show funny message to the user

        return jsonify({
            "success": False,
            "message": random.choice(ERRORS)
        }), 500
    
    print("Gemini:", time.time() - start)

    # send result back to frontend

    return jsonify({
        "success": True,
        "repo": repo,
        "roast": roast
    })


    if __name__ == "__main__":
        app.run(debug=True)