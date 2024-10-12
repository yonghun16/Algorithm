/*

input ex
1 2
3
4

*/
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 구조분해할당을 사용하여 한 줄에 N과 M을 가져오기
const [N, M] = input[0].split(" ").map(Number);
console.log(N +" "+ typeof(N), M +" "+ typeof(M));

// D숫자를 object타입으로 가져오기
const D = input[1].split().map(Number);
console.log(D + " " + typeof(D));

// O숫자를 number타입으로 가져오기
let O = Number(input[2]);
console.log(O + " " + typeof(O));      // object 타입 채 반환

O = input[2].split().map(Number)[0];   // object 타입을 받아온 뒤 첫 번재 요소만 반환
console.log(O + " " + typeof(O));
