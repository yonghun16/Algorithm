/*
----------------------------------------------
Sub : [BOJ] 체육은 코딩과목 입니다.
Link: https://www.acmicpc.net/problem/
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let result = 0

for (let i=0; i<10; i++) {
  let n = Number(input[i])
  result += n
  if (result > 3) {
    result -= 4
  }
}

if (result === 0) result = 'N'
else if (result === 1) result = 'E'
else if (result === 2) result = 'S'
else if (result === 3) result = 'W'

console.log(result)
