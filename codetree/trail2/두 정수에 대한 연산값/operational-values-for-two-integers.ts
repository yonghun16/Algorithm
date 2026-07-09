declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
    ? "./input_test.txt"
    : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\n+/);

/* 📥 Input */
const getInputData = (): [number, number] => {
    let idx: number = 0;
    const [a, b] = input[idx].split(' ').map(Number);
  
    return [a, b]
};

/* ⚙️ Logic */
const solution = (a: number, b: number): [number, number] => {
    if (a > b) {
        a += 25;
        b *= 2;
    }
    else {
        b += 25;
        a *= 2;
    }

    return [a, b];
};

/* 🚀 Run Program */
(() => {
    console.log(...solution(...getInputData())); 
})();