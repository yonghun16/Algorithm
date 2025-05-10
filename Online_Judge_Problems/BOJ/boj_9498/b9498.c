// 시험 성적
// https://www.acmicpc.net/problem/9498

#include <stdio.h>

int main(void) {
  int inputVal;
  scanf("%d", &inputVal);

  if (inputVal >= 90) printf("A");
  else if (inputVal >= 80) printf("B");
  else if (inputVal >= 70) printf("C");
  else if (inputVal >= 60) printf("D");
  else printf("F");

  return 0;
}
