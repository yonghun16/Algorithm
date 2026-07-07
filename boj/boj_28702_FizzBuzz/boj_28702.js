/*-----------------------------------------------------
Sub  : [BOJ] FizzBuzz
Link : https://www.acmicpc.net/problem/28702  
Level: 브론즈 1
Tag  : JS, 문자열
Memo
-----------------------------------------------------*/

const TEST_MODE = false;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


function fizzBuzz(n) {
  if (n % 15 === 0) return 'FizzBuzz';
  if (n % 3 === 0) return 'Fizz';
  if (n % 5 === 0) return 'Buzz';
  return n.toString();
}

// 주어진 세 문자열 중 숫자가 있는 위치를 찾아서 시작 인덱스를 추정
function getStartIndex(input) {
  for (let i = 0; i < 3; i++) {
    const val = input[i];
    if (!isNaN(Number(val))) {
      // input[i]가 실제로 숫자라면 i번째 숫자는 val이므로
      return Number(val) - i;
    }
  }
  // 만약 숫자가 없다면 브루트포스 탐색
  return findByBruteForce(input);
}

function findByBruteForce(input) {
  for (let i = 1; i <= 100000; i++) {
    if (
      fizzBuzz(i) === input[0] &&
      fizzBuzz(i + 1) === input[1] &&
      fizzBuzz(i + 2) === input[2]
    ) {
      return i;
    }
  }
  return -1;
}

const start = getStartIndex(input);
console.log(fizzBuzz(start + 3));
