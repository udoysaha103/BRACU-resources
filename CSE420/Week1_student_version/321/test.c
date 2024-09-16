#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char teststr[] = "The quick brown fox jumps over the lazy dog.\n";

int main()
{
    int fd;
    int len;
    ssize_t r;
    fd = open("testfile", O_WRONLY | O_CREAT, 0600);

    printf("fd = %d\n", fd);

    if (fd < 0)
    {
        /* just ungracefully bail out */
        perror("File open failed");
        exit(1);
    }

    len = strlen(teststr);
    printf("Attempting to write %d bytes\n", len);

    r = write(fd, teststr, len);

    if (r < 0)
    {
        perror("File write failed");
        exit(1);
    }

    printf("Wrote %d bytes\n", (int)r);
    close(fd);
}

/*

1.
The code firstly opens a file in write only mode. If the file is not present, it creates the file.
Then it writes the string 'teststr' to the file and closes the file.
In between, it calculates the length of the string in bytes and prints it.

The output will be same as the 'teststr' string value.
The 'testfile' will have - "The quick brown fox jumps over the lazy dog.\n"

2.
In addition to O_WRONLY, we can use O_RDWR or O_APPEND to open a file.

3.
Open returns the I/O channel to fd. It is used as a reference to an open file in a process.
For the case of successful file open, fd will be a positive integer (usually 3).
In case of failure, it will be a negative integer.
*/