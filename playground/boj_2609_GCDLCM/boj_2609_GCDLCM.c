/*-----------------------------------------------------
Sub  : [BOJ] 최대공약수와 최소공배수
Link : https://www.acmicpc.net/problem/2609
Level: 브론즈 1
Tag  : C,
Memo

-----------------------------------------------------*/

#include <stdio.h>

// 유클리드 알고리즘을 이용한 GCD (최대공약수)
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// LCM (최소공배수) 계산: (a * b) / gcd(a, b)
int lcm(int a, int b) {
    return (a / gcd(a, b)) * b; // 나눗셈 먼저 수행하여 오버플로 방지
}

int main() {
    int n, m;
    
    // 입력
    scanf("%d %d", &n, &m);

    // 출력
    printf("%d\n", gcd(n, m));
    printf("%d\n", lcm(n, m));

    return 0;
}
