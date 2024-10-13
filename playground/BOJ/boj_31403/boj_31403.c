/*
----------------------------------------------
Sub : [BOJ] A+B-C
Link: https://www.acmicpc.net/problem/31403
Tag : C, String
Memo
  sprintf(char A, format, value);  // printf 출력을 char A에 넣음
  strcpy(concat, strA)  // strA를 concat에 복사
  strcat(concat, strB)  // strB를 concat에 연결하기
  atoi(concat)          // 문자열 concat를 정수화 
----------------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int A, B, C;
  char strA[10], strB[10], concat[20];

  scanf("%d", &A);
  scanf("%d", &B);
  scanf("%d", &C);

  // 첫 번째 출력: A + B - C (수로 처리)
  int resultNumber = A + B - C;
  printf("%d\n", resultNumber);

  // 두 번째 출력: A, B를 문자열로 이어붙인 후 C를 뺀 결과
  sprintf(strA, "%d", A);
  sprintf(strB, "%d", B);
  strcpy(concat, strA);
  strcat(concat, strB);

  // 이어붙인 문자열을 정수로 변환하고 C를 뺌
  int resultStringNumber = atoi(concat) - C;
  printf("%d\n", resultStringNumber);

  return 0;
}
