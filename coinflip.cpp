#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define HEADS 0
#define TAILS 1

#define GAMES 100000

int main()
{   
    srand((unsigned int)time(NULL));

    int heads = 0;

    for (int i = 0; i < GAMES; i++)
    {
        int coin = HEADS;

        // COMPUTER FLIP?
        if (rand() % 2) coin = rand() % 2;

        // HUMAN FLIP?
        if (rand() % 2) coin = rand() % 2;

        // COMPUTER FLIP?
        if (rand() % 2) coin = rand() % 2;

        if (coin == HEADS) heads++;
    }
    printf("Heads %d out of %d games\n", heads, GAMES);

    return 0;
}