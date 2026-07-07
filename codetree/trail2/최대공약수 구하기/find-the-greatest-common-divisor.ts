declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

// 📥 Get Input Data
let n: number;
let m: number;

const getInputData = () => {
  let idx: number = 0;

  n = Number(input[idx++]);
  m = Number(input[idx++]);
};

// 최대공약수 함수
const gcd = (a: number, b: number): number => {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }

  return a;
};

// ⚙️ Core Logic
const solution = () => {
  console.log(gcd(n, m));
};

// 🚀 Run Program
(() => {
  getInputData();
  solution();
})();
