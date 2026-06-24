const fs = require("fs");

const [n, m] = fs.readFileSync(0, "utf-8").trim().split(" ").map(Number);

function printRectangle(rows, cols) {
  const line = "1".repeat(cols);
  for (let i = 0; i < rows; i++) {
    console.log(line);
  }
}

printRectangle(n, m);