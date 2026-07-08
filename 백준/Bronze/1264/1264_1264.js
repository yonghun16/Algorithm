/*
----------------------------------------------
Sub : [BOJ] 모음의 개수
Link: https://www.acmicpc.net/problem/1264
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');

// 입력 파일 읽기
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 모음 목록
const vowels = 'aeiouAEIOU';

// 모음 개수 세는 함수
function countVowels(line) {
    let count = 0;
    for (let char of line) {
        if (vowels.includes(char)) {
            count++;
        }
    }
    return count;
}

// 각 줄마다 모음 개수 세기
input.forEach(line => {
    if (line === '#') return;
    console.log(countVowels(line));
});
