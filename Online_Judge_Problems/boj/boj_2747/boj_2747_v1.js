/*----------------------------------------------
Sub  : [BOJ] 피보나치 수
Link : https://www.acmicpc.net/problem/2747
Level: Bronz 2
Tag  : JS, 수학, 피보나치, 다이나믹
Memo
 - 
----------------------------------------------*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

const n = parseInt(input);

// fibonacci 함수
function fibonacci(n) {
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    }

    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        let temp = b;
        b = a + b;
        a = temp;
    }
    return b;
}

// n번째 피보나치 수 출력
console.log(fibonacci(n));
