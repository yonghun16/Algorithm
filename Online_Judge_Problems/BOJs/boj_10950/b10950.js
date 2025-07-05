// A+B -3
// https://www.acmicpc.net/problem/10950

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let input = []

// 두 수를 더하는 함수
function getSum(a, b) {
  return a + b
}

rl.on('line', (line) => {
  input.push(line)
})

rl.on('close', () => {
  const n = parseInt(input[0])
  let answer = []

  for (let i = 1; i <= n; i++) {
    const [a, b] = input[i].split(' ').map(Number)
    answer.push(getSum(a, b))
  }

  answer.forEach(answer => console.log(answer))
})
