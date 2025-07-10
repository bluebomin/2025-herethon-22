// 댓글 작성하면 댓글 +1개 (완)
// 공감 누르면 사진 교체 (완)

// 좋아요
document.addEventListener("DOMContentLoaded", function () {
  const likeImg = document.getElementById("likeImg");

  const flikeImg = [
    "/static/img/like.png", // 현재 이미지
    "/static/img/flike.png", // 교체 이미지
  ];

  let current = 0;

  likeImg.addEventListener("click", function () {
    current = (current + 1) % flikeImg.length;
    likeImg.src = flikeImg[current];
  });
});
// 응원해요
document.addEventListener("DOMContentLoaded", function () {
  const goodImg = document.getElementById("goodImg");

  const fgoodImg = [
    "/static/img/good.png", // 현재 이미지
    "/static/img/fgood.png", // 교체 이미지
  ];

  let current = 0;

  goodImg.addEventListener("click", function () {
    current = (current + 1) % fgoodImg.length;
    goodImg.src = fgoodImg[current];
  });
});
// 도움이 됐어요
document.addEventListener("DOMContentLoaded", function () {
  const smileImg = document.getElementById("smileImg");

  const fsmImg = [
    "/static/img/smile.png", // 현재 이미지
    "/static/img/fsm.png", // 교체 이미지
  ];

  let current = 0;

  smileImg.addEventListener("click", function () {
    current = (current + 1) % fsmImg.length;
    smileImg.src = fsmImg[current];
  });
});
//스크랩
document.addEventListener("DOMContentLoaded", function () {
  const starImg = document.getElementById("star");

  const fStarImg = [
    "/static/img/Star 1.png", // 현재 이미지
    "/static/img/fStar 1.png", // 교체 이미지
  ];

  let current = 0;

  starImg.addEventListener("click", function () {
    current = (current + 1) % fStarImg.length;
    starImg.src = fStarImg[current];
  });
});

// // 댓글 기능
document.addEventListener("DOMContentLoaded", function () {
  const commentForm = document.getElementById("coW");
  const commentInput = document.getElementById("myCo");
  const commentCountSpan = document.querySelector("#coTitle span");

  commentForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const commentText = commentInput.value.trim();
    if (commentText === "") return;

    // //alert 창에 표시
    // alert("입력한 댓글: " + commentText);

    // 댓글 수 +1
    let count = parseInt(commentCountSpan.innerText);
    commentCountSpan.innerText = count + 1;

    // // 콘솔출력
    // console.log(`댓글 ${count + 1}개`);
    // console.log(`작성한 내용: ${commentText}`);

    commentInput.value = "";
  });
});
