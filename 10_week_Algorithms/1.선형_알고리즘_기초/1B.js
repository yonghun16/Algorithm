// 문제1B-원소의 합 구하기


const readline = require('readline')

// 입력을 읽기 위한 인터페이스 설정
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

// 입력을 저장할 변수
let input = []

// 각 줄의 입력을 처리
rl.on('line', (line) => {
  input.push(line)
})

// 모든 입력을 받은 후 처리
rl.on('close', () => {
  const n = parseInt(input[0].trim(), 10)
  const inputNumbers = input[1].trim().split(' ').map(Number)
  const answer = getSum(inputNumbers)
  console.log(answer)
})

// 합계를 계산하는 함수
function getSum(inputNumbers) {
  let sum = 0
  for (let num of inputNumbers) {
    sum += num
  }
  return sum
}
