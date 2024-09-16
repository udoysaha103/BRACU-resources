#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>

void *t_ret1, *t_ret2, *t_ret3;

int sum_of_chars(char *name){
    int sum = 0;
    for (int i = 0; i < strlen(name); ++i) {
        sum += name[i];
    }
    return sum;
}

void *func_thread(char *name){
    pthread_exit((void *)sum_of_chars(name));
}

int main(){
    char name1[] = "af";
    char name2[] = "be";
    char name3[] = "cd";

    pthread_t t1, t2, t3;

    pthread_create(&t1,NULL,(void *)func_thread,name1);
    pthread_create(&t2,NULL,(void *)func_thread,name2);
    pthread_create(&t3,NULL,(void *)func_thread,name3);

    pthread_join(t1,&t_ret1);
    pthread_join(t2,&t_ret2);
    pthread_join(t3,&t_ret3);

    if (t_ret1 == t_ret2 && t_ret2 == t_ret3){
        printf("Youreka\n");
    } else if (t_ret1 == t_ret2 || t_ret2 == t_ret3 || t_ret1 == t_ret3){
        printf("Miracle\n");
    } else {
        printf("Hasta la vista\n");
    }
    
    return 0;
}