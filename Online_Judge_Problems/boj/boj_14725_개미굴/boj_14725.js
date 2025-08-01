/*-----------------------------------------------------
Sub  : [BOJ] 개미굴
Link : https://www.acmicpc.net/problem/14725
Level: 골드 3
Tag  : JS, 자료구조, 집합, 트라이
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

const N = Number(input[0]);

// 루트 노드: 최상위 Map
const root = new Map();

// 경로 삽입 함수
function insert(path) {
  let current = root;
  for (const food of path) {
    if (!current.has(food)) {
      current.set(food, new Map());
    }
    current = current.get(food);
  }
}

// 출력 함수 (DFS)
function print(node, depth) {
  const sortedKeys = [...node.keys()].sort();
  for (const key of sortedKeys) {
    console.log('--'.repeat(depth) + key);
    print(node.get(key), depth + 1);
  }
}

// 입력 처리 및 트라이 구축
for (let i = 1; i <= N; i++) {
  const [k, ...foods] = input[i].trim().split(' ');
  insert(foods);
}

// 결과 출력
print(root, 0);
