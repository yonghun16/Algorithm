// AxB -7
// https://www.acmicpc.net/problem/11021

#include <stdio.h>
#include <stdlib.h>

int main() {
  int a, b;
  int t;

  scanf("%d", &t);

  int *results = (int *)malloc(t * sizeof(int));

  for (int i = 0; i < t; i++) {
    scanf("%d %d", &a, &b);
    results[i] = a + b;
  }

  for (int i = 0; i < t; i++) {
    printf("Case #%d: %d\n", i+1, results[i]);
  }

  free(results);

  return 0;
}