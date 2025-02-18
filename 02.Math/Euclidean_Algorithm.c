/*-----------------------------------------------------
Sub  : [BOJ] 최대공약수와 최소공배수
Link : https://www.acmicpc.net/problem/2609
Level: 브론즈 1
Tag  : C,
Memo
  - 두 수 A와 B (A > B)가 있을 때,
    👉 A와 B의 최대공약수(GCD)는 A를 B로 나눈 나머지(R)와 B의 최대공약수와 같다.
    즉, GCD(A, B) = GCD(B, A mod B)
    이 과정을 나머지가 0이 될 때까지 반복하면, 남은 값이 최대공약수가 됩니다.
  - 유클리드 알고리즘을 활용하면 **최소공배수(LCM)**도 쉽게 구할 수 있습니다.
    LCM(A, B) = (A * B) / GCD(A, B)
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
