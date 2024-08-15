// 윤년

#include <stdio.h>

int main() {
    int year;
    int result;

    scanf("%d", &year);
    if ( (!(year % 4) && year % 100) || !(year % 400)) {
        printf("1\n");
    }
    else {
        printf("0\n");
    }

    return 0;
}
