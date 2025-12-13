// Copyright (c) 2025 yonghun-song. All rights reserved.
/* ------------------------------------------------------------
 * File     : arrayList.c
 * Brief    : 배열 리스트 기초 코드
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------ */

#include <stdio.h>
#include <stdlib.h>

/* 두 수를 더하는 함수. */
int getSum(int a, int b) { return a + b; }

/* main 함수. */
int main() {
    int a, b;
    int n = 0;
    int* results = (int*)malloc(n * sizeof(int));

    // 입력
    while (scanf("%d %d", &a, &b) != EOF) {
        results[n++] = getSum(a, b);
    }

    // 출력
    for (int i = 0; i < n; i++) {
        printf("%d\n", results[i]);
    }

    free(results);

    return 0;
}
