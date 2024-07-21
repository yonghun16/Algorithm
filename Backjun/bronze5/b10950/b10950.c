// A+B -3
// https://www.acmicpc.net/problem/10950

#include <stdio.h>
#include <stdlib.h>

// 두 수를 더하는 함수
int getSum(int a, int b) {
    return a + b;
}

int main() {
    int n;

    scanf("%d", &n);

    // 결과를 저장할 배열을 동적으로 할당합니다.
    int *result = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        result[i] = getSum(a, b);
    }

    for (int i = 0; i < n; i++) {
        printf("%d\n", result[i]);
    }

    free(result);

    return 0;
}
