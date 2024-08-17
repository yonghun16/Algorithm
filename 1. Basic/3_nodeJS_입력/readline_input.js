/* 한 줄씩 입력을 연달아 받아야 할 때는 readline 모듈을 사용. */

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
})

const inputData = []

rl.on("line", function (line) {
  // 콘솔 입력 창에서 줄바꿈(Enter)를 입력할 때마다 호출
  inputData.push(line.trim())
}).on("close", function () {
  const inputVal = inputData[0].split(" ").map(Number)
  main(inputVal)
  process.exit()
});


function main(inputVal) {
  console.log(inputVal)
}
