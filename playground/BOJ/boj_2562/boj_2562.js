/*
----------------------------------------------
Sub : [BOJ] 최댓값
Link: https://www.acmicpc.net/problem/2562
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');


let numbers = [];

// 9개의 숫자를 입력받음
for (let i = 0; i < 9; i++) {
  numbers.push(Number(input[i]));
}

const maxValue = Math.max(...numbers);
const maxIndex = numbers.indexOf(maxValue) + 1;

// 결과 출력
console.log(maxValue);
console.log(maxIndex);


