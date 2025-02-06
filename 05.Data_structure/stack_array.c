#include <stdio.h>

#define SIZE 10
#define INF 99999999

int stack[SIZE];
int top = -1;

// 스택 요소 넣기
void push(int data) {
    if (top == SIZE - 1) {
        printf("스텍 오버플로우가 발생했습니다.\n");
        return;
    }
    stack[++top] = data;
}

// 요소 빼기
int pop() {
    if (top == -1) {
        printf("스택 언더플로우가 발생했씁니다.\n");
        return -INF;
    }
    return stack[top--];
}

// 스택 보여주기
void display() {
    printf("\n   ↓ 스택의 최상단 \n");
    printf("│     │\n");
    for (int i = top; i >= 0; i--) {
        printf("│%4d │\n", stack[i]);
    }
    printf("└─────┘\n");
}

int main() {
    printf("───────────────────────────────\n");
    printf("  Array을 이용한 Stack의 구현  \n");
    printf("───────────────────────────────\n");
    printf("\n");

    int c, n;

    while (1) {
        printf("Push(1), Pop(2), EXIT(0) : ");
        scanf("%d", &c);
        if (c == 1) {
            printf("Push 할 숫자를 적으세요 : ");
            scanf("%d", &n);
            push(n);
            display();
        } else if (c == 2) {
            pop();
            display();
        } else if (c == 0) {
            printf("프로그램을 종료합니다.\n");
            break;
        } else {
            printf("메뉴의 숫자를 입력해 주세요.\n\n");
            continue;
        }
    }

    return 0;
}
