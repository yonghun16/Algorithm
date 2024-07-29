// N 찍기
// https://www.acmicpc.net/problem/2741

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let input = []

rl.on('line', (line) => {
  input.push(line)
})

rl.on('close', () => {
  const n = parseInt(input[0], 10)

  for (let i = 1; i <= n; i++) {
    console.log(i)
  }
})
