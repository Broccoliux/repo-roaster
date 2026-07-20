from flask import Flask, render_template, request, jsonify, Response
from github import fetch_repo_data, build_repo_context
from roaster import roast_repo
from cache import repo_cache


import time
import random

app = Flask(__name__)

# Funny error messages shown to the user if Gemini fails
ERRORS = [
    "💀 Repo Roaster rage quit. Your repo dealt psychic damage to the AI. Try again in a minute, you freak.",
    "🤢 Your repo was so painful that Repo Roaster filed for workers' compensation.",
    "☠️ My LLM refused hazard pay after seeing this repository.",
    "💀 Even my LLM couldn't survive this codebase. Give it a minute to recover.",
    "🤡 Your repo crashed the roaster before it could finish. I think you already know how cooked this repo is."
]


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/repo", methods = ["POST"])
def repo():

    data = request.get_json()
    repo_url = data.get("url", "")

    start = time.time()

    repo = fetch_repo_data(repo_url)

    print(f"Repo: {time.time() - start:.3f}s")

    if repo is None:
        return jsonify({
            "success": False,
            "message": "Repository not found."
        }), 404
    
    return jsonify({
        "success": True,
        "repo": repo 
    })


@app.route("/stream", methods=["POST"])
def stream():

    data = request.get_json()
    repo_url = data.get("url", "")

    #build context
    start = time.time()

    if repo_url in repo_cache:
        context = repo_cache[repo_url]
        print("context: Loaded from cache")
    else: 
        context = build_repo_context(repo_url)
        repo_cache[repo_url] = context
        print("Context: Built and cached")

    print(f"Context: {time.time() - start:.3f}s")

    # Stream Gemnini

    try:
        return Response(
            roast_repo(context),
            mimetype="text/plain"
        )
    
    except Exception as e:
        print("Gemini Error:", e)

        return jsonify({
            "success": False,
            "message" : random.choice(ERRORS)
        }), 500



if __name__ == "__main__":
    app.run(debug=True)