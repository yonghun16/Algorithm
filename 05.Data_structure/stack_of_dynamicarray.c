#include <stdio.h>
#include <stdlib.h>

#define SIZE 10
#define INF 99999999

// 스택에 요소 넣기
void push(int stack[], int *top, int data) {
    if (*top == SIZE - 1) {
        printf("스택 오버플로우가 발생했습니다.\n");
        return;
    }
    stack[++(*top)] = data;
}

// 스택에서 요소 빼기
int pop(int stack[], int *top) {
    if (*top == -1) {
        printf("스택 언더플로우가 발생했습니다.\n");
        return -INF;
    }
    return stack[(*top)--];
}

// 스택의 최상단 요소 가져오기
int peek(int stack[], int top) {
    if (top == -1) {
        printf("스택이 비어 있습니다.\n");
        return -INF;
    }
    return stack[top]; 
}

// 스택 출력
void display(int stack[], int top) {
    printf("\n   ↓ 스택의 최상단 \n");
    printf("│     │\n");
    for (int i = top; i >= 0; i--) {
        printf("│%4d │\n", stack[i]);
    }
    printf("└─────┘\n");
}

int main() {
    printf("─────────────────────────────────────\n");
    printf(" Dynamic Array을 이용한 Stack의 구현 \n");
    printf("─────────────────────────────────────\n");
    printf("\n");

    int c, n;
    int *stack = (int *)malloc(SIZE * sizeof(int));
    static int top = -1;

    while (1) {
        printf("Push(1), Pop(2), Peek(3), EXIT(0) : ");
        scanf("%d", &c);
        if (c == 1) {
            printf("Push 할 숫자를 적으세요 : ");
            scanf("%d", &n);
            push(stack, &top, n);
            display(stack, top);
        } else if (c == 2) {
            printf("* Pop value : %d\n", pop(stack, &top));
            display(stack, top);
        } else if (c == 3) {
            printf("* Peek value : %d\n\n", peek(stack, top));
        } else if (c == 0) {
            printf("프로그램을 종료합니다.\n");
            break;
        } else {
            printf("메뉴의 숫자를 입력해 주세요.\n\n");
            continue;
        }
    }

    free(stack);
    return 0;
}
