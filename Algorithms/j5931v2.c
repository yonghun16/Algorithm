// 숫자사각형 4-1
// https://www.jungol.co.kr/problem/5931

#include <stdio.h>
#include <stdlib.h>

int* getQuadrangle(int* arr, int inputVal_a);
int answer(int *arr, int inputval_a);

int main() {
    int inputVal_a;
    scanf("%d", &inputVal_a);

    int* arr = (int *)malloc(sizeof(int) * inputVal_a * inputVal_a);   // 동적할당

    answer(getQuadrangle(arr, inputVal_a), inputVal_a);  // 답변 출력

    free(arr);
    return 0;
}

int* getQuadrangle(int *arr, int inputVal_a) {
    int num = 1;

    for (int i = 0; i < inputVal_a * inputVal_a; i++) {
        arr[i] = (i + 1) % inputVal_a == 0 ? num++ : num;    // 한변의 크기(inputVal_a)
    }

    return arr;
}

int answer(int* arr, int inputVal_a) {
    for (int i = 0; i < inputVal_a * inputVal_a; i++) {
        if (i != 0 && i % inputVal_a == 0)
            printf("\n");
        printf("%d ", arr[i]);
    }
    
    return 0;
}
