/*
----------------------------------------------
[BOJ] 1448. 삼각형 만들기
----------------------------------------------
Link: https://www.acmicpc.net/problem/1448
Tag: js, greedy, sort
Memo:
  inputData.slice(1).sort((a, b) => b - a);  // 내림차순으로 정렬
----------------------------------------------
*/
 
const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

const inputData = []

rl.on('line', (line) => {
  inputData.push(line.trim())
})

rl.on('close', () => {
  const n = parseInt(inputData[0])
  const sidesOfTriangle = inputData.slice(1).sort((a, b) => b - a);  // 내림차순으로 정렬
  let result = -1

  for (let i = 0; i < n - 2; i++) {
    const a = parseInt(sidesOfTriangle[i])
    const b = parseInt(sidesOfTriangle[i + 1])
    const c = parseInt(sidesOfTriangle[i + 2])

    if (a < b + c) {
      result = a + b + c;
      break;
    }
  }

  console.log(result);
})
