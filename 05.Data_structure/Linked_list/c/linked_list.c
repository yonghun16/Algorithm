#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 연결 리스트에 새 노드 추가
void addNode(Node** head, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));  // 새 노드 생성
    if (newNode == NULL) {
        printf("메모리 할당 실패\n");
        return;
    }
    newNode->data = value;  // 값 할당
    newNode->next = *head;  // 새 노드의 next를 현재 head로 설정
    *head = newNode;        // head를 새 노드로 갱신
}

// 연결 리스트 출력
void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// 메모리 해제
void freeList(Node* head) {
    Node* current = head;
    Node* nextNode;
    while (current != NULL) {
        nextNode = current->next;
        free(current);
        current = nextNode;
    }
}

int main() {
    Node* head = NULL;  // 리스트의 처음은 NULL로 설정

    // 노드 추가
    addNode(&head, 10);
    addNode(&head, 20);
    addNode(&head, 30);

    // 연결 리스트 출력
    printf("연결 리스트: ");
    printList(head);

    // 메모리 해제
    freeList(head);

    return 0;
}
