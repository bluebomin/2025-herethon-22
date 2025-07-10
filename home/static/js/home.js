//스크랩(id로 변경시 사용)
// document.addEventListener("DOMContentLoaded", function () {
//   const starImg = document.getElementByIdBy("Tcstar");

//   const fStarImg = [
//     "/img/Star 1.png", // 현재 이미지
//     "/img/fStar 1.png", // 교체 이미지
//   ];

//   let current = 0;

//   starImg.addEventListener("click", function () {
//     current = (current + 1) % fStarImg.length;
//     starImg.src = fStarImg[current];
//   });
// });

// 스크랩(class 사용)
document.addEventListener("DOMContentLoaded", function () {
  const starImgs = document.querySelectorAll(".Tcstar");

  const fStarImg = ["static/img/Star 1.png", "static/img/fStar 1.png"];

  starImgs.forEach((starImg) => {
    let current = 0;

    starImg.addEventListener("click", function () {
      current = (current + 1) % fStarImg.length;
      starImg.src = fStarImg[current];
    });
  });
});

//헤더 알림 on
document.addEventListener("DOMContentLoaded", function () {
  const BellImg = document.getElementById("BellImg");

  // 백엔드 연동 전-> 임시로 알림 온 상태로 설정 (true)
  const hasNotification = true; //false면 알람표시x

  if (hasNotification) {
    BellImg.src = "static/img/Group 327.png"; // 알림 온 상태 이미지
  } else {
    BellImg.src = "static/LandingPage/img/Bell.png"; // 기본 종 이미지
  }
});

// //연동시 반영
// fetch("/api/notifications/unread")
//   .then((res) => res.json())
//   .then((data) => {
//     const bellIcon = document.getElementById("bellIcon");
//     if (data.hasUnread) {
//       bellIcon.src = "/img/Bell_active.png";
//     } else {
//       bellIcon.src = "/img/Bell.png";
//     }
//   });

//알림 클릭
document.getElementById("BellImg").addEventListener("click", function () {
  const notifBox = document.getElementById("notif-box");
  notifBox.style.display =
    notifBox.style.display === "block" ? "none" : "block";
});

//돋보기 클릭
document.addEventListener("DOMContentLoaded", function () {
  const searchIcon = document.getElementById("SearchImg");
  const searchContainer = document.getElementById("search-container");
  const loginImg = document.getElementById("login");
  const userImg = document.getElementById("UserImg");
  const bellIcon = document.getElementById("BellImg");
  const loginUser = document.getElementById("LoginUserIf");
  let isSearchOpen = false;

  searchIcon.addEventListener("click", function () {
    if (!isSearchOpen) {
      searchContainer.style.display = "flex";
      loginImg.style.display = "none";
      userImg.style.display = "none";
      bellIcon.style.display = "none";
      loginUser.style.display = "none";
    } else {
      searchContainer.style.display = "none";
      loginImg.style.display = "inline";
      userImg.style.display = "inline";
      bellIcon.style.display = "inline";
      loginUser.style.display = "inline";
    }
    isSearchOpen = !isSearchOpen;
  });
});

//검색어 입력시 변화
document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");

  searchInput.addEventListener("input", function () {
    if (searchInput.value.trim() !== "") {
      searchInput.style.color = "black";
      searchInput.style.fontWeight = "400";
    } else {
      searchInput.style.color = "  #9ca3af";
      searchInput.style.fontWeight = "300";
    }
  });
});

//로그인 유저 이름 반환

// 전역 로그인 상태 (연동 전 임시로 true)
const isLoggedIn = true;
// const userName = "신명서";

document.addEventListener("DOMContentLoaded", function () {
  // 요소 선언
  const loginIcon = document.getElementById("login");
  const loginUserBox = document.getElementById("LoginUserIf");
  const userNameText = document.getElementById("LoginUserName");
  const searchIcon = document.getElementById("SearchImg");
  const searchContainer = document.getElementById("search-container");
  const userImg = document.getElementById("UserImg");
  const bellIcon = document.getElementById("BellImg");

  //로그인 상태 설정
  if (isLoggedIn) {
    loginIcon.style.display = "none";
    loginUserBox.style.display = "flex";
    userNameText.textContent = userName;
  } else {
    loginIcon.style.display = "inline";
    loginUserBox.style.display = "none";
  }

  // 돋보기 토글
  let isSearchOpen = false;

  searchIcon.addEventListener("click", function () {
    if (!isSearchOpen) {
      searchContainer.style.display = "flex";
      loginIcon.style.display = "none";
      loginUserBox.style.display = "none";
      userImg.style.display = "none";
      bellIcon.style.display = "none";
    } else {
      searchContainer.style.display = "none";

      //로그인 상태 고려하여 UI 복원
      if (isLoggedIn) {
        loginIcon.style.display = "none";
        loginUserBox.style.display = "flex";
      } else {
        loginIcon.style.display = "inline";
        loginUserBox.style.display = "none";
      }

      userImg.style.display = "inline";
      bellIcon.style.display = "inline";
    }

    isSearchOpen = !isSearchOpen;
  });
});
