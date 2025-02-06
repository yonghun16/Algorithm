#include <stdio.h>

#define MAX 10

int stack[MAX];

int top = -1;

void push(int n) {
   stack[++top] = n;
}

int pop() {
    if (top == -1) {
        printf("스텍이 비어 있습니다.\n");
    }
    return stack[top--];
}

void display() {
    for (int i=top; i>=0; i--) {
        printf("%d \n", stack[i]);
    }
}

int main() {

    push(10);
    push(20);
    push(34);
    display();
    printf("\n");

    pop();
    pop();
    push(323);
    display();
    pop();
    pop();
    pop();
    pop();
    pop();
    display();

    return 0;
}
