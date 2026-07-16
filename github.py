import requests
from urllib.parse import urlparse

def extract_repo_info(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts [0],parts [1]

def fetch_repo_data(url):
    owner, repo = extract_repo_info(url)
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(api_url)
    data = response.json()
    return data

print(fetch_repo_data("https://github.com/torvalds/linux"))

print(repo["name"])repo = fetch_repo_data("https://github.com/torvalds/linux")
print(repo["discription"])
print(repo["languages"])
print(repo["stargazers_count"])
print(repo["forks_count"])
print(repo["owner"]["login"])

repo = fetch_repo_data("https://github.com/torvalds/linux")

print(repo["name"])

