const articleSignUpBtn = document.querySelector(".article__btn");
const loginForm = document.querySelector(".login__form");
const formCancle = document.querySelector(".form__cancle");
const formKakao = document.querySelector(".form__kakao");
const formGoogle = document.querySelector(".form__google");
const formSubmit = document.querySelector(".form__submit");
const formEmail = document.querySelector(".form__email");


window.onload = initIntro();

function initIntro() {
    articleSignUpBtn.addEventListener("click", clickSignUp);
    formCancle.addEventListener("click", clickFormCancle);
    formKakao.addEventListener("click", clickFormKakao);
    formGoogle.addEventListener("click", clickFormGoogle);
    formSubmit.addEventListener("click", clickFormSubmit);
}

function clickSignUp() {
    loginForm.classList.add("active");
}

function clickFormCancle() {
    loginForm.classList.remove("active");
}

function clickFormKakao() {
    location.href = "/users/login/kakao/";
}

function clickFormGoogle() {
    location.href = "/users/login/google/";
}