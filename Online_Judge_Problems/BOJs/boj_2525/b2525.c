// 오븐 시계
// https://www.acmicpc.net/problem/2525

#include <stdio.h>

int main(void) {
  int a, b, c;
  int totalMinute;

  scanf("%d %d", &a, &b);
  scanf("%d", &c);

  totalMinute = (a*60 + b + c) % 1440;
  a = totalMinute / 60;
  b = totalMinute % 60;

  printf("%d %d", a, b);

  return 0;
}
