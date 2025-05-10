/*
----------------------------------------------
Sub  : [BOJ] 그대로 출력하기
Link : https://www.acmicpc.net/problem/11718
Tag  : C, 문자열, 입력
Memo
----------------------------------------------
*/

#include <stdio.h>

int main() {
  char line[101]; // 한 줄에 최대 100글자 + null 문자

  // EOF가 나올 때까지 반복적으로 입력받고 출력
  while (fgets(line, sizeof(line), stdin)) {
    printf("%s", line); // 입력받은 줄을 그대로 출력
  }

  return 0;
}
