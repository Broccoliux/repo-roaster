const input = document.getElementById("repo-url");
const button = document.getElementById("roast-btn");

button.addEventListener("click", () => {
    const url = input.vlaue.trim();

    if (url === "") {
        alert("Pleas enter a Github repositiry URL.");
        return;
    }

    console.log("Repository URL: ", url);
});
