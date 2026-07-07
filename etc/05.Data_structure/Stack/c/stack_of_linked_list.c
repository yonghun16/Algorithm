#include <stdio.h>
#include <stdlib.h>

#define INF 9999999

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct Stack {
    Node *top;
} Stack;

// 스택에 요소 넣기
void push(Stack *stack, int data) {
    Node *curNode = (Node *)malloc(sizeof(Node));
    curNode->data = data;
    curNode->next = stack->top;
    stack->top = curNode;
}

// 스택에서 요소 빼기
int pop(Stack *stack) {
    if (stack->top == NULL) {
        printf("스택 언더플로우가 발생했습니다. \n");
        return -INF;
    }
    Node *curNode = stack->top;
    int data = curNode->data;
    stack->top = curNode->next;
    free(curNode);
    return data;
}

// 스택 출력
void show(Stack *stack) {
    Node *curNode = stack->top;
    printf("\n   ↓ 스택의 최상단 \n");
    printf("│     │\n");
    while (curNode != NULL) {
        printf("│%4d │\n", curNode->data);
        curNode = curNode->next;
    }
    printf("└─────┘\n");
}

int main(void) {
    Stack s;
    s.top = NULL;

    int c, n;
    printf("──────────────────────────────────────\n");
    printf("  Linked List를 이용한 Stackd 구현  \n");
    printf("──────────────────────────────────────\n");

    while (1) {
        printf("Push(1), Pop(2), EXIT(0) : ");
        scanf("%d", &c);
        if (c == 1) {
            printf("Push 할 숫자를 적으세요 : ");
            scanf("%d", &n);
            push(&s, n);
            show(&s);
        } else if (c == 2) {
            pop(&s);
            show(&s);
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
