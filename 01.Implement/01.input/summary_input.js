const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');


// === 1. 하나를 입력 받아 숫자형 변수에 저장 ===
// 입력
// 3
const num = Number(input[0]);

// 출력
console.log(num);



// === 2. 한 줄 입력받아 각각의 숫자형 변수에 저장 ===
// 입력
// 3 5
const [a, b] = input[0].split(' ').map(Number);

// 출력
console.log(a, b);



// === 3. 한 줄 입력 받아 어레이로 저장 ===
// 1 2 3 4 5 6 7 8 9
const arr = input[0].split(' ').map(Number);

// 출력
console.log(arr);



// === 4. 한 줄 입력받아 각각의 문자열 변수에 저장 ===
// abc def
const [a, b] = input[0].split(' ');

// 출력
console.log(a, b);



// === 5. 문자열 여러 줄을 입력받아 1차원 리스트에 저장 ===
// 1차원 배열 형태로 저장, n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
// node는 Ctrl+ D 를 누르기 전까지 누적해서 입력데이터가 쌓임
// 입력
// ABCDEF
// BCDEFA
// CDEFAB  (Ctrl + D)

// 출력
console.log(input[0]);
console.log(input[1]);
console.log(input[2]);

arr = [];
for (let i = 0; i < 3; i++) {
  arr.push(input[i]);
}
console.log(arr);
