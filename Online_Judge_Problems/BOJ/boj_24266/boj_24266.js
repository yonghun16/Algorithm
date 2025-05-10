/*-----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행시간 5
Link : https://www.acmicpc.net/problem/24266
Level: 브론즈3
Tag  : JS, BigO
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const n = BigInt(input[0]);
const answer = n * n * n;

console.log(answer.toString());
console.log(3);
