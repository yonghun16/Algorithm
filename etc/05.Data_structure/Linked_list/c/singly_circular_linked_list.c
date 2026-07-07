/* ------------------------------------------------------------
 * File     : circular_linked_list.c
 * Brief    : 단일 원형 연결 리스트
 * Author   : 송용훈
 * Date     : 2025-11-23
 * Version  :
 * History
 * ------------------------------------------------------------ */

#include <stdio.h>
#include <stdlib.h>

// 노드 구조체
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 리스트 구조체
typedef struct CircularLinkedList {
    Node* head;
} CircularLinkedList;

// 리스트 초기화
void initList(CircularLinkedList* list) {
    list->head = NULL;
}

// 노드 생성
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// 리스트 끝에 노드 추가
void appendNode(CircularLinkedList* list, int data) {
    Node* newNode = createNode(data);

    if (list->head == NULL) {
        list->head = newNode;
        newNode->next = newNode;  // 자기 자신을 가리킴
    } else {
        Node* temp = list->head;
        while (temp->next != list->head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = list->head;
    }
}

// 리스트에서 노드 삭제 (값 기준)
void deleteNode(CircularLinkedList* list, int data) {
    if (list->head == NULL) return;

    Node* curr = list->head;
    Node* prev = NULL;

    // 단일 노드이면서 값이 일치하는 경우
    if (curr->data == data && curr->next == list->head) {
        free(curr);
        list->head = NULL;
        return;
    }

    // head 삭제인 경우
    if (curr->data == data) {
        // 마지막 노드 찾기
        Node* last = list->head;
        while (last->next != list->head) {
            last = last->next;
        }
        last->next = curr->next;
        list->head = curr->next;
        free(curr);
        return;
    }

    // 중간 혹은 끝 노드 삭제
    prev = curr;
    curr = curr->next;
    while (curr != list->head) {
        if (curr->data == data) {
            prev->next = curr->next;
            free(curr);
            return;
        }
        prev = curr;
        curr = curr->next;
    }
}

// 리스트 출력
void printList(CircularLinkedList* list) {
    if (list->head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* temp = list->head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != list->head);
    printf("(head)\n");
}

// 테스트
int main() {
    CircularLinkedList list;
    initList(&list);

    appendNode(&list, 10);
    appendNode(&list, 20);
    appendNode(&list, 30);
    appendNode(&list, 40);

    printf("Initial List:\n");
    printList(&list);

    deleteNode(&list, 10);
    printf("After deleting 10:\n");
    printList(&list);

    deleteNode(&list, 30);
    printf("After deleting 30:\n");
    printList(&list);

    deleteNode(&list, 40);
    printf("After deleting 40:\n");
    printList(&list);

    deleteNode(&list, 20);
    printf("After deleting 20:\n");
    printList(&list);

    return 0;
}
