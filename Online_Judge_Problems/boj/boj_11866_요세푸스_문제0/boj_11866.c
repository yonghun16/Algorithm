/*-----------------------------------------------------
Sub  : [BOJ] 요세푸스 문제0
Link : https://www.acmicpc.net/problem/11866
Level: 실버 4
Tag  : C, Queue
Memo
-----------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    int *arr = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) arr[i] = i + 1;

    int size = N, idx = 0;
    printf("<");

    for (int i = 0; i < N; i++) {
        idx = (idx + K - 1) % size;  // K번째 사람
        printf("%d", arr[idx]);

        if (i != N - 1) printf(", ");

        for (int j = idx; j < size - 1; j++) {
            arr[j] = arr[j + 1];  // 제거 후 시프트
        }
        size--;
    }
    printf(">\n");

    free(arr);
    return 0;
}
