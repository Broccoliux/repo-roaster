from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv


import base64
import os
import requests

from urllib.parse import urlparse

#load variable from .env file.
# this gives us the access to GitHub token.

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")


# extract the owner and repo name from the github url.

def extract_repo_info(url):
    parsed = urlparse(url)

    parts = parsed.path.strip("/").split("/")

    if len(parts) < 2:
        return None, None
    
    owner = parts[0]
    repo = parts[1]

    return owner, repo

# fetch basic repo info.

# this endpoint is called first by app.py.
# it only retiurs the mata data
# owner, name , stars, forks, language

def fetch_repo_data(url):
    owner, repo = extract_repo_info(url)
    if owner is None:
        return None

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    response = requests.get(
        api_url,
        headers=headers,
        timeout=30
    )

    # Repo doesnt exists or github rejected the requests.

    if response.status_code != 200:
        return None

    data = response.json()

    repo_info = {
        "name": data["name"],
        "description": data["description"],
        "language": data["language"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "owner": data["owner"]["login"],
    }

    return repo_info

# download the complete repo tree.

# this lets us see every file inside the repo.
# we dont download the files here only their paths.

def fetch_repo_tree(url):

    owner, repo = extract_repo_info(url)

    if owner is None:
        return None

    api_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/trees/HEAD?recursive=1"
    )

    headers = {
        "Authorization": f"token {TOKEN}"
    }

    response = requests.get(
        api_url,
        headers=headers,
        timeout=20
    )

    if response.status_code != 200:
        return None

    return response.json()["tree"]

# download the content of a single file.

# github returns file contents encoded in base64.
# we decode it back into normal text defore returning it.



def fetch_file_content(url, file_path):

    owner, repo = extract_repo_info(url)

    if owner is None:
        return None

    api_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contents/{file_path}"
    )

    headers = {
        "Authorization": f"token {TOKEN}"
    }

    response = requests.get(
        api_url,
        headers=headers,
        timeout=20
    )

    if response.status_code != 200:
        return None

    data = response.json()

    try:
        return base64.b64decode(
            data["content"]
        ).decode(
            "utf-8",
            errors="ignore"
        )

    except Exception:
        return None
    

# decide which files are worth sending to gemini

# i have intentionally skip things like node_modules, build folders
# build folder and test files because they,re huge
# and usually useless for roasting.
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

# files inside these folders are usually important
# because they contain the application's source code.

    priority_folders = (
        "src/",
        "templates/",
        "static/",
        "components/",
        "lib/",
        "pages/",
    )

# programming language we care about.

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

# ignore large/genrated folder.
    ignored = (
        ".git/",
        "node_modules/",
        "__pycache__/",
        "venv/",
        ".venv/",
        "dist/",
        "build/",
        ".next/",
        ".idea/",
        ".vscode/",
    )

    for file in tree:

        path = file["path"]

        # Skip ignored folders.
        if any(path.startswith(folder) for folder in ignored):
            continue

        filename = path.split("/")[-1].lower()

    # skip the files.

        if filename.startswith("test"):
            continue

    # dont roast our own helper scripts.
    
        if filename == "cloner.py":
            continue

    # keep the file if:
    # if the file is priority file,
    # its inside a priority folder,
    # or it has a source-code extenion.

        if (
            filename in priority_files
            or path.startswith(priority_folders)
            or path.endswith(extensions)
        ):
            important.append(path)

    return important


# build one large text block that will be sent to gemini.

# Every important file is downloaded, trimmed and appended
# into a single context string.

def build_repo_context(url):
    tree = fetch_repo_tree(url)

    if tree is None:
        return None

    important_files = get_important_files(tree)
    print("Files:", len(important_files))
    context = ""

    # downloading multiple files simultaneously.
    # this is much faster then downloading them one-by-one.
    with ThreadPoolExecutor(max_workers=8) as executor:

        contents = executor.map(
            lambda file: (
                file,
                fetch_file_content(url, file)
            ),
            important_files
        )

        for file, content in contents:

            print(file)

        #skip files that failed to download.
            if content is None:
                continue

        # add a saparator so gemini knows where
        #each  file starts.

            context += f"\n\n===== {file} =====\n"

        # limit each files size.
        # this keeps the final prompt from becoming
        # unnecessarily huge.

            context += content[:4000]

    return context
