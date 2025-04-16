/* 한 줄씩 입력을 연달아 받아야 할 때는 readline 모듈을 사용. */

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
})

const data = []

rl.on('line', (line) => {
  data.push(line.trim())
})

rl.on('close', () => {
  const input = data[0].split(' ').map(Number)

  console.log(data)
  console.log(input)
});
