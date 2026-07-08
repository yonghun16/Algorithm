/*----------------------------------------------
Sub  : [BOJ] 피보나치 수 5
Link : https://www.acmicpc.net/problem/10870
Level: 브론즈 2
Tag  : JS, 피보나치, 동적계획
Memo
----------------------------------------------*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

n = Number(input[0])

let [a, b] = [0, 0]

for (let i=0; i<n; i++) {
  if (i === 0){
    [a, b] = [0, 1]
    continue;
  }
  let temp  = b
  b = a+temp
  a = temp
}

console.log(b)
