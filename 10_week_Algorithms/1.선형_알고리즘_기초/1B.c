// 문제1B-원소의 합 구하기


#include <stdio.h>

// 입력된 정수 배열의 합을 계산하는 함수
int getSum(int n, int inputNumbers[]) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += inputNumbers[i];
    }
    return sum;
}

int main() {
    // 첫 번째 줄에서 데이터의 수n을 읽습니다.
    int n;
    scanf("%d", &n);

    int inputNumbers[n];

    // 두 번째 줄에서 공백으로 구분된 n개의 정수를 읽어 옵니다.
    for (int i = 0; i < n; i++) {
        scanf("%d", &inputNumbers[i]);
    }
    
    // 합계 계산
    int answer = getSum(n, inputNumbers);
    
    // 결과 출력
    printf("%d\n", answer);
    
    return 0;
}
