// A-B -8
// https://www.acmicpc.net/problem/11022

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
  const t = Number(input[0])

  for (let i = 1; i <= t; i++) {
    const [a, b] = input[i].split(' ').map(Number)
    console.log(`Case #${i}: ${a} + ${b} = ${a + b}`)
  }
})


