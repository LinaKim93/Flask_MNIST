const canvas = document.querySelector("#canvas");
const ctx = canvas.getContext("2d");
ctx.clearRect(0, 0, 300, 300);
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);
const draw = (e) => {
  const x = e.offsetX;
  const y = e.offsetY;
  if (!drawing) return;
  ctx.lineWidth = 30;
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

const predict_btn = document.querySelector(".result");
const clear_btn = document.querySelector(".clear");
const result = document.querySelector("#result");

result.textContent = "result : ";

predict_btn.addEventListener("click", function () {
  result.textContent = "Predicting...";
  let canvasObj = document.getElementById("canvas");
  let img = canvasObj.toDataURL("image/url");
  let data = {
    image: img,
  };
  sendImg(data);
  getImg();
});

clear_btn.addEventListener("click", function () {
  result.textContent = "result : ";
  ctx.clearRect(0, 0, 300, 300);
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
});

function sendImg(data) {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", "./predict", true);
  xhr.onload = function () {
    if (xhr.status === 200 || xhr.status === 201) {
      console.log(xhr.responseText);
    } else {
      console.error(xhr.responseText);
    }
  };
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send(JSON.stringify(data));
}

function getImg() {
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "./predict", true);
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log(xhr.response);
      result.textContent = `result : ${xhr.response}`;
    } else {
      console.log("fail");
    }
  };
  xhr.send();
}
