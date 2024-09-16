#include <pthread.h>
#include <stdio.h>
#include <string.h>

#define MAX 10 // producers and consumers can produce and consume upto MAX
#define BUFLEN 6
#define NUMTHREAD 2 /* number of threads */

void *consumer(int *id);
void *producer(int *id);
char buffer[BUFLEN];
char source[BUFLEN]; // from this array producer will store it's production into buffer
int pCount = 0;
int cCount = 0;
int buflen;

// initializing pthread mutex and condition variables
pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t nonEmpty = PTHREAD_COND_INITIALIZER;
pthread_cond_t full = PTHREAD_COND_INITIALIZER;

int thread_id[NUMTHREAD] = {0, 1};
int i = 0;
int j = 0;

main()
{
    /* define the type to be pthread */
    pthread_t thread[NUMTHREAD];
    strcpy(source, "abcdef");
    buflen = strlen(source);
    /* create 2 threads*/
    /* create one consumer and one producer */
    /* define the properties of multi threads for both threads  */
    // Write Code Here

    pthread_create(&thread[0], NULL, (void *)producer, &thread_id[0]);
    pthread_create(&thread[1], NULL, (void *)consumer, &thread_id[1]);

    // wait for the threads to finish
    pthread_join(thread[0], NULL);
    pthread_join(thread[1], NULL);
    return 0;
}


void *producer(int *id)
{
    /*
    1. Producer stores the values in the buffer (Here copies values from source[] to buffer[]).
    2. Use mutex and thread communication (wait(), sleep() etc.) for the critical section.
    3. Print which producer is storing which values using which thread inside the critical section.
    4. Producer can produce up to MAX
    */
    // Write code here

	int *producer_id = (int *)id;
    while (pCount < MAX)
    {
        pthread_mutex_lock(&count_mutex);

        while (j >= BUFLEN) // if buffer is full
        {
            pthread_cond_wait(&full, &count_mutex);
        }

        buffer[j] = source[pCount % buflen];
        printf("%d produced %c by Thread %d\n", pCount, buffer[j], *producer_id);

        j++;
        pCount++;

        pthread_mutex_unlock(&count_mutex);
        pthread_cond_signal(&nonEmpty); // signal that buffer is not empty
    }
    pthread_exit(NULL);

}


void *consumer(int *id)
{
    /*
    1. Consumer takes out the value from the buffer and makes it empty.
    2. Use mutex and thread communication (wait(), sleep() etc.) for critical
    section
    3. Print which consumer is taking which values using which thread inside the
    critical section.
    4. Consumer can consume up to MAX
    */
    // Write code here

	int *consumer_id = (int *)id;
    while (cCount < MAX)
    {
        pthread_mutex_lock(&count_mutex);
        while (j <= 0) // check if buffer is empty
        {
            pthread_cond_wait(&nonEmpty, &count_mutex); // wait until buffer is not empty
        }

        char val = buffer[0]; // consume the last value from the buffer
        printf("%d consumed %c by Thread %d\n", cCount, val, *consumer_id);

		for (int i = 0; i < j-1; i++)
		{
			buffer[i] = buffer[i + 1]; // shift the buffer to left
		}

        j--;
        cCount++;

        pthread_mutex_unlock(&count_mutex);
        pthread_cond_signal(&full); // signal that buffer is not full
    }
	
    pthread_exit(NULL);
}
