/*-----------------------------------------------------
Sub  : [BOJ] 369
Link : https://www.acmicpc.net/problem/17614
Level: 브론즈 3
Tag  : JS, 브루투포스
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

// 입력 변수
N = Number(input[0])

// 출력 변수
answer = 0;

// 369 박수 수 구하기
// 시간복잡도 O(N^2)
// 시간복잡도 O(7N) : 1,000,000 * 7  = 7,000,000
clap = 0;
for(i = 1; i <= N; i++){
  for (j = 0; j < i.toString().length; j++) {
    if(i.toString()[j].includes('3') || i.toString()[j].includes('6') || i.toString()[j].includes('9')) {
      clap++;
    }
  }
}

// 출력
answer = clap
console.log(answer)
