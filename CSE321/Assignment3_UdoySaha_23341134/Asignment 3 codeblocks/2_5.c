#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = fork();

    if (pid == 0) {
        // Child process
        printf("2. Child process ID: %d\n", getpid());

        // Create three grandchild processes
        for (int i = 0; i < 3; ++i) {
            pid_t grandchild_pid;
            grandchild_pid = fork();

            if (grandchild_pid == 0) {
                // Grandchild process
                printf("%d. Grandchild process ID: %d\n", i+3, getpid());

                exit(EXIT_SUCCESS);
            }
        }

        // Wait for all grandchild processes to finish
        for (int i = 0; i < 3; ++i) {
            wait(NULL);
        }

        // Child process exits after all grandchild processes finish
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        printf("1. Parent process ID: %d\n", getpid());
        wait(NULL);
    }

    return 0;
}
