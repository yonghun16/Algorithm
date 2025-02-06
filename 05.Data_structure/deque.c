#include <stdio.h>
#include <stdlib.h>

#define MAX 5

// 덱 구조체 정의
typedef struct {
    int arr[MAX];
    int front, rear;
} Deque;

// 덱 초기화
void initDeque(Deque* dq) {
    dq->front = -1;
    dq->rear = -1;
}

// 덱이 비었는지 확인
int isEmpty(Deque* dq) { return (dq->front == -1); }

// 덱이 꽉 찼는지 확인
int isFull(Deque* dq) { return (dq->rear == MAX - 1); }

// 앞에 요소 삽입
void insertFront(Deque* dq, int value) {
    if (isFull(dq)) {
        printf("Deque is full\n");
        return;
    }
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else if (dq->front == 0) {
        dq->front = MAX - 1;
    } else {
        dq->front--;
    }
    dq->arr[dq->front] = value;
}

// 뒤에 요소 삽입
void insertRear(Deque* dq, int value) {
    if (isFull(dq)) {
        printf("Deque is full\n");
        return;
    }
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else {
        dq->rear = (dq->rear + 1) % MAX;
    }
    dq->arr[dq->rear] = value;
}

// 앞에서 요소 삭제
void deleteFront(Deque* dq) {
    if (isEmpty(dq)) {
        printf("Deque is empty\n");
        return;
    }
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else {
        dq->front = (dq->front + 1) % MAX;
    }
}

// 뒤에서 요소 삭제
void deleteRear(Deque* dq) {
    if (isEmpty(dq)) {
        printf("Deque is empty\n");
        return;
    }
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else if (dq->rear == 0) {
        dq->rear = MAX - 1;
    } else {
        dq->rear--;
    }
}

// 덱의 앞부분 요소 보기
int getFront(Deque* dq) {
    if (isEmpty(dq)) {
        printf("Deque is empty\n");
        return -1;
    }
    return dq->arr[dq->front];
}

// 덱의 뒷부분 요소 보기
int getRear(Deque* dq) {
    if (isEmpty(dq)) {
        printf("Deque is empty\n");
        return -1;
    }
    return dq->arr[dq->rear];
}

// 덱의 상태 출력
void display(Deque* dq) {
    if (isEmpty(dq)) {
        printf("Deque is empty\n");
        return;
    }
    int i = dq->front;
    while (i != dq->rear) {
        printf("%d ", dq->arr[i]);
        i = (i + 1) % MAX;
    }
    printf("%d\n", dq->arr[dq->rear]);
}

int main() {
    Deque dq;
    initDeque(&dq);

    insertRear(&dq, 5);
    insertRear(&dq, 10);
    insertFront(&dq, 15);
    insertFront(&dq, 20);

    printf("Deque after insertions: ");
    display(&dq);

    deleteFront(&dq);
    printf("Deque after deleting front: ");
    display(&dq);

    deleteRear(&dq);
    printf("Deque after deleting rear: ");
    display(&dq);

    printf("Front element: %d\n", getFront(&dq));
    printf("Rear element: %d\n", getRear(&dq));

    return 0;
}
