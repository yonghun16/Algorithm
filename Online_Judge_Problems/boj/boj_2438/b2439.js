// 별 찍기 - 1
// https://www.acmicpc.net/problem/2438

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

// 별을 출력하는 함수
const printStar = (n) => {
  for (let i = 1; i <= n; i++) {
    console.log('*'.repeat(i))
  }
}

rl.question('', (input) => {
  const n = parseInt(input.trim())
  printStar(n)
  rl.close()
})
