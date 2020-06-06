let avatar = document.querySelector("#fst-avatar");
let hiddenAvatar = document.querySelector("#fst-hidden-input");
let subTitle = document.querySelector("#fst-sub")

avatar.addEventListener("click", clickAvatar);
hiddenAvatar.addEventListener("change", selectAvatar);

function clickAvatar() {
    hiddenAvatar.click();
}

function selectAvatar() {
    console.log("sdf");
    let file = this.files[0];
    const img = document.createElement("img");
    img.classList.add("fst-selected-img");
    img.file = file;
    avatar.appendChild(img);

    const reader = new FileReader();
    reader.onload = (function (aImg) { return function (e) { aImg.src = e.target.result; }; })(img);
    reader.readAsDataURL(file);

    subTitle.innerHTML = "프로필 사진이 선택되었습니다."
}

