// 엄청난 부자2
// https://www.acmicpc.net/problem/1271

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DIGITS 1000 // 최대 자릿수

int main(void) {

    char a[100];
    char b[100];
    scanf("%s %s", a, b);

    int a_len = strlen(a);
    int b_len = strlen(b);

    for (int i=a_len; i>=0; i--) {
       printf("%c", a[i]);    // a[i] 
    }


    return 0;
}
