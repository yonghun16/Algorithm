/*-----------------------------------------------------
Sub  : [BOJ] 요세푸스 문제0
Link : https://www.acmicpc.net/problem/11866
Level: 실버 4
Tag  : JS, Queue
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// 입력
const [N, K] = input[0]

// 풀이 함수
function josephus(N, K) {
    let q = [];
    for (let i = 1; i <= N; i++) q.push(i);

    let result = [];
    let idx = 0;

    while (q.length > 0) {
        idx = (idx + K - 1) % q.length; // K번째 이동
        result.push(q.splice(idx, 1)[0]); // 제거
    }
    return result;
}

// 출력
let result = josephus(N, K);
console.log("<" + result.join(", ") + ">");
