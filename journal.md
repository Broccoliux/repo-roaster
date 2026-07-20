yooo was upp


today is 16/7/2026

i am making a webapp that will roste u like hell, on ur repos

i have made tye files now making the virtual env.

the virtual env is now set. now i haev to install the needed libs and pakages


i am done with all packages and everthing , i needed now gonna build. 

just tested everything is working very well now

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
```
✅ Flask backend
✅ GitHub API
✅ Token auth
✅ Input validation
✅ Error handling
✅ Frontend displays repo info
✅ Debug code removed
```
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

rn its is taking a lil bit time, and i did not find the way to make this happen fast. even AI didnt helped me.


not  a good sign it the context must be more then 10K

```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 102-280-820
127.0.0.1 - - [18/Jul/2026 11:11:32] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Jul/2026 11:11:33] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 -
127.0.0.1 - - [18/Jul/2026 11:11:33] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [18/Jul/2026 11:11:33] "GET /static/script.js HTTP/1.1" 304 -
127.0.0.1 - - [18/Jul/2026 11:11:38] "GET /favicon.ico HTTP/1.1" 404 -
============================================================
context lenght: 6612
============================================================
127.0.0.1 - - [18/Jul/2026 11:12:05] "POST /roast HTTP/1.1" 200 -
```

let me check the total context lenght for my repo. then it will tell us if oour repo is small or the problem is some where else


my test repo have only 
TOTAL: 6215
test.py 129

TOTAL: 6344


going great do far

i aws tesing with my repo, now i will test it with the other lenghty repos.

working file with other repos too just taking a bit more time

```
$ python test.py
README.md 4991

TOTAL: 4991
resources/symbols/AT7456E/Altair/Readme.html 285

TOTAL: 5276
resources/symbols/AT7456E/Altium/Readme.html 326

TOTAL: 5602
resources/symbols/AT7456E/DEHDL/at7456e/sym_1/symbol.css 3718

TOTAL: 9320
resources/symbols/AT7456E/DesignSpark PCB/Readme.html 813

TOTAL: 10133
resources/symbols/AT7456E/EAGLE/Readme.html 2014

TOTAL: 12147
resources/symbols/AT7456E/EasyEDA/Readme.html 599

TOTAL: 12746
resources/symbols/AT7456E/PADS/AT7456E.c 2178

TOTAL: 14924
resources/symbols/AT7456E/Proteus/8.8 or earlier/Readme.html 708

TOTAL: 15632
resources/symbols/AT7456E/Proteus/8.9 or later/Readme.html 416

TOTAL: 16048
resources/symbols/OpenESC_20X20-main/README.md 6345

TOTAL: 22393
resources/symbols/OpenESC_20X20-main/hardware/scripts/v_beta_hygiene_fix.py 6710

TOTAL: 29103
resources/symbols/OpenESC_20X20-main/hardware/tools/esc_thermal.py 21612

TOTAL: 50715
resources/symbols/OpenESC_20X20-main/licensing/README.md 695

TOTAL: 51410
(venv) 

```

this is where i am rn

```

GitHub URL
      ↓
GitHub API
      ↓
Repository Context
      ↓
JSON Response

```

what my goal is 
```
GitHub URL
      ↓
GitHub API
      ↓
Repository Context
      ↓
LLM
      ↓
Roast

```

so the next step is to connect LLm and then prompt engineering. i know how to connect the LLm but idk what to do with prompt, i only the img genration prompt lol.

also i need the LLM that is free and have big enough context window.

i think i will go with.

i think i will go with the NVIDIA free API, like GLM 4 or KIMI 2.5

hnow gonna get the API from the NVIDIA. 
why the hell they asks too much.
its taking soo much time. idk if this is my internet

fkup, to get the API i need to verify with my number and NIVIDA is not availible in pkakistan. damn man. now i have to get any other API.

now going with gemini

so this is where i am rn and what i need to get
greens means i completed that and while means i have to do it.
```
✅ GitHub API
✅ Repo Tree
✅ Important Files
✅ Context Builder

⬜ Gemini API Key
⬜ Connect Gemini
⬜ Build Roast Prompt
⬜ Return AI Roast
⬜ Display on Website
⬜ Make it look 🔥
```
bruh finally got the API key from google. 

