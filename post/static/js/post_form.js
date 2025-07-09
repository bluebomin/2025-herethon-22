// document.getElementById("stSubmit").addEventListener("click", (e) => {
//   e.preventDefault(); // a태그 기본 이동 막기

//   const title = document.getElementById("wrStoryTitle").value;
//   const content = document.getElementById("wrStoryN").value;

//   // if (!title || !content) {
//   //   alert("제목과 내용을 모두 입력해주세요.");
//   //   return;
//   // }

//   // 기존 글 목록 불러오기
//   const oldData = JSON.parse(localStorage.getItem("stories")) || [];

//   // 새로운 글 추가
//   oldData.push({ title, content });

//   // 다시 저장
//   localStorage.setItem("stories", JSON.stringify(oldData));

//   // 자동 페이지 계산 (예: 10개당 1페이지)
//   const currentPage = Math.ceil(oldData.length / 10);

//   // 페이지 번호와 함께 StoryDetail로 이동
//   window.location.href = `./StoryDetail.html?page=${currentPage}`;
// });
