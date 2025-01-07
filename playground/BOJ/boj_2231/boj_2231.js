/*
----------------------------------------------
Sub : [BOJ] 분해합
Link: https://www.acmicpc.net/problem/2231
Tag : JS, Math
Memo
----------------------------------------------
*/

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])

let [cnt, minN] = [N, N]

// 생성자를 반환하는 함수
const devideSum = (num) => {
  const el = num.toString();
  let elSum = num
  for (let i = 0; i < el.length; i++) {
    elSum += Number(el[i])
  }

  if (elSum === N) return num

  return 0
}

while (cnt > N / 2) {
  cnt -= 1
  let cur = devideSum(cnt)
  if (cur !== 0 && cur < minN) minN = cur
}

// 출력
if (minN === N) console.log(0)
else console.log(minN)
