#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int num = 1;

void *func_thread(int *n){
    for (int i = 0; i < 5; ++i) {
        printf("Thread %d prints %d\n",*n,num);
        num++;
    }
}

int main(){
    for (int i = 0; i < 5; ++i) {
        pthread_t t1;

        pthread_create(&t1,NULL,(void *)func_thread,&i);
        pthread_join(t1,NULL);
    }
	
	return 0;
}