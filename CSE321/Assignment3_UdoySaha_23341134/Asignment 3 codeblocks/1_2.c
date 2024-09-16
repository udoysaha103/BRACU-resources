/*
Write a C program to print perfect numbers between given intervals using a function. A perfect
number is a positive integer equal to the sum of its positive divisors, excluding the number itself
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int is_perfect(int number)
{
    if (number <= 1)
    {
        return 0;
    }
    int sum = 1;
    for (int i = 2; i <= sqrt(number); i++)
    {
        if (number % i == 0)
        {
            sum += i;
            sum += number / i;
        }
    }
    if (sum == number)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int lower_limit, upper_limit;
    scanf("%d", &lower_limit);
    scanf("%d", &upper_limit);

    for (int i = lower_limit; i <= upper_limit; i++)
    {
        if (is_perfect(i))
        {
            printf("%d\n", i);
        }
    }

    return 0;
}