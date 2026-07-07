/*
 * ------------------------------
 *      점화식 (nCr 계산)
 * ------------------------------
 */

#include <stdio.h>

long combi(int n, int r) {
    int i;
    long p = 1;

    for (i = 1; i <= r; i++) {
        p = p * (n - i + 1) / i;
    }
    return p;
}

int main() {
    int n, r;

    printf("n : ");
    scanf("%d", &n);
    printf("r : ");
    scanf("%d", &r);

    printf("%d C %d = %ld\n", n, r, combi(n, r));

    return 0;
}