pip installed now gonna start the real thinbg
i amgetting the error that the model i am ttrying to use is not for free users.

let mee see what model are avalible for me

yoo i have inmpressive varity

```


  import google.generativeai as genai
models/gemini-2.5-flash
models/gemini-2.5-pro
models/gemini-2.0-flash
models/gemini-2.0-flash-001
models/gemini-2.0-flash-lite-001
models/gemini-2.0-flash-lite
models/gemini-2.5-flash-preview-tts
models/gemini-2.5-pro-preview-tts
models/gemma-4-26b-a4b-it
models/gemma-4-31b-it
models/gemini-flash-latest
models/gemini-flash-lite-latest
models/gemini-pro-latest
models/gemini-2.5-flash-lite
models/gemini-2.5-flash-image
models/gemini-3-pro-preview
models/gemini-3-flash-preview
models/gemini-3.1-pro-preview
models/gemini-3.1-pro-preview-customtools
models/gemini-3.1-flash-lite-preview
models/gemini-3.1-flash-lite
models/gemini-3-pro-image-preview
models/gemini-3-pro-image
models/nano-banana-pro-preview
models/gemini-3.1-flash-image-preview
models/gemini-3.1-flash-image
models/gemini-3.1-flash-lite-image
models/gemini-3.5-flash
models/gemini-omni-flash-preview
models/lyria-3-clip-preview
models/lyria-3-pro-preview
models/gemini-3.1-flash-tts-preview
models/gemini-robotics-er-1.5-preview
models/gemini-robotics-er-1.6-preview
models/gemini-2.5-computer-use-preview-10-2025
models/antigravity-preview-05-2026
models/deep-research-max-preview-04-2026
models/deep-research-preview-04-2026
models/deep-research-pro-preview-12-2025
```

let mee what modle is best for my specific use case.

so i am gonna use the **gemini-3.5-flash**

idk why it is taking soo much time.

idk what the hack is this yt td


ohh man its working
```
Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)
$ python gemini_test.py
Hello, I hope you are having a wonderful day!
(venv) 
Smart Tech@DESKTOP-3V1CTK6 MINGW64 /f/OneDrive/Desktop/cloned repos/repo-roaster (main)
$ 
```
now its time for fun part.

i have made the prompt for now this is soo simple just to check if everything is working fine or not.

its is taking soo much time.

there was an error int he code so i hit the error that time now i have fixed lets see how it goes this time>


ohh man this shit that i made roasted mee fahh.

u should must read this

```
Oh boy, look what drifted in from the "delusional-projects" bin of GitHub. Grab some popcorn, because we are about to witness a $300 financial ruin speedrun (Any% category). 

Meet **Dragonfly**—which is a highly ironic name, because this thing is never leaving the ground. It’s a custom Flight Controller + ESC All-In-One board that currently has the processing power of a brick.

Let’s dissect this absolute trainwreck of a repository.

---

### 1. WHY THE HECK DID YOU BUILD THIS?
You spent **$250 to $300** to design a custom 4-layer PCB using prehistoric STM32F405 silicon, just so you could say you built it "from scratch." 
Bro, a SpeedyBee AIO costs $45 and actually flies. You built a literal fire hazard in KiCad because you wanted to look like Tony Stark in your bedroom, but instead, you ended up with a $300 paperweight that is **"not reqady to flash"** (yes, you even misspelled "ready" in your main status update. Peak professionalism).

---

### 2. ARCHITECTURE: The "I Can't Commit" Special
You claim this is "designed for me by me." If so, why does your repository contain an *entirely separate open-source project* (`OpenESC_20X20-main`) inside your `resources/symbols` folder? 
* Did you actually design an ESC, or did you just copy-paste someone else's 6-layer design, realize you couldn't route 6 layers, downscale it to 4 layers, and pray the EMF noise doesn't instantly reboot your gyro the moment you arm the motors?
* You are running an **STM32F405** in 2026. That chip belongs in a museum, not on a "freestyle" quad. Enjoy those looptimes.

---

### 3. FOLDER STRUCTURE & STORAGE POLLUTION
Your repository’s folder structure looks like a digital landfill.
* Why on earth did you commit the **entire unzipped SamacSys download** for the `AT7456E` OSD chip?
* You literally committed `Readme.html` files for **Altium, EAGLE, DesignSpark, Proteus, and EasyEDA** into a **KiCad** repository! Why do we need instructions on how to load a footprint into Altium when your project is in KiCad? Did you just select-all and drag-and-drop the entire `Downloads` folder into Git?
* Your `resources/symbols` folder is literally 90% spam. Delete the garbage, it's not a storage unit.

---

### 4. CODE SMELLS: The "V-Beta Hygiene Fix" Horror Show
Let's talk about `v_beta_hygiene_fix.py`. 
```python
# Operates on .kicad_sch files in BINARY MODE. Touches only the bytes inside
# property values; never modifies whitespace...

