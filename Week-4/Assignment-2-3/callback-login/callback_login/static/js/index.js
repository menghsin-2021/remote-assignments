var signUpTable = document.getElementById("singUpTable");
var signInTable = document.getElementById("signInTable");

function switchToSignIn() {
  signUpTable.className = "d-none flex-column align-items-center col-12";
  signInTable.className = "d-flex flex-column align-items-center col-12";
}

function switchToSignUp() {
  signUpTable.className = "d-flex flex-column align-items-center col-12";
  signInTable.className = "d-none flex-column align-items-center col-12";
}
