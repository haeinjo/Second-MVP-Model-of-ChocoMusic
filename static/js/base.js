const uploadBtn = document.querySelector(".nav-menu-2-upload");

window.onload = initWindow();

function initWindow() {
    uploadBtn.addEventListener("click", clickUploadBtn);
}

function clickUploadBtn() {
    location.href = url;
}