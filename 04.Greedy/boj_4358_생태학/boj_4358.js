/*-----------------------------------------------------
Sub  : [BOJ] 생태학
Link : https://www.acmicpc.net/problem/4358
Level: 실버 2
Tag  : JS, Map
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



/*----------------------------------
      front-end Data handling 
-----------------------------------*/
const trees = input
const totalTrees = trees.length;

const treeMap = new Map();

for (const tree of trees) {
  if (treeMap.has(tree)) {
    treeMap.set(tree, treeMap.get(tree) + 1);  // 이미 키가 존재하면, 기존 값에 1을 더해 다시 저장
  } else {
    treeMap.set(tree, 1);   // 키가 존재하지 않으면, 1로 새로 추가
  }
}

// Map -> Object
const treeObject = Object.fromEntries(treeMap);

// 전송할 데이터 셋팅
const data = [
  { "Total Trees": totalTrees },
  treeObject
]

// Array[Object] -> JSON
const dataJSON = JSON.stringify(data, null, 2);
// console.log("전송할 데이터", dataJSON);



/*----------------------------------
      back-end Data handling 
-----------------------------------*/

// JSON -> Array[Object]
const receivedData = JSON.parse(dataJSON);
// console.log("전송받은 데이터", receivedData);

const totalTreesBackend = receivedData[0]["Total Trees"];
const treeMapBackend = new Map(Object.entries(receivedData[1]));

// 나무 이름만 정렬
const sortedTreeNames = Array.from(treeMapBackend.keys()).sort();

const result = [];
for (const name of sortedTreeNames) {
  const count = treeMapBackend.get(name);
  const percentage = ((count / totalTreesBackend) * 100).toFixed(4);

  result.push(`${name} ${percentage}`);
}

console.log(result.join('\n'));