* **What in the regex-hell is this?** You wrote a custom Python script to do *surgical binary-level string replacements* on KiCad schematic files because your component footprint naming conventions were so messed up.
* Instead of just using KiCad’s built-in, GUI-based bulk footprint association tool like a civilized human, you decided to write a Python script that runs raw regex replacements on raw schematic bytes. One wrong character match and your entire schematic is corrupted beyond repair. This isn't "hygiene," this is playing Russian roulette with your hardware files.

---

### 5. NAMING & DOCUMENTATION
* **The Typo of Doom:** `"Status: in progress configuration and pin-mapping stage, not reqady to flash"`
If you can’t even proofread the main status line of your repository, how can we trust you mapped the pinout of a 64-pin MCU correctly? One wrong pin and you're going to feed 8V directly into the STM32's 3.3V rail.
* **Dragonfly?** More like **Firefly**, because those discrete FD6288Q gate drivers and unvetted MOSFETs are going to turn into a brilliant puff of white smoke the millisecond you plug in a 4S battery.

---

### 6. MISSING FEATURES (The Sad Reality)
* **Firmware:** *None.*
* **Unified Target:** *Non-existent.*
* **Code:** *Literally just a list of parts.*
This isn’t a flight controller repository; this is a **KiCad shopping list**. You have committed zero lines of actual configuration. You don't have a Betaflight unified target; you have a `notes.md` file with a "pin mapping reference." 

---

### Summary of the Roast
You designed a custom board, bought the components, 3D printed a frame, and set up a GitHub repo, all before checking if the firmware would even compile or flash. 

You built a **$300 simulator of a drone** that exists only in Fusion 360 and your dreams. Clean up your folder structure, delete the stolen sub-repos, learn how to use KiCad's footprint editor instead of writing terrifying Python scripts, and please... buy a smoke stopper before you plug this thing in
```

going to take a breat for 2hrs to recahrg.

yooooooo i back,

actully i didnt reset i liged 1 extra hr for macondo to maintain my streek, rn it is 19 days yayyayayayy.

it is taking too long to response, i have write the code to see how much time it takes to print the output, 

ohh man this is teribal, and this is was my repo that wasnt event that long. but still gemini took 55secs

```

Repo: 0.6832201480865479
context: 8.919949531555176
Gemini: 55.55069708824158
127.0.0.1 - - [18/Jul/2026 19:01:52] "POST /roast HTTP/1.1" 200 -

