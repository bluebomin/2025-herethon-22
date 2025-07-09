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
