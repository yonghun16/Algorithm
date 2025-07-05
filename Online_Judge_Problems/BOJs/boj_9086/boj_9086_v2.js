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

for (let i=1; i<=T; i++) {
  let s = input[i]
  console.log(s[0] + s[s.length -1])
}
