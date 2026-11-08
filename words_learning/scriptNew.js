const ol = document.querySelector("ol");
const countEl = document.querySelector("#count");

function updateCount() {
  const total = ol.children.length;
  const marked = ol.querySelectorAll("li.marked").length;
  countEl.textContent =
    ol.classList.contains("only-forgotten") && marked === 0
      ? "Выбранных слов нет. Нажмите «Только выбранные», чтобы вернуть весь список."
      : `Всего слов: ${total}, выбрано: ${marked}`;
}

ol.addEventListener("click", (e) => {
  const li = e.target.closest("li");
  if (!li) return;
  li.classList.toggle("marked");
  updateCount();
});

function setMode(mode) {
  ol.classList.remove("only-srb", "only-ru");
  if (mode) ol.classList.add(mode);
  document
    .querySelectorAll("#b-srb, #b-ru, #b-all")
    .forEach((b) => b.classList.remove("active"));
  const id = { "only-srb": "b-srb", "only-ru": "b-ru", "": "b-all" }[mode];
  document.getElementById(id).classList.add("active");
}

function shuffle() {
  const lis = [...ol.children];
  for (let i = lis.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [lis[i], lis[j]] = [lis[j], lis[i]];
  }
  ol.replaceChildren(...lis);
  ol.classList.add("no-days");
}

function toggleForgotten() {
  const on = ol.classList.toggle("only-forgotten");
  document.getElementById("b-forgotten").classList.toggle("active", on);
  updateCount();
}

updateCount();
