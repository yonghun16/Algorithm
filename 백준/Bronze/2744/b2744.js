// 대소문자 바꾸기
// https://www.acmicpc.net/problem/2744

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input) => {
    const swapped = input.split('').map(char => {
        if (char === char.toUpperCase()) {
            return char.toLowerCase();
        } else {
            return char.toUpperCase();
        }
    }).join('');

    console.log(swapped);
    rl.close();
});
