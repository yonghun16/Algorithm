const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
})

const data = []

rl.on('line', (line) => {
  data.push(line.trim())
}).on('close', () => {
  const [n, m] = data[0].split(' ').map(Number)
  console.log(n)
});
