/* ----------------------------------------------
Sub : [BOJ] 분해합
Link: https://www.acmicpc.net/problem/2231
Tag : JS, Math, Brute-Force
Memo
---------------------------------------------- */

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

// 입력 변수
const N = Number(input[0]);    // N(1 ≤ N ≤ 1,000,000)

;[cnt, minN] = N, N;
let answer = 0;

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
answer = minN
console.log(answer)
