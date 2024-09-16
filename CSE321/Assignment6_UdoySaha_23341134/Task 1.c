#include <stdlib.h>
#include <stdio.h>

int main()
{

    int n = 5;                        // Number of processes
    int m = 4;                        // Number of resources
    int alloc[5][4] = {{0, 1, 0, 3},  // P0// Allocation Matrix
                       {2, 0, 0, 0},  // P1
                       {3, 0, 2, 0},  // P2
                       {2, 1, 1, 5},  // P3
                       {0, 0, 2, 2}}; // P4
    int max[5][4] = {{6, 4, 3, 4},    // P0 // MAX Matrix
                     {3, 2, 2, 1},    // P1
                     {9, 1, 2, 6},    // P2
                     {2, 2, 2, 8},    // P3
                     {4, 3, 3, 7}};   // P4
    int avail[4] = {3, 3, 2, 1};      // Available resources

    // need matrix
    int need[n][m];

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            need[r][c] = max[r][c] - alloc[r][c];
        }
    }

    // bankers algorithm
    int finish[n];
    for (int i = 0; i < n; i++)
    {
        finish[i] = 0;
    }

    int count = 0;

    while (count < n)
    {
        int found = 0;
        for (int p = 0; p < n; p++)
        {
            if (finish[p] == 0)
            {
                int j;
                for (j = 0; j < m; j++)
                {
                    if (need[p][j] > avail[j])
                    {
                        break;
                    }
                }
                if (j == m)
                {
                    for (int k = 0; k < m; k++)
                    {
                        avail[k] += alloc[p][k];
                    }
                    finish[p] = 1;
                    found = 1;
                }
            }
        }
        if (found == 0)
        {
            printf("Deadlock Ahead\n");
            return 0;
        }
    }

    printf("Safe here\n");

    return 0;
}