```

aahhh man idk what to do now. i think if i limit the gemini to fetch very less data and also shorten the response of the it will be fast, i am sure of it let me try.

i have also found few more things that will destory my pipline, so i need to fixx all that tooo.

gonna check the lenght of the prompt.
bruh i dont know why the fk this happening.

i am soo worked up.

soo this time it only took 28secs last time it took 55sec.
also its entire prompt is 29362 which is soo big.

next i am going to measure how many files i am sending to Gemmini.

bruh i am sending soo many junk

```
Repo: 1.0051443576812744
Files: 14
README.md
resources/symbols/AT7456E/Altair/Readme.html
resources/symbols/AT7456E/Altium/Readme.html
resources/symbols/AT7456E/DEHDL/at7456e/sym_1/symbol.css
resources/symbols/AT7456E/DesignSpark PCB/Readme.html
resources/symbols/AT7456E/EAGLE/Readme.html
resources/symbols/AT7456E/EasyEDA/Readme.html
resources/symbols/AT7456E/PADS/AT7456E.c
resources/symbols/AT7456E/Proteus/8.8 or earlier/Readme.html
resources/symbols/AT7456E/Proteus/8.9 or later/Readme.html
resources/symbols/OpenESC_20X20-main/README.md
resources/symbols/OpenESC_20X20-main/hardware/scripts/v_beta_hygiene_fix.py
resources/symbols/OpenESC_20X20-main/hardware/tools/esc_thermal.py
resources/symbols/OpenESC_20X20-main/licensing/README.md
context: 10.869335889816284
29362
Gemini: 33.50249218940735
127.0.0.1 - - [18/Jul/2026 19:51:58] "POST /roast HTTP/1.1" 200 -
```

this is not what we need this is vendor docs, that we dont need.

they are wasting Github aoi requests, context building time abd Gemini input token.

gonna make the filter more better.

looks good but still why only one file.

```
Repo: 2.5675048828125
Files: 1
README.md
context: 1.5661237239837646
4729
Gemini: 16.5479257106781
127.0.0.1 - - [18/Jul/2026 20:04:39] "POST /roast HTTP/1.1" 200 -
```

bro time is not consistent, i dont what the problem is but, its is taking soo much time, and i need to solve this.

```
Repo: 10.060757160186768
Files: 1
README.md
context: 1.9480702877044678
4729
Gemini: 19.89607524871826
127.0.0.1 - - [18/Jul/2026 20:28:13] "POST /roast HTTP/1.1" 200 -

```

i have optimized enogh, now just the gemini late respose left and if i tell it to reply in only curtin amounbt of words. i hope this will help


ohh damn man tghis is soo much better.

but its brutelness has droped idk why, first time i really felt it but now its not that hard.
only the last one is fun

```

### Delusional Documentation
Naming this "Dragonfly" is an insult to insects; "Mosquito with a short circuit" is more accurate. Your documentation is just a spec-sheet brag list for a project that hasn't even survived its maiden crash yet.

Delete this repository before the fire department does.
```



i changed the prompt but still its is not giving what i wanted.

i have made the prompt soo bruatal that this is mt limit i cant go any further then this,

now lets check if this gives what we want.

bro wtf 

```
Your "July 10" firmware deadline is already dead, just like your future in engineering.

```
ok so now the response is actually moremlike i wanted, i like too much.
but rn the roast takes the full page and we have to scroll to get the full view, i am gonna fix this.

### 19/7/2026

last day i sleep with everything working but now it is not working idk why i need to debug this.

i think the the problem is the js, there is the error in the brower console, that says.

```
script.js:73 Uncaught SyntaxError: Unexpected token '<'
```

fahh, bro i was writing the code in js with html syntan is had to write that code in the result.innerHTML =

i messed up the code while debigging, faggg

now i am hitting the rate limit for gemini api
it is printing this 

```
429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 7.873561735s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '7s'}]}}
```

i need one more account for this.

got the new api now time to test it.
its working now yayayayay.
but rpompt need a lil more adjustments

now gonna take a risk of trying the repo of the antropic, this gonna take soo much time fs

it took around 45 secs to respond on antropic repo, and its was in 45 sec because of the filter, the filter i made is not good for the every repo, i mainly designed it for hackclubs kids projects. for antropic, it only fetched the plgins and responded to that.

now that frontend and backend is working fine. but the api limit exceed error is printing on the web page. i dont want it like this, i want it to print something that will mock the user on this too.

i did something again and now it is only giving this,

```
n)
$ python app.py
API KEY: *************************************************
(venv) 
```

next step is 

cache repo context so if someone roasts the same repo again, u skip GitHub fetching and send the cached context dorectly to gemini.

i made it now just need to test it.

cache is working perfectly check this out:

```
API KEY: AQ.Ab8RN6LVK9VJgESR_T57JMH7a3Or3tX-ihS3h32R_iJFCYPDXw
 * Debugger is active!
 * Debugger PIN: 102-280-820
