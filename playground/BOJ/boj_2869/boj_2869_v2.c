/*-----------------------------------------------------
Sub  : [BOJ] 달팽이는 올라가고 싶다
Link : https://www.acmicpc.net/problem/2869
Level: 브론즈 1
Tag  : C, 수학
Memo
 - v2 : 더 간단.
-----------------------------------------------------*/

#include <stdio.h>
#include <math.h>

int main() {
    int A, B, V;
    
    // 입력 받기
    scanf("%d %d %d", &A, &B, &V);

    // 올림 계산
    int day = ceil((double)(V - B) / (A - B));

    // 결과 출력
    printf("%d\n", day);

    return 0;
}
