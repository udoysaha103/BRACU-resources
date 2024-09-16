#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *file_pointer;
    char string[100];

    if (argc == 2)
    {
        file_pointer = fopen(argv[1], "w");

        if (file_pointer == NULL)
        {
            printf("File could not be opened!\n");
            return 1;
        }

        while (1)
        {
            printf("Enter string: ");
            scanf(" %s", string);
            if (strcmp(string, "-1") == 0)
            {
                break;
            }
            fprintf(file_pointer, "%s\n", string);
        }

        fclose(file_pointer);

        return 0;
    }
    else
    {
        printf("Please enter a file!");
        return 1;
    }
}