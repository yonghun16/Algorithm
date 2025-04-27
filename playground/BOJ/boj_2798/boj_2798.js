/*----------------------------------------------
Sub  : [BOJ] 블랙잭
Link : https://www.acmicpc.net/problem/2798
Level: Bronze 2
Tag  : JS, 브루트포스
Memo
 - 
----------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n')

// 입력 받기
const [N, M] = input[0].split(" ").map(Number);     //  3 <= N <= 100
const cards = input[1].split(" ").map(Number);      // 10 <= M <= 300,000

// 출력 변수
answer = 0;

// 블랙잭 카드 3장 선택
// 시간복잡도 : O(N^3)          -> 100^3 = 1,000,000
//              n(n-1)(n-2)/6   -> 100*99*98/6 = 161,700
function blackjack(N, M, cards) {
  let maxSum = 0;

  // 3중 for문으로 카드 3장을 선택
  for (let i = 0; i < N-2; i++) {
    for (let j = i + 1; j < N-1; j++) {
      for (let k = j + 1; k < N; k++) {
        const currentSum = cards[i] + cards[j] + cards[k];
        if (currentSum <= M) {
          maxSum = Math.max(maxSum, currentSum);
        }
      }
    }
  }

  return maxSum;
}

// 결과 출력
answer = blackjack(N, M, cards);
console.log(answer);
