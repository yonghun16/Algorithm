declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

/* 📥 Get Input Data */
const getInputData = () => {
  const [n, m] = input.map(Number);

  return [n, m];
};

/* ⚙️ Core Logic */
// 최대공약수(GCD) 함수 (유클리드 호제법)
const gcd = (a: number, b: number): number => {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
};

// 최소공배수(LCM) 함수
const lcm = (a: number, b: number): number => {
  return (a * b) / gcd(a, b);
};
const solution = (n: number, m: number) => {
  // 두 숫자를 인자로 받아 최소공배수를 구해 출력
  console.log(lcm(n, m));
};

/* 🚀 Run Program */
(() => {
  const [n, m] = getInputData();
  solution(n, m);
})();
