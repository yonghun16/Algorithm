/** * -----------------------------------------------------------
 * Sub    : [BOJ] 탑
 * Link   : https://www.acmicpc.net/problem/2493
 * Level  : Gold 5
 * Tag    : TS, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

import * as fs from "fs";

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

let inputIdx: number = 0;

interface InputData {
  N: number;
  towers: number[];
}

// input & init
const getInput = (): InputData => {
  const N: number = parseInt(input[inputIdx++]);
  const towers: number[] = input.slice(inputIdx, inputIdx + N).map(Number);
  return { N, towers };
};

// solve
const solve = (N: number, towers: number[]): void => {
  if (!towers || towers.length === 0) return;

  // 인덱스를 저장하는 스택
  const stack: number[] = [];
  const answer: number[] = [];

  for (let i = 0; i < N; i++) {
    const currentHeight: number = towers[i];

    while (
      stack.length > 0 &&
      towers[stack[stack.length - 1]] < currentHeight
    ) {
      stack.pop();
    }

    // 스택이 비어있으면 수신할 탑이 없음(0), 있다면 top의 인덱스+1 저장
    if (stack.length === 0) {
      answer.push(0);
    } else {
      answer.push(stack[stack.length - 1] + 1);
    }

    stack.push(i);
  }

  console.log(answer.join(" "));
};

// main
const { N, towers }: InputData = getInput();
solve(N, towers);
