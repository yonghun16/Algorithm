/*
----------------------------------------------
Sub : [BOJ] 스물셋
Link: https://www.acmicpc.net/problem/23251
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')


T = Number(input[0])

for (i = 1; i < T+1; i++) {
  k = Number(input[i])
  console.log(k*23)
}
