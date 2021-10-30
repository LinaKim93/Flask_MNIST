const canvas = document.querySelector("#canvas");
const ctx = canvas.getContext("2d");
const draw = (e) => {
  const x = e.offsetX;
  const y = e.offsetY;
  if (!drawing) return;
  ctx.lineWidth = 20;
  ctx.lineCap = "round";
  ctx.strokeStyle = "#000";
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x, y);
  ctx.stroke();
};

let drawing = false;
canvas.addEventListener("mousedown", () => {
  drawing = true;
});
canvas.addEventListener("mouseup", () => {
  drawing = false;
});
canvas.addEventListener("mousemove", draw);
