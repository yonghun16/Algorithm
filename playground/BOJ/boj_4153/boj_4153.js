/*
----------------------------------------------
Sub : [BOJ] 직각삼각형
Link: https://www.acmicpc.net/problem/4153
Tag : JS, math
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');


function is_right_triangle(a, b, c) {
  const sides = [a, b, c];
  sides.sort((x, y) => x - y);
  return sides[0] ** 2 + sides[1] ** 2 === sides[2] ** 2;
}


let i = 0
while(true) {
  let [a, b, c] = input[i++].split(" ").map(Number);
    if (a === 0 && b === 0 && c === 0) {
      break;
    } else {
      if (is_right_triangle(a, b, c)) {
        console.log('right');
      }else{
        console.log('wrong');
      }
    }
}
