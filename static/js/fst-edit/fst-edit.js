const avatarInput = document.querySelector("#id_avatar");
const avatarForm = document.querySelector(".form__avatar");
const avatarImg = document.querySelector(".avatar__img");


window.onload = initFstEdit();

function initFstEdit() {
    initAvatarForm();
    avatarForm.addEventListener("click", clickAvatarForm);
    avatarInput.addEventListener("change", changeAvatarInput);
}

function initAvatarForm() {
    console.log(avatarInput.files);
    if (avatarInput.value !== "") {
        avatarImg.src = `/media/${avatarInput.value}`;
        if (!avatarImg.classList.contains("loaded"))
            avatarImg.classList.add("loaded");
    }
}

function setAvatarForm() {
    const changedFile = avatarInput.files[0];

    if (!changedFile.type.startsWith('image/'))
        return undefined;

    if (!avatarImg.classList.contains("loaded"))
        avatarImg.classList.add("loaded");
    avatarImg.file = changedFile;

    const reader = new FileReader();
    reader.onload = (function (aImg) { return function (e) { aImg.src = e.target.result; }; })(avatarImg);
    reader.readAsDataURL(changedFile);
}

function clickAvatarForm() {
    avatarInput.type = "file";
    avatarInput.click();
}

function changeAvatarInput() {
    setAvatarForm();
}




// let avatar = document.querySelector("#fst-avatar");
// let hiddenAvatar = document.querySelector("#fst-avatar > input");
// let subTitle = document.querySelector("#fst-sub");
// // let username = document.querySelector("#id_username");
// // let fstBtn = document.querySelector(".fst-btn");


// avatar.addEventListener("click", clickAvatar);
// hiddenAvatar.addEventListener("change", selectAvatar);
// // fstBtn.addEventListener("click", clickFstBtn);


// function clickAvatar() {
//     console.log(hiddenAvatar);
//     hiddenAvatar.click();
// }

// function selectAvatar() {
//     console.log("sdf");
//     let file = this.files[0];
//     const img = document.createElement("img");
//     img.classList.add("fst-selected-img");
//     img.file = file;
//     avatar.appendChild(img);

//     const reader = new FileReader();
//     reader.onload = (function (aImg) { return function (e) { aImg.src = e.target.result; }; })(img);
//     reader.readAsDataURL(file);

//     subTitle.innerHTML = "프로필 사진이 선택되었습니다."
// }
