// 검증수
// https://www.acmicpc.net/problem/2475

const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

// 검증수를 구하는 함수
function getVerification(a, b, c, d, e) {
  return (a * a + b * b + c * c + d * d + e * e) % 10
}

rl.question("", (input) => {
  const [a, b, c, d, e] = input.split(" ").map(Number)
  const answer = getVerification(a, b, c, d, e)
  console.log(answer)
  rl.close()
})
