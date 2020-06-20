// Control Element to Show
// Control progress
`use strict`;


let stepLevel = "type";
const contentType = document.querySelector(".content__type");
const contentFile = document.querySelector(".content__file");
const contentInfo = document.querySelector(".content__info");
const contentCheck = document.querySelector(".content__check");
const dotAll = document.querySelectorAll(".progress__dot");
const lineAll = document.querySelectorAll(".progress__line");
const btnPre = document.querySelector(".btn__pre__img");
const btnNext = document.querySelector(".btn__next__img");
const cardImgAll = document.querySelectorAll(".card__img");
const typeInput = document.querySelector("#id_content_type");
const fileInput = document.querySelector("#id_content_file");
const photoInput = document.querySelector("#id_content_photo");
const projectInput = document.querySelector("#id_project");
const titleInput = document.querySelector("#id_content_title");
const genreInput = document.querySelector("#id_genre");
const descriptionInput = document.querySelector("#id_description");
const exposureLevelInput = document.querySelector("#id_exposure_level");
const formButton = document.querySelector(".form__button");
const mainContent = document.querySelector(".main__content");


window.onload = initCreateContent();

function initCreateContent() {
    // Set First Form
    contentType.classList.toggle("active");
    mainContent.style.height = "64%";

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
                contentType.classList.toggle("active");
                contentFile.classList.toggle("active");
                btnPre.classList.remove("element--hidden");
                stepLevel = "file";
                mainContent.style.height = "64%";
            }
            break;
        case "file":
            if (fileInput.files.length === 0) {
                //경고를 뛰운다.
            } else {
                contentFile.classList.toggle("active");
                contentInfo.classList.toggle("active");
                stepLevel = "info";
            }
            break;
        case "info":
            if (titleInput.value && projectInput.selectedIndex && genreInput.selectedIndex && descriptionInput.value) {
                contentInfo.classList.toggle("active");
                contentCheck.classList.toggle("active");
                setCheckPhoto();
                setCheckTitle();
                setCheckGenre();
                setCheckProject();
                stepLevel = "check";
            } else {
                //경고를 뛰운다.
            }
            break;
        case "check":
            break;
        default:
            break;
    }
    setProgressBar();
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
            dotAll[2].classList.add("progress--set");
            lineAll[1].classList.add("progress--set");
            break;
        case "check":
            dotAll[3].classList.add("progress--set");
            lineAll[2].classList.add("progress--set");
            btnNext.classList.add("element--hidden");
            break;
        default:
            break;
    }
}