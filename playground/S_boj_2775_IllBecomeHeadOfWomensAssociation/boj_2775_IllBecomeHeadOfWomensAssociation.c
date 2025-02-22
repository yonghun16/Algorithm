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

#define N_MAX 15
#define K_MAX 15

int apt_arr[K_MAX][N_MAX];

int get_resident(int apt_arr[][N_MAX], int k, int n) {
    // k층 0호,  0층 n호 초기화
    for (int i = 0; i <= k; i++) apt_arr[i][0] = 0;
    for (int j = 0; j <= n; j++) apt_arr[0][j] = j;

    // DP 방식으로 거주민 수 채우기
    for (int i = 1; i <= k; i++) {
        for (int j = 1; j <= n; j++){
            apt_arr[i][j] = apt_arr[i][j-1] + apt_arr[i-1][j];
        }
    }

    return apt_arr[k][n];
}

int main() {
    int t, k, n;

    // 테스트 케이스 개수 입력
    scanf("%d", &t);

    // 각 테스트 케이스 실행
    for (int i = 0; i < t; i++) {
        scanf("%d%d", &k, &n);
        printf("%d\n", get_resident(apt_arr, k, n));
    }

    return 0;
}
