#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
#define INF 99999999

int stack[SIZE];
int top = -1;

void push(int data) { 
    if(top == SIZE -1){
        printf("스텍 오버플로우가 발생했습니다.\n");
        return;
    }
    stack[++top] = data;
}

int pop() {
    if(top == -1){
        printf("스택 언더플로우가 발생했씁니다.\n");
        return -INF;
    }
    return stack[top--];
}

void show() {
    printf("\n   ↓ 스택의 최상단 \n");
    printf("│     │\n");
    for(int i = top; i>=0; i--){
        printf("│%4d │\n", stack[i]);
    }
    printf("└─────┘\n");
}

int main() {
    int c, n;
    printf("───────────────────────────────\n");
    printf("   배열을 이용한 스텍의 구현   \n");
    printf("───────────────────────────────\n");

    while(1){
        printf("Push(1), Pop(2), EXIT(0) : ");
        scanf("%d", &c);
        if(c == 1){
            printf("Push 할 숫자를 적으세요 : ");
            scanf("%d", &n);
            push(n);
            show();
        }
        else if(c == 2){
            pop();
            show();
        }
        else if(c == 0){
            printf("프로그램을 종료합니다.\n");
            break;
        }
    }

    return 0;
}
