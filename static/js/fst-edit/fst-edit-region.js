let city = document.querySelectorAll("#fst-city > div");
const cityLength = city.length;
let region = document.querySelector("#fst-region-dict");
let boroughPanel = document.querySelector("#fst-borough");

// console.log(JSON.parse(region.innerHTML).서울특별시);

for (let i = 0; i < cityLength; ++i)
    city[i].addEventListener("click", clickCity);

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
    const boroughs = JSON.parse(region.innerHTML)[thisCity];
    const boroughsCnt = boroughs.length;

    boroughPanel.querySelectorAll('*').forEach(n => n.remove());

    for (let i = 0; i < boroughsCnt; ++i) {
        newDiv = document.createElement("div");
        newDiv.classList.add("borough-element");
        newDiv.innerHTML = boroughs[i];
        boroughPanel.appendChild(newDiv);
    }
}