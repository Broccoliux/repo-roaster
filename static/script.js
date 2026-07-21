const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");
const result = document.getElementById("result");
const defaultButtonText = button.innerHTML;


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

  button.disabled = true;
  button.innerHTML = "🔥 boiling iron";
  input.disabled = true;

  // Loading message

  result.innerHTML = `
         <h2 id="loading-text">🔥 Preparing your funeral...</h2>

         <div class="progress-container">
            <div class="progress-bar" id="progress-bar"></div>
        </div>

        <p id="progress-percent">0%</p>

        `;

  const progressBar = document.getElementById("progress-bar");
  const progressPercent = document.getElementById("progress-percent");
  const loadingText = document.getElementById("loading-text");

  let progress = 0;

  const loadingMessages = [
    "🔍 Stalking your repo...",
    "📂 Reading your crimes...",
    "🧠 Teaching Gemini to hate you...",
    "💀 Preparing psychological damage...",
    "🔥 Loading insults..."
  ];

  const progressInterval = setInterval(() => {

    if (progress < 95) {
      progress += Math.random() * 7;

      progressBar.style.width = progress + "%";
      progressPercent.textContent = Math.floor(progress) + "%";
    }

    loadingText.textContent =
      loadingMessages[Math.floor(progress / 20)] || "🔥 Almost there...";

  }, 250);


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

      clearInterval(progressInterval);

      button.disabled = false;
      button.innerHTML = defaultButtonText;
      input.disabled = false;

      result.innerHTML = `
            <h2>${data.message}</h2>
            `;

      return;

    }

    clearInterval(progressInterval);

    progressBar.style.width = "100%";
    progressPercent.textContent = "100%";
    loadingText.textContent = "☠️ Roast ready.";
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

            <div class="roast-actions">
                <button id="copy-btn">Copy Roast</button>
                <button id="download-btn">Download Roast</button>
            </div>

            <div id="roast-output"></div>
        `;

    //stram Roast

    const roastOutput = document.getElementById("roast-output");

    const copyBtn = document.getElementById("copy-btn");
    const downloadBtn = document.getElementById("download-btn");
    copyBtn.style.display = "none";
    downloadBtn.style.display = "none";

    const streamResponse = await fetch("/stream", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        url: url
      })
    });

    if (!streamResponse.ok) {
      const error = await streamResponse.json();

      roastOutput.innerHTML = `

                <div class="error-card">
                    <h2>${error.message}</h2>
                </div>
            `;

      button.disabled = false;
      button.innerHTML = defaultButtonText;
      input.disabled = false;

      return;
    }

    if (!streamResponse.body) {

      roastOutput.innerHTML = `
                <div class="error-card">
                    <h2>No response from Repo Reaper.</h2>
                </div>
            `;

      button.disabled = false;
      button.innerHTML = defaultButtonText;
      input.disabled = false;

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
    copyBtn.style.display = "inline-block";
    downloadBtn.style.display = "inline-block";

    copyBtn.addEventListener("click", async () => {

      try {

        await navigator.clipboard.writeText(roast);
        copyBtn.innerHTML = "✅ Copied!";

        setTimeout(() => {
          copyBtn.innerHTML = "Copy Roast";
        }, 2000);

      }

      catch {
        alert("Couldn't copy your insult.");
      }

    });

    downloadBtn.addEventListener("click", () => {
      console.log(roast);

      const content =
    `REPO REAPER ☠️
    =-=-=-=-=-=-=-=-=-==-=-=-=-=

    Repository:
    ${url}

    Generated:
    ${new Date().toLocaleString()}
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    ${roast}
    `;

      const blob = new Blob([content], {
        type: "text/plain"
      });

      const file = URL.createObjectURL(blob);

      const a = document.createElement("a");

      a.href = file;
      a.download = "repo-roast.txt";

      document.body.appendChild(a);
      a.click();
      a.remove();

      URL.revokeObjectURL(file);

    });


      button.disabled = false;
      button.innerHTML = defaultButtonText;
      input.disabled = false;
    }



  catch (error) {
      console.error(error);

      clearInterval(progressInterval);

      result.innerHTML = `
        <div class="error-card">
            <h2>☠️ Repo Reaper tripped over your code.</h2>
            <p>${error.message}</p>
        </div>
        `;

      button.disabled = false;
      button.innerHTML = defaultButtonText;
      input.disabled = false;
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
