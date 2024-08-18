const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

const inputData = []

rl.on('line', (line) => {
  inputData.push(line.trim())
})

rl.on('close', () => {
  const n = parseInt(inputData[0])
  const sidesOftriangle = lengths = inputData.slice(1).sort((a, b) => b - a);  // 내림차순으로 정렬
  let result = -1

  for (let i = 0; i < n - 2; i++) {
    const a = lengths[i];
    const b = lengths[i + 1];
    const c = lengths[i + 2];
    
    if (a < b + c) {
      result = a + b + c;
      break;
    }
  }

  console.log(result);
})
