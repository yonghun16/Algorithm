/* ----------------------------------------
 * [BOJ] 1448. 삼각형 만들기
 * https://www.acmicpc.net/problem/1448
 * 구분 : 그리디, 정렬
-----------------------------------------*/


#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int*)b - *(int*)a; // 내림차순 정렬
}
/* qsort의 다양한 정렬 조건
 * 오름차순 정렬: compare 함수에서 int_a < int_b일 때 음수를 반환
 * 내림차순 정렬: compare 함수에서 int_a > int_b일 때 음수를 반환 */

int main() {
  int n, a, b, c;
  int result = -1;

  scanf("%d", &n);

  int *sideOfTriangle = (int *)malloc(n * sizeof(int));

  for(int i = 0; i < n; i++) {
    scanf("%d", &sideOfTriangle[i]);
  }
  qsort(sideOfTriangle, n, sizeof(int), compare);

  for(int i = 0; i < n-2; i++) {
    a = sideOfTriangle[i];
    b = sideOfTriangle[i+1];
    c = sideOfTriangle[i+2];
    if(a < b + c) {
      result = a + b + c;
      break;
    }
  }

  free(sideOfTriangle);

  printf("%d\n", result);

  return 0;
}
