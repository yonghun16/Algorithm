/* ------------------------------------------------------------
 * Sub    : [BOJ] 막대기
 * Link   : https://www.acmicpc.net/problem/1094
 * Level  : 실버 5
 * Tag    : C, 수학
 * Memo
 * ----------------------------------------------------------- */

#include <stdio.h>

int main() {
    int X, count = 0;
    scanf("%d", &X);

    while (X > 0) {
        if (X % 2 == 1) {
            count++;
        }
        X = X / 2;
    }

    printf("%d\n", count);
    return 0;
}
