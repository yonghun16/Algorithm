// 검증수
// https://www.acmicpc.net/problem/2475

#include <stdio.h>

// 검증수를 구하는 함수
int getVerification(int numbers[]) {
    int sum=0;
    for (int i=0; i<5;i++) {
        sum += numbers[i]*numbers[i];
    }
    return sum%10;
}

int main() {
    int numbers[5];
    int answer;

    for (int i=0; i<5; i++) {
        scanf("%d", &numbers[i]);
    }

    answer = getVerification(numbers);
    printf("%d\n", answer);

    return 0;
}
