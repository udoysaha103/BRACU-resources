#include <stdio.h>
#include <stdlib.h>

struct Paratha
{
    int quantity;
    int unit_price;
};

struct Vegetable
{
    int quantity;
    int unit_price;
};

struct Mineral_Water
{
    int quantity;
    int unit_price;
};

int main()
{
    struct Paratha paratha;
    struct Vegetable vegetable;
    struct Mineral_Water mineral_water;
    int number_of_people;

    printf("Quantity Of Paratha: ");
    scanf("%d", &paratha.quantity);
    printf("Unit Price: ");
    scanf("%d", &paratha.unit_price);

    printf("Quantity Of Vegetables: ");
    scanf("%d", &vegetable.quantity);
    printf("Unit Price: ");
    scanf("%d", &vegetable.unit_price);

    printf("Quantity Of Mineral Water: ");
    scanf("%d", &mineral_water.quantity);
    printf("Unit Price: ");
    scanf("%d", &mineral_water.unit_price);

    printf("Number of People: ");
    scanf("%d", &number_of_people);

    if (number_of_people <= 0)
    {
        printf("Individual people will pay: 0 tk");
    }
    else{
        printf("Individual people will pay: %.2f tk", (float)((paratha.quantity * paratha.unit_price) + (vegetable.quantity * vegetable.unit_price) + (mineral_water.quantity * mineral_water.unit_price)) / (float) number_of_people);
    }

    return 0;
}