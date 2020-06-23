const articleSignUpBtn = document.querySelector(".article__btn");
const loginForm = document.querySelector(".login__form");
const formCancle = document.querySelector(".form__cancle");


window.onload = initIntro();

function initIntro() {
    articleSignUpBtn.addEventListener("click", clickSignUp);
    formCancle.addEventListener("click", clickFormCancle);
}

function clickSignUp() {
    loginForm.classList.add("active");
}

function clickFormCancle() {
    loginForm.classList.remove("active");
}