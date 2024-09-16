#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <semaphore.h>

int count = 0;
sem_t semaphore;

int main()
{
    if (sem_init(&semaphore, 0, 1) == -1)
    {
        perror("Semaphore initialization failed");
        exit(EXIT_FAILURE);
    }

    printf("Count = %d\n", count);
    pid_t a, b, c, d;
    a = fork();
    b = fork();
    c = fork();

    if (a == 0)
    {
        // child block
        if (getpid() % 2 != 0) // odd, create another child
        {
            d = fork();

            if (d == 0)
            {
                // grandchild

                sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                count++;
                sem_post(&semaphore); // Release the semaphore after updating count

                printf("Count = %d\n", count);
                exit(EXIT_SUCCESS);
            }
            else
            {
                // child
                wait(NULL);

                sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                count++;
                sem_post(&semaphore); // Release the semaphore after updating count

                printf("Count = %d\n", count);
                exit(EXIT_SUCCESS);
            }
        }
        else // even, no child created
        {
            // child

            sem_wait(&semaphore); // Wait on the semaphore to access the critical section
            count++;
            sem_post(&semaphore); // Release the semaphore after updating count

            printf("Count = %d\n", count);
            exit(EXIT_SUCCESS);
        }
    }
    else
    {
        // parent block
        wait(NULL);

        if (b == 0)
        {
            // child block
            if (getpid() % 2 != 0) // odd, create another child
            {
                d = fork();

                if (d == 0)
                {
                    // grandchild

                    sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                    count++;
                    sem_post(&semaphore); // Release the semaphore after updating count

                    printf("Count = %d\n", count);
                    exit(EXIT_SUCCESS);
                }
                else
                {
                    // child
                    wait(NULL);

                    sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                    count++;
                    sem_post(&semaphore); // Release the semaphore after updating count

                    printf("Count = %d\n", count);
                    exit(EXIT_SUCCESS);
                }
            }
            else // even, no child created
            {
                // child

                sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                count++;
                sem_post(&semaphore); // Release the semaphore after updating count

                printf("Count = %d\n", count);
                exit(EXIT_SUCCESS);
            }
        }
        else
        {
            // parent block
            wait(NULL);

            if (c == 0)
            {
                // child block
                if (getpid() % 2 != 0) // odd, create another child
                {
                    d = fork();

                    if (d == 0)
                    {
                        // grandchild

                        sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                        count++;
                        sem_post(&semaphore); // Release the semaphore after updating count

                        printf("Count = %d\n", count);
                        exit(EXIT_SUCCESS);
                    }
                    else
                    {
                        // child
                        wait(NULL);

                        sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                        count++;
                        sem_post(&semaphore); // Release the semaphore after updating count

                        printf("Count = %d\n", count);
                        exit(EXIT_SUCCESS);
                    }
                }
                else // even, no child created
                {
                    // child

                    sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                    count++;
                    sem_post(&semaphore); // Release the semaphore after updating count

                    printf("Count = %dd\n", count);
                    exit(EXIT_SUCCESS);
                }
            }
            else
            {
                // parent block
                wait(NULL);
                wait(NULL);
                wait(NULL);

                sem_wait(&semaphore); // Wait on the semaphore to access the critical section
                count++;
                sem_post(&semaphore); // Release the semaphore after updating count

                printf("Count = %d\n", count);
                printf("Total processes created: %d\n", count);
            }
        }
    }

    return 0;
}