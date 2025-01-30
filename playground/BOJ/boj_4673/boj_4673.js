/*----------------------------------------------
Sub  : [BOJ] 셀프 넘버
Link : https://www.acmicpc.net/problem/4673
Level: 실버 5
Tag  : JS, Brute Force
Memo
 - 
----------------------------------------------*/

const allNumberSet = new Set();
for (let i = 1; i < 10000; i++) {
  allNumberSet.add(i);
}

const createNumberSet = new Set();

allNumberSet.forEach(i => {
  let createNumber = i;
  for (const digit of String(i)) {
    createNumber += Number(digit);
  }
  createNumberSet.add(createNumber);
});

const selfNumberSet = [...allNumberSet].filter(num => !createNumberSet.has(num))
selfNumberSet.sort((a, b) => a - b);

// 결과 출력
selfNumberSet.forEach(num => console.log(num));
