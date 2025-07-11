/*-----------------------------------------------------
Sub  : [BOJ] 신입 사원
Link : https://www.acmicpc.net/problem/1946
Level: 실버 1
Tag  : JS, greedy
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

// solution
const sol = (applicants) => {
  let count = 1;
  let minInterview = applicants[0][1];

  for (let i = 1; i < applicants.length; i++) {
    if (applicants[i][1] < minInterview) {
      count++;
      minInterview = applicants[i][1];
    }
  }

  return count;
};


// input
const T = Number(input[0]);
let idx = 1;

for (let t = 0; t < T; t++) {
  let N = Number(input[idx++]);
  let applicants = [];

  for (let i = 0; i < N; i++) {
    const [doc, interview] = input[idx++].split(' ').map(Number);
    applicants.push([doc, interview]);
  }

  applicants.sort((a, b) => a[0] - b[0]);

  // solution
  const count = sol(applicants);

  // output
  console.log(count);
}


