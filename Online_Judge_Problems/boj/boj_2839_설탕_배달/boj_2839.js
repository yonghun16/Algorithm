/*-----------------------------------------------------
Sub  : [BOJ] 설탕 배달
Link : https://www.acmicpc.net/problem/2839
Level: 실버 4
Tag  : JS, 그리디
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input2.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// input
const N = input[0];


// solution
function sugarBags(N) {
  let count = 0;
  while (N >= 0) {
    if (N % 5 === 0) {
      count += N / 5;
      return count;
    }
    N -= 3;
    count++;
  }
  return -1;
}


// output
console.log(sugarBags(N));
