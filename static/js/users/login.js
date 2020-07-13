const loginEmailBtn = document.querySelector(".login__email");


window.onload = initWindow();

function initWindow() {
    loginEmailBtn.addEventListener("click", clickLoginEmailBtn);
}

function clickLoginEmailBtn() {
    location.href = "/users/signup/"
}