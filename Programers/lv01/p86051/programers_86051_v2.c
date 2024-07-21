#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;

    for(int i=0; i<numbers_len; i++)
        answer += numbers[i];

    return 45 - answer;
}

int main(void) {
	//input data
    int numbers[] = { 1, 2, 3, 4, 6, 7, 8, 0 };
	
	//process
    int numbers_len = sizeof(numbers)/sizeof(numbers[0]);
    printf("%d\n", solution(numbers, numbers_len));
}
