/*
----------------------------------------------
Sub: [BOJ] 2736. 행렬 덧셈(https://www.acmicpc.net/problem/2738)
Tag: C, 구현, 동적 2차배열
Memo
----------------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>

// 동적 2차원 배열 생성
int **create_2d_array(int rows, int cols) {
  int **array = (int **)malloc(rows * sizeof(int *));

  for (int i = 0; i < rows; i++) {
    array[i] = (int *)malloc(cols * sizeof(int));
  }

  return array;
}

// 메모리 해제
void free_2d_array(int **array, int rows) {
  for (int i = 0; i < rows; i++) {
    free(array[i]);
  }
  free(array);
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);

  int **array_a = create_2d_array(n, m);
  int **array_b = create_2d_array(n, m);

  // 행렬A 입력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &array_a[i][j]);
    }
  }

  // 행렬B 입력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &array_b[i][j]);
    }
  }

  // 행렬A + 행렬B 결과값 출력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      printf("%d ", array_a[i][j] + array_b[i][j]);
    }
    printf("\n");
  }

  free_2d_array(array_a, n);
  free_2d_array(array_b, n);

  return 0;
}
