declare var require: any;

const fs = require("fs");
const n: number = Number(fs.readFileSync(0, "utf8").trim());

let num = 1;
const result: string[] = [];

for (let i = 0; i < n; i++) {
  const row: number[] = [];

  for (let j = 0; j < n; j++) {
    row.push(num);
    num = (num % 9) + 1;
  }

  result.push(row.join(" "));
}

console.log(result.join("\n"));