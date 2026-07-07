// 대소문자 바꾸기
// https://www.acmicpc.net/problem/2744

#include <stdio.h>
#include <ctype.h>

int main() {
    char word[101]; // 단어의 최대 길이는 100이므로 101 크기로 배열 선언
    scanf("%100s", word); // 단어 입력 받기

    for (int i = 0; word[i] != '\0'; i++) {
        if (islower(word[i])) {
            word[i] = toupper(word[i]);
        } else if (isupper(word[i])) {
            word[i] = tolower(word[i]);
        }
    }

    printf("%s\n", word); // 변환된 단어 출력

    return 0;
}