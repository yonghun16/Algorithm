/*-----------------------------------------------------
Sub  : [BOJ] 최소, 최대
Link : https://www.acmicpc.net/problem/10818
Level: 브론즈 5
Tag  : JS, 
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

let data = input[1].split(' ').map(x => Number(x));

let minValue = data.reduce((a, b) => Math.min(a, b));
let maxValue = data.reduce((a, b) => Math.max(a, b));

console.log(minValue + ' ' + maxValue);
