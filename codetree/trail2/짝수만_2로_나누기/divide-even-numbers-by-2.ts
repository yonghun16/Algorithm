declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
    ? "./input_test.txt"
    : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\n+/);

/* 📥 Input */
const getInputData = (): [number, number[]] => {
    const n = Number(input[0])
    const numbers: number[] = input[1].split(' ').map(Number);
  
    return [n, numbers];
};

/* ⚙️ Logic */
const solution = (n: number, numbers: number[]): number[] => {
    const answer : number[] = [];
    
    for (const number of numbers) {
        if (number % 2 === 0) {
            answer.push(number / 2);
        }
        else {
            answer.push(number);
        }
    }

    return answer;
};

/* 🚀 Run Program */
(() => {
    const [n, numbers] = getInputData();
    console.log(solution(n, numbers).join(' ')); 
})();