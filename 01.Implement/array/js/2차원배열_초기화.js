// 기본 문법
let arr = Array.from(Array(4), () => new Array(5))

console.log(arr)


// 초기화 : 0
const rows = 4;
const cols = 5;
const arr2 = Array.from({ length: rows }, () => Array(cols).fill(0));

console.log(arr2)


// 초기화 : 0 ~ 19
let arr3 = new Array(4);

for (let i = 0; i < arr3.length; i++) {
  arr3[i] = Array.from( { length: 5 }, (_, j) => i * 5 + j);
}

console.log(arr3)
