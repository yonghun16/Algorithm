/*-----------------------------------------------------
Sub  : [Goorm] 막대기
Link : https://level.goorm.io/exam/48193/막대기/quiz/1
Level: 1
Tag  : C, 
Memo
-----------------------------------------------------*/

#include <stdio.h>

int main() {

    return 0;
}

#include <stdio.h>

int main() {

    return 0;
}

#include <stdio.h>
int main() {
    int n;
    int h[100000]={0,};
    int count=1; //시작부터 마지막꺼 포함
    int temp;
    //입력부분
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &h[i]);
    }
    //연산
    temp = h[n-1];
    for(int j=n-2; j>=0; j--){
        if(h[j]>temp){
            temp=h[j];
            count++;
        }
    }
    //출력
    printf("%d", count);

    return 0;
}
