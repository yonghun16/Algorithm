// A+B -5
// https://www.acmicpc.net/problem/10952

#include <stdio.h>
#include <stdlib.h>

// 두 수를 더하는 함수
int getSum(int a, int b) {
    return a + b;
}

int main() {
    int a, b;
    int n = 0;
    int *results = (int *)malloc(n * sizeof(int));

    while (1) {
        scanf("%d %d", &a, &b);
        if (a == 0 && b == 0) {
            break;
        }
        results[n++] = getSum(a, b);
    }

    for (int i = 0; i < n; i++) {
        printf("%d\n", results[i]);
    }

    return 0;
}
