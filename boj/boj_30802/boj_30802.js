const fs = require('fs');

// 입력 읽기
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 입력 데이터 파싱
const N = parseInt(input[0]); // 참가자 수
const [S, M, L, XL, XXL, XXXL] = input[1].split(' ').map(Number); // 각 사이즈별 참가자 수
const [T, P] = input[2].split(' ').map(Number); // 티셔츠와 펜 묶음 크기

// 티셔츠 묶음 계산
const sizes = [S, M, L, XL, XXL, XXXL];
let minTshirtBundles = 0;

sizes.forEach(size => {
    minTshirtBundles += Math.ceil(size / T); // 각 사이즈별 묶음 계산
});

// 펜 묶음 계산
const maxPenBundles = Math.floor(N / P); // 최대 펜 묶음
const remainingPens = N % P; // 남는 펜 개수

// 결과 출력
console.log(minTshirtBundles);
console.log(`${maxPenBundles} ${remainingPens}`);
