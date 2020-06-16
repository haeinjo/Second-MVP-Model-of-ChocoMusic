const typeNextBtn = document.querySelector("#type-next-btn");   // 나중에 create_content.js에 통합되어 져야 된다.
const photoDiv = document.querySelector("#check-photo");
const titleDiv = document.querySelector("#check-title");
const genreDiv = document.querySelector("#check-genre");
const projectDiv = document.querySelector("#check-project");
const levelUl = document.querySelector("#id_exposure_level");
const titleInput = document.querySelector("#id_content_title");
const descriptionInput = document.querySelector("#id_description");


window.onload = initCheckContent();

function initCheckContent() {
    typeNextBtn.classList.add("hidden-element");


    // Note: The file system has been prefixed as of Google Chrome 12:
    window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;

    navigator.webkitPersistentStorage.requestQuota(100 * 1024 * 1024, function (grantedBytes) {
        window.requestFileSystem(PERSISTENT, grantedBytes, onInitFs, errorHandler);
    }, function (e) {
        console.log('Error', e);
    });

    // Set Progress bar;
    document.querySelector("#dot1").style.backgroundColor = "#FFAA00";
    document.querySelector("#line2").style.backgroundColor = "#FFAA00";
    document.querySelector("#dot2").style.backgroundColor = "#FFAA00";
    document.querySelector("#line3").style.backgroundColor = "#FFAA00";
    document.querySelector("#dot3").style.backgroundColor = "#FFAA00";
    document.querySelector("#line4").style.backgroundColor = "#FFAA00";
    document.querySelector("#dot4").style.backgroundColor = "#FFAA00";
    setDiv();
}

function setDiv() {
    setCheckPhoto();
    setCheckTitle();
    setCheckGenre();
    setCheckProject();
    setCheckDescription();
}

function setCheckPhoto() {
    const contentPhoto = sessionStorage.getItem("content_photo");
    window.requestFileSystem(window.PERSISTENT, 100 * 1024 * 1024, onInitPhoto, errorHandler);
}

function setCheckTitle() {
    const contentTitle = sessionStorage.getItem("content_title");
    titleDiv.innerText = contentTitle;
    titleInput.value = contentTitle;
}

function setCheckGenre() {
    genreDiv.innerText = sessionStorage.getItem("genre");
}

function setCheckProject() {
    projectDiv.innerText = sessionStorage.getItem("project");
}

function setCheckDescription() {
    const description = sessionStorage.getItem("description");
    descriptionInput.value = description;
}



function onInitFs(e) {
    console.log("Success Init Persistent FS");
}

function errorHandler(e) {
    var msg = '';

    switch (e.code) {
        case FileError.QUOTA_EXCEEDED_ERR:
            msg = 'QUOTA_EXCEEDED_ERR';
            break;
        case FileError.NOT_FOUND_ERR:
            msg = 'NOT_FOUND_ERR';
            break;
        case FileError.SECURITY_ERR:
            msg = 'SECURITY_ERR';
            break;
        case FileError.INVALID_MODIFICATION_ERR:
            msg = 'INVALID_MODIFICATION_ERR';
            break;
        case FileError.INVALID_STATE_ERR:
            msg = 'INVALID_STATE_ERR';
            break;
        default:
            msg = 'Unknown Error';
            break;
    };

    console.log('Error: ' + msg);
}

function onInitPhoto(fs) {
    fs.root.getFile(sessionStorage.getItem('content_photo'), {}, function (fileEntry) {
        console.log("SDsdfsdfsf");
        // Get a File object representing the file,
        // then use FileReader to read its contents.
        const fileURL = fileEntry.toURL();
        console.log(`fileURL: ${fileURL}`);
        photoDiv.style.backgroundImage = `url(${fileURL})`;
        photoDiv.classList.add("check-bg");
    }, errorHandler);
}