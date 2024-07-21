// 문제1A 최대값 함수

#include <stdio.h>

int getMax(int a, int b) {
    if(a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int a, b;
    int answer;
    
    scanf("%d %d", &a, &b);

    answer = getMax(a, b);
    printf("%d\n", answer);

    return 0;
}
