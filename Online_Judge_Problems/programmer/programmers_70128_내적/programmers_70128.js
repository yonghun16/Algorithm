/*-----------------------------------------------------
Sub  : [Programmers] 내적
Link : https://programmers.co.kr/learn/courses/30/lessons/70128
Level: 1
Tag  : JS, Math
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

function solution (a,b){
    let answer = 0;
    for(let i=0; i<a.length; i++){
            answer += a[i]*b[i];
        } 
    return answer;
}
