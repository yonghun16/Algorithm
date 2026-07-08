/*-----------------------------------------------------
Sub  : [BOJ] 회의실 배정
Link : https://www.acmicpc.net/problem/1931
Level: 골드 5
Tag  : JS, greddy
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


//input
const N = Number(input[0]);
const roomTimes = input.slice(1).map(line => line.trim().split(' ').map(Number));


// processing
roomTimes.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];  // 종료 시간 같으면 시작 시간 오름차순
  return a[1] - b[1];
});

let answer = 0;
let currentEnd = 0;

for (let i = 0; i < N; i++) {
  const [start, end] = roomTimes[i];
  if (start >= currentEnd) {
    answer++;
    currentEnd = end;
  }
}

console.log(answer);
