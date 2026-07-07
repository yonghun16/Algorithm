/*-----------------------------------------------------
Sub  : [BOJ] 알고리즘 수업 - 피보나치 수 1
Link : https://www.acmicpc.net/problem/24416
Level: 브론즈 1
Tag  : C, dynamic
Memo
-----------------------------------------------------*/

#include <stdio.h>

int fib_recursive(int n, int *count1) {
    if (n == 1 || n == 2) {
        (*count1)++;
        return 1;
    }
    return fib_recursive(n - 1, count1) + fib_recursive(n - 2, count1);
}

int fibonacci_dp(int n) {
    int f[n + 1];
    int count2 = 0;

    f[1] = f[2] = 1;

    for (int i = 3; i <= n; i++) {
        f[i] = f[i - 1] + f[i - 2];
        count2++;
    }

    return count2;
}

int main() {
    int n;

    // 입력
    scanf("%d", &n);

    // 피보나치 수 재귀로 구하기
    int count1 = 0;
    fib_recursive(n, &count1);

    // 피보나치 수 동적 프로그래밍으로 구하기
    int count2 = fibonacci_dp(n);

    // 출력
    printf("%d %d\n", count1, count2);

    return 0;
}
