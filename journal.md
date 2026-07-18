yooo was upp


today is 16/7/2026

i am making a webapp that will roste u like hell, on ur repos

i have made tye files now making the virtual env.

the virtual env is now set. now i haev to install the needed libs and pakages

![alt text](image.png)

i am done with all packages and everthing , i needed now gonna build. 

just tested everything is working very well now

something happed
![alt text](image-1.png)
=======

something is not going well

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/0dca3be2-1ea7-4dea-a7a7-d1eb38b869a6" />

i did it

<img width="678" height="703" alt="image" src="https://github.com/user-attachments/assets/9b27379d-201e-4327-825c-04b8b3932832" />


ohh my yessssssss

i am learning

<img width="1366" height="735" alt="image" src="https://github.com/user-attachments/assets/02a261eb-8000-4d8d-9d2b-746430283b20" />

i was coding and tesing and suddenly hit the the wall of api limit reached.so now gonna make own api, that will be mroe relibal.

i am dumb i am not gonna make a new api but will be using PAT.
got the api, i hope now i dont have to take care for apis.

i have fixed the part of code that were not respondiong. i hope the will work and gonna test 10-15 repos.

oky so the all repos are woking fine and the data is getting fetched.

made the .env to store the API keys.

ohh my yess it working yyayayyayyayayayayyayayayyayayay


i added the new code but it is not wokring idk why, need to fix, i think i am forgeting something, i take a break for 2hrs, i think i forgot, lol, im dumb

bro idk but i am stuck

bruh my code as alr, but i accidently pused the.env to github with api. and github revoked that api, thats all

now all the main things work check the list below.

✅ Flask backend
✅ GitHub API
✅ Token auth
✅ Input validation
✅ Error handling
✅ Frontend displays repo info
✅ Debug code removed

next gonna make the thing, where the repo will be cloned for a while and this will help to read the actuall matirial in the repo, like

 main.py
package.json
README.md
app.js

idk why test.py is taking too long just to colne a small repo/

ohh the reason wwas that the repo i was trying to clone was soo big soo it took soo much time, then triedthe hello world repo it was cloned instantly, it showd me HELLO WORLD init, means it is working the cloning.

cuz the repo is taking too long to be loned soo i need to find solution to this, cuzz this is too waste of time.

soo this is it for today, will start working from tmro i dont have time to waste. i need to get to the SIN no mattter, what. 

