// A+B-2
// https://www.acmicpc.net/problem/2558

#include <stdio.h>

// 두 수를 더하는 함수
int getSum(int a, int b) {
    return a + b;
}

int main() {
    int a, b;
    int answer;

    scanf("%d", &a);
    scanf("%d", &b);

    answer = getSum(a, b);
    printf("%d\n", answer);

    return 0;
}
