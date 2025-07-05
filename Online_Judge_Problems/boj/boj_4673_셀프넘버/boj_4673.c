/*----------------------------------------------
Sub  : [BOJ] 셀프 넘버
Link : https://www.acmicpc.net/problem/4673
Level: 실버 5
Tag  : C, Brute Force
Memo
 -
----------------------------------------------*/

#include <stdio.h>

#define MAX 10000

// 생성자를 이용해 숫자를 생성하는 함수
int generate(int n) {
    int sum = n;
    while (n > 0) {
        sum += n % 10;  // 각 자릿수를 더함
        n /= 10;
    }
    return sum;
}

int main() {
    int isSelfNumber[MAX];  // 1이면 셀프 넘버, 0이면 생성자가 있음

    // 배열을 모두 1(셀프 넘버)로 초기화
    for (int i = 0; i < MAX; i++) {
        isSelfNumber[i] = 1;
    }

    // 생성자가 있는 숫자를 체크
    for (int i = 1; i < MAX; i++) {
        int num = generate(i);
        if (num < MAX) {
            isSelfNumber[num] = 0;  // 생성자가 있는 숫자는 제외
        }
    }

    // 셀프 넘버 출력
    for (int i = 1; i < MAX; i++) {
        if (isSelfNumber[i] == 1) {
            printf("%d\n", i);
        }
    }

    return 0;
}
