// A+B
// https://www.acmicpc.net/problem/1000
// v2 : 문자열로 덧셈하여 큰 수 커버 가능하게 하기

#include <stdio.h>
#include <string.h>

#define MAX_DIGITS 1000

// 문자열로 큰 수의 합 구하기
void getSum(const char* a, const char* b, char* answer) {
    int len1 = strlen(a);
    int len2 = strlen(b);
    int carry = 0, sum;
    int i = len1 - 1, j = len2 - 1, k = 0;
    
    // 결과를 임시로 저장할 배열
    char tempResult[MAX_DIGITS + 1] = {0};

    // 뒤에서부터 각 자릿수를 더하기
    while (i >= 0 || j >= 0 || carry > 0) {
        int digit1 = (i >= 0) ? a[i--] - '0' : 0;
        int digit2 = (j >= 0) ? b[j--] - '0' : 0;
        sum = digit1 + digit2 + carry;
        carry = sum / 10;
        tempResult[k++] = (sum % 10) + '0';
    }

    // 결과 뒤집기
    for (int l = 0; l < k; l++) {
        answer[l] = tempResult[k - 1 - l];
    }
    answer[k] = '\0';
}

int main() {
    char a[MAX_DIGITS + 1], b[MAX_DIGITS + 1], answer[MAX_DIGITS + 2];

    scanf("%1000s %1000s", a, b);

    getSum(a, b, answer);

    printf("%s\n", answer);

    return 0;
}
