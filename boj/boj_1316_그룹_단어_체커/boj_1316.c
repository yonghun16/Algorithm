/*-----------------------------------------------------
Sub  : [BOJ] 그룹 단어 체커
Link : https://www.acmicpc.net/problem/1316
Level: 실버 5
Tag  : C, String
Memo
-----------------------------------------------------*/

#include <stdio.h>
#include <string.h>

// 그룹 단어인지 확인하는 함수
int is_group_word(const char *word) {
    int seen[26] = {0};  // 알파벳 방문 여부 저장
    char prev = 0;

    for (int i = 0; word[i] != '\0'; i++) {
        char current = word[i];
        if (current != prev) {
            if (seen[current - 'a']) {
                return 0;
            }
            seen[current - 'a'] = 1;
        }
        prev = current;
    }
    return 1;
}

int main() {
    int N, count = 0;
    char word[101];

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%s", word);
        if (is_group_word(word)) {
            count++;
        }
    }

    printf("%d\n", count);
    return 0;
}
