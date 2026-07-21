const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");
const result = document.getElementById("result");


console.log("NEW SCRIPT LOADED");


button.addEventListener("click", async () => {

    const url = input.value.trim();

    // Empty input
    if (url === "") {
        alert("mera dimag na shat kar masalli")
        return;
    }

    
    if (!isValidGitHubUrl(url)) {
    alert("Akal ni tare pee. Janwar, GitHub repo daal.");
    return;
}

    // Loading message

    result.innerHTML = `
        <h2>🔥 tu bach beta ab tuu gaya... </h2>
    `;

    try {

        // fetch repository information

        const repoResponse = await fetch("/repo", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await repoResponse.json();


        if (!repoResponse.ok || !data.success) {
            result.innerHTML = `
                <h2>${data.message}</h2>
            `;
            return;
        }

        // drawing the repo info

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

            <div id="roast-output"></div>
        `;

        //stram Roast

        const roastOutput = document.getElementById("roast-output");

        const streamResponse = await fetch("/stream", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        if (!streamResponse.ok || !streamResponse.body) {
            roastOutput.innerHTML = `
                <h2>Gian hoo appp</h2>
            `;
            return;
        }


        const reader = streamResponse.body.getReader();
        const decoder = new TextDecoder();

        let roast = "";

        while (true) {
            const { done, value } = await reader.read();

            if (done) break;
            roast += decoder.decode(value, {
                stream: true
            });
            roastOutput.innerHTML = renderRoast(roast);
        }
    }

    catch (error) {
        console.error(error);

        result.innerHTML = `
            <h2>💀 Something exploded.</h2>
            <p>${error.message}</p>
        `;
    }
});

// Validate the GitHub url

function isValidGitHubUrl(url) {
    const pattern = /^https?:\/\/github\.com\/[^\/]+\/[^\/]+\/?$/;
    return pattern.test(url);
}


// stream roast will be converted into cards
function renderRoast(roast) {
    const sections = roast
        .trim()
        .split(/\n(?=[💀📂🐍📝🤡☠️])/);

    return sections
        .map(section => `
            <div class="roast-card">
                ${section.replace(/\n/g, "<br>")}
            </div>
        `)
        .join("");
}