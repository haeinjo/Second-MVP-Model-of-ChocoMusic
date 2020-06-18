// Control Element to Show
// Control progress
`use strict`;


let stepLevel = "type";
const contentType = document.querySelector(".content__type");
const contentFile = document.querySelector(".content__file");
const dotAll = document.querySelectorAll(".progress__dot");
const lineAll = document.querySelectorAll(".progress__line");
const btnPre = document.querySelector(".btn__pre__img");
const btnNext = document.querySelector(".btn__next__img");
const cardImgAll = document.querySelectorAll(".card__img");
const typeInput = document.querySelector("#id_content_type");
const fileInput = document.querySelector("#id_content_file");
const mainContent = document.querySelector(".main__content");


window.onload = initCreateContent();

function initCreateContent() {
    contentFile.classList = "";
    contentFile.classList.add("element--hidden");
    // Set Btns
    setBtn();
    // Set Button Handler
    btnNext.addEventListener("click", handleBtnNext);
    btnPre.addEventListener("click", handleBtnPre);
    // Set Proress Bar
    setProgressBar();
}

function setBtn() {
    btnPre.classList.add("element--hidden");
}

function handleBtnNext() {
    switch (stepLevel) {
        case "type":
            if (typeInput.selectedIndex === 0) {
                // 경고를 뛰운다.
            } else {
                // Type Div를 안보이게 설정하고 다음 Step의 Div를 보이게 한다.
                contentType.classList = "";
                contentType.classList.add("element--hidden");
                contentFile.classList.remove("element--hidden");
                contentFile.classList.add("content__file");
                btnPre.classList.remove("element--hidden");
                stepLevel = "file";
                mainContent.style.height = "64%";
                setProgressBar();
            }
            break;
        case "file":
            break;
        case "info":
            break;
        case "check":
            break;
        default:
            break;
    }
}

function handleBtnPre() {

}

function setProgressBar() {
    switch (stepLevel) {
        case "type":
            dotAll[0].classList.add("progress--set");
            break;
        case "file":
            dotAll[1].classList.add("progress--set");
            lineAll[0].classList.add("progress--set");
            break;
        case "info":
            break;
        case "check":
            break;
        default:
            break;
    }
}