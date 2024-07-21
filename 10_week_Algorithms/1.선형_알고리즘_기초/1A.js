// 두 수 비교하기

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

function getMax(a, b) {
  if (a > b) {
    return a
  } else {
    return b
  }
}

rl.question('', (input) => {
  const [a, b] = input.split(' ').map(Number)
  answer = getMax(a, b)

  console.log(answer)

  rl.close()
})
