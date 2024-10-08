// 두 수 비교하기
// https://www.acmicpc.net/problem/1330

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// 두 정수를 비교하고 결과 출력
function compare(a, b) {
  if (a > b) {
    return ">";
  } else if (a < b) {
    return "<";
  } else {
    return "==";
  }
}

rl.question('', (input) => {
  const [a, b] = input.split(' ').map(Number);

  console.log(compare(a, b));

  rl.close();
});
