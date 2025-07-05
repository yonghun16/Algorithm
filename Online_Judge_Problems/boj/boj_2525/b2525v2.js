// 오븐 시계
// https://www.acmicpc.net/problem/2525

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let [a, b] = inputData[0].split(' ').map(Number);
let c = Number(inputData[1]);

let totalMinute = a*60 + b + c;   // 분의 형태로 바꾸기
totalMinute %= 1440;  // 24*60=1440
a = parseInt(totalMinute/60);
b = totalMinute % 60;

console.log(a + " " + b);
