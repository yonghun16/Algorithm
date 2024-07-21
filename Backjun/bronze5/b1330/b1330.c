// 두 수 비교하기
// https://www.acmicpc.net/problem/1330

#include <stdio.h>

// 두 정수를 비교하고 결과 출력
const char* compare(int a, int b) {
    if (a > b) {
        return ">";
    } else if (a < b) {
        return "<";
    } else {
        return "==";
    }
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    printf("%s\n", compare(a, b));

    return 0;
}
