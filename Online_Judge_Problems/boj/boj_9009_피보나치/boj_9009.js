/*-----------------------------------------------------
Sub  : [BOJ] 피보나치
Link : https://www.acmicpc.net/problem/9009
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


// input
const nums = input.slice(1).map(Number);
const answer = [];

/**
 * 최대값 num으로 근접하는 피보나치 수열 반환
 */
const fibonacci = (num) => {
  const sequence = [1, 2];
  while (true) {
    const next = sequence.at(-1) + sequence.at(-2);
    if (next > num) break;
    sequence.push(next);
  }
  return sequence;
};

/**
 * num을 만족하는 최소의 피보나치 원소들을 구합니다.
 *
 * @param {number} num - 피보나치 원소들의 합이 num
 * @returns {Array<number>} 피보나치 원소들의 배열 
 */
const findMinimalFiboSequence = (num) => {
  const fiboSequence = fibonacci(num);
  const results = [];
  const sortedFiboSequence = fiboSequence.sort((a, b) => b - a);
  let current = num;

  for (el of sortedFiboSequence) {
    if (current === 0) {
      break;
    }
    else if (current >= el) {
      current = current - el;
      results.push(el);
    }
  }

  return results;
}


for (const num of nums) {
  answer.push(findMinimalFiboSequence(num).sort((a, b) => a - b).join(' '));
}

console.log(answer.join('\n'));
