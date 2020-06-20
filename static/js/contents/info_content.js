const teamInput = document.querySelector(".team__input");
const selectProject = document.querySelector(".project__input");
const sectionPhoto = document.querySelector(".section1__photo");
const sectionTitle = document.querySelector(".section2__title");
const sectionDescription = document.querySelector(".description__input");
const selectGenre = document.querySelector(".genre__select");
const xhttp = new XMLHttpRequest();


window.onload = initContentInfo();

function initContentInfo() {
    teamInput.addEventListener("change", changeTeamInput);
    xhttp.addEventListener("load", loadXhttp);
    sectionPhoto.addEventListener("dragOver", FileDragHover, false);
    sectionPhoto.addEventListener("drop", FileSelectHandler, false);
    sectionPhoto.addEventListener("click", clickSectionPhoto);
    sectionTitle.addEventListener("change", changeSectionTitle);
    photoInput.addEventListener("change", changePhotoInput);
    selectGenre.addEventListener("change", changeSelectGenre);
    selectProject.addEventListener("change", changeSelectProject);
    sectionDescription.addEventListener("change", changeSectionDescription);
}


function changeTeamInput() {
    const team = this.value;
    // console.log(`team: ${team}`);
    const option = document.createElement("option");
    xhttp.open("POST", "http://127.0.0.1:8000/contents/create/", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    xhttp.send(`team=${team}`);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function loadXhttp() {
    const temp = xhttp.response;
    let htemp = document.createElement("div");

    htemp.innerHTML = temp;
    htemp = htemp.querySelector("#id_project");

    const projectOptions = htemp.querySelectorAll("#id_project option");
    selectProject.innerHTML = '';
    for (let i = 0; projectOptions[i]; ++i) {
        selectProject.appendChild(projectOptions[i]);
    }
    selectProject.selectedIndex = 0;
}


function FileDragHover(e) {
    e.stopPropagation();
    e.preventDefault();
    console.log(e.type);
    const hoverClass = (e.type == "dragover" ? "element--hover" : "");
    if (hoverClass !== "")
        filePanel.classList.add(hoverClass);
}

function FileSelectHandler(e) {
    FileDragHover(e);

    const thisFile = e.target.files || e.dataTransfer.files;
    fileInput.files = thisFile;
}

function clickSectionPhoto() {
    photoInput.click();
}

function changeSectionTitle() {
    const thisTitle = this.value;
    titleInput.value = thisTitle;
}

function changePhotoInput(e) {
    const changedPhoto = e.target.files[0];
    const newImg = document.createElement("img");
    newImg.file = changedPhoto;
    newImg.classList.add("added__img");
    sectionPhoto.innerHTML = "";
    sectionPhoto.appendChild(newImg);

    const reader = new FileReader();
    reader.onload = (function (aImg) { return function (e) { aImg.src = e.target.result; }; })(newImg);
    reader.readAsDataURL(changedPhoto);
}

function changeSelectGenre() {
    const thisValue = this.selectedOptions[0].value;
    const selectedOption = genreInput.querySelector(`option[value="${thisValue}"]`);
    selectedOption.selected = true;
}

function changeSelectProject() {
    const thisValue = this.selectedOptions[0].value;
    const selectedOption = projectInput.querySelector(`option[value="${thisValue}"]`);
    selectedOption.selected = true;
}

function changeSectionDescription() {
    const thisValue = this.value;
    descriptionInput.value = thisValue;
}

// const typeNextBtn = document.querySelector("#type-next-btn");   // 나중에 create_content.js에 통합되어 져야 된다.
// const submitBtn = document.querySelector("button");
// const contentPhoto = document.querySelector("#content-photo");
// const photoInput = document.querySelector("#id_content_photo");
// const genreSelect = document.querySelector("#id_genre");
// const titleInput = document.querySelector("#id_content_title");
// const descriptionInput = document.querySelector("#id_description");
// const teamInput = document.querySelector("#id_content_team");
// const projectSelect = document.querySelector("#id_project");
// const projectLabel = document.querySelector("#content-project > div");
// const xhttp = new XMLHttpRequest();

// window.onload = initInfoContent();

// function initInfoContent() {
//     contentPhoto.addEventListener("click", clickContentPhoto);
//     photoInput.addEventListener("change", changePhotoInput);
//     genreSelect.addEventListener("change", changeGenreSelect);
//     titleInput.addEventListener("change", changeTitleInput);
//     descriptionInput.addEventListener("change", changeDescriptionInput);
//     teamInput.addEventListener("change", changeTeamInput);
//     typeNextBtn.addEventListener("click", clickSubmitBtn);
//     projectSelect.addEventListener("change", changeProjectSelect);
//     xhttp.addEventListener("load", loadXhttp);
//     projectToggle();
//     // Set Progress bar;
//     document.querySelector("#dot1").style.backgroundColor = "#FFAA00";
//     document.querySelector("#line2").style.backgroundColor = "#FFAA00";
//     document.querySelector("#dot2").style.backgroundColor = "#FFAA00";
//     document.querySelector("#line3").style.backgroundColor = "#FFAA00";
//     document.querySelector("#dot3").style.backgroundColor = "#FFAA00";



//     // Note: The file system has been prefixed as of Google Chrome 12:
//     window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;

//     navigator.webkitPersistentStorage.requestQuota(100 * 1024 * 1024, function (grantedBytes) {
//         window.requestFileSystem(PERSISTENT, grantedBytes, onInitFs, errorHandler);
//     }, function (e) {
//         console.log('Error', e);
//     });
// }

// function loadXhttp() {
//     const temp = xhttp.response;
//     const htemp = document.createElement("div");
//     htemp.innerHTML = temp;
//     const projectOptions = htemp.querySelectorAll("#id_project > option");
//     console.log(projectOptions);
//     projectSelect.innerHTML = '';
//     const optionLength = projectOptions.length;
//     for (let i = 0; i < optionLength; ++i) {
//         projectSelect.appendChild(projectOptions[i]);
//     }
//     projectSelect.selectedIndex = 0;
// }

// function clickContentPhoto() {
//     photoInput.click();
// }

// function changePhotoInput() {
//     const files = this.files;

//     window.requestFileSystem(window.PERSISTENT, 100 * 1024 * 1024, function (fs) {
//         // Duplicate each file the user selected to the app's fs.
//         for (var i = 0, file; file = files[i]; ++i) {

//             // Capture current iteration's file in local scope for the getFile() callback.
//             (function (f) {
//                 sessionStorage.setItem('content_photo', f.name);
//                 fs.root.getFile(f.name, { create: true, exclusive: true }, function (fileEntry) {
//                     fileEntry.createWriter(function (fileWriter) {
//                         fileWriter.write(f); // Note: write() can take a File or Blob object.
//                     }, errorHandler);
//                 }, errorHandler);
//             })(file);

//         }
//     }, errorHandler);

//     window.requestFileSystem(window.PERSISTENT, 100 * 1024 * 1024, function (fs) {
//         fs.root.getFile(sessionStorage.getItem('content_photo'), {}, function (fileEntry) {
//             console.log("SDsdfsdfsf");
//             // Get a File object representing the file,
//             // then use FileReader to read its contents.
//             const fileURL = fileEntry.toURL();
//             console.log(fileURL);
//             contentPhoto.style.backgroundImage = `url(${fileURL})`;
//             contentPhoto.classList.add("check-bg");
//             contentPhoto.innerHTML = "";
//         }, errorHandler);
//     }, errorHandler);
// }

// function changeGenreSelect() {
//     const selectedValue = this.options[this.selectedIndex].text;
//     sessionStorage.setItem("genre", selectedValue);
// }

// function changeProjectSelect() {
//     const selectedValue = this.options[this.selectedIndex].text;
//     sessionStorage.setItem("project", selectedValue);
// }

// function changeTitleInput() {
//     const title = this.value;
//     sessionStorage.setItem("content_title", title);
// }



// function changeDescriptionInput() {
//     const des = this.value;
//     sessionStorage.setItem("description", des);
// }

// function changeTeamInput() {
//     const team = this.value;
//     const option = document.createElement("option");
//     xhttp.open("POST", "http://127.0.0.1:8000/contents/create/info/", true);
//     xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//     xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//     xhttp.send(`team=${this.value}`);
//     projectToggle();
// }

// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// function projectToggle() {
//     projectSelect.classList.toggle("hidden-element");
//     projectLabel.classList.toggle("hidden-element");
// }

// function clickSubmitBtn() {
//     //session으로 프론트에서 컨트롤하기
//     submitBtn.click();
// }





// function onInitFs(e) {
//     console.log("Success Init Persistent FS");
// }

// function errorHandler(e) {
//     var msg = '';

//     switch (e.code) {
//         case FileError.QUOTA_EXCEEDED_ERR:
//             msg = 'QUOTA_EXCEEDED_ERR';
//             break;
//         case FileError.NOT_FOUND_ERR:
//             msg = 'NOT_FOUND_ERR';
//             break;
//         case FileError.SECURITY_ERR:
//             msg = 'SECURITY_ERR';
//             break;
//         case FileError.INVALID_MODIFICATION_ERR:
//             msg = 'INVALID_MODIFICATION_ERR';
//             break;
//         case FileError.INVALID_STATE_ERR:
//             msg = 'INVALID_STATE_ERR';
//             break;
//         default:
//             msg = 'Unknown Error';
//             break;
//     };

//     console.log('Error: ' + msg);
// }
