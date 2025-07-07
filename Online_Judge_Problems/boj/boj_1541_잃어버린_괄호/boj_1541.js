/*-----------------------------------------------------
Sub  : [BOJ] 잃어버린 괄호
Link : https://www.acmicpc.net/problem/1541
Level: 실버 2
Tag  : JS, 그리디
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input4.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// input
const expression = input[0].split("-");

// solution
let answer = [];

for (let el of expression) {
  let num = [...el.split("+").map(Number)].reduce((acc, cur) => acc += cur)
  answer.push(-(num));
}

answer[0] *= -1


// output
const output = answer.reduce((acc, cur) => acc += cur)
console.log(output)

