/*-----------------------------------------------------
Sub  : [BOJ] 부녀회장이 될테야
Link : https://www.acmicpc.net/problem/2775
Level: Bronze 1
Tag  : C, Dynamic Programming
Memo
  - 비슷한 문제
    ACM 호텔 (10250)
-----------------------------------------------------*/

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

// 동적 2차원 배열 해제
void free2DArray(int **array, int rows) {
    for (int i = 0; i < rows; i++) {
        free(array[i]);
    }
    free(array);
}

// 거주민 수 계산
int get_resident(int k, int n) {
    // (k+1) x (n+1) 크기의 동적 배열 생성
    int **apt_arr = create2DArray(k + 1, n + 1);

    // k층 0호,  0층 n호 초기화
    for (int i = 0; i <= k; i++) apt_arr[i][0] = 0;
    for (int j = 0; j <= n; j++) apt_arr[0][j] = j;

    // DP 방식으로 거주민 수 채우기
    for (int i = 1; i <= k; i++) {
        for (int j = 1; j <= n; j++) {
            apt_arr[i][j] = apt_arr[i][j - 1] + apt_arr[i - 1][j];
        }
    }

    int result = apt_arr[k][n];
    free2DArray(apt_arr, k + 1);

    return result;
}

int main() {
    int t, k, n;

    // 테스트 케이스 개수 입력
    scanf("%d", &t);

    // 각 테스트 케이스 실행
    for (int i = 0; i < t; i++) {
        scanf("%d%d", &k, &n);
        printf("%d\n", get_resident(k, n));
    }

    return 0;
}
