#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
  return *(int *)a - *(int *)b;
}

int main() {
  int n, x;
  scanf("%d %d", &n, &x);
  int *a = (int *)malloc(n * sizeof(int));

  for (int i=0; i<n; i++) {
    scanf("%d", &a[i]);
  }

  qsort(a, n, sizeof(int), compare);

  for (int i=0; i<n; i++) {
    if(a[i] < x) printf("%d ", a[i]); 
  }

  return 0;
}
