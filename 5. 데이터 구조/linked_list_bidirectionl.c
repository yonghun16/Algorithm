/* 양방향 링크드 리스트 */

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *prev; //이전 노드
    struct Node *next; //다음 노드
}Node;

Node *head, *tail;

void insert(int data){
    Node *newNode = (Node*)malloc(sizeof(Node)); // 새로운 노드 공간할당
    newNode->data = data;  // 새로운 노드에 data 삽입
    Node *curNode;      // 임시노드
    curNode = head->next;  //임시노드에 head의 다음 방향 가르킴

    while(curNode->data < data && curNode != tail) {  //오름차순 정렬 (순서대로 삽입)
        curNode = curNode->next;
    }
    //반복문이 끝나면 현재노드는 새로운 노드의 뒷 부분이 됨.
    Node *prevNode = curNode->prev; // 현재 노드의 이전 노드를 prevNode 라는 변수로 선언

    prevNode->next = newNode;   //이전 노드의 앞방향을 새로운 노드로
    newNode->prev = prevNode;   //새로운 노드의 뒷방향을 이전 노드로
    curNode->prev =newNode;     //현재 노드의 뒷방향을 새로운 노드로
    newNode->next =curNode;     //새로운 노드의 앞방향을 현재 노드로
}

void removeData(int data){
    Node *curNode = head->next;
    while(curNode != NULL){
        Node *prevNode = curNode->prev;
        if(curNode->data == data){
            Node *delNode = prevNode->next; 
            prevNode->next = delNode->next; 
            Node *nextNode = delNode->next; 
            nextNode->prev =prevNode; 
            free(delNode);
        }
        curNode = curNode->next;
    }
}

void freeAll(Node *head){
    Node *curNode = head->next;
    while(curNode != NULL){
        Node *nextNode = curNode->next;
        free(curNode);
        curNode = nextNode;
    }
}

void showAll(Node *head){
    Node *curNode = head->next;
    printf("-------------------------------\n");
    while(curNode != NULL && curNode->data != -999){
        printf("%d ", curNode->data);
        curNode = curNode->next;
    }
    printf("\n-------------------------------\n");
    printf("\n");
}

int main(){
    int n, c;

    head = (Node*)malloc(sizeof(Node));
    tail = (Node*)malloc(sizeof(Node));

    head->next = tail;
    head->prev = head;
    tail->next = NULL;
    tail->data = -999;
    tail->prev = head;

    while(1){
        printf("삽입(1) 삭제(2) 종료(0) : ");
        scanf("%d", &c);

        if(c == 1){
            printf("입력할 데이터 : ");
            scanf("%d", &n);
            insert(n);
            showAll(head);
        }
        else if(c == 2){
            printf("삭제할 데이터 : ");
            scanf("%d", &n);
            removeData(n);
            showAll(head);
        }
        else if(c == 0){
            printf("프로그램을 종료합니다. :) \n");
            freeAll(head);
            break;
        }
        else {
            printf(" 1, 2, 0 중 하나를 입력해 주세요\n");
        }
    }

    return 0;
}
