import requests
from urllib.parse import urlparse

def extract_repo_info(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts [0],parts [1]

def fetch_repo_data(url):
    owner, repo = extract_repo_info(url)
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    print(owner)
    print(repo)
    print(api_url)
    response = requests.get(api_url)
    print(response.url)
    
    print("Status:", response.status_code)
    print("Final URL:, respoonse.url")
    print("Response:", response.text[:300])

print(fetch_repo_data("https://github.com/torvalds/linux"))
