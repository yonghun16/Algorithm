/*-----------------------------------------------------
Sub  : [BOJ] 가희와 방어율 무시
Link : https://www.acmicpc.net/problem/25238
Level: 브론즈 4
Tag  : C, 사칙연산
Memo
-----------------------------------------------------*/

#include <stdio.h>

int get_effective_defence(int a, int b) {
    return a * (100-b)/100;
}

int main(void) {
    int a, b;
    int effective_defence;

    // 입력 받기
    scanf("%d %d", &a, &b);

    effective_defence = get_effective_defence(a, b);

    // 출력하기
    if (effective_defence >= 100) {
        puts("0");
    } else {
        puts("1");
    }
    return 0;
}

