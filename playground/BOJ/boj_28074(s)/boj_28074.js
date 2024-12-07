/*
----------------------------------------------
Sub : [BOJ] 모비스
Link: https://www.acmicpc.net/problem/28074
Tag : JS, String
Memo
----------------------------------------------
*/

const fs = require('fs');

const input = fs.readFileSync('/dev/stdin', 'utf8').toString().trim();

function canFormMobis(string) {
    const requiredChars = "MOBIS";
    for (const char of requiredChars) {
        if (!string.includes(char)) {
            return "NO";
        }
    }
    return "YES";
}

// 결과 출력
console.log(canFormMobis(input));

