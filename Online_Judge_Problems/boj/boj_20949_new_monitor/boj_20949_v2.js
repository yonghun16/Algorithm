/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 효령과 새 모니터
 * Link   : https://www.acmicpc.net/problem/20949
 * Level  : Silver 5
 * Tag    : JS, sort
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

let input;

if (process.platform === "linux") {
  input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
} else {
  const path = require("path");
  const filePath = path.join(__dirname, "input.txt");
  input = require("fs").readFileSync(filePath, "utf-8").trim().split("\n");
}

// input
const N = parseInt(input[0]);
const monitors = [];

for (let i = 1; i <= N; i++) {
  const [W, H] = input[i].split(" ").map(Number);

  // (일반 Number 타입으로도 이 범위는 커버 가능하지만 정확성을 위해 권장)
  const ppiValue = BigInt(W) * BigInt(W) + BigInt(H) * BigInt(H);

  monitors.push({
    id: i,
    ppiValue: ppiValue,
  });
}

// sort
monitors.sort((a, b) => {
  if (b.ppiValue > a.ppiValue) return 1;
  if (b.ppiValue < a.ppiValue) return -1;

  // PPI가 같으면 번호(id)가 작은 순서대로
  return a.id - b.id;
});

// print
console.log(monitors.map((m) => m.id).join("\n"));
