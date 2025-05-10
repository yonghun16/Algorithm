/*
----------------------------------------------
Sub : [BOJ] 문자열
Link: https://www.acmicpc.net/problem/9086
Tag : js, 문자열
Memo
----------------------------------------------
*/

// fs모듈을 통한 입력
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 테스트 케이스의 개수 입력
const T = Number(input[0]);
// 문자열 배열 선언
let s = [];

for (let i=1; i<=T; i++) {
  s.push(input[i])
}
for (let i=0; i<T; i++) {
  // 첫 글자와 마지막 글자를 추출하여 출력
  console.log(s[i][0] + s[i][s[i].length -1])
}
