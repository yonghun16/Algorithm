// A-B
// https://www.acmicpc.net/problem/1001

#include <stdio.h>

// 뺄셈 함수
int getSub(int a, int b) {
    return a - b;
}

int main(void)
{
    int a, b;
    int answer;

    scanf("%d %d", &a, &b);
    
    answer = getSub(a, b);

    printf("%d", answer);

    return 0;
}

