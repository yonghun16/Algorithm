/*-----------------------------------------------------
Sub  : [BOJ] 완전 제곱수
Link : https://www.acmicpc.net/problem/6131
Level: 브론즈 3
Tag  : C, Brute Force
Memo
-----------------------------------------------------*/

#include <stdio.h>

#define MAX 500

int main() {
    int n;
    int a = 1, b = 1;
    int count = 0;

    // 입력
    scanf("%d", &n);

    while (b < MAX) {
        if (a * a == (b * b + n)) {
            count++;
            b++;
            a = b;
        }
        if (a * a > b * b + n) {
            b++;
            a = b;
            continue;
        }
        a++;
    }

    // 출력
    printf("%d\n", count);

    return 0;
}
