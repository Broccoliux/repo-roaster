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

def fetch_file_content(url, file_path):
    owner, repo = extract_repo_info(url)

    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"

    headers = {
        "Authorization": f"token  {TOKEN}"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code !=200:
        return None
    
    data = response.json()

    return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")