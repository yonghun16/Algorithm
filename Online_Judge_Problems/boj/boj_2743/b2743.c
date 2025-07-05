// 단어 길이 재기
// https://www.acmicpc.net/problem/2743

#include <stdio.h>
#include <string.h>

int main() {
  char inputWord[101];
  int lengthOfWord;
  int result;

  scanf("%100s", inputWord); // 최대 100개의 문자를 읽도록 지정하여 버퍼 오버플로우 방지
  lengthOfWord = strlen(inputWord);

  result = lengthOfWord;

  printf("%d", result);

  return 0;
}