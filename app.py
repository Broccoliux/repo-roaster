from flask import Flask, render_template, request, jsonify
from github import fetch_repo_data, build_repo_context

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/roast", methods=["POST"])
def roast():
    data = request.get_json()

    repo_url = data.get("url", "")

    repo = fetch_repo_data(repo_url)

    context = build_repo_context(repo_url)

    if repo is None:
        return jsonify({
            "success": False,
            "message": "Repository not found."
    }), 404

    return jsonify({
        "success" : True,
        "repo": repo,
        "context": context
    })


if __name__ == "__main__":
    app.run(debug=True)
