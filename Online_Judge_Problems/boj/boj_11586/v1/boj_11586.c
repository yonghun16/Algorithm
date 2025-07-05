/*-----------------------------------------------------
Sub  : [BOJ] 지영 공주님의 마법 거울
Link : https://www.acmicpc.net/problem/11586
Level: 브론즈 3
Tag  : C, String
Memo
  - v1 : 2차원 배열을 입력 받을 시 개행 처리가 중요
    mirror[i][j] = getchar();
-----------------------------------------------------*/

#include <stdio.h>

#define MAX 100

void puts_mirror(int K, int N, char mirror[MAX][MAX]);

int main() {
    int N, K;
    char mirror[MAX][MAX];

    // 입력
    scanf("%d", &N);
    getchar();
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            mirror[i][j] = getchar();
        }
        getchar();
    }
    scanf("%d", &K);

    // 출력
    puts_mirror(K, N, mirror);

    return 0;
}

void puts_mirror(int K, int N, char mirror[MAX][MAX]) {
    if (K == 1) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                printf("%c", mirror[i][j]);
            }
            printf("\n");
        }
    } else if (K == 2) {
        for (int i = 0; i < N; i++) {
            for (int j = N - 1; j >= 0; j--) {
                printf("%c", mirror[i][j]);
            }
            printf("\n");
        }
    } else if (K == 3) {
        for (int i = N - 1; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                printf("%c", mirror[i][j]);
            }
            printf("\n");
        }
    }
}
