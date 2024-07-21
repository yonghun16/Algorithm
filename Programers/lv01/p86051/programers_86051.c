#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int check_numbers[10] = { 0, };

    for(int i=0; i<numbers_len; i++) {
        check_numbers[numbers[i]]++;
    }

    for(int i=0; i<10; i++) {
        if(check_numbers[i] == 0) {
            answer += i;
        }
    }
    return answer;
}

int main(void) {
    int numbers[] = { 1, 2, 3, 4, 6, 7, 8, 0 };
    int numbers_len = sizeof(numbers)/sizeof(numbers[0]);
    printf("%d\n", solution(numbers, numbers_len));
}
