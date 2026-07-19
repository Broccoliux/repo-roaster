const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");
const result = document.getElementById("result");

console.log("NEW SCRIPT LOADED");

button.addEventListener("click", async () => {
    console.log("Button clicked")
    const url = input.value.trim();


    if (url === "") {
        alert("empty");
        return;
    }

    console.log(url);
    console.log(isValidGitHubUrl(url));

    if (!isValidGitHubUrl(url)) {
        alert("invalid");
        return;
    }

    console.log("Passed validation");
    console.log("Sending request...");
    const response = await fetch("/roast", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url
        })
    });
    console.log(response.status);

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    result.innerHTML = "";

    while (true) {
        const {done, value} = await reader.read();

        if (done) break;

        result.innerHTML += decoder.decode(value)
    }

    
    console.log(data);

    if (!data.success) {
        result.innerHTML = `<h2>${data.message}</h2>`;
        return;
    }


    result.innerHTML = `
    <h2>📦 ${data.repo.name}</h2>

    <div class="repo-stats">

        <div class="stat-card">
            <span>👤</span>
            <div>
                <small>Owner</small>
                <strong>${data.repo.owner}</strong>
            </div>
        </div>

        <div class="stat-card">
            <span>⭐</span>
            <div>
                <small>Stars</small>
                <strong>${data.repo.stars}</strong>
            </div>
        </div>

        <div class="stat-card">
            <span>🍴</span>
            <div>
                <small>Forks</small>
                <strong>${data.repo.forks}</strong>
            </div>
        </div>

        <div class="stat-card">
            <span>💻</span>
            <div>
                <small>Language</small>
                <strong>${data.repo.language || "Unknown"}</strong>
            </div>
        </div>

    </div>

    <hr>

    ${renderRoast(data.roast)}
`;

});

function isValidGitHubUrl(url) {
    const pattern = /^https?:\/\/github\.com\/[^\/]+\/[^\/]+\/?$/;
    return pattern.test(url);
}

function renderRoast(roast) {

    const sections = roast.trim().split(/\n(?=[💀📂🐍📝🤡☠️])/);

    return sections.map(section => `
        <div class="roast-card">
            ${section.replace(/\n/g, "<br>")}
        </div>
    `).join("");

}
