/*
----------------------------------------------
Sub : [BOJ] 16진수
Link: https://www.acmicpc.net/problem/
Tag : JS,math
Memo
----------------------------------------------
*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').split('\n')

const N = input[0];
let power = 0
let DexNum = 0
let sumNum = 0

for (let i=N.length-1; i>=0; i--) {
    if (N[i] === 'A') DexNum = 10
    else if (N[i] == 'B') DexNum = 11
    else if (N[i] == 'C') DexNum = 12
    else if (N[i] == 'D') DexNum = 13
    else if (N[i] == 'E') DexNum = 14
    else if (N[i] == 'F') DexNum = 15
    else DexNum = Number(N[i])

    sumNum += DexNum*(16**power)
    power += 1
}

console.log(sumNum)
