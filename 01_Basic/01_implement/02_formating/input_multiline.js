/*
---------------------------------------------
A+B -4
---------------------------------------------
link: https://www.acmicpc.net/problem/10951
tag: js, 구현, 입력
memo: 한줄에 여려 번수를 입력받음
---------------------------------------------
*/

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let input = []

rl.on('line', (line) => {
  input.push(line)
})

const getSum = (a, b) => {
  return a + b
}

rl.on('close', () => {
  let results = []
  for (let i in input) {
    const [a, b] = input[i].split(' ').map(Number)
    results.push(getSum(a, b))
  }

  results.forEach(results => console.log(results))
})
