/*
----------------------------------------------
Sub : [BOJ] 단순한 문제(Small)
Link: https://www.acmicpc.net/problem/25494
Tag : JS, Brute Force. Math
Memo
----------------------------------------------
*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').split('\n')

const match = (a, b, c) => {
  let count = 0
  for (let x=1; x<=a; x++) {
    for (let y=1; y<=b; y++) {
      for (let z=1; z<=c; z++) {
        if (x%y === y%z && z%x === x%y) {
          count++
        }
      }
    }
  }
  return count
}

const n = Number(input[0])

for (let i=1; i<=n; i++) {
  const [a, b, c] = input[i].split(' ').map(Number)
  console.log(match(a, b, c))
}
