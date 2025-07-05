// A+B - 6
// https://www.acmicpc.net/problem/10953

#include <stdio.h>
#include <stdlib.h>

// 두 수를 더하는 함수
int getSum(int a, int b) {
    return a + b;
}

int main() {
    int a, b;
    int n;

    scanf("%d", &n);
    int *results = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%d,%d", &a, &b);
        results[i] = getSum(a, b);
    }

    for (int i = 0; i < n; i++) {
        printf("%d\n", results[i]);
    }

    free(results);

    return 0;
}
