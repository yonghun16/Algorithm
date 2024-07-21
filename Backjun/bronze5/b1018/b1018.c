#include <stdio.h>

#define MAX_WIDTH 51
#define MAX_HEIGHT 51

char board[MAX_WIDTH][MAX_HEIGHT];
int main()
{
	int n, m;
    int i, j;

	scanf("%d %d", &n, &m);

	for (i = 0; i < n; i++)
		scanf("%s", &board[i]);
	int sr, sc, min = 64;

	for (sr = 0; sr <= n - 8; sr++) {
		for (sc = 0; sc <= m - 8; sc++) {
			int count1 = 0, count2 = 0;
			char c = board[sr][sc];
			for (i = 0; i < 8; i++) {
				for (j = 0; j < 8; j++) {
					if (i % 2 == j % 2) {
						if (board[sr + i][sc + j] == c)
							count2++;
						else
							count1++;
					}
					else {
						if (board[sr + i][sc + j] == c)
							count1++;
						else
							count2++;
					}
				}
			}
			if (count1 < min)
				min = count1;
			if (count2 < min)
				min = count2;
		}
	}
	printf("%d", min);
    return 0;
}
