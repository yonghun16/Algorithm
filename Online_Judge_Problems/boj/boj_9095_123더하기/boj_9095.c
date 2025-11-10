/* ------------------------------------------------------------
 * Sub    : [BOJ] 1, 2, 3 더하기
 * Link   : https://www.acmicpc.net/problem/9095
 * Level  : 실버 3
 * Tag    : C, DP
 * Memo
 * ----------------------------------------------------------- */

#include <stdio.h>

int main(void) {
    int T, n;
    int dp[12] = {0};

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 4; i <= 11; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        printf("%d\n", dp[n]);
    }

    return 0;
}
