/*-----------------------------------------------------
Sub  : [BOJ] 숫자의 합.
Link : https://www.acmicpc.net/problem/11720
Level: 브론즈 4
Tag  : JS, 수학 구현 문자열
Memo
 - arr.reduce(callbackFn, initialValue)
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
// const filePath = require('path').join(__dirname, 'input.txt');
// const input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');

const numbers = input[1].split('');

const result = numbers.reduce((sum, number) => sum + Number(number), 0);
console.log(result)
