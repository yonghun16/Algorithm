#include <stdio.h>

#define SIZE 5

int queue[SIZE];
int front = 0, rear = 0;

int isFull() {
    return rear == SIZE;
}

int isEmpty() {
    return front == rear;
}

// 큐에 요소 삽입
void enqueue(int value) {
    if (isFull()) {
        printf("Queue is full!\n");
        return;
    }
    queue[rear++] = value;
}

// 큐에서 요소 제거
int dequeue() {
    if (isEmpty()) {
        printf("Queue is empty!\n");
        return -1;
    }
    int data = queue[0];
    for (int i = 0; i < rear - 1; i++) {
        queue[i] = queue[i + 1];
    }
    rear--;
    return data;
}

// 큐 출력
void display() {
    if (isEmpty()) {
        printf("Queue is empty!\n");
        return;
    }
    printf("\n");
    printf("\n───────────────────────────────\n");
    for (int i = 0; i < rear; i++) {
        printf("%d ", queue[i]);
    }
    printf("\n───────────────────────────────\n\n");
}

int main() {
    printf("───────────────────────────────\n");
    printf("   Array 이용한 queue의 구현   \n");
    printf("───────────────────────────────\n");
    printf("\n");

    int c, n;

    while (1) {
        printf("enqueue(1), dequeue(2), EXIT(0) : ");
        scanf("%d", &c);
        if (c == 1) {
            printf("enqueue 할 숫자를 적으세요 : ");
            scanf("%d", &n);
            enqueue(n);
            display();
        } else if (c == 2) {
            dequeue();
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
