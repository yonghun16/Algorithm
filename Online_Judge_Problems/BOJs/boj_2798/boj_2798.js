/*----------------------------------------------
Sub  : [BOJ] 블랙잭
Link : https://www.acmicpc.net/problem/2798
Level: Bronze 2
Tag  : JS, 브루트포스
Memo
 - 조합(콤비네이션)
   n개의 카드 중에서 3개를 뽑는 조합으로 문제 풀이
----------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n')

// 입력 받기
const [N, M] = input[0].split(" ").map(Number);     //  3 <= N <= 100,   10 <= M <= 300,000
const cards = input[1].split(" ").map(Number);  

// 출력 변수
answer = 0;

// 블랙잭 카드 3장 선택
// 시간복잡도 : O(N^3)          -> 100^3 = 1,000,000
//              n(n-1)(n-2)/6   -> 100*99*98/6 = 161,700
function blackjack(N, M, cards) {
  let maxSum = 0;

  // 3중 for문으로 카드 3장을 선택
  for (let i = 0; i < N-2; i++) {                           // 첫 번째 카드 뽑기
    for (let j = i + 1; j < N-1; j++) {                     // 두 번째 카드 뽑기
      for (let k = j + 1; k < N; k++) {                     // 세 번재 카드 뽑기
        const currentSum = cards[i] + cards[j] + cards[k];  // 카드 3개 숫자 다 더하기
        if (currentSum <= M) {                              // 카드 합이 M보다 같거나 작은 수에 한에서
          maxSum = Math.max(maxSum, currentSum);            // 이전의 카드합과, 지금의 카드합 중 더 큰 것을 maxSum에 갱신
        }
      }
    }
  }

  return maxSum;                                            // 최종 maxSum을 반환
}

// 결과 출력
answer = blackjack(N, M, cards);
console.log(answer);
