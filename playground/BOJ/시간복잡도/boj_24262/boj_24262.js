/*-----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행시간 1
Link : https://www.acmicpc.net/problem/24262
Level: 브론즈 5
Tag  : JS, BigO
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const n = Number(input[0]);
const A = Array(n).fill(0).map(() => Math.floor(Math.random() * 10));

/* 
MenOfPassion(A[], n) {
  i = ⌊n / 2⌋;
  return A[i]; # 코드1
}
*/

function MenOfPassion(A, n) {
  let count = 0;
  const i = Math.floor(n / 2);
  //return arr[i];
  count += 1;

  return count;
}
const resultCount = MenOfPassion(A, n);


// 결과출력
// 시간복잡도 -> O(1)
console.log(resultCount);   // 상수 시간
console.log(0);             // O(1)의 차수 -> 0
