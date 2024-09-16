#include <stdio.h>

int main() {
    FILE *f1, *f2;
    char c;
    int space_count = 0;

    f1 = fopen("b_input.txt", "r");
    f2 = fopen("b_output.txt", "w");

    if (f1 == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    while ((c = fgetc(f1)) != EOF) {
        if (c == ' ') {
            space_count++;
            if (space_count == 1) {
                fputc(c, f2);
            }
        }
        else {
            fputc(c, f2);
            space_count = 0;
        }
    }

    fclose(f1);
    fclose(f2);

    return 0;
}