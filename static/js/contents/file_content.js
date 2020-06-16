const fileSelect = document.querySelector("#id_content_file");
const fileScraper = document.querySelector("#file-scraper");
const fileInput = document.querySelector("#id_content_file");
const typeNextBtn = document.querySelector("#type-next-btn");   // 나중에 create_content.js에 통합되어 져야 된다.
const filePanel = document.querySelector("#file-panel");
const submitBtn = document.querySelector("button");


window.onload = initFileContent();

function initFileContent() {
    fileSelect.classList.add("hidden-element");
    document.querySelector("#dot1").style.backgroundColor = "#FFAA00";
    document.querySelector("#line2").style.backgroundColor = "#FFAA00";
    document.querySelector("#dot2").style.backgroundColor = "#FFAA00";
    fileScraper.addEventListener("click", clickFileScraper);
    typeNextBtn.addEventListener("click", clickSubmitBtn);
    fileInput.addEventListener("change", changeFileInput);
    if (window.File && window.FileList && window.FileReader)
        setFileDAD();

    // Note: The file system has been prefixed as of Google Chrome 12:
    window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;

    navigator.webkitPersistentStorage.requestQuota(100 * 1024 * 1024, function (grantedBytes) {
        window.requestFileSystem(PERSISTENT, grantedBytes, onInitFs, errorHandler);
    }, errorHandler);
}

// function clearFs(fs) {
//     fs.root.getFile({ create: false }, function (fileEntry) {

//         fileEntry.remove(function () {
//             console.log('File removed.');
//         }, errorHandler);

//     }, errorHandler);



//     // fs.root.getDirectory('filesystem', {}, function (dirEntry) {
//     //     console.log("SDFSFSDf");
//     //     dirEntry.remove(function () {
//     //         console.log("FS cleared.");
//     //     }, errorHandler);
//     // }, errorHandler);
// }

function onInitFs(e) {
    console.log("Success Init Persistent FS");
}

//업로드할 파일이 선택되면 해당 파일 정보 세션에 저장
function changeFileInput(e) {
    var files = this.files || e.files;
    console.log(files);

    window.requestFileSystem(window.PERSISTENT, 100 * 1024 * 1024, function (fs) {
        // Duplicate each file the user selected to the app's fs.
        for (var i = 0, file; file = files[i]; ++i) {

            // Capture current iteration's file in local scope for the getFile() callback.
            (function (f) {
                sessionStorage.setItem('content_file', f.name);
                fs.root.getFile(f.name, { create: true, exclusive: true }, function (fileEntry) {
                    fileEntry.createWriter(function (fileWriter) {
                        fileWriter.write(f); // Note: write() can take a File or Blob object.
                    }, errorHandler);
                }, errorHandler);
            })(file);

        }
    }, errorHandler);
};

function clickFileScraper() {
    fileInput.click();
}

function setFileDAD() {
    // fileInput.addEventListener("change", FileSelectHandler);

    const xhr = new XMLHttpRequest();
    if (xhr.upload) {
        // file drop
        filePanel.addEventListener("dragover", FileDragHover, false);
        // filedrag.addEventListener("dragleave", FileDragHover, false);
        filePanel.addEventListener("drop", FileSelectHandler, false);
    }
}

function FileDragHover(e) {
    e.stopPropagation();
    e.preventDefault();
    console.log(e.type);
    const hoverClass = (e.type == "dragover" ? "hover" : "");
    if (hoverClass !== "")
        e.target.classList.add(hoverClass);
}

function FileSelectHandler(e) {
    FileDragHover(e);

    const thisFile = e.target.files || e.dataTransfer.files;
    fileInput.files = thisFile;
    changeFileInput(e.dataTransfer);

}

function clickSubmitBtn() {
    console.log(fileInput.files.length);
    if (fileInput.files.length !== 0)
        submitBtn.click();
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