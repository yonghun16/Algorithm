// 1부터 n까지 수 출력하기
// https://www.biko.kr/problem/1408

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n>100) {
        printf("n이 100을 초과하였습니다.");
    }
    else {
        for (int i=0; i<n; i++) {
            printf("%d\n", i+1);
        }
    }

    return 0;
}
