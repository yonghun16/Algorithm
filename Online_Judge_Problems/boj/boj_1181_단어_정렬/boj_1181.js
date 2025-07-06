/*-----------------------------------------------------
Sub  : [BOJ]  단어 정렬
Link : https://www.acmicpc.net/problem/1181
Level: 실버 5
Tag  : JS, Sort
Memo
-----------------------------------------------------*/

const TEST_MODE = false;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// input
const N = Number(input[0]);
const words = new Set(input.slice(1, N + 1).sort().sort((a, b) => { if (a.length < b.length) return -1 }))

// output
let answer = '';
for (let word of words) {
  answer += word + '\n'
}
console.log(answer)
