/*----------------------------------------------
Sub  : [BOJ] 블랙잭
Link : https://www.acmicpc.net/problem/2798
Level: Bronze 2
Tag  : JS, 브루트포스
Memo
 - 
----------------------------------------------*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

// 입력 받기
const [N, M] = input[0].split(" ").map(Number);
const cards = input[1].split(" ").map(Number);

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
console.log(blackjack(N, M, cards));
