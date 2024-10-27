/*
----------------------------------------------
Sub : [BOJ] 최소, 최대
Link: https://www.acmicpc.net/problem/10818
Tag : JS, math
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const arr = input[1].split(' ').map(Number);

console.log(Math.min(...arr) + ' ' + Math.max(...arr));
