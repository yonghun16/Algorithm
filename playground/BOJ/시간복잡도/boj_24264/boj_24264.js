/*-----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행 시간3
Link : https://www.acmicpc.net/problem/24264
Level: 브론즈 3
Tag  : JS, BigO
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const n = Number(input[0]);
// const A = Array(n).fill(0).map(() => Math.floor(Math.random() * 10));

/*
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
*/

//function MenOfPassion(A, n) {
//  let count = 0;
//  let sum = 0;
//  for (let i = 1; i <= n; i++) {
//    for (let j = 1; j <= n; j++) {
//      sum += A[i] * A[j];
//      count++;
//    }
//  }
//  //return sum;
//  return count;
//}
//
//const result_count = MenOfPassion(A, n);

// 결과출력
// 시간복잡도 -> O(n^2)
//console.log(result_count);    // O(n^2)
console.log(n**2);
console.log(2);               // n^2의 차수 -> 2
