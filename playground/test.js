const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

const inputData = []

rl.on('line', (line) => {
  inputData.push(line.trim())
})

function factorial(n) {
  if (n === 0) {
    return 1
  }
  return n * factorial(n - 1)
}
rl.on('close', () => {
  const n = parseInt(inputData[0])
  inputData[0]
  console.log(factorial(n))
})

