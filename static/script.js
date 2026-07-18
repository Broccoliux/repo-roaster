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

    console.log(data.context);

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
        <hr>
        <pre>${data.roast}</pre>
    `;

}); 

function isValidGitHubUrl(url) {
    const pattern = /^https?:\/\/github\.com\/[^\/]+\/[^\/]+\/?$/;
    return pattern.test(url);
}