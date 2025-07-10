document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".scrap").forEach((button) => {
    button.addEventListener("click", function () {
      const jobId = this.dataset.jobId;
      const currentImg = this;

      fetch(`/bookmark/${jobId}/toggle/`, {
        method: "GET",
        credentials: "include", // 로그인 세션 유지
      })
        .then((response) => {
          if (response.ok) {
            // 이미지 토글
            const isBookmarked = currentImg.src.includes("scrapbtn-filled.svg");
            currentImg.src = isBookmarked
              ? "/static/img/scrapbtn.svg"
              : "/static/img/scrapbtn-filled.svg";
          } else if (response.status === 403) {
            alert("스크랩은 로그인 후 이용할 수 있어요.");
            window.location.href = "/login/";
          } else {
            alert("스크랩 처리에 실패했어요.");
          }
        })
        .catch((error) => {
          console.error("에러 발생:", error);
          alert("서버와 통신 중 오류가 발생했어요.");
        });
    });
  });
});