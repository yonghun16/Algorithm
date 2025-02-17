/*-----------------------------------------------------
Sub  : [BOJ] 평균
Link : https://www.acmicpc.net/problem/1546
Level: 브론즈 1
Tag  : C,
Memo
-----------------------------------------------------*/

#include <stdio.h>

int main() {
    int n;
    int max_score = 0;
    int score[1000];
    long double sum = 0;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &score[i]);
        // 최대값
        if (score[i] > max_score) max_score = score[i];
    }

    for (int i = 0; i < n; i++) {
        sum += ((long double)score[i] / max_score) * 100;
    }
    printf("%Lf\n", sum / n);

    return 0;
}
