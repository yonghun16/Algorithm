// A+B -4
// https://www.acmicpc.net/problem/10951
// 동적배열

/*-----------------------------------------------------
Sub  : [BOJ] A+B -4
Link : https://www.acmicpc.net/problem/10951
Level: Bronze 5
Tag  : C,
Memo
-----------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>

// 두 수를 더하는 함수
int getSum(int a, int b) { return a + b; }

int main() {
    int a, b;
    int n = 0;
    int *results = (int *)malloc(n * sizeof(int));

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
