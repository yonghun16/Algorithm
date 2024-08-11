const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function factorial(n) {
    let result = BigInt(1);
    for (let i = 2; i <= n; i++) {
        result *= BigInt(i);
    }
    return result;
}

rl.question('', (input) => {
    const N = parseInt(input);
    console.log(factorial(N).toString());
    rl.close();
});
