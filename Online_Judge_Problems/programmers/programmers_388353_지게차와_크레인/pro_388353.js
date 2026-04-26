/**
 * -----------------------------------------------------------
 * Sub    : [Programmers] 지게차와 크레인
 * Link   : https://school.programmers.co.kr/learn/courses/30/lessons/388353
 * Level  : 2
 * Tag    : BFS, Simulation
 * ------------------------------------------------------------
 * Solution
 * 1. 크레인 (요청 길이 2)
 *     해당 문자 전부 제거
 * 2. 지게차 (요청 길이 1)
 *    - "외부와 연결된" 컨테이너만 제거
 *    - 외부 판정 방법
 *        - 빈 공간('.')을 기준으로 가장자리에서 BFS 수행
 *        - BFS로 퍼지면서 만난 target 컨테이너만 제거 가능
 * ------------------------------------------------------------
 */

const fs = require("fs");

const filePath = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input = fs.readFileSync(filePath, "utf-8").trim().split("\n");

// 📥 Get Input Data
const getInputData = () => {
  const storage = input[0].trim().split(" ");
  const requests = input[1].trim().split(" ");

  return { storage, requests };
};

// ⚙️ Core Logic
const solution = (storage, requests) => {
  const n = storage.length;
  const m = storage[0].length;

  const board = storage.map((row) => row.split(""));

  // 지게차
  const removeByForklift = (target) => {
    const visited = Array.from({ length: n }, () => Array(m).fill(false));

    const queue = [];
    let head = 0;

    const removable = new Set();

    // 테두리 탐색
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (i === 0 || i === n - 1 || j === 0 || j === m - 1) {
          if (board[i][j] === ".") {
            queue.push([i, j]);
            visited[i][j] = true;
          } else if (board[i][j] === target) {
            removable.add(`${i},${j}`);
          }
        }
      }
    }

    const directions = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];

    // BFS
    while (head < queue.length) {
      const [x, y] = queue[head++];

      for (const [dx, dy] of directions) {
        const nx = x + dx;
        const ny = y + dy;

        if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
          visited[nx][ny] = true;

          if (board[nx][ny] === ".") {
            queue.push([nx, ny]);
          } else if (board[nx][ny] === target) {
            removable.add(`${nx},${ny}`);
          }
        }
      }
    }

    // 제거
    for (const pos of removable) {
      const [x, y] = pos.split(",").map(Number);
      board[x][y] = ".";
    }
  };

  // 요청 처리
  for (const req of requests) {
    const target = req[0];

    // 크레인
    if (req.length === 2) {
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
          if (board[i][j] === target) {
            board[i][j] = ".";
          }
        }
      }
    }
    // 지게차
    else {
      removeByForklift(target);
    }
  }

  // 남은 개수
  let answer = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] !== ".") answer++;
    }
  }

  return answer;
};

// 🚀 Run Program
(() => {
  const { storage, requests } = getInputData();
  console.log(solution(storage, requests));
})();
