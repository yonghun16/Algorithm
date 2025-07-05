/*-----------------------------------------------------
Sub  : [BOJ] 최소, 최대
Link : https://www.acmicpc.net/problem/10818
Level: 브론즈 5
Tag  : C, 
Memo
-----------------------------------------------------*/

#include <stdio.h>

int main() {
    int n;
    int min = 1000000;
    int max = -1000000;

    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        int num;
        
        scanf("%d", &num);
        if(num < min) min = num;
        if(num > max) max = num;
    }

    printf("%d %d\n", min, max);

    return 0;
}
