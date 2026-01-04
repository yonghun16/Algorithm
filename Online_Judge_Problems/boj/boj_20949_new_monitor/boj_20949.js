/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 문제 제목
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

const D = 77;

// calculate PPI
const calculatePPi = (W, H) => {
  return Math.sqrt(W * W + H * H) / D;
};

// input
const N = Number(input[0]);
const monitor = [];
const sortMonitor = [[0, 0]];

for (let i = 1; i <= N; i++) {
  const [W, H] = input[i].split(" ").map(Number);
  monitor.push([i, calculatePPi(W, H)]);
}

// sort
for (let i = 0; i < N; i++) {
  for (let j = 0; j < sortMonitor.length; j++) {
    if (monitor[i][1] > sortMonitor[j][1]) {
      sortMonitor.splice(j, 0, monitor[i]);
      break;
    }
  }
}

// print
for (let i = 0; i < N; i++) {
  console.log(sortMonitor[i][0]);
}
