// 킹, 퀸, 룩, 비숍, 나이트, 폰
// https://www.acmicpc.net/problem/3003

#include <stdio.h>

int main() {
    int piecesOfInput[6];  // king, queen, rook, bishop, knight, pawn
    int piecesOfRight[6] = {1, 1, 2, 2, 2, 8};
    int results[6];

    for(int i = 0; i < 6; i++) {
        scanf("%d", &piecesOfInput[i]);
    }

    for (int i = 0; i<6; i++) {
        results[i] = piecesOfRight[i] - piecesOfInput[i];
        printf("%d ", results[i]);
    }
    printf("\n");

    return 0;
}