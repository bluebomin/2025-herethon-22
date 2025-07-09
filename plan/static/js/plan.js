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
    BellImg.src = "/plan/static/img/Group 327.png"; // 알림 온 상태 이미지
  } else {
    BellImg.src = "/plan/static/img/Bell.png"; // 기본 종 이미지
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

  let isSearchOpen = false;

  searchIcon.addEventListener("click", function () {
    if (!isSearchOpen) {
      searchContainer.style.display = "flex";
      loginImg.style.display = "none";
      userImg.style.display = "none";
      bellIcon.style.display = "none";
    } else {
      searchContainer.style.display = "none";
      loginImg.style.display = "inline";
      userImg.style.display = "inline";
      bellIcon.style.display = "inline";
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

document.addEventListener("DOMContentLoaded", function () {
  const dropdownContainers = document.querySelectorAll(".dropdown-container");

  //드롭다운 메뉴
  dropdownContainers.forEach((container) => {
    const btn = container.querySelector(".dropdownBtn");
    const menu = container.querySelector(".dropdown-menu");

    btn.addEventListener("click", function (e) {
      e.stopPropagation(); // 이벤트 전파 막기

      const isActive = container.classList.contains("active");

      // 이미 열려 있다면 -> 닫기
      if (isActive) {
        container.classList.remove("active");
      } else {
        // 열려 있지 않다면 -> 모두 닫고 이 메뉴만 열기
        closeAllDropdowns();
        container.classList.add("active");
      }
    });

    // 바깥 클릭 시 닫기
    window.addEventListener("click", function (e) {
      if (!container.contains(e.target)) {
        container.classList.remove("active");
      }
    });
  });

  function closeAllDropdowns() {
    document.querySelectorAll(".dropdown-container").forEach((c) => {
      c.classList.remove("active");
    });
  }
});

//스크랩 버튼 클릭 시 서버에 해당 카드 id 전송
document.querySelectorAll(".scrap").forEach((button) => {
  button.addEventListener("click", function () {
    const jobId = this.dataset.id;

    fetch(`/bookmark/${jobId}/toggle/`, {
      method: "GET",
      credentials: "include", // 로그인 정보 함께 전송 (로그인 여부 체크용)
    })
      .then((response) => {
        if (response.ok) {
          console.log("북마크 요청 성공");
        } else {
          console.error("북마크 요청 실패");
        }
      })
      .catch((error) => {
        console.error("에러 발생:", error);
      });
  });
});
//버튼 클릭시 채워진 이미지로 변경
document.addEventListener("DOMContentLoaded", function () {
  const scrapButtons = document.querySelectorAll(".scrap");

  scrapButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const isFilled = btn.getAttribute("src").includes("scrapbtn-filled.svg");

      btn.setAttribute(
        "src",
        isFilled
          ? "../static/img/scrapbtn.svg"
          : "../static/img/scrapbtn-filled.svg"
      );
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const addBtn = document.getElementById("addBtn");
  const input = document.getElementById("skillInput");
  const container = document.getElementById("skillTags");

  addBtn.addEventListener("click", () => {
    const value = input.value.trim();
    if (!value) return;

    const tags = Array.from(container.querySelectorAll(".tag-text")).map(
      (el) => el.textContent
    );
    if (tags.includes(value)) {
      input.value = "";
      return;
    }

    const tag = document.createElement("div");
    tag.className = "skill-tag";
    tag.style.cssText = `
        display: flex;
        align-items: center;
        padding: 8px 12px;
        border: 2px solid #9ac9a3;
        border-radius: 40px;
        font-size: 15px;
        color: #333;
        background-color: #f7fdf7;
        width:auto;
      `;

    const text = document.createElement("span");
    text.className = "tag-text";
    text.textContent = value;

    const removeBtn = document.createElement("span");
    removeBtn.innerHTML = "&nbsp;&nbsp;✕";
    removeBtn.style.cssText = "cursor: pointer; color: #5b9968;";
    removeBtn.addEventListener("click", () => tag.remove());

    tag.appendChild(text);
    tag.appendChild(removeBtn);
    container.appendChild(tag);

    input.value = "";
  });
});

//글머리기호
document.addEventListener("DOMContentLoaded", function () {
  const textarea = document.getElementById("TA");

  // 첫 입력 시 자동으로 글머리표 추가
  textarea.addEventListener("focus", function () {
    if (textarea.value.trim() === "") {
      textarea.value = "• ";
    }
  });

  // 엔터키 눌렀을 때 다음 줄에 글머리표 자동 추가
  textarea.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault(); // 기본 줄바꿈 막고
      const cursorPos = textarea.selectionStart;
      const value = textarea.value;

      // 현재 줄바꿈 후 글머리표 넣기
      const before = value.substring(0, cursorPos);
      const after = value.substring(cursorPos);

      textarea.value = before + "\n• " + after;

      // 커서를 글머리표 뒤로 이동
      textarea.selectionStart = textarea.selectionEnd = cursorPos + 3;
    }
  });
});
