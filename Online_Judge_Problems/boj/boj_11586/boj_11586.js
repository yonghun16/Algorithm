/*-----------------------------------------------------
Sub  : [BOJ] 지영 공주님의 마법 거울
Link : https://www.acmicpc.net/problem/11586
Level: 브론즈 3
Tag  : JS, String 
  -  result = mirror.map(row => row.split('').reverse().join(''));
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const mirror = []
let result = []

// 입력
const N = Number(input[0]);

for (let i = 0; i < N; i++) {
  mirror.push(input[i + 1]);
}

const K = Number(input[N + 1]);

// K 값에 따른 변환
if (K === 1) {
  result = mirror;
}
else if (K === 2) {
  result = mirror.map(row => row.split('').reverse().join(''));
}
else if (K === 3) {
  result = mirror.reverse();
}

// 출력
console.log(result.join("\n"));
