/* ----------------------------------------------
Sub: [BOJ] 2738. 행렬 덧셈
Link: https://www.acmicpc.net/problem/2738
Tag: C, 구현, 동적 2차배열
Memo
---------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>

// 동적 2차원 배열 생성
int **create2DArray(int rows, int cols) {
  int **array = (int **)malloc(rows * sizeof(int *));

  for (int i = 0; i < rows; i++) {
    array[i] = (int *)malloc(cols * sizeof(int));
  }

  return array;
}

// 메모리 해제
void free2DArray(int **array, int rows) {
  for (int i = 0; i < rows; i++) {
    free(array[i]);
  }
  free(array);
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);

  int **arrayA = create2DArray(n, m);
  int **arrayB = create2DArray(n, m);

  // 행렬A 입력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &arrayA[i][j]);
    }
  }

  // 행렬B 입력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &arrayB[i][j]);
    }
  }

  // 행렬A + 행렬B 결과값 출력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      printf("%d ", arrayA[i][j] + arrayB[i][j]);
    }
    printf("\n");
  }

  free2DArray(arrayA, n);
  free2DArray(arrayB, n);

  return 0;
}
