// A+B - 6
// https://www.acmicpc.net/problem/10953

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let input = []

rl.on('line', function (line) {
  input.push(line)
})

const getSum = (a, b) => {
  return a + b
}

rl.on('close', function () {
  const n = parseInt(input[0])
  let results = []

  for (let i = 1; i <= n; i++) {
    const [a, b] = input[i].split(',').map(Number)
    results.push(getSum(a, b))
  }

  results.forEach(result => console.log(result));
})