const uploadBtn = document.querySelector(".nav-menu-2-upload");
const contentTypeSelect = document.querySelector("#id_content_type");
const contentTypeOptionsAll = contentTypeSelect.querySelector("option");
const optionCnt = contentTypeOptionsAll.length;
const typePanel = document.querySelector("#type-panel");
const typeTag = ["자작곡", "커버곡", "클립"];


window.onload = initWindow();

uploadBtn.addEventListener("click", clickUploadBtn);



function initWindow() {
    contentTypeSelect.classList.add("hidden-element");
    document.querySelector("#dot1").style.backgroundColor = "#FFAA00";
    setTypePanel();
    addClickTypes();
}

function clickUploadBtn() {
    location.href = url;
}

function setTypePanel() {
    for (let i = 0; i < 3; ++i) {
        let newDiv = document.createElement("div");
        newDiv.classList.add("type-card");
        let typeName = document.createElement("div");
        typeName.classList.add("type-card-name");
        typeName.innerText = typeTag[i];
        newDiv.appendChild(typeName);
        let typeImg = document.createElement("div");
        typeImg.classList.add("type-card-img");
        newDiv.appendChild(typeImg);
        typePanel.appendChild(newDiv);
    }
}

function addClickTypes() {
    const types = typePanel.querySelectorAll(".type-card-img");
    const typesCnt = types.length

    for (let i = 0; i < typesCnt; ++i) {
        types[i].addEventListener("click", () => clickType(types[i], types, typesCnt));
    }
}

function clickType(thisType, types, typesCnt) {
    const parent = thisType.parentNode;
    const typeName = parent.querySelector(".type-card-name");
    thisType.classList.add("selected-element");
    handleTypes(thisType, types, typesCnt);
    handleSelect(typeName);
}

function handleTypes(thisType, types, typesCnt) {
    for (let i = 0; i < typesCnt; ++i)
        if (thisType !== types[i])
            types[i].classList.remove("selected-element");
}

function handleSelect(name) {
    if (name.innerText === "자작곡") {
        for (let i = 0; i < optionCnt; ++i)
            if (option[i].innerText === "Own") {
                option[i].selected = true;
                break;
            }
    }
    else if (name.innerText === "커버곡") {
        for (let i = 0; i < optionCnt; ++i)
            if (option[i].innerText === "Cover") {
                option[i].selected = true;
                break;
            }
    }
    else {
        for (let i = 0; i < optionCnt; ++i)
            if (option[i].innerText === "Clip") {
                option[i].selected = true;
                break;
            }
    }
}