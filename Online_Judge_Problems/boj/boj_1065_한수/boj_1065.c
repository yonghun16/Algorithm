/* ------------------------------------------------------------
 * Sub    : [BOJ] 한수
 * Link   : https://www.acmicpc.net/problem/1065
 * Level  : 실버 4
 * Tag    : C, brute force
 * Memo
 * ----------------------------------------------------------- */

#include <stdio.h>

int is_hansu(int x) {
    if (x < 100) return 1;  // 1~99는 모두 한수

    int a = x / 100;        // 백의 자리
    int b = (x / 10) % 10;  // 십의 자리
    int c = x % 10;         // 일의 자리

    return (a - b) == (b - c);
}

int main() {
    int N, count = 0;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        if (is_hansu(i)) count++;
    }

    printf("%d\n", count);
    return 0;
}
