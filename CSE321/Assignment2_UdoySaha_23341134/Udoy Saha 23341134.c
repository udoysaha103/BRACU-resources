/*
1. Get an integer array as input.
2. Create two threads.
3. Thread 1 sums the even elements of the array.
4. Thread 2 sums the odd elements of the array.
5. You can declare only 1 function outside the main function.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *thread1(void *arr, int *parity){
    int *x = arr;
    int sum = 0;

    if(parity == 0){
        printf("Entered thread1:\n");

        for(int i=0; i<4; i++){
            if(x[i]%2 == 0){
                sum += x[i];
            }
        }

        printf("Sum of even elements from Thread 1: %d\n", sum);
    }
    else{
        printf("Entered thread2:\n");

        for(int i=0; i<4; i++){
            if(x[i]%2 != 0){
                sum += x[i];
            }
        }

        printf("Sum of odd elements from Thread 2: %d\n", sum);
    
    }
}

int main(){
    // Get an integer array as input.
    int arr[4];
    for(int i=0;i<4;i++){
        scanf("%d",&arr[i]);
    }

    // Create two threads.
	pthread_t t1, t2;

	pthread_create(&t1,NULL,thread1,((void *)arr, 0));  // 0 for even
	pthread_create(&t2,NULL,thread1,((void *)arr, 1));  // 1 for odd
	
	pthread_join(t1,NULL);
	pthread_join(t2,NULL);
	
	return 0;
}