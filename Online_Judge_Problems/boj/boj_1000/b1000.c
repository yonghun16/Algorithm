 // A+B
 // https://www.acmicpc.net/problem/1000

#include <stdio.h>

int getSum(int a, int b) {
    return a + b;
}

int main() {
    int a, b;
    int answer;

    scanf("%d %d", &a, &b);

    answer = getSum(a, b);

    printf("%d\n", answer);

    return 0;
}
