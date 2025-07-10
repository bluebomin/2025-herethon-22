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
