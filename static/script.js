const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");
const result = document.getElementById("result");


button.addEventListener("click", async () => {
    const url = input.value.trim();

    if (url === "") {
        alert("dont make a fuss u punk, drop ur sh**ty repo URL rn");
        return;
    }

    if (!isValidGitHubUrl(url)) {
        alert("dont play with me kid, drop ur real sh*t");
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

    console.log("Reached here");
    console.log(data);

    result.textContent = `function isValidGitHubUrl(url) {
  const pattern = /^https?:\\/\\/github\\.com\\/[^\\/]+\\/[^\\/]+\\/?$/;
  return pattern.test(url);
}`;
1