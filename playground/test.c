#include <stdio.h>
#include <stdlib.h>

int **create2DArray(int rows, int cols) {
  int **array = (int **)malloc(rows * sizeof(int *));

  for (int i = 0; i < rows; i++) {
    array[i] = (int *)malloc(cols * sizeof(int));
  }

  return array;
}

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

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &arrayA[i][j]);
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &arrayB[i][j]);
    }
  }

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
