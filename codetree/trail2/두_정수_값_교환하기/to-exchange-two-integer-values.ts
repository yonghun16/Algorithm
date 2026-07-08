declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
    ? "./input_test.txt"
    : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

/* 📥 Input */
const getInputData = (): [number, number] => {
    const [n, m] = input.map(Number);
  
    return [n, m];
};

/* ⚙️ Logic */
const solution = (n: number, m: number): [number, number] => {
    
    const temp = n;
    n = m;
    m = temp;

    return [n, m];
};

/* 🚀 Run Program */
(() => {
    const [n, m] = getInputData();
    console.log(solution(n, m).join(" ")); 
})();