/*-----------------------------------------------------
Sub  : [BOJ] 가희와 방어율 무시
Link : https://www.acmicpc.net/problem/25238
Level: 브론즈 4
Tag  : JS, 사칙연산
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const getEffectiveDefence = (a, b) => {
  return a * (100 - b) / 100;
}

// 입력 받기
const [a, b] = input[0].split(' ').map(Number)

// 출력하기
console.log(getEffectiveDefence(a, b) < 100 ? 1 : 0)
