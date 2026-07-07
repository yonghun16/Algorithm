/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 6174
 * Link   : https://www.acmicpc.net/problem/9047
 * Level  : Silver 5
 * Tag    : TS, Math
 * ------------------------------------------------------------
 */

import * as fs from "fs";
import * as path from "path";

let input: string[];

if (process.platform === "linux") {
  input = fs.readFileSync(process.stdin.fd, "utf-8").trim().split("\n");
} else {
  const filePath: string = path.join(__dirname, "input.txt");
  input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
}

/**
 * 카프리카 연산 함수
 * @param n 현재 숫자 (number 또는 string)
 * @returns 연산 결과 (number)
 */
function getKaprekar(n: number | string): number {
  const digits: string[] = n.toString().padStart(4, "0").split("");

  const big: number = parseInt(
    [...digits].sort((a, b) => b.localeCompare(a)).join(""),
  );
  const small: number = parseInt(
    [...digits].sort((a, b) => a.localeCompare(b)).join(""),
  );

  return big - small;
}

function solve(): void {
  // variable
  const KAPREKAR_CONSTANT: number = 6174;
  const result: number[] = [];

  // input
  const n: number = parseInt(input[0]);
  const nums: string[] = [];

  for (let i = 1; i <= n; i++) {
    nums.push(input[i].trim());
  }

  // logic
  for (const num of nums) {
    let count: number = 0;
    let current: number = parseInt(num);

    while (current !== KAPREKAR_CONSTANT) {
      current = getKaprekar(current);
      count++;
    }

    result.push(count);
  }

  // output
  console.log(result.join("\n"));
}

solve();
