/*----------------------------------------------
Sub  : [BOJ] 피보나치 수
Link : https://www.acmicpc.net/problem/4150
Level: 브론즈 1
Tag  : JS, 피보나치, 동적계획
Memo
 -  BigInt 사용
----------------------------------------------*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

const n = Number(input);

// 피보나치 수열 계산 함수 (BigInt 사용)
function fibonacciBigInt(n) {
  if (n === 1 || n === 2) return BigInt(1); // f(1)과 f(2)는 1
  
  let a = BigInt(1);
  let b = BigInt(1);
  
  for (let i = 3; i <= n; i++) {
    const temp = a + b; // 이전 두 항의 합
    a = b;
    b = temp;
  }
  
  return b;
}

// 결과 출력
console.log(fibonacciBigInt(n).toString());
