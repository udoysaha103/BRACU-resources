#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{   
    int arr[] = {1, 2, 3, 4, 5};

    pid_t pid;
    pid = fork();
    
    if (pid == 0)
    {
        // child block
        execl("sort", "sort", "1", "2", "3", "4", "5", NULL);
    }
    else
    {
        // parent
        wait(NULL);
        execl("oddeven", "oddeven", "1", "2", "3", "4", "5", NULL);
    }
    
    return 0;
}