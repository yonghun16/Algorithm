/*-----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행시간 5
Link : https://www.acmicpc.net/problem/24266
Level: 브론즈3
Tag  : C, BigO
Memo
-----------------------------------------------------*/

/*
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
*/

#include <stdio.h>
#include <stdlib.h>

long long MenOfPassion(int A[], int n) {
    long long sum = 0;      // 결과가 매우 클 수 있으므로 long long 사용
    long long count = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                sum += (long long)A[i] * A[j] * A[k];
                count++;
            }
        }
    }
    // return sum;
    return count;
}

int main() {
    long long n;
    scanf("%lld", &n);

    int A[n + 1];

    for (int i = 0; i <= n; i++) {
        A[i] = rand() % 10 + 1;  // 1부터 10까지의 랜덤 정수
    }

    long long result_count = MenOfPassion(A, n);

    // 결과출력
    // 시간복잡도 -> n^3
    printf("%lld\n", result_count);
    /*printf("%lld\n", n*n*n);     // n^3의 최고차항 -> 3*/
    printf("%d\n", 3);

    return 0;
}
