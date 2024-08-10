// 킹, 퀸, 룩, 비숍, 나이트, 폰
// https://www.acmicpc.net/problem/3003

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
    let pieces_of_input = []
    let pieces_of_right = [1, 1, 2, 2, 2, 8]
    let results = []

    pieces_of_input = input[0].split(' ').map(Number)

    for (let i = 0; i < 6; i++) {
        results.push(pieces_of_right[i] - pieces_of_input[i])
    }

    console.log(results.join(" "));
})