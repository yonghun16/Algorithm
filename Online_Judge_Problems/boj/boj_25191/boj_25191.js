const fs = require('fs');

// 입력값을 읽어옵니다. (한 줄씩 배열로 저장)
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 첫 번째 줄: 치킨집의 치킨 개수 N
const N = parseInt(input[0]);

// 두 번째 줄: 콜라 A, 맥주 B
const [A, B] = input[1].split(' ').map(Number);

// 콜라와 맥주로 먹을 수 있는 최대 치킨 수 계산
const drinkLimit = Math.floor(A / 2) + B;

// 치킨집의 재고(N)와 음료수 제한(drinkLimit) 중 최솟값 출력
console.log(Math.min(N, drinkLimit)); 