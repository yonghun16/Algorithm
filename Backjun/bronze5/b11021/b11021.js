// AxB -7
// https://www.acmicpc.net/problem/11021

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
  const t = parseInt(input[0], 10);
  let results = []

  for (let i=1; i<=t; i++) {
    const [a, b] = input[i].split(' ').map(Number)
    results.push(a + b)
  }

  for (let i in results) {
    console.log(`Case #${parseInt(i)+1}: ${results[i]}`);
  }
})
