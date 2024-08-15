// 사칙연산

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
  const [a, b] = input[0].split(' ').map(Number)
  console.log(a+b)
  console.log(a-b)
  console.log(a*b)
  console.log(Math.floor(a/b))
  console.log(a%b)
})
