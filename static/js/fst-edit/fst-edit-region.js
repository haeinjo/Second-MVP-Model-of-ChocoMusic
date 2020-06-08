let city = document.querySelectorAll("#fst-city > div");
const cityLength = city.length;
let region = document.querySelector("#fst-region-dict");
let boroughPanel = document.querySelector("#fst-borough");
let boroughOptionAll = document.querySelectorAll("form > select > option");
let optionCnt = boroughOptionAll.length;

//모든 city 버튼에 클릭 이벤트 추가
for (let i = 0; i < cityLength; ++i)
    city[i].addEventListener("click", clickCity);
//처음 화면이 로딩되면 서울 클릭
window.onload = initializeBorough();


function initializeBorough() {
    city[0].click();
}

function clickCity() {
    for (let i = 0; i < cityLength; ++i)
        city[i].classList.remove("selected-city");

    this.classList.add("selected-city");
    const fullCity = this.querySelector("span");
    const thisCity = fullCity.innerHTML;
    let boroughs = JSON.parse(region.innerHTML)[thisCity];
    boroughs = getBoroughs(boroughs);
    const boroughsCnt = boroughs.length;

    boroughPanel.querySelectorAll('*').forEach(n => n.remove());

    let rowCnt = boroughsCnt / 3;
    if (boroughsCnt % 3 !== 0)
        rowCnt += 1;

    let i = 0;
    for (let j = 0; j < rowCnt; ++j) {
        let newRow = document.createElement("div");
        newRow.classList.add("borough-row");
        for (let k = 0; i < boroughsCnt && k < 3; ++i, ++k) {
            newDiv = document.createElement("div");
            newDiv.classList.add("borough-element");
            newDiv.innerHTML = boroughs[i];
            newRow.appendChild(newDiv);
        }
        boroughPanel.appendChild(newRow);
    }
    addEventBorough(thisCity);
}

function getBoroughs(target) {
    if (typeof target === "string") {
        return [target];
    }
    else {
        return target;
    }
}

function clickBorough(e, city) {
    // 이미 클릭되어진 borough
    if (e.target.classList.contains("selected-borough")) {
        e.target.classList.remove("selected-borough");
        sessionStorage.removeItem(e.target.innerHTML);
    }
    // 처음 클릭되어진 borough
    else {
        e.target.classList.add("selected-borough");
        const clickedBorough = e.target.innerHTML;
        console.log(clickedBorough);

        //실제 form 정보 변경
        for (let i = 0; i < optionCnt; ++i) {
            let thisBorough = boroughOptionAll[i];
            if (thisBorough.innerHTML.search(clickedBorough) !== -1) {
                console.log(thisBorough.selected);
                thisBorough.selected == true;
                break;
            }
        }
    }
}

function addEventBorough(city) {
    let boroughAll = document.querySelectorAll(".borough-element")
    const boroughLength = boroughAll.length;
    //모든 borough 버튼에 클릭 이벤트 추가
    for (let i = 0; i < boroughLength; ++i) {
        const clickThisBorough = (event) => clickBorough(event, city);
        boroughAll[i].addEventListener("click", clickThisBorough);
    }
}