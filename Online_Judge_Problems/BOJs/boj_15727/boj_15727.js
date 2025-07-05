const fs = require('fs');

// 입력 파일 읽기
const input = fs.readFileSync('/dev/stdin').toString().trim();
const L = parseInt(input, 10);

// 성우가 이동할 수 있는 최대 거리: 5
const maxDistancePerMinute = 5;

// 최소 시간 계산
const minTime = Math.ceil(L / maxDistancePerMinute);

// 결과 출력
console.log(minTime);
