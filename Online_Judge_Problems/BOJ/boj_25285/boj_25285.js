/*
----------------------------------------------
Sub : [BOJ] 심준의 병역판정검사
Link: https://www.acmicpc.net/problem/25285
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');

const input = fs.readFileSync(0, 'utf-8').split('\n');
let index = 0;

const T = parseInt(input[index++]);

for (let i = 0; i < T; i++) {
    const [a, b] = input[index++].split(' ').map(Number);
    const BMI = b / ((a / 100) ** 2);

    if (a >= 204) {
        console.log(4);
    } else if (a >= 161) {
        if (BMI >= 35 || BMI < 16) {
            console.log(4);
        } else if (BMI >= 20 && BMI < 25) {
            console.log(1);
        } else if ((BMI >= 18.5 && BMI < 20) || (BMI >= 25 && BMI < 30)) {
            console.log(2);
        } else if ((BMI >= 16 && BMI < 18.5) || (BMI >= 30 && BMI < 35)) {
            console.log(3);
        }
    } else if (a >= 159) {
        if (BMI >= 16 && BMI < 35) {
            console.log(3);
        } else {
            console.log(4);
        }
    } else if (a >= 146) {
        console.log(4);
    } else if (a >= 140.1) {
        console.log(5);
    } else {
        console.log(6);
    }
}
