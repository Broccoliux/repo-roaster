from flask import Flask, render_template, request, jsonify
from github import fetch_repo_data


app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/roast", methods=["POST"])
def roast():
    data = request.get_json()

    repo_url = data.get("url", "")
    repo= fetch_repo_data(repo_url)
    print(repo_url)

    return jsonify({
        "success": True,
        "repo": repo
        
    })

if __name__ == "__main__":
    app.run(debug=True)





