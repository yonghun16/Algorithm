const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.output,
});

const inputData = [];
rl.on("line", function (line) {
  inputData.push(line.trim());
}).on("close", function () {
  const inputVal = inputData[0].split(" ").map(Number);
  main(inputVal);
  process.exit();
});

function main(inputVal) {
  const a = inputVal[0];
  const b = inputVal[1];

  console.log(a * b);
}
