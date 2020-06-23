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
const mainError = document.querySelector(".main__error");


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
                // ValueError: Empty Value
                const errorMessage = document.createElement("span");
                errorMessage.innerText = "업로드할 파일 유형을 선택해 주세요.";
                errorMessage.classList.add("error__message");
                mainError.innerHTML = '';
                mainError.appendChild(errorMessage);
                mainError.classList.toggle("active");
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
                btnNext.classList.toggle("element--hidden");
                setCheckPhoto();
                setCheckTitle();
                setCheckGenre();
                setCheckProject();
                stepLevel = "check";
            } else {
                //경고를 뛰운다.
            }
            break;
        default:
            break;
    }
    setProgressBar();
}

function handleBtnPre() {
    switch (stepLevel) {
        case "file":
            contentType.classList.toggle("active");
            contentFile.classList.toggle("active");
            btnPre.classList.add("element--hidden");
            setProgressBar();
            stepLevel = "type";
            mainContent.style.height = "60%";
            break;
        case "info":
            contentInfo.classList.toggle("active");
            contentFile.classList.toggle("active");
            setProgressBar();
            stepLevel = "file";
            break;
        case "check":
            contentInfo.classList.toggle("active");
            contentCheck.classList.toggle("active");
            btnNext.classList.toggle("element--hidden");
            setProgressBar();
            stepLevel = "info";
            break;
        default:
            break;
    }
}

function setProgressBar() {
    switch (stepLevel) {
        case "type":
            dotAll[0].classList.toggle("progress--set");
            break;
        case "file":
            dotAll[1].classList.toggle("progress--set");
            lineAll[0].classList.toggle("progress--set");
            break;
        case "info":
            dotAll[2].classList.toggle("progress--set");
            lineAll[1].classList.toggle("progress--set");
            break;
        case "check":
            dotAll[3].classList.toggle("progress--set");
            lineAll[2].classList.toggle("progress--set");
            break;
        default:
            break;
    }
}