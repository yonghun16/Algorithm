/*
----------------------------------------------
Sub : [BOJ] A+B-C
Link: https://www.acmicpc.net/problem/31403
Tag : JS
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

A = input[0]
B = input[1]
C = input[2]

console.log(Number(A) + Number(B) - Number(C))
console.log(Number(A+B) - Number(C))
