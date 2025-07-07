/*-----------------------------------------------------
Sub  : [BOJ] 나이순 정렬
Link : https://www.acmicpc.net/problem/
Level: 실버 5
Tag  : JS, 정렬, 집합, 맵
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

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
const arr = input.slice(1, N+1).map(v => v.split(' ')).sort((a, b) => a[0] - b[0]);

// solution
const myMap = new Map();

for (let i = 0; i < N; i++) {
  const [age, name] = arr[i];
  myMap.set(age, [...myMap.get(age) || [], name]);
}

// output
let answer = '';
for (let [age, names] of myMap.entries()) {
  for (let name of names) {
    answer += `${age} ${name}\n`;
  }
}

console.log(answer);
