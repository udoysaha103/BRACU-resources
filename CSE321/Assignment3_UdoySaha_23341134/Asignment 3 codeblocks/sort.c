#include <stdio.h>
#include <stdlib.h>

// descending selection sort
void sort(int *arr, int n) {
    int i, j, temp;

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;	
            }
        }
    }
}

int main(int argc, char *argv[]) {
    int n = argc - 1;
    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    sort(arr, n);

    printf("Descending (sort.c): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    printf("\n");

    free(arr);

    return 0;
}
