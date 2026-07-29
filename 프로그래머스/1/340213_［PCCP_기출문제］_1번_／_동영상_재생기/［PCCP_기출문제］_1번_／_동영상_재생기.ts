/** -----------------------------------------------------------
 * Sub    : [Programmers] 동영상 재생기
 * Link   : https://school.programmers.co.kr/learn/courses/30/lessons/
 * Level  :
 * Tag    : TS, Simulation, Math
 * ------------------------------------------------------------
 * Approach
 * 모든 시간을 초(second)로 변환하여 계산한다.
 * 현재 위치가 오프닝 구간이면 op_end로 이동한다.
 * 각 명령(prev, next)을 수행한다.
 * 명령 수행 후 다시 오프닝 구간인지 검사한다.
 * 마지막 위치를 "mm:ss" 형식으로 변환하여 반환한다.
 * ------------------------------------------------------------
 */

declare var require: any;
const fs = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

/* 📥 Input */
const getInputData = () => {
  const [videoLen, pos, opStart, opEnd, ...commands] = input;
  return [videoLen, pos, opStart, opEnd, commands] as const;
};

/* ⚙️ Logic */
const toSeconds = (time: string): number => {
  const [minute, second] = time.split(":").map(Number);
  return minute * 60 + second;
};

const toTime = (seconds: number): string => {
  const minute = Math.floor(seconds / 60);
  const second = seconds % 60;

  return `${String(minute).padStart(2, "0")}:${String(second).padStart(2, "0")}`;
};

const solution = (
  videoLen: string,
  pos: string,
  opStart: string,
  opEnd: string,
  commands: string[],
) => {
  const videoLength = toSeconds(videoLen);
  const openingStart = toSeconds(opStart);
  const openingEnd = toSeconds(opEnd);

  let current = toSeconds(pos);

  const skipOpening = (time: number): number =>
    openingStart <= time && time <= openingEnd ? openingEnd : time;

  // 시작 위치에서도 오프닝 스킵
  current = skipOpening(current);

  for (const command of commands) {
    if (command === "prev") {
      current = Math.max(0, current - 10);
    } else {
      current = Math.min(videoLength, current + 10);
    }

    current = skipOpening(current);
  }

  console.log(toTime(current));
};

/* 🚀 Run Program */
(() => {
  solution(...getInputData());
})();
