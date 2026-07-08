/*
----------------------------------------------
Sub : [BOJ] 특별한 가지
Link: https://www.acmicpc.net/problem/31668
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = Number(inputData[0]);
const M = Number(inputData[1]);
const K = Number(inputData[2]);

result = M/N * K;

console.log(result)
