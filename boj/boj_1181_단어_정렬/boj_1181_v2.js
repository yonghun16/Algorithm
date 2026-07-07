/*-----------------------------------------------------
Sub  : [BOJ]  단어 정렬
Link : https://www.acmicpc.net/problem/1181
Level: 실버 5
Tag  : JS, Sort
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
const N = Number(input[0]);
let arr = input.slice(1, N + 1).sort();

arr = [...new Set(arr)];

// sort
arr.sort((a, b) => {
  if (a.length !== b.length) return a.length - b.length;  
  else {  // 사전 순으로 정렬
      if (a < b) return -1;
      else if (a > b) return 1;
      else return 0
    }
});


// output
for (let x of arr){
  console.log(x)
}

