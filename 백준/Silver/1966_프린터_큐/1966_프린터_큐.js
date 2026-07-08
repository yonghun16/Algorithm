/*-----------------------------------------------------
Sub  : [BOJ] 프린터 큐
Link : https://www.acmicpc.net/problem/1966
Level: 실버 3
Tag  : JS, queue
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

// -- input --
const T = Number(input[0]);

// -- process --
let count = 0;
for (let i = 0; i < T; i++) {
  let [N, M] = input[++count].split(" ").map(Number);
  let priorities = input[++count].split(" ").map(Number);

  // 큐: [문서 인덱스, 중요도]
  let queue = priorities.map((p, idx) => [idx, p]);

  let order = 0;

  while (queue.length > 0) {
    let current = queue.shift(); // 맨 앞 문서 꺼냄

    // 뒤에 더 높은 중요도가 있는지 확인
    if (queue.some(([_, p]) => p > current[1])) {
      queue.push(current); // 뒤로 보냄
    } else {
      order++; // 출력됨
      if (current[0] === M) {
        console.log(order);
        break;
      }
    }
  }
}
