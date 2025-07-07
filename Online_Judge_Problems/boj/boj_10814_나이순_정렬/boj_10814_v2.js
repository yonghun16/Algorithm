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
let arr = [];

// solution
for (let i = 1; i <=N; i++) {
  // 각 사람의 (나이, 이름) 정보를 입력받기
  let age = Number(input[i].split(' ')[0]);
  let name = input[i].split(' ')[1];
  arr.push([age, name]);
}

arr.sort((a, b) => a[0] - b[0]);

// print
let answer = "";
for (let el of arr) {
  answer += el[0] + " " + el[1] + "\n";
}
console.log(answer);
