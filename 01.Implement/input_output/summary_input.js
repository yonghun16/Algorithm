const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');


// === 1. 하나를 입력 받아 숫자형 변수에 저장 ===
// 입력
// 3
const num = Number(input[0]);

console.log(num);



// === 2. 한 줄 입력받아 각각의 숫자형 변수에 저장 ===
// 입력
// 3 5
const [a, b] = input[0].split(' ').map(Number);

console.log(a, b);



// === 3. 한 줄 입력 받아 어레이로 저장 ===
// 1 2 3 4 5 6 7 8 9
const arr = input[0].split(' ').map(Number);

console.log(arr);



// === 4. 한 줄 입력받아 각각의 문자열 변수에 저장 ===
// abc def
const [a, b] = input[0].split(' ');

console.log(a, b);



// === 5. 문자열 여러 줄을 입력받아 1차원 리스트에 저장 ===
// 1차원 배열 형태로 저장, n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
// node는 Ctrl+ D 를 누르기 전까지 누적해서 입력데이터가 쌓임
// 선언형으로 작성하시오.
// 입력
// ABCDEF
// BCDEFA
// CDEFAB  (Ctrl + D)
const str = Array.from({ length: 3 }, (_, i) => input[i].trim());

console.log(str);



// === 6. 공백이 없는 숫자 데이터 여러 줄을 입력받아 2차원 리스트에 저장 ===
// 숫자열 데이터로 변환 후, 2차원 배열 형태로 저장,
// n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
// 선언형으로 작성하시오.
// 입력
// 0101
// 1010
// 2020
const grid = Array.from({ length: 3 }, (_, i) =>
  Array.from(input[i].trim(), Number)
);

console.log(grid);



// === 7. 숫자 데이터의 2차원 배열을 입력받기 ===
// 한 줄에 띄어쓰기가 있는 배열을, 여려 개의 줄을 통해 입력 받을 때, 2차원 배열 형태로 저장
// 선언형으로 작성하시오.
// 입력
// 0 1 0 1
// 1 0 1 0
// 2 0 2 0
const arr = Array.from({ length: 3 }, (_, i) =>
  Array.from(input[i].trim().split(' '), Number)
);

console.log(arr);



// === 8. 파일 여러 줄씩 읽기 ===
// 예: 첫 줄에 테스트 케이스 개수, 이후 줄마다 숫자 한 개씩 들어 있다고 가정
// 선언형으로 작성하시오.
/* -----------
// input.txt 
3
1
2
3
--------------*/
const filePath = require('path').join(__dirname, 'input.txt');
const lines = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');

const T = Number(lines[0]);

const numbers = Array.from({ length: T }, (_, i) => Number(lines[i + 1].trim())
);

console.log(numbers);
