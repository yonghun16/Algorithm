/*
----------------------------------------------
Sub : [BOJ] 문자열
Link: https://www.acmicpc.net/problem/9086
Tag : C, 문자열
Memo
----------------------------------------------
*/

#include <stdio.h>
#include <string.h>

int main() {
  int T;           // 테스트 케이스의 개수
  scanf("%d", &T); // 입력받기

  for (int i = 0; i < T; i++) {
    char s[1001];
    scanf("%s", s);

    int len = strlen(s);
    printf("%c%c\n", s[0], s[len - 1]); // 첫 글자와 마지막 글자 출력
  }

  return 0;
}
