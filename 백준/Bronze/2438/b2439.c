// 별 찍기 - 1
// https://www.acmicpc.net/problem/2438

#include <stdio.h>

// 별을 출력하는 함수
void printStar(int n) {
    for (int i=0; i<n; i++) {
        for (int j=0; j<=i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);

    printStar(n);

    return 0;
}
