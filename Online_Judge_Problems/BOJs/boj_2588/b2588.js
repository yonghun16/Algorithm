const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');
const inputVal_a = inputData[0];
const inputVal_b = inputData[1];

main(inputVal_a, inputVal_b);

function main(inputVal_a, inputVal_b) {
  const a = Number(inputVal_a);
  const b = Number(inputVal_b);
  const b_1 = Number(inputVal_b[2]);  // 일의 자리
  const b_2 = Number(inputVal_b[1]);  // 십의 자리
  const b_3 = Number(inputVal_b[0]);  // 백의 자리

  console.log(a * b_1);
  console.log(a * b_2);
  console.log(a * b_3);
  console.log(a * b);
}
