from github import fetch_repo_tree, get_important_files, fetch_file_content

url = "https://github.com/Broccoliux/dragonfly"

files = get_important_files(fetch_repo_tree(url))

total = 0

for file in files:
    content = fetch_file_content(url, file)

    if content:
        print(file, len(content))
        total += len(content)

    print("\nTOTAL:", total)

    