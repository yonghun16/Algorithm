/** -----------------------------------------------------------
 * Sub    : [JOL] 연필 공장
 * Link   : https://jungol.co.kr/problem/5545
 * Level  : Silver 5
 * Tag    : TS, Math
 * ------------------------------------------------------------
 * Approach
 *
 * ------------------------------------------------------------
 */

declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\n+/);

/* 📥 Input */
const getInputData = (): [number, number, number] => {
  let idx: number = 0;
  const [p, v, k]: number[] = input[idx].split(" ").map(Number);

  return [p, v, k];
};

/* ⚙️ Logic */
const gcd = (a: number, b: number): number => (b === 0 ? a : gcd(b, a % b));

/* ⚙️ Logic */
const solution = (data: ReturnType<typeof getInputData>) => {
  const [p, v, k]: number[] = data;

  const cp = p + 1; // 도색 주기
  const cv = v + 1; // 광택 주기
  const lcm = (cp / gcd(cp, cv)) * cv;

  const pf = Math.floor(k / cp); // 도색 실패
  const vf = Math.floor(k / cv); // 광택 실패
  const both = Math.floor(k / lcm); // 둘 다 실패

  const a = k - pf - vf + both;
  const b = both;
  const c = vf - both;
  const d = pf - both;

  return [a, b, c, d].join(" ");
};

/* 🚀 Run Program */
(() => {
  console.log(solution(getInputData()));
})();
