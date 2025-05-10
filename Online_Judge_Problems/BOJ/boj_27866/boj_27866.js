/*
----------------------------------------------
Sub: [BOJ] 27866. 문자와 문자열
Link: https://www.acmicpc.net/problem/27866
Tag: Javascript, 문자열
Memo
- 문자열은 0부터 인덱스 시작
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 문자열 S와 정수 i입력 받기
const S = input[0].trim();
const i = Number(input[1]);

// 결과 출력
console.log(S[i - 1]);
