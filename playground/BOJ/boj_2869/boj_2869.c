/*-----------------------------------------------------
Sub  : [BOJ] 달팽이는 올라가고 싶다
Link : https://www.acmicpc.net/problem/2869
Level: 브론즈 1
Tag  : C, 수학
Memo
-----------------------------------------------------*/

#include <stdio.h>

int main(void) {
    int A, B, V = 0;
    int days_count, distance = 0;
    int answer = 0;

    // 입력 받기
    scanf("%d %d %d", &A, &B, &V);

    days_count = (V - A) / (A - B);
    distance = days_count * (A - B);

    while (1) {
        days_count += 1;
        distance += A;
        if (distance >= V) {
            answer = days_count;
            break;
        } else {
            distance -= B;
        }
    }

    // 결과 출력
    printf("%d\n", answer);

    return 0;
}
