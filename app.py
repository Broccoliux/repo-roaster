from flask import Flask, render_template, request, jsonify, Response
from github import fetch_repo_data, build_repo_context
from roaster import roast_repo
from cache import repo_cache

import time
import random

# creats the flask application

app = Flask(__name__)

#funny error msg will be shown to the user then Gemini dies.
# without this the webpage will show the api error, so instead if the error the user will see the these messages. too the web page intertaning.

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

# reop end point

# JavaScript calls this frist.
# purpose:
# Validata the Github repo
# fetch stars, forks, owner, language, etc.
# returns only repo info.

@app.route("/repo", methods=["POST"])
def repo():

    data = request.get_json()
    repo_url = data.get("url", "")


    start = time.time()
    repo = fetch_repo_data(repo_url)
    print(f"Repo: {time.time() - start:.3f}s")

    if repo is None:
        return jsonify({
            "success": False,
            "message": "Cant find that garbage"
        }), 404

    return jsonify({
        "success": True,
        "repo": repo
    })


#stream endpoint

# javaScript calls this Scnd

#purpose:
# this build the repo context.
# cache it so the future reequests are faster
#stream Gemini output chunk-ny chunk

#this is where the Ai will start working

@app.route("/stream", methods=['POST'])
def stream():

    data = request.get_json()
    repo_url = data.get("url", "")

    #build context or will load from cache, if savedf

    start = time.time()
    
    if repo_url in repo_cache:

        context = repo_cache[repo_url]
        print("Context: loaded from cache")

    else:
        context = build_repo_context(repo_url)
        repo_cache[repo_url] = context

        print("Context: Built and cached")

    print(f"Context: {time.time() - start:.3f}s")


#this streams the Gemini response

# roast_repo() is generator because it uses the ("yield")

# Response() forward every chunk directly
# to the browser as soon as Gemini sends it.

    try:

        return Response(
            roast_repo(context),
            mimetype="text/plain"
        )
    
    except Exception as e:
        print("GEmini Error:", e)

        return jsonify({
            "success": False,
            "message": random.choice(ERRORS),
            "error": str(e)
        }), 500
    
# start Flask server

#debug=True auto reloads the server whenever someone saves the file.

if __name__ == "__main__":
    app.run(debug=True)