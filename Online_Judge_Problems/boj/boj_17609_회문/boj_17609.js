/*-----------------------------------------------------
Sub  : [BOJ] 회문
Link : https://www.acmicpc.net/problem/17609
Level: 골드 5
Tag  : JS, greedy, string
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
} else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}

// input
const N = +input[0];
const words = input.slice(1);

// 좌우 범위로 회문인지 확인
function isPalindromeRange(s, left, right) {
  while (left < right) {
    if (s[left] !== s[right]) return false;
    left++;
    right--;
  }
  return true;
}

function checkPalindrome(s) {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] === s[right]) {
      left++;
      right--;
    } else {
      // 한 글자 삭제 시 회문 가능 여부 확인
      if (isPalindromeRange(s, left + 1, right) || isPalindromeRange(s, left, right - 1)) {
        return 1; // 유사회문
      } else {
        return 2; // 일반 문자열
      }
    }
  }
  return 0; // 회문
}

// 결과 출력
words.forEach(word => console.log(checkPalindrome(word)));
