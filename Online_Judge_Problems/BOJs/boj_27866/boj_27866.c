/*
----------------------------------------------
Sub: [BOJ] 27866. 문자와 문자열
Link: https://www.acmicpc.net/problem/27866
Tag: C, 문자열
Memo
- 문자열은 0부터 인덱스 시작
----------------------------------------------
*/

#include <stdio.h>

int main() {
  char S[1001];
  int i;

  // 문자열과 정수 입력 받기
  scanf("%s", S);
  scanf("%d", &i);

  // 결과 출력
  printf("%c\n", S[i - 1]);

  return 0;
}
