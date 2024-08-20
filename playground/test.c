// [BOJ] X보다 작은 수
// https://www.acmicpc.net/problem/10871

#include <stdio.h>
#include <stdlib.h>

int main() {
  int n, x;
  scanf("%d %d", &n, &x);
  int *a = (int *)malloc(n * sizeof(int));

  for (int i=0; i<n; i++) {
    scanf("%d", &a[i]);
  }

  for (int i=0; i<n; i++) {
    if(a[i] < x) printf("%d ", a[i]); 
  }

  return 0;
}
