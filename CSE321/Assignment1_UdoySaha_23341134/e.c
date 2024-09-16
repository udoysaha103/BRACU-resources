#include <stdio.h>

int main() {
    char str[100];
    char *ptr1, *ptr2;
    int len = 0;
    ptr1 = ptr2 = str;

    printf("Enter a string : ");
    scanf("%[^\n]s", str);

    while (str[len] != '\0') {
        len++;
    }

    int left_index = 0, right_index = len - 1;
    ptr2 += right_index;

    while (left_index < right_index) {
        if (*ptr1 != *ptr2) {
            printf("Not palindrome");
            return 0;
        }
        left_index++;
        ptr1++;
        right_index--;
        ptr2--;
    }

    printf("Palindrome");

    return 0;
}