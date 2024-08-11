// 팩토리얼 2
// https://www.acmicpc.net/problem/27433

#include <stdio.h>

#define MAX 500

void multiply(int x, int result[], int *result_size) {
    int carry = 0;
    for (int i = 0; i < *result_size; i++) {
        int prod = result[i] * x + carry;
        result[i] = prod % 10;
        carry = prod / 10;
    }
    
    while (carry) {
        result[(*result_size)++] = carry % 10;
        carry /= 10;
    }
}

void factorial(int n) {
    int result[MAX];
    
    result[0] = 1;
    int result_size = 1;
    
    for (int x = 2; x <= n; x++) {
        multiply(x, result, &result_size);
    }
    
    for (int i = result_size - 1; i >= 0; i--) {
        printf("%d", result[i]);
    }
    printf("\n");
}

int main() {
    int N;
    
    scanf("%d", &N);
    
    factorial(N);
    
    return 0;
}
