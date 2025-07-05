// A+B-2
// https://www.acmicpc.net/problem/2558

const readline = require('readline')

// readline 인터페이스 생성
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let input = []

// 두 수를 더하는 함수
const getSum = (a, b) => {
  return a + b
}

rl.on('line', (line) => {
  input.push(parseInt(line))
  if (input.length === 2) rl.close()
})

rl.on("close", () => {
  const a = input[0]
  const b = input[1]
  const answer = getSum(a, b)

  console.log(answer)
})
