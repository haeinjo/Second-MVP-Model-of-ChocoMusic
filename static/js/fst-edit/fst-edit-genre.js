const genreSelect = document.querySelector("#id_genres");
const selectOptionAll = genreSelect.querySelectorAll("option");
const optionCnt = selectOptionAll.length;
const genres = document.querySelectorAll(".genre-info");
const genrePanel = document.querySelector("#fst-genre");
const genresCnt = genres.length;


window.onload = initWindow();


function initWindow() {
    genrePaint();
    genreSelect.classList.add("fst-hidden");
}

function genrePaint() {
    let rowCnt = genresCnt / 2;
    if (genresCnt % 2 !== 0)
        rowCnt += 1;

    let i = 0;
    for (let j = 0; j < rowCnt; ++j) {
        let newRow = document.createElement("div");
        newRow.classList.add("genre-row");
        for (let k = 0; i < genresCnt && k < 2; ++i, ++k) {
            newDiv = document.createElement("div");
            newDiv.classList.add("genre-element");
            newDiv.innerHTML = genres[i].innerText;
            addEventGenre(newDiv);
            newRow.appendChild(newDiv);
        }
        genrePanel.appendChild(newRow);
    }
}

function addEventGenre(genre) {
    genre.addEventListener("click", clickGenre);
}

function clickGenre() {
    this.classList.toggle("selected-genre");
    if (this.classList.contains("selected-genre")) {
        for (let i = 0; i < optionCnt; ++i) {
            if (selectOptionAll[i].innerText === this.innerText) {
                selectOptionAll[i].selected = true;
                break;
            }
        }
    }
    else {
        for (let i = 0; i < optionCnt; ++i) {
            if (selectOptionAll[i].innerText === this.innerText) {
                selectOptionAll[i].selected = false;
                break;
            }
        }
    }
}