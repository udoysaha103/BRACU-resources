// priority scheduling algorithm

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

int main()
{
    int n = 5;
    int P[] = {1, 2, 3, 4, 5};
    int AT[] = {0, 14, 3, 9, 7};
    int BT[] = {15, 5, 10, 22, 16};
    int priority[] = {2, 4, 0, 3, 1};
    int CT[] = {0, 0, 0, 0, 0};
    int TA[] = {0, 0, 0, 0, 0};
    int WT[] = {0, 0, 0, 0, 0};

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

        temp = priority[i];
        priority[i] = priority[pos];
        priority[pos] = temp;
    }

    // initialize the initial time of the first process
    int time = AT[0];

    // execute current process untill next process arrives
    int arrived = 0, current = 0;

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

            BT[current] -= timeLeft;
            time += timeLeft;

            CT[current] = time;
            TA[current] = CT[current] - AT[current];

            // all other arrived processes are waiting
            for (int i = 0; i <= arrived; i++)
            {
                if (BT[i] != 0)
                {
                    WT[i] += timeLeft;
                }
            }

            // select the already arrived process with smallest priority
            int now = -1;
            for (int i = 0; i <= arrived; i++)
            {
                if (BT[i] != 0)
                {
                    now = i;
                    break;
                }
            }
            for (int i = now + 1; i <= arrived; i++)
            {
                if (BT[i] != 0 && priority[i] < priority[now])
                {
                    now = i;
                }
            }

            // if no process is selected
            if (now == -1)
            {
                // all processes have finished
                break;
            }
            else  // a process is selected
            {
                current = now;
            }
        }
        // all process have not arrived
        else
        {
            int nextAT = AT[arrived + 1];
            
            // if this is the time for next process to arrive
            if (time == nextAT)
            {
                arrived++;
                
                // select the already arrived process with smallest priority
                int now = -1;
                for (int i = 0; i <= arrived; i++)
                {
                    if (BT[i] != 0)
                    {
                        now = i;
                        break;
                    }
                }
                for (int i = now + 1; i <= arrived; i++)
                {
                    if (BT[i] != 0 && priority[i] < priority[now])
                    {
                        now = i;
                    }
                }

                // if no process is selected
                if (now == -1)
                {
                    // select the next arrived process
                    arrived++;

                    current = arrived;
                    time = AT[current];
                }
                else  // a process is selected
                {
                    current = now;
                }
            }
            else  // current process is executing
            {
                BT[current]--;
                time++;

                // all other arrived processes are waiting
                for (int i = 0; i <= arrived; i++)
                {
                    if (i != current && BT[i] != 0)
                    {
                        WT[i]++;
                    }
                }

                // if current process has finished
                if (BT[current] == 0)
                {
                    CT[current] = time;
                    TA[current] = CT[current] - AT[current];

                    // select the already arrived process with smallest priority
                    int now = -1;
                    for (int i = 0; i <= arrived; i++)
                    {
                        if (BT[i] != 0)
                        {
                            now = i;
                            break;
                        }
                    }
                    for (int i = now + 1; i <= arrived; i++)
                    {
                        if (BT[i] != 0 && priority[i] < priority[now])
                        {
                            now = i;
                        }
                    }

                    // if no process is selected
                    if (now == -1)
                    {
                        // select the next arrived process
                        arrived++;

                        current = arrived;
                        time = AT[current];
                    }
                    else  // a process is selected
                    {
                        current = now;
                    }
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

        temp = priority[i];
        priority[i] = priority[pos];
        priority[pos] = temp;
    }

    printf("Process\tCompletion Time(CT)\tTurnaround Time(TAT)\tWaiting Time(WT)\n");

    for (int i = 0; i < n; i++)
    {
        printf("P%d\t\t%d\t\t\t%d\t\t\t%d\n", P[i], CT[i], TA[i], WT[i]);
    }

    return 0;
}