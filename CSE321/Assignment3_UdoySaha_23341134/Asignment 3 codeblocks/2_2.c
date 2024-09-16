#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    pid_t pid;
    int status;
    pid = fork();

    if (pid == 0)
    {
        // child block
        pid_t pid2;
        pid2 = fork();

        if (pid2 == 0)
        {
            // grandchild
            printf("I am grandchild\n");
        }
        else
        {
            // child
            wait(&status);
            printf("I am child\n");
        }
    }
    else
    {
        // parent
        wait(&status);
        printf("I am parent\n");
    }

    return 0;
}