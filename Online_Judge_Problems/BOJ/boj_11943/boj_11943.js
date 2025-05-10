/*
----------------------------------------------
Sub : [BOJ] 파일 옮기기
Link: https://www.acmicpc.net/problem/11943
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [a, b] = input[0].split(" ").map(Number)
const [c, d] = input[1].split(" ").map(Number)

const result = b+c < a+d ? b+c : a+d

console.log(result)

