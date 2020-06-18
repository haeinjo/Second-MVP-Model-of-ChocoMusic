const typeNextBtn = document.querySelector("#type-next-btn");   // 나중에 create_content.js에 통합되어 져야 된다.
const photoDiv = document.querySelector("#check-photo");
const titleDiv = document.querySelector("#check-title");
const genreDiv = document.querySelector("#check-genre");
const projectDiv = document.querySelector("#check-project");
const levelUl = document.querySelector("#id_exposure_level");
const typeInput = document.querySelector("#id_content_type");
const titleInput = document.querySelector("#id_content_title");
const descriptionInput = document.querySelector("#id_description");
const fileInput = document.querySelector("#id_content_file");
const uploadButton = document.querySelector("button")


window.onload = initCheckContent();

function initCheckContent() {
    typeNextBtn.classList.add("hidden-element");
    uploadButton.addEventListener("click", clickUploadBtn);

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

    // Set Empty Tags
    setDiv();
}

function clickUploadBtn() {
    const contentType = sessionStorage.getItem("content_type");
    const contentTitle = sessionStorage.getItem("content_title");

}

function setDiv() {
    setCheckPhoto();
    setCheckFile();
    setCheckType();
    setCheckTitle();
    setCheckGenre();
    setCheckProject();
    setCheckDescription();
}

function setCheckPhoto() {
    const contentPhoto = sessionStorage.getItem("content_photo");
    window.requestFileSystem(window.PERSISTENT, 100 * 1024 * 1024, onInitPhoto, errorHandler);
}

function setCheckFile() {
    window.requestFileSystem(window.PERSISTENT, 100 * 1024 * 1024, onInitFile, errorHandler);
}

function setCheckType() {
    const contentType = sessionStorage.getItem("content_type");
    setTypeInput(contentType);
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

function setTypeInput(ct) {
    let optionList = typeInput.options;
    let inputValue = "";

    if (ct === "커버곡") {
        inputValue = "cover";
    } else if (ct === "자작곡") {
        inputValue = "own";
    } else {
        inputValue = "clip";
    }

    for (let i = 0; optionList[i]; ++i) {
        if (optionList[i].value === inputValue) {
            typeInput.selectedIndex = i;
            break;
        }
    }
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
        // Get a File object representing the file,
        // then use FileReader to read its contents.
        const fileURL = fileEntry.toURL();
        photoDiv.style.backgroundImage = `url(${fileURL})`;
        photoDiv.classList.add("check-bg");
    }, errorHandler);
}

function onInitFile(fs) {
    fs.root.getFile(sessionStorage.getItem('content_file'), {}, function (fileEntry) {
        // Get a File object representing the file,
        // then use FileReader to read its contents.
        fileEntry.file(function (f) {
            console.log(f);
            const reader = new FileReader();

            fileInput.files = reader.readAsArrayBuffer(f);
            console.log(fileInput.files);
            //    var reader = new FileReader();

            //    reader.onloadend = function(e) {
            //      var txtArea = document.createElement('textarea');
            //      txtArea.value = this.result;
            //      document.body.appendChild(txtArea);
            //    };

            //    reader.readAsText(file);
        }, errorHandler);

    }, errorHandler);
}