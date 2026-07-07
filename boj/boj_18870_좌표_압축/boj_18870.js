/*-----------------------------------------------------
Sub  : [BOJ] 좌표 압축
Link : https://www.acmicpc.net/problem/18870
Level: 실버 2
Tag  : JS, Array, Sort
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input1.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


/* input */
const arr = input[1].split(' ').map(Number);


/* solution */
const sorted = [...arr].sort((a, b) => a - b);
const map = new Map();

let num = 0
map.set(sorted[0], num);

for (let i = 1; i < sorted.length; i++) {
  if(sorted[i-1] !== sorted[i]) {
    map.set(sorted[i], ++num)
  } else {
    map.set(sorted[i], num)
  }
}


/* output */
let answer = '';
arr.forEach(el => {
  answer += map.get(el) + " ";
});

console.log(answer)
