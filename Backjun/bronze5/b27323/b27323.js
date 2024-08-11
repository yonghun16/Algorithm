// 직사각형
// https://www.acmicpc.net/problem/27323

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let input = []

rl.on('line', (line) => {
  input.push(line)
})

rl.on('close', () => {
  const a = input[0].split(' ').map(Number)
  const b = input[1].split(' ').map(Number)

  const result = a * b

  console.log(result)
})
