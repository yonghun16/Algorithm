/*----------------------------------------------
Sub  : [BOJ] 벌집
Link : https://www.acmicpc.net/problem/2292
Level: B2
Tag  : JS, 수학
Memo
 - 
----------------------------------------------*/

const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

// 입력 받기
const N = parseInt(input);

function findMinRooms(N) {
    if (N === 1) {
        return 1;      // 중심은 방 하나로 충분
    }
    
    let layer = 1;     // 껍질 수
    let rangeEnd = 1;  // 각 껍질의 마지막 숫자

    while (rangeEnd < N) {
        rangeEnd += 6 * layer; // 다음 껍질 범위의 끝 계산
        layer += 1;
    }
    
    return layer;
}

console.log(findMinRooms(N));
