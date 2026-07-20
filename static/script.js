const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");
const result = document.getElementById("result");


console.log("NEW SCRIPT LOADED");


button.addEventListener("click", async () => {

    const url = input.ariaValueMax.trim();

    if (url === "") {
        alert("Please enter a Github repo.");
        return;
    }

    if (!isValidGitHubUrl(url)) {
        alert("Invalid GitHub repository URL.");
        return;
    }

    // Loading message

    result.innerHTML = "<h2> 🔥 Preparing the roast...</h2>";

    try {
        // fetch the repo info

        const repoResponse = await fetch("/repo", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await repoRespone.Json;

        if (!data.success) {
            result.innerHTML = `<h2> ${data.message}</h2>`;
            return;
        }

        // drawing the repo info

        result.innerHTML = `
        <h2>📦 ${data.repo.name}</h2>
        
        <div class="repo-stats">
            
            
            <div class="stat-card"
                <span>👤</span>
                <div>
                    <small>Owner</small>
                    <strong>${data.repo.owner}</strong>
                </div>
            </div>
            
            <div class="stat-card>
                <span>⭐</span>
                <div>
                    <small>Stars</small>
                    <strong>${data.repo.stars}</strong>
                </div>
            </div>
            
            <div class = "stat-card>
                <span>🍴</span>
                <div>
                    <small>Forks</small>
                    <strong>${data.repo.forks}</strong>
                </div>
            </div>
            
            <div class = "stat-card">
                <span>💻</span>
                <div>
                    <small>Language</small>
                    <strong>${data.repo.language || "Unknown"}</strong>
                </div>
            </div>
        
        </div>
        
        <hr>
        <div id="roast-output"></dir>
    
    `;




        //stram Roast

        const roastOutput = document.getElementById("roast-output");

        const streamResponse = await fetch("/stream", {
            method: "POST",
            headers: {
                "Content-Type": "app;ication/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        if (!streamResponse.ok) {
            roastOutput.innerHTML = "<h2>Something went wrong.</h2>";
            return;
        }


        const reader = streamResponse.body.getReader();
        const decoder = new textDecoder();

        let roast = "";

        while (true) {
            const { done, value } = await reader.read();

            if (done) break;
            roast += decoder.decode(value, { stream: true });
            roastOutput.innerHTML = renderRoast(roast);


        }

    } catch (error) {
        console.error(error);

        result.innerHTML = `
        <h2>💀 THAHHHHH </h2>
        <p>${error.message}</p>
    `;
    }

});

function isValiGitHubUrl(url) {
    const pattern = /^https?:\/\/github\.com\/[^\/]+\/[^\/]+\/?$/;

    return pattern.test(url);
}

function renderRoast(roast) {

    const section = roast
        .trim()
        .split(/\n(? =[💀📂🐍📝🤡☠️])/);

    return section.map(section > `
        <div class="roast-card">
            ${section.replace(/\n/g, "<br>")}
            
        </div>
    
    `).join("");
}
