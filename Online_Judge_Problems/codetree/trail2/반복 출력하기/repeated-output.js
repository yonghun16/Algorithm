const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf-8").trim());

function printLines(count) {
  const line = "12345^&*()_";
  for (let i = 0; i < count; i++) {
    console.log(line);
  }
}

printLines(n);