# Repo Roaster

Repo roaster is a web app that takes the public Github repo and absolutely destroys it.

Paste a GitHub repo URL, and Repo Reaper reads the codebase before generating brutal roast covering architecture, folder structure, naming, documentation, code smells, and questionable life choices.


---

## FEATURES

- Roast any github repo.
- Reads the actual repo structure before roasting.
- AI-generated roasts stremed in real time.
- Repository stats (stars, forks, language)
- Copy roast
- Download roast as `.txt`
- Text to speech roast
- Progress bar while analyzing
- Horror Jumpscare (because why not)

---

## TECH STACK

### Backend

- Python
- Flask
- Google Gemini API
- GitHub REST API

### FRONTEND
- HTML
- CSS
- Vanilla JavaScripts

---

# PROJECT STRUCTURE

```
repo-roaster/
│
├── app.py
├── github.py
├── roaster.py
├── cache.py
│
├── static/
│   ├── audio/
│   ├── images/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md
```

## INSTALLATION

Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/repo-roaster.git
cd repo-roaster
```

Create a Virtual Environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
GEMINI_API_KEY=your_api_key
GITHUB_TOKEN=your_github_token
```

Run the server

```bash
python app.py
```
---

## ENVIROMENT VARIABLES

| Variable | Required |
|----------|----------|
| GEMINI_API_KEY | ✅ |
| GITHUB_TOKEN | ✅ |

---

AI is use to Build this project, about 25% or less, I havent copy paste but learn it and did it myself.

## License
MIT
