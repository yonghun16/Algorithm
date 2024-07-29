// N 찍기
// https://www.acmicpc.net/problem/2741

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let result = []

rl.on('line', (input) => {
    const n = parseInt(input.trim(), 10);

    for (let i = 1; i <= n; i++) {
      result.push(i)
    }

});

rl.on('close', () => {
    for (let i = 0; i < result.length; i++) {
      console.log(result[i])
    }
})