127.0.0.1 - - [19/Jul/2026 14:56:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/Jul/2026 14:56:54] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Jul/2026 14:56:55] "GET /static/script.js HTTP/1.1" 304 -
127.0.0.1 - - [19/Jul/2026 14:57:12] "GET /favicon.ico HTTP/1.1" 404 -
Repo: 4.362728595733643
Files: 1
README.md
conetxt: Built and cached
conetxt: 2.0085861682891846
5711
Gemini: 12.13570499420166
127.0.0.1 - - [19/Jul/2026 14:58:21] "POST /roast HTTP/1.1" 200 -
127.0.0.1 - - [19/Jul/2026 15:01:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/Jul/2026 15:01:26] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Jul/2026 15:01:26] "GET /static/script.js HTTP/1.1" 304 -
127.0.0.1 - - [19/Jul/2026 15:01:30] "GET /favicon.ico HTTP/1.1" 404 -
Repo: 1.1845471858978271
context: Loaded from cache
conetxt: 8.702278137207031e-05
5711
Gemini: 9.877235651016235
127.0.0.1 - - [19/Jul/2026 15:01:58] "POST /roast HTTP/1.1" 200 -
127.0.0.1 - - [19/Jul/2026 15:02:29] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/Jul/2026 15:02:29] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Jul/2026 15:02:29] "GET /static/script.js HTTP/1.1" 304 -
127.0.0.1 - - [19/Jul/2026 15:02:32] "GET /favicon.ico HTTP/1.1" 404 -
Repo: 1.0337169170379639
context: Loaded from cache
conetxt: 0.00024080276489257812
5711
Gemini: 10.74187707901001
127.0.0.1 - - [19/Jul/2026 15:02:48] "POST /roast HTTP/1.1" 200 -

```

it is working too well
```
Repo: 1.1973795890808105
Files: 1
README.md
conetxt: Built and cached
Context: 1.669s
5711
Gemini: 13.261s
127.0.0.1 - - [19/Jul/2026 15:12:23] "POST /roast HTTP/1.1" 200 -
Repo: 0.6747703552246094
context: Loaded from cache
5711
Gemini: 19.949s
127.0.0.1 - - [19/Jul/2026 15:13:36] "POST /roast HTTP/1.1" 200 -
```

next i am going too stream the roast to the frontend as Gemini genrates, like all LLms to show that AI is fast and the user start reading instantly. this will make it feel fast.

time to test it ^.

it works fahhh.

today goona lock in sooo hard, gonna slam everone in leaderboard today. ZEHAHAHAHH

bruh just rewrote full JS , there was too many errors and i made the very big chnages in the code. 

damn man debugging is hell.

im stuck pull me out.rg=

idk whst happening server isnt respondong

ahhh ,man idk what to dooooooo

idk what but gemini is not working. let me check it.

ohh man found it was the lib error, the lib was not responding idk why but it not wokring even i have instaloled it

nah its not the lib error./
googlle api is on hogh demand and is not wokting. rn

the API is working but only for very small things like say hello, not for the roasting

thid happening whenever i run Python app.py
```
 * Restarting with stat
API KEY: AQ.Ab8RN6KyE50sPTASxTJrTlvDyVXYjyFGL6kjmesGUdpqmF12vA
 * Debugger is active!
 * Debugger PIN: 102-280-820
127.0.0.1 - - [20/Jul/2026 14:34:20] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Jul/2026 14:34:20] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [20/Jul/2026 14:34:20] "GET /static/script.js HTTP/1.1" 200 -
127.0.0.1 - - [20/Jul/2026 14:34:23] "GET /favicon.ico HTTP/1.1" 404 -
Repo: 1.323s
127.0.0.1 - - [20/Jul/2026 14:34:29] "POST /repo HTTP/1.1" 200 -
Files: 1
README.md
Context: Built and cached
Context: 3.472s
5711
127.0.0.1 - - [20/Jul/2026 14:34:56] "POST /stream HTTP/1.1" 200 -
```


ohh man this is tooo hard.idk what too do i am comnpletely work out rn.srty

i am solving one error. 5 more are comming idk what to doo, i cant even take the break.

i am dead, idk if i will make this or not

i haev fixed the most of the code  but now the libs are playing with me.

ahhhhhhhhhhhhhhhh

bro its not working idk what to doo now.

everything is now orking fine but when AI works starts it sucks