/** * -----------------------------------------------------------
 * Sub    : [BOJ] 탑
 * Link   : https://www.acmicpc.net/problem/2493
 * Level  : Gold 5
 * Tag    : JS,
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

const fs = require("fs");

const filePath = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";
const input = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

let inputIdx = 0;

// input & init
const getInput = () => {
  const N = parseInt(input[inputIdx++]);
  const towers = input.slice(inputIdx, inputIdx + N).map(Number);

  return { N, towers };
};

// solve
const solve = (N, towers) => {
  // 예외 처리: 입력이 제대로 안 들어왔을 경우 방어 코드
  if (!towers || towers.length === 0) return;

  const stack = [];
  const answer = [];

  for (let i = 0; i < N; i++) {
    const currentHeight = towers[i];

    // 스택이 비어있지 않고, 현재 탑보다 낮은 탑들은 pop
    while (
      stack.length > 0 &&
      towers[stack[stack.length - 1]] < currentHeight
    ) {
      stack.pop();
    }

    // 결과 배열에 수신 탑 번호 기록 (비어있으면 0)
    answer.push(stack.length === 0 ? 0 : stack[stack.length - 1] + 1);

    // 현재 인덱스 푸시
    stack.push(i);
  }

  console.log(answer.join(" "));
};

// 실행
const { N, towers } = getInput();
solve(N, towers);
