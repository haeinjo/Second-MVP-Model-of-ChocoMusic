const articleSignUpBtn = document.querySelector(".article__btn");


window.onload = initIntro();

function initIntro() {
    articleSignUpBtn.addEventListener("click", clickSignUp);
}

function clickSignUp() {
    location.href = "/users/login/";
}