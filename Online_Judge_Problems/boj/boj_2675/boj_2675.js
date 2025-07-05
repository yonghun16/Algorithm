/*
----------------------------------------------
Sub : [BOJ] 문자열 반복
Link: https://www.acmicpc.net/problem/2675
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 첫 번째 줄은 테스트 케이스 개수
const T = parseInt(input[0]);

// 각 테스트 케이스 처리
for (let i = 1; i <= T; i++) {
    // 각 줄에서 R과 S를 분리
    let [R, S] = input[i].split(' ');
    R = parseInt(R);
    
    // 문자열 P 생성
    let P = '';
    for (let char of S) {
        P += char.repeat(R);
    }
    
    // 결과 출력
    console.log(P);
}
