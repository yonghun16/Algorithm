// 단어 길이 재기
// https://www.acmicpc.net/problem/2743

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
  const lengthOfWord = input[0].length
  const result = lengthOfWord

  console.log(result)
})