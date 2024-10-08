/*
 * 구름 크기 출력하기
 * 난이도 1
 * https://level.goorm.io/exam/150332/%ED%98%84%EB%8C%80%EB%AA%A8%EB%B9%84%EC%8A%A4-%EB%AA%A8%EC%9D%98%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B5%AC%EB%A6%84-%ED%81%AC%EA%B8%B0-%EC%B8%A1%EC%A0%95%ED%95%98%EA%B8%B0/quiz/1
 */

// Run by Node.js
const readline = require('readline');
const input = [];

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
    input.push(line.trim());
	}
	
  main(input);
	process.exit();
})();

function main(input) {
  const inputNum = input[0].split(" ").map(Number);

  console.log(inputNum[0] * inputNum[1]);
}
