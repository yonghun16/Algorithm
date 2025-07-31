/*-----------------------------------------------------
Sub  : [BOJ] 주유소
Link : https://www.acmicpc.net/problem/13305
Level: 실버 3
Tag  : JS, greedy
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input1.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
} else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}

const N = Number(input[0]);
const distances = input[1].split(' ').map(BigInt); // N-1개
const prices = input[2].split(' ').map(BigInt);    // N개

// Map 구성
const distanceMap = new Map();
const priceMap = new Map();

for (let i = 0; i < N - 1; i++) {
  distanceMap.set(i, distances[i]);
  priceMap.set(i, prices[i]);
}
priceMap.set(N - 1, prices[N - 1]); // 마지막 도시의 가격도 저장

// 로직
let totalCost = 0n;
let minPrice = priceMap.get(0);

for (let i = 0; i < N - 1; i++) {
  const dist = distanceMap.get(i);
  const price = priceMap.get(i);

  // 지금까지의 최소 가격으로 이동
  minPrice = price < minPrice ? price : minPrice;
  totalCost += minPrice * dist;
}

console.log(totalCost.toString()); // BigInt 출력 시 문자열로 변환
