/*-----------------------------------------------------
Sub  : [BOJ] 지영 공주님의 마법 거울
Link : https://www.acmicpc.net/problem/11586
Level: 브론즈 3
Tag  : C, String
Memo
  - 2차원 배열 입력 시 '개행문자'를 포함해 받음. -> 더 간결 
    scanf(" %c", &mirror[i][j]);
  - char mirror[N][N];
-----------------------------------------------------*/

#include <stdio.h>

int main() {
    int N, K;
    
    // 입력
    scanf("%d", &N);
    char mirror[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf(" %c", &mirror[i][j]);
        }
    }
    scanf("%d", &K);

    if (K == 1) {
        // 원본 그대로 출력
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                printf("%c", mirror[i][j]);
            }
            printf("\n");
        }
    } else if (K == 2) {
        // 좌/우 반전 처리
        for (int i = 0; i < N; i++) {
            for (int j = N - 1; j >= 0; j--) {
                printf("%c", mirror[i][j]);
            }
            printf("\n");
        }
    } else if (K == 3) {
        // 상/하 반전 처리
        for (int i = N - 1; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                printf("%c", mirror[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
