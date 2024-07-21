/* 주사위 세개 */
/* https://www.acmicpc.net/problem/2480 */ 

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let [a, b, c] = inputData[0].split(' ').map(Number);

if (a===b && b===c) {
  console.log(a*1000 + 10000);
}
else if (a===b) console.log(a*100 + 1000);
else if (a===c) console.log(a*100 + 1000);
else if (b===c) console.log(b*100 + 1000);
else console.log(Math.max(a,b,c)*100);
