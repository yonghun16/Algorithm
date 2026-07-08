// A+B -5
// https://www.acmicpc.net/problem/10952

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
    if (a !== 0 && b !== 0 ){
      results.push(getSum(a, b))
    }
  }

  results.forEach(results => console.log(results))
})
