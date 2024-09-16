// round robin scheduling algorithm

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int sumBT(int BT[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += BT[i];
    }
    return sum;
}

// an array based circular queue of length n
struct Queue
{
    int *arr;
    int front, rear;
};

int main()
{
    int n = 4;
    int P[] = {1, 2, 3, 4};
    int AT[] = {0, 0, 0, 0};
    int BT[] = {53, 17, 68, 24};
    int CT[] = {0, 0, 0, 0};
    int TA[] = {0, 0, 0, 0};
    int WT[] = {0, 0, 0, 0};

    // the queue
    struct Queue que;
    que.arr = (int *)malloc(n * sizeof(int));
    que.front = 0;
    que.rear = -1;

    // time quantum
    int tq = 20;

    // sorting according to arrival time
    for (int i = 0; i < n; i++)
    {
        int pos = i;
        for (int j = i + 1; j < n; j++)
        {
            if (AT[j] < AT[pos])
            {
                pos = j;
            }
        }

        int temp = P[i];
        P[i] = P[pos];
        P[pos] = temp;

        temp = AT[i];
        AT[i] = AT[pos];
        AT[pos] = temp;

        temp = BT[i];
        BT[i] = BT[pos];
        BT[pos] = temp;
    }

    // initialize the initial time of the first process
    int time = AT[0];

    // execute current process untill next process arrives
    que.rear++;
    que.arr[que.rear] = 0;
    int arrived = 0, current = que.arr[que.front];

    while (1)
    {
        // check if all processes have arrived and finished
        if (arrived == (n - 1))
        {
            if (sumBT(BT, n) == 0)
            {
                break;
            }
        }

        // check if all processes have arrived
        if (arrived == (n - 1))
        {
            int timeLeft = BT[current];

            if (timeLeft > tq)
            {
                timeLeft = tq;

                BT[current] -= timeLeft;
                time += timeLeft;

                // all other arrived processes are waiting
                for (int i = 0; i <= arrived; i++)
                {
                    if (BT[i] != 0 && i != current)
                    {
                        WT[i] += timeLeft;
                    }
                }

                que.rear = (que.rear + 1) % n;
                que.arr[que.rear] = current;
                que.front = (que.front + 1) % n;

                current = que.arr[que.front];
            }
            else
            {
                BT[current] -= timeLeft;
                time += timeLeft;

                CT[current] = time;
                TA[current] = CT[current] - AT[current];

                // all other arrived processes are waiting
                for (int i = 0; i <= arrived; i++)
                {
                    if (BT[i] != 0 && i != current)
                    {
                        WT[i] += timeLeft;
                    }
                }

                que.front = (que.front + 1) % n;
                current = que.arr[que.front];
            }
        }
        else
        {
            int timeLeft = BT[current];

            if (timeLeft > tq)
            {
                timeLeft = tq;
            }

            BT[current] -= timeLeft;
            time += timeLeft;

            // all other arrived processes are waiting
            for (int i = 0; i <= arrived; i++)
            {
                if (BT[i] != 0 && i != current)
                {
                    WT[i] += timeLeft;
                }
            }

            // check if any process has arrived
            for (int i = arrived+1; i < n; i++)
            {
                if (AT[i] <= time && BT[i] != 0)
                {
                    arrived++;
                    que.rear = (que.rear + 1) % n;
                    que.arr[que.rear] = i;
                }
            }

            // some part of the current process is still left
            if (BT[current] != 0)
            {
                que.rear = (que.rear + 1) % n;
                que.arr[que.rear] = current;

                que.front = (que.front + 1) % n;
                current = que.arr[que.front];
            }
            else  // current process has finished
            {
                CT[current] = time;
                TA[current] = CT[current] - AT[current];

                que.front = (que.front + 1) % n;
                current = que.arr[que.front];

                // check if there is no process in the queue
                if (que.front == (que.rear + 1) % n)
                {
                    que.rear = (que.rear + 1) % n;
                    que.arr[que.rear] = arrived + 1;
                    current = que.arr[que.front];

                    arrived++;
                    time = AT[current];
                }
            }
        }
    }

    // sorting according to process id
    for (int i = 0; i < n; i++)
    {
        int pos = i;
        for (int j = i + 1; j < n; j++)
        {
            if (P[j] < P[pos])
            {
                pos = j;
            }
        }

        int temp = P[i];
        P[i] = P[pos];
        P[pos] = temp;

        temp = AT[i];
        AT[i] = AT[pos];
        AT[pos] = temp;

        temp = BT[i];
        BT[i] = BT[pos];
        BT[pos] = temp;

        temp = CT[i];
        CT[i] = CT[pos];
        CT[pos] = temp;

        temp = TA[i];
        TA[i] = TA[pos];
        TA[pos] = temp;

        temp = WT[i];
        WT[i] = WT[pos];
        WT[pos] = temp;
    }

    printf("Process\tCompletion Time(CT)\tTurnaround Time(TAT)\tWaiting Time(WT)\n");

    for (int i = 0; i < n; i++)
    {
        printf("P%d\t\t%d\t\t\t%d\t\t\t%d\n", P[i], CT[i], TA[i], WT[i]);
    }

    return 0;
}