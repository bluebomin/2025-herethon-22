// // 뒤로가기,앞으로가기, 페이지 추가...

// const urlParams = new URLSearchParams(window.location.search);
// const page = parseInt(urlParams.get("page")) || 1;

// const stories = JSON.parse(localStorage.getItem("stories")) || [];
// const postsPerPage = 10;
// const start = (page - 1) * postsPerPage;
// const end = start + postsPerPage;

// const visibleStories = stories.slice(start, end);
// const article = document.querySelector("article");
// article.innerHTML = ""; // 기존 글 지우기

// visibleStories.forEach((story) => {
//   const div = document.createElement("div");
//   div.className = "storyCt";
//   div.innerHTML = `
//     <p class="story">${story.content}</p>
//     <div class="storyIf">
//       <img class="profile" src="/img/profile.png" alt="프로필 이미지" />
//       <div class="userIf">
//         <p class="userName">익명</p>
//         <div class="userSt">
//           <p class="userT">경력 단절 N년</p>
//           <p class="userJ">직무 미입력</p>
//         </div>
//       </div>
//     </div>
//   `;
//   article.appendChild(div);
// });

// 페이지 번호 출력
const totalPages = Math.ceil(stories.length / postsPerPage);
const thisPage = document.getElementById("thisPage");
thisPage.textContent = `${page}`;

// 다음 페이지 버튼 기능
document.getElementById("mvN").addEventListener("click", () => {
  if (page < totalPages) {
    window.location.href = `StoryDetail.html?page=${page + 1}`;
  }
});
document.getElementById("mvB").addEventListener("click", () => {
  if (page > 1) {
    window.location.href = `StoryDetail.html?page=${page - 1}`;
  }
});
document.getElementById("mvF").addEventListener("click", () => {
  window.location.href = `StoryDetail.html?page=1`;
});
document.getElementById("mvE").addEventListener("click", () => {
  window.location.href = `StoryDetail.html?page=${totalPages}`;
});

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

  const fStarImg = ["/img/Star 1.png", "/img/fStar 1.png"];

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
    BellImg.src = "/static/img/Group 327.png"; // 알림 온 상태 이미지
  } else {
    BellImg.src = "/static/LandingPage/img/Bell.png"; // 기본 종 이미지
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

document.addEventListener("DOMContentLoaded", function () {
  const searchIcon = document.getElementById("SearchImg");
  const searchContainer = document.getElementById("search-container");
  const loginIcon = document.getElementById("login");
  const userImg = document.getElementById("UserImg");
  const bellIcon = document.getElementById("BellImg");
  const loginUserBox = document.getElementById("LoginUserIf");

  let isSearchOpen = false;

  searchIcon.addEventListener("click", function () {
    if (!isSearchOpen) {
      // 검색창 열기
      searchContainer.style.display = "flex";
      if (loginIcon) loginIcon.style.display = "none";
      if (userImg) userImg.style.display = "none";
      if (bellIcon) bellIcon.style.display = "none";
      if (loginUserBox) loginUserBox.style.display = "none";
    } else {
      // 검색창 닫기
      searchContainer.style.display = "none";
      if (loginIcon) loginIcon.style.display = "inline";
      if (userImg) userImg.style.display = "inline";
      if (bellIcon) bellIcon.style.display = "inline";
      if (loginUserBox) loginUserBox.style.display = "flex";
    }
    isSearchOpen = !isSearchOpen;
  });
});
