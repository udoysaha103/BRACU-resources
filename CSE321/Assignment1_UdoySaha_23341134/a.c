#include <stdio.h>

int addition(int a, int b) {
    return a + b;
}

int subtraction(int a, int b) {
    return a - b;
}

int multiplication(int a, int b) {
    return a * b;
}

int main() {
    int a, b;
    char c;

    printf("First number : ");
    scanf("%d", &a);

    printf("Second number : ");
    scanf("%d", &b);

    printf("Operator : ");
    scanf(" %c", &c);

    if (a > b){
        printf("Subtraction: %d\n", subtraction(a, b));
    }
    else if (a < b){
        printf("Addition: %d\n", addition(a, b));
    }
    else{
        printf("Multiplication: %d\n", multiplication(a, b));
    }

    return 0;
}