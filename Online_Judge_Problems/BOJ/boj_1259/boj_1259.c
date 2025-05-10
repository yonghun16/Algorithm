/*-----------------------------------------------------
Sub  : [BOJ] 팰린드롬수
Link : https://www.acmicpc.net/problem/1259
Level: 브론즈 1
Tag  : C, String
Memo
-----------------------------------------------------*/

#include <stdio.h>
#include <string.h>

#define MAX_STRING 6

int main() {
    char n[MAX_STRING];

    while (1) {
        // 입력 받기
        scanf("%s", n);

        // '0'이면 종료
        if (strcmp(n, "0") == 0) {
            break;
        }

        // 팰린드롬 검사
        int len = strlen(n);
        int is_palindrome = 1;  // 기본값을 참(true)로 설정

        for (int i = 0; i < len / 2; i++) {
            if (n[i] != n[len - 1 - i]) {
                is_palindrome = 0;  // 팰린드롬이 아님
                break;
            }
        }

        // 출력
        if (is_palindrome) {
            printf("yes\n");
        } else {
            printf("no\n");
        }
    }

    return 0;
}
