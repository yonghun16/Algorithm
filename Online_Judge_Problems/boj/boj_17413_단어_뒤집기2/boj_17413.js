/** * -----------------------------------------------------------
 * Sub    : [BOJ] 단어 뒤집기 2
 * Link   : https://www.acmicpc.net/problem/17413
 * Level  : Silver 3
 * Tag    : JS, String, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

const fs = require("fs");
const path = require("path");

const filePath = path.join(process.cwd(), "input_test.txt");
const input = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8")
  : fs.readFileSync(0, "utf8");

let inputIdx = 0;

// init
let stack = [];
let result = [];
let isTag = false;

// solve
while (inputIdx < input.length) {
  let char = input[inputIdx];

  // 개행 문자를 만나면 종료 (백준/입력 환경 대응)
  if (char === "\n" || char === "\r") break;

  if (char === "<") {
    // 1. 태그 시작 전, 스택에 쌓인 일반 단어들을 모두 뒤집어서 결과에 추가
    while (stack.length > 0) {
      result.push(stack.pop());
    }
    isTag = true;
    result.push(char); // '<' 추가
  } else if (char === ">") {
    // 2. 태그 종료
    isTag = false;
    result.push(char); // '>' 추가
  } else if (isTag) {
    // 3. 태그 내부: 뒤집지 않고 그대로 결과에 추가
    result.push(char);
  } else {
    // 4. 태그 밖 (일반 문자/공백)
    if (char === " ") {
      // 공백을 만나면 그 앞의 단어를 뒤집어서 추가
      while (stack.length > 0) {
        result.push(stack.pop());
      }
      result.push(char); // 공백 본인 추가
    } else {
      // 일반 문자면 스택에 쌓기 (나중에 거꾸로 꺼내기 위함)
      stack.push(char);
    }
  }
  inputIdx++;
}

// 루프가 끝난 후 스택에 남아있는 마지막 단어 처리
while (stack.length > 0) {
  result.push(stack.pop());
}

// print
process.stdout.write(result.join("") + "\n");
