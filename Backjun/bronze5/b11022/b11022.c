// A-B -8
// https://www.acmicpc.net/problem/11022

#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    int t;

    scanf("%d", &t);

    int *results = (int *)malloc(t * sizeof(int));

    for (int i = 0; i < t; i++) {
        scanf("%d %d", &a, &b);
        results[i] = a + b;
        printf("Case #%d: %d + %d = %d\n", i+i, a, b, results[i]);
    }

    return 0;
}
