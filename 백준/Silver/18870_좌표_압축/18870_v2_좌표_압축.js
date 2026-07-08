/*-----------------------------------------------------
Sub  : [BOJ] 좌표 압축
Link : https://www.acmicpc.net/problem/18870
Level: 실버 2
Tag  : JS, Array, Sort
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input1.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


/* input */
const arr = input[1].split(' ').map(Number);


/* solution */
const uniqueArray = [...new Set(arr)]; // 집합으로 변경해 중복 값을 없앤 뒤 다시 배열로 변환
uniqueArray.sort((a, b) => a - b);     // 오름차순 정렬

const myMap = new Map();
for (let i=0; i< uniqueArray.length; i++) {  // 0부터 차례대로 매핑 수행
  myMap.set(uniqueArray[i], i);
}


/* output */
let answer = '';
arr.forEach(el => {
  answer += myMap.get(el) + " ";
});

console.log(answer)
