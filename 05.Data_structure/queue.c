#include <stdio.h>
#include <stdlib.h>

#define SIZE 5  // 큐의 크기

typedef struct {
    int items[SIZE];
    int front, rear;
} CircularQueue;

// 큐 초기화
void initQueue(CircularQueue *q) {
    q->front = -1;
    q->rear = -1;
}

// 큐가 가득 찼는지 확인
int isFull(CircularQueue *q) { return ((q->rear + 1) % SIZE == q->front); }

// 큐가 비어있는지 확인
int isEmpty(CircularQueue *q) { return (q->front == -1); }

// 큐에 요소 추가 (enqueue)
void enqueue(CircularQueue *q, int value) {
    if (isFull(q)) {
        printf("큐가 가득 찼습니다!\n");
        return;
    }

    if (isEmpty(q)) {
        q->front = 0;
    }

    q->rear = (q->rear + 1) % SIZE;
    q->items[q->rear] = value;
    printf("Enqueued: %d\n", value);
}

// 큐에서 요소 제거 (dequeue)
int dequeue(CircularQueue *q) {
    if (isEmpty(q)) {
        printf("큐가 비어 있습니다!\n");
        return -1;
    }

    int value = q->items[q->front];

    if (q->front == q->rear) {
        // 큐에 한 개의 요소만 있을 경우 초기화
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % SIZE;
    }

    printf("Dequeued: %d\n", value);
    return value;
}

// 큐의 상태 출력
void displayQueue(CircularQueue *q) {
    if (isEmpty(q)) {
        printf("큐가 비어 있습니다!\n");
        return;
    }

    printf("큐 요소: ");
    int i = q->front;
    while (1) {
        printf("%d ", q->items[i]);
        if (i == q->rear) break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

// 메인 함수
int main() {
    CircularQueue q;
    initQueue(&q);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    enqueue(&q, 40);
    enqueue(&q, 50);

    displayQueue(&q);

    dequeue(&q);
    dequeue(&q);

    displayQueue(&q);

    enqueue(&q, 60);
    enqueue(&q, 70);

    displayQueue(&q);

    return 0;
}
