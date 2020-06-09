let city = document.querySelectorAll("#fst-city > div");
let region = document.querySelector("#fst-region-dict");
let boroughPanel = document.querySelector("#fst-borough");
let boroughOptionAll = document.querySelectorAll("form > select > option");
const selectElement = document.querySelector("#id_borough");
let selectedBoroughs = new Object();
const optionCnt = boroughOptionAll.length;
const cityLength = city.length;
const submitBtn = document.querySelector(".fst-btn");


//모든 city 버튼에 클릭 이벤트 추가
for (let i = 0; i < cityLength; ++i) {
    city[i].addEventListener("click", clickCity);
    selectedBoroughs[city[i].innerText] = new Array();
}
//처음 화면이 로딩되면 서울 클릭
window.onload = initWindow();
submitBtn.addEventListener("click", submitHandler);

function initWindow() {
    city[0].click();
    selectElement.classList.add("fst-hidden");
}

function submitHandler() {
    // selectedBoroughs에 저장된 요소들을 boroughOptionAll에 적용 시킨다.
    // let headings = document.evaluate("//option[contains(., '서울')]", boroughPanel, null, XPathResult.ANY_TYPE, null);
    // let thisHeadings = headings.iterateNext();
    // console.log(thisHeadings);
    // thisHeadings = headings.iterateNext();
    // console.log(thisHeadings);
    // while (heading = headings.iterateNext())
    //     console.log(heading);
    //모든 도시 순회
    //도시 마다 선택되어진 구 정보 저장
    //option중에서 시와 구가 다 있는 option select
    for (let i = 0; i < cityLength; ++i) {
        const thisCity = city[i].innerText;
        const thisBoroughs = selectedBoroughs[thisCity];
        console.log(`thisBoroughs: ${thisBoroughs}`);
        const thisLen = thisBoroughs.length;
        console.log(`thisCity: ${thisCity}`);
        let headings = document.evaluate('//option[contains(.,"' + thisCity + '")]', selectElement, null, XPathResult.ANY_TYPE, null);
        for (let j = 0; j < thisLen; ++j) {
            let heading;
            while (heading = headings.iterateNext()) {
                console.log(`thisHeading: ${heading.innerText}`);
                if (heading.innerText.search(thisBoroughs[j]) != -1) {
                    console.log(`modified: ${heading.innerText}`);
                    heading.selected = true;
                    break;
                }
            }
        }
    }
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
            paintBorough(thisCity, newDiv);
            newRow.appendChild(newDiv);
        }
        boroughPanel.appendChild(newRow);
    }
    addEventBorough(thisCity);
}

//selected == true 상태인 자치구 정보 불러오기
function paintBorough(thisCity, borough) {
    preCity = thisCity.slice(0, 2);
    selectedTarget = selectedBoroughs[preCity].findIndex((element) => element === borough.innerText);
    if (selectedTarget != -1)
        borough.classList.add("selected-borough");
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
    //클릭되어진 자치구 스트링
    const clickedBorough = e.target.innerHTML;
    // 이미 클릭되어진 borough
    if (e.target.classList.contains("selected-borough")) {
        e.target.classList.remove("selected-borough");
        removeSelectedBorough(e.target.innerHTML, city);
    }
    // 처음 클릭되어진 borough
    else {
        e.target.classList.add("selected-borough");
        setSelectedBorough(e.target.innerHTML, city);
        sb = Object.values(selectedBoroughs);
        sb = sb.flat(2);
    }
}

function removeSelectedBorough(borough, city) {
    const preCity = city.slice(0, 2); 0
    removeTarget = selectedBoroughs[preCity].findIndex((element) => element === borough);
    selectedBoroughs[preCity].splice(removeTarget, 1);
}

function setSelectedBorough(borough, city) {
    const preCity = city.slice(0, 2);
    selectedBoroughs[preCity].push(borough);
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