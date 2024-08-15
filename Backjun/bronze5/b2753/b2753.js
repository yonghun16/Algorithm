// 윤년

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
  const year = parseInt(input[0])
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        console.log("1")
    }
    else {
        console.log("0")
    }
})
