/*-----------------------------------------------------
Sub  : [BOJ] 오븐 시계
Link : https://www.acmicpc.net/problem/2525
Level: 브론즈 3
Tag  : JS, 사칙연산
Memo
-----------------------------------------------------*/
const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

// 입력 형식
const [A, B] = input[0].split(' ').map(Number);   // 현재 시, 분
const C = Number(input[1]);                       // 요리 시간 (분)

// 출력 형식
answer = {
  hour: 0,          // 요리 종료 시
  min: 0            // 요리 종료 분
}

// 입력 검사
const checkInput = (A, B, C) => {
  if (A < 0 || A > 23 || B < 0 || B > 59 || C < 0 || C > 1000) {
    throw new Error("입력갑이 허용범위를 초과합니다.");
  }
}
checkInput(A, B, C);

// 요리 후 시각 계산
function solution(A, B, C) {
  // 분 단위로 변환 후 계산
  const oneDayMinute = 24 * 60;              // 하루 분
  let totalMinute = (A * 60) + B + C;        // 요리 종료 시간
  totalMinute %= oneDayMinute;               // 요리 종료 시각 : 하루가 넘어가는 경우는 하루 분(1440)으로 나누어 나머지 값으로 변경
  const hour = Math.floor(totalMinute / 60);       // 시 계산
  const min = totalMinute % 60;                    // 분 계산
  return [hour, min];
}

// 결과 출력
[answer.hour, answer.min] = solution(A, B, C);
console.log(answer.hour, answer.min);
