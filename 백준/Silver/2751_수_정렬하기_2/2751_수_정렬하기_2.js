/*-----------------------------------------------------
Sub  : [BOJ] 수 정렬하기 2
Link : https://www.acmicpc.net/problem/2751
Level: 실버 5
Tag  : JS, sort
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
// const filePath = require('path').join(__dirname, 'input1.txt');
// const input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');

const N = Number(input[0]);
const arr = input.slice(1).map(Number);


const mergeSort = (arr) => {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
};

const merge = (left, right) => {
  const result = [];

  let leftIdx = 0;
  let rightIdx = 0;

  while (leftIdx < left.length && rightIdx < right.length) {
    if (left[leftIdx] < right[rightIdx]) {
      result.push(left[leftIdx++]);
    } else {
      result.push(right[rightIdx++]);
    }
  }

  return result.concat(left.slice(leftIdx)).concat(right.slice(rightIdx));
};

const sorted = mergeSort(arr);
console.log(sorted.join('\n'));
