#include <stdio.h>

int main(){
    char email[100];
    scanf("%s", email);

    int i = 0;
    while (email[i] != '@'){
        i++;
    }

    if (email[i + 1] == 's' && email[i + 2] == 'h' && email[i + 3] == 'e' && email[i + 4] == 'b' && email[i + 5] == 'a' && email[i + 6] == '.' && email[i + 7] == 'x' && email[i + 8] == 'y' && email[i + 9] == 'z'){
        printf("Email address is okay\n");
    }
    else{
        printf("Email address is outdated\n");
    }

    return 0;
}