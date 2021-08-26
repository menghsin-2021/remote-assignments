const welcomeMessage = document.querySelector(".welcome-message");
const buttons = document.querySelector("#buttons");
const hidedContents = document.querySelector("#hided-contents");

// Click to change text.
welcomeMessage.addEventListener("click", () => {
  welcomeMessage.textContent = "Have a Good Time!";
});

// Click to show more content boxes.
buttons.addEventListener("click", (event) => {
  if (event.target.className === "call-to-action") {
    hidedContents.style.display = "flex";
  }
});