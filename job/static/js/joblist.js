document.getElementById("dropdownButton").addEventListener("click", function () {
  const menu = document.getElementById("dropdownMenu");
  menu.style.display = menu.style.display === "block" ? "none" : "block";
});

// 바깥 클릭 시 닫기
window.addEventListener("click", function (e) {
  const menu = document.getElementById("dropdownMenu");
  const button = document.getElementById("dropdownButton");
  if (!button.contains(e.target) && !menu.contains(e.target)) {
    menu.style.display = "none";
  }
});
const button = document.getElementById("dropdownButton");
const menu = document.getElementById("dropdownMenu");

button.addEventListener("click", function () {
  menu.style.display = "grid";
}); //클릭 시 체크박스가 눈에 보이면서 그리드로

// const checkboxes = document.querySelectorAll("input[name='job']:checked");
// checkboxes.forEach(cb => console.log(cb.value));

