/*
----------------------------------------------
Sub : [BOJ] 최댓값
Link: https://www.acmicpc.net/problem/2562
Tag : C, 
Memo
----------------------------------------------
*/

#include <stdio.h>

int main() {

  int numbers[9];
  int maxValue = 0;
  int maxIndex = 0;

  for (int i = 0; i < 9; i++) {
    scanf("%d", &numbers[i]);
    if (numbers[i] > maxValue) {
      maxValue = numbers[i];
      maxIndex = i;
    }
  }

  printf("%d\n%d", maxValue, maxIndex + 1);

  return 0;
}
