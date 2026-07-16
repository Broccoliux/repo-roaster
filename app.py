from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/roast", methods=["POST"])
def roast():
    data = request.get_json()

    repo_url = data.get("url", "")

    return jsonify({
        "success": True,
        "message": "Backend received the URL!",
        "url": repo_url
    })

if __name__ == "__main__":
    app.run(debug=True)