/* ------------------------------------------------------------
 * Sub    : [BOJ] 등수 구하기
 * Link   : https://www.acmicpc.net/problem/1205
 * Level  : 실버 4
 * Tag    : C, 구현
 * Memo
 * ----------------------------------------------------------- */

#include <stdio.h>

int main() {
    int N, score, P;
    scanf("%d %d %d", &N, &score, &P);

    int arr[51];
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    // 경우 1: 리스트가 비어있는 경우
    if (N == 0) {
        printf("1\n");
        return 0;
    }

    // 새 점수의 등수 계산 (자기보다 큰 점수 개수 + 1)
    int rank = 1;
    for (int i = 0; i < N; i++) {
        if (arr[i] > score)
            rank++;
        else
            break;
    }

    // 경우 2: 리스트가 꽉 찼을 때
    if (N == P && arr[N - 1] >= score) {
        printf("-1\n");
        return 0;
    }

    // 들어갈 수 있는 경우 등수 출력
    printf("%d\n", rank);

    return 0;
}
