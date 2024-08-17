const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

const inputData = []

rl.on('line', (line) => {
  inputData.push(line.trim())
})

rl.on('close', () => {
  const x = parseInt(inputData[0])
  const y = parseInt(inputData[1])

  if ( x > 0 && y > 0) {
    console.log("1")
  }
  else if ( x < 0 && y > 0) {
    console.log("2")
  }
  else if ( x < 0 && y < 0) {
    console.log("3")
  }
  else console.log("4")
})

