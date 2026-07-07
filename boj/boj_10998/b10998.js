// AxB
// https://www.acmicpc.net/problem/10998

const readline = require('readline')

const rl = readline.createInterface ({
  input: process.stdin,
  output: process.stdout
})

let inputData = []

rl.on('line', (line) => {
  inputData.push(line)
})

rl.on('close', () => {
  const [a, b] = inputData[0].split(' ').map(Number)
  const results = a * b
  console.log(results)
})