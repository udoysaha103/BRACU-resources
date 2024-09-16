#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *func_thread(int *n){
    printf("thread-%d running\n",*n);
    printf("thread-%d closed\n",*n);
}

int main(){
    for (int i = 0; i < 5; ++i) {
        pthread_t t1;

        pthread_create(&t1,NULL,(void *)func_thread,&i);
        pthread_join(t1,NULL);
    }
	
	return 0;
}