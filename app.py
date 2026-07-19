from flask import Flask, render_template, request, jsonify
from github import fetch_repo_data, build_repo_context
from roaster import roast_repo
import time


app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/roast", methods=["POST"])
def roast():
    data = request.get_json()

    repo_url = data.get("url", "")

    start = time.time()
    repo = fetch_repo_data(repo_url)
    print("Repo:", time.time() - start)

    if repo is None:
        return jsonify({
            "success": False,
            "message": "Repository not found."
    }), 404

    start = time.time()
    context = build_repo_context(repo_url)
    print("context:", time.time() - start)

    start = time.time()
    
    try:
        roast = roast_repo(context)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    
    print("Gemini:", time.time() - start)
 

    return jsonify({
        "success" : True,
        "repo" : repo,
        "roast": roast
    })

if __name__ == "__main__":
    app.run(debug=True)
