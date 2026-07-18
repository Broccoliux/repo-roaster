from github import fetch_file_content

content = fetch_file_content(
    "https://github.com/octocat/Hello-World",
    "README"
)

print(content)