let signUp = document.querySelector("#sign-up");
let loginPanel = document.querySelector(".login-panel");
let kakaoBtn = document.querySelector("#kakao-btn");
let googleBtn = document.querySelector("#google-btn");


signUp.addEventListener("click", () => {
    loginPanel.classList.remove("no-display-flex");
    loginPanel.classList.add("display-flex");
});

kakaoBtn.addEventListener("click", () => {
    location.href = "/users/login/kakao/"
})

googleBtn.addEventListener("click", () => {
    location.href = "/users/login/google/"
})

document.addEventListener("click", (e) => {
    if (!loginPanel.contains(e.target) && !e.target.classList.contains("display-clip")) {
        loginPanel.classList.remove("display-flex");
        loginPanel.classList.add("no-display-flex");
    }
})













// var container = document.getElementById('map');
// var options = {
//     center: new kakao.maps.LatLng(33.450701, 126.570667),
//     level: 3
// };
// var map = new kakao.maps.Map(container, options);
// let marker = new kakao.maps.Marker({
//     map: map
// });
// kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
//     console.log(mouseEvent.latLng.getLat());
//     console.log(mouseEvent.latLng.getLng());
//     const lat = mouseEvent.latLng.getLat();
//     const lng = mouseEvent.latLng.getLng();
//     // alert(mouseEvent.latLng instanceof kakao.maps.LatLng); // true
//     marker.setPosition(new kakao.maps.LatLng(lat, lng));
// });

// var places = new kakao.maps.services.Places();

// // 키워드 검색 완료 시 호출되는 콜백함수 입니다 
// const placesSearchCB = function (data, status, pagination) {
//     if (status === kakao.maps.services.Status.OK) {

//         // 테스트용
//         console.log(data);

//         // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
//         // LatLngBounds 객체에 좌표를 추가합니다
//         var bounds = new kakao.maps.LatLngBounds();

//         for (var i = 0; i < data.length; i++) {
//             displayMarker(data[i]);
//             bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
//         }

//         // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
//         map.setBounds(bounds);
//     }
// }

// // 지도에 마커를 표시하는 함수입니다
// const displayMarker = function (place) {

//     // 마커를 생성하고 지도에 표시합니다
//     var marker = new kakao.maps.Marker({
//         map: map,
//         position: new kakao.maps.LatLng(place.y, place.x)
//     });

//     // 마커에 클릭이벤트를 등록합니다
//     kakao.maps.event.addListener(marker, 'click', function () {
//         // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
//         infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
//         infowindow.open(map, marker);
//     });
// }

// places.keywordSearch('부산 온천장', placesSearchCB);