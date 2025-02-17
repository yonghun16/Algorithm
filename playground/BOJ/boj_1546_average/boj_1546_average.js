/*-----------------------------------------------------
Sub  : [BOJ] 평균
Link : https://www.acmicpc.net/problem/1546
Level: 브론즈 1
Tag  : JS,
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

// 입력
const n = parseInt(input[0], 10);
const scores = input[1].split(' ').map(Number);

// 최댓값
const maxScore = Math.max(...scores);

// 고친 점수들의 합
const sum_score = scores.reduce((acc, score) => acc + (score / maxScore) * 100, 0);

// 평균
const average_score = sum_score /n

// 출력
console.log(average_score);
