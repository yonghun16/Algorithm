/*-----------------------------------------------------
Sub  : [BOJ] 달팽이는 올라가고 싶다
Link : https://www.acmicpc.net/problem/2869
Level: 브론즈 1
Tag  : JS, 수학
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const [A, B, V] = input[0].split(' ').map(Number);

const day = Math.ceil((V - B) / (A - B));

console.log(day);
