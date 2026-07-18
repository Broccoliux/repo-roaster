from concurrent.futures import ThreadPoolExecutor
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

    priority_files = {
        "readme.md",
        "package.json",
        "requirements.txt",
        "app.py",
        "main.py",
        "manage.py",
        "index.js",
        "server.js",
        "github.py",
    }

    priority_folder = (
        "src/",
        "templates/",
        "static/",
        "components/",
        "lib/",
        "page/",
    )

    extensions = (
        ".py",
        ".js",
        ".ts",
        ".jsx",
        ".tsx",
        ".html",
        ".css",
        ".java",
        ".cpp",
        ".c",
        ".cs",
        ".go",
        ".rs",
        ".php",
    )

    ignored = (
        ".git/",
        "node_modules/",
        "__pycache__/",
        "venv",
        ".venv/",
        "dist/",
        "build/",
        ".next/",
        "idea/",
        "vscode/",
    )

    for file in tree:
        path = file["path"]

        skip_folder = (
            "resources/",
            "vendor/",
            "node_modules/",
            "dist/",
            "build/",
            "docs/",
        )

        if path.startswith(skip_folder):
            continue

        if any(path.startswith(folder) for folder in ignored):
            continue 
        
        filename = path.split("/")[-1].lower()

        if filename.startswith("test"):
            continue

        if filename == "cloner.py":
            continue

        if (
            filename in priority_files
            or path.startswith(priority_folder)
            or path.endswith(extensions)
        ):
            important.append(path)
    
    return important


def build_repo_context(url):
    tree = fetch_repo_tree(url)
    
    if tree is None:
        return None
    
    important_files = get_important_files(tree)
    print("Files:", len(important_files))

    context = ""

    with ThreadPoolExecutor(max_workers=8) as executor:
        contents  =executor.map(
            lambda file: (file, fetch_file_content(url, file)),
            important_files
        )

        for file, content in contents:
            print(file)

            if content is None:
                continue

            context += f"\n\n===== {file} =====\n"
            context += content[:4000]

    return context

