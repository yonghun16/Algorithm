declare var require: any;
const fs = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

/* 📥 [Input] 데이터 파싱 및 전처리 */
const getInputData = () => {
  const [n, m] = input.map(Number);
  return [n, m];
};

/* ⚙️ [Logic] 유클리드 호제법 기반 공약수/공배수 계산 */
/**
 * 유클리드 호제법을 이용하여 두 수의 최대공약수(GCD)를 구합니다.
 * @param a - 첫 번째 정수
 * @param b - 두 번째 정수
 * @returns 두 수의 최대공약수
 */
const gcd = (a: number, b: number): number => {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
};

// 오버플로우 방지를 위해 (a / gcd) * b 형태로 계산하는 것이 더 안전함
const lcm = (a: number, b: number): number => {
  return (a / gcd(a, b)) * b;
};

const solution = (n: number, m: number) => {
  console.log(lcm(n, m));
};

/* 🚀 [Execution] 프로그램 시작점 */
(() => {
  const [n, m] = getInputData();
  solution(n, m);
})();
