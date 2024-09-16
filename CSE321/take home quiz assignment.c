#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

// number of threads
#define n 12

int persons[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
int count = 10;  // tickets left

// a semaphore for each thread
sem_t* semaphores;

void *t_func(int *idp)
{
    int id = * (int*) idp;

    // wait for our semaphore to become unlocked
    sem_wait(&semaphores[id]);
    
    if (count > 0)
    {
        printf("Person %d is purchasing\n", id+1);
        printf("Tickets left: %d\n", count);
        count--;
        printf("Person: %d, Purchase Done\n", id+1);
    }
    else
    {
        printf("Person %d can not purchase\n", id+1);
        printf("Tickets left: %d\n", count);
        printf("Person: %d, Purchase failed\n", id+1);
    }

    // unlock the semaphore belonging to the next thread (unless last)
    if (id < (n - 1)) {
        sem_post(&semaphores[id + 1]);
    }
}

int main()
{
    pthread_t t[n];

    // create the semaphores
    sem_t s[n];
    semaphores = s;

    // initialize the semaphores to 0
    for (int i = 0; i < n; i++) {
        sem_init(&semaphores[i], 0, 0);
    }

    // unlock thread 0
    sem_post(&semaphores[0]);

    // create the threads
    for (int i = 0; i < n; i++)
    {
        pthread_create(&t[i], NULL, (void *)t_func, &persons[i]);
    }

    // wait for the threads to finish
    for (int i = 0; i < n; i++)
    {
        pthread_join(t[i], NULL);
    }

    // destroy the semaphores
    for (int i = 0; i < n; i++) {
        sem_destroy(&semaphores[i]);
    }
    free(semaphores);

    return 0;
}