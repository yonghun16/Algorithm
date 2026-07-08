declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
    ? "./input_test.txt"
    : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\n+/);

/* 📥 Input */
const getInputData = (): string => {
    const word = input[0]
  
    return word
};

/* ⚙️ Logic */
const solution = (word: string): string => {
    for (let i = 0; i < word.length; i++) {
        if (word[i] !== word[word.length - i - 1]) {
            return "No";
        }
    }
    return "Yes";
};

/* 🚀 Run Program */
(() => {
    console.log(solution(getInputData())); 
})();