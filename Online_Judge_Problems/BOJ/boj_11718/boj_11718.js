/*
----------------------------------------------
Sub  : [BOJ] 그대로 출력하기
Link : https://www.acmicpc.net/problem/11718
Tag  : js, 문자열, 입력
Memo
----------------------------------------------
*/

const fs = require("fs")
let input = fs.readFileSync("/dev/stdin").toString().split("\n")

input.forEach((input) => {
  console.log(input);  // 저장된 줄들을 그대로 출력
});
