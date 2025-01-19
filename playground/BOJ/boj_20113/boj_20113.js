/*----------------------------------------------
Sub  : [BOJ] 긴급 회의
Link : https://www.acmicpc.net/problem/20113
Level: B1
Tag  : JS, 구현
Memo
 - 
----------------------------------------------*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

const N = parseInt(input[0]);
const X = input[1].split(" ").map(Number);

const votes = Array(N).fill(0);
let maxVote = 0;
let imposter = 0;
let count = 0;

// 가장 많이 받은 투표수(max_vote)와 그 사람(imposter)을 검색
for (let i = 0; i < N; i++) {
  if (X[i] !== 0) {
    votes[X[i] - 1] += 1;
    if (maxVote < votes[X[i] - 1]) {
      maxVote = votes[X[i] - 1];
      imposter = X[i];
    }
  }
}

// 가장 많이 받은 투표 수 중복수를(count) 체크
for (const vote of votes) {
  if (vote === maxVote) {
    count += 1;
  }
}

// 결과 출력
if (count > 1) {
  console.log("skipped");
} else {
  console.log(imposter);
}
