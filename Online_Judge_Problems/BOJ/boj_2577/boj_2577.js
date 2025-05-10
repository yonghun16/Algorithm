/*
----------------------------------------------
Sub : [BOJ] 숫자의 개수
Link: https://www.acmicpc.net/problem/2577
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const A = input[0];
const B = input[1];
const C = input[2];

// A × B × C의 결과 계산
const result = A * B * C;

// 결과를 문자열로 변환
const resultStr = result.toString();

// 0부터 9까지 각 숫자의 빈도 계산 및 출력
for (let i = 0; i <= 9; i++) {
    const count = resultStr.split(i).length - 1; // 숫자 i의 개수를 카운트
    console.log(count);
}
