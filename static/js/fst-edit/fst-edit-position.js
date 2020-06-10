const positionSelect = document.querySelector("#id_positions");
const selectOptionAll = positionSelect.querySelectorAll("option");
const optionCnt = selectOptionAll.length;
const positions = document.querySelectorAll(".position-info");
const positionPanel = document.querySelector("#fst-position");
const positionsCnt = positions.length;


window.onload = initWindow();


function initWindow() {
    positionPaint();
    positionSelect.classList.add("fst-hidden");
}

function positionPaint() {
    let rowCnt = positionsCnt / 2;
    if (positionsCnt % 2 !== 0)
        rowCnt += 1;

    let i = 0;
    for (let j = 0; j < rowCnt; ++j) {
        let newRow = document.createElement("div");
        newRow.classList.add("position-row");
        for (let k = 0; i < positionsCnt && k < 2; ++i, ++k) {
            newDiv = document.createElement("div");
            newDiv.classList.add("position-element");
            newDiv.innerHTML = positions[i].innerText;
            addEventPosition(newDiv);
            newRow.appendChild(newDiv);
        }
        positionPanel.appendChild(newRow);
    }
}

function addEventPosition(position) {
    position.addEventListener("click", clickPosition);
}

function clickPosition() {
    this.classList.toggle("selected-position");
    if (this.classList.contains("selected-position")) {
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