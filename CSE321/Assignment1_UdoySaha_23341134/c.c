#include <stdio.h>

int main(){
    char password[20];
    scanf("%s", password);

    int lowercase = 0, uppercase = 0, digit = 0, special = 0;

    for (int i = 0; password[i] != '\0'; i++){
        if (password[i] >= 'a' && password[i] <= 'z'){
            lowercase++;
        }
        else if (password[i] >= 'A' && password[i] <= 'Z'){
            uppercase++;
        }
        else if (password[i] >= '0' && password[i] <= '9'){
            digit++;
        }
        else if (password[i] == '_' || password[i] == '$' || password[i] == '#' || password[i] == '@'){
            special++;
        }
    }

    int count = 0;

    if (lowercase == 0){
        count++;
        if (count == 1){
            printf("Lowercase character missing");
        }
        else{
            printf(", Lowercase character missing");
        }
    }

    if (uppercase == 0){
        count++;
        if (count == 1){
            printf("Uppercase character missing");
        }
        else{
            printf(", Uppercase character missing");
        }
    }

    if (digit == 0){
        count++;
        if (count == 1){
            printf("Digit missing");
        }
        else{
            printf(", Digit missing");
        }
    }

    if (special == 0){
        count++;
        if (count == 1){
            printf("Special character missing");
        }
        else{
            printf(", Special character missing");
        }
    }

    if (count == 0){
        printf("OK");
    }
}