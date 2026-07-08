// 알람 시계
// https://www.acmicpc.net/problem/2884

#include <stdio.h>

int main(void) {
  int h, m;
  scanf("%d %d", &h, &m);
  if (m >= 45) {
    m = m-45;
  }
  else {
    m = 60-(45-m);
    if (h == 0) {
      h = 23;
    }
    else h = h-1;
  }

  printf("%d %d", h, m);

  return 0;
}