i have chenged the clone process now it will only clone the depth 1 means only lates commits. but still for BIG repo like [text](https://github.com/different-ai/openwork) it is taking soo much time.

idk how i am gonna do it ut i will definatly wont leave it like this, i will make it work in secs, or ms, but idk how, or if this is possible or not. 
soo byeeee. for today. 

-----------------------------

 18/7/2025

------------------------------


today gonna make the AI start roasting

but even before that we are gonna find the solution for the late cloning, id this very bad and will give bad impresion.

i am going with completely new appproch where, i will not clone the repo instead we will go with GitHub APi. i have 5000 requeest per hr so it will be enough, 

```
For example, if one roast uses:

1 request → repo info
1 request → file tree
15 requests → important files

= 17 requests per roast

So:

5000 / 17 ≈ 294 full roasts per hour

```

The planed Architecture

User repo URL
      │
      ▼
Github API
      │
      ├── Repo info
      ├── File tree
      ├── readme
      ├── package.json
      ├── requirment.txt
      ├── Main spurce file
      ▼
 AI
      ▼
Roast Roast Roast



**OH MY YESS**

```
Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)
$ python test.py
Hello World!

(venv) 
Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)

```

rn i am working on new thing, that will might speed up the fetch but i am not sure.

ahh bro i am stuck



ohhhhhhhhhhh yesssssssssssssssshhhhhhhhhhhhh

```

Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)
$ python test.py
.gitignore
.vscode
.vscode/settings.json
LICENSE
README.md
__pycache__
__pycache__/github.cpython-313.pyc
app.py
cloner.py
github.py
journal.md
requirements.txt
roaster.py
static
static/script.js
static/style.css
templates
templates/index.html
terminal-wakatime.ps1
test.py
(venv) 
Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)
```


ohh my yesss we rolllin

rn i am trying to store the fetch the files data no just the name. 

ohh yeaaaaaa i did it.

```

 python test.py


==== README.md ====
# repo-roaster

==== app.py ====
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

    repo = fetch_repo_data(repo_url)

    if repo is None:
        return jsonify({
            "success": False,
            "message": "Repository not found."
    }), 404

    return jsonify({
        "success" : True,
        "repo": repo
    })


if __name__ == "__main__":
    app.run(debug=True)


==== cloner.py ====
import tempfile

from git import Repo

def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(repo_url, temp_dir, depth=1)

    return temp_dir


==== github.py ====
from dotenv import load_dotenv
import base64
import os 
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

import requests
from urllib.parse import urlparse

def extract_repo_info(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts [0],parts [1]

def fetch_repo_data(url):
    owner, repo = extract_repo_info(url)
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    response = requests.get(api_url, headers=headers)

    data = response.json()
    
    if response.status_code !=200:
        return None
    

    repo_info = {
        "name": (data["name"]),
        "description": (data["description"]),
        "language": (data["language"]),
        "stars": (data["stargazers_count"]),
        "forks": (data["forks_count"]),
        "owner": data["owner"]["login"],
    }
    return repo_info

def fetch_repo_tree(url):
    owner, repo = extract_repo_info(url)

    api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"

    headers = {
        "Authorization": f"token {TOKEN}"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        return None

    return response.json()["tree"]

def fetch_file_content(url, file_path):
    owner, repo = extract_repo_info(url)

    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"

    headers = {
        "Authorization": f"token {TOKEN}"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code !=200:
        return None
    
    data = response.json()

    return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")

def get_important_files(tree):
    important = []

    extention = (

        ".py", ".js", ".ts", ".jsx", ".tsx",
        ".java", ".cpp", ".c", ".cs", ".go",
        ".rs", ".php", ".html", ".css"
    )

    for file in tree:
        path = file["path"]

        if (
            path.lower() == "readme.md"
            or path.lower() == "package.json"
            or path.lower() == "requirements.txt"
            or path.lower() == "pyproject.toml"
            or path.endswith(extensions)
        ):
            important.append(path)

    return important[:20]

==== requirements.txt ====
blinker==1.9.0
certifi==2026.6.17
charset-normalizer==3.4.9
click==8.4.2
colorama==0.4.6
Flask==3.1.3
gunicorn==26.0.0
idna==3.18
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
packaging==26.2
python-dotenv==1.2.2
requests==2.34.2
urllib3==2.7.0
Werkzeug==3.1.8


==== static/script.js ====
const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");
const result = document.getElementById("result");

console.log("NEW SCRIPT LOADED");

button.addEventListener("click", async () => {

    const url = input.value.trim();


    if (url === "") {
        alert("empty");
        return;
    }

    if (!isValidGitHubUrl(url)) {
        alert("invalid");
        return;
    }

    const response = await fetch("/roast", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url
        })
    });

    const data = await response.json();

    if (!data.success) {
        result.innerHTML = `<h2>${data.message}</h2>`;
        return;
    }

    result.innerHTML = `
        <h2>📦 ${data.repo.name}</h2>
        <p>👤 ${data.repo.owner}</p>
        <p>⭐ ${data.repo.stars}</p>
        <p>🍴 ${data.repo.forks}</p>
        <p>💻 ${data.repo.language || "Unknown"}</p>
        <p>📝 ${data.repo.description || "No description provided."}</p>
    `;

}); 

function isValidGitHubUrl(url) {
    const pattern = /^https?:\/\/github\.com\/[^\/]+\/[^\/]+\/?$/;
    return pattern.test(url);
}

==== static/style.css ====
body{
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #0a0a0a;
     color: white;

}

main{
    width: 90%;
    max-width: 900px;
    margin: auto;
    padding-top: 80px;
}

.hero{
    display: flex;
    flex-direction: column;
    gap: 18px;
}

input{
    padding: 14px;
    font-size: 16px;
}

button{
    width: 130px;
    padding: 15px;
    cursor: progress;

}

==== templates/index.html ====
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repo Roaster</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <script src="{{ url_for('static', filename='script.js') }}" defer></script>
</head>

<body>
   <main>
     <section class="hero">
        <h1>🔥 REPO ROASTER</h1>

        <p>Paste a Github repo URL. GET destyroyed.</p>

        <input
        type="text"
        id="repo-url"
        placeholder="https://github.com/owner/repository"
        >

        <button id="roast-btn">
            Roast it
        </button>
     </section>
     <section id="result">
     </section>
   </main>
</body>
</html>


==== test.py ====
from github import fetch_file_content

content = fetch_file_content(
    "https://github.com/octocat/Hello-World",
    "README"
)

print(content)
(venv) 
Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)
$ 

```

its is gving the files data

next i ma going to connect the LLM

but even before that we need to test this pipeline in our local host server.

it works in local host too

<img width="1366" height="725" alt="image" src="https://github.com/user-attachments/assets/3f9e25f9-1e61-49a1-9cf8-1e6d029fe0d7" />
