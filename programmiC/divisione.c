#include <stdio.h>

int main()
{
    int numeratore;
    int denominatore;
    int divisione;

    printf("Dammi in primo numero: ");
    scanf("%d", &numeratore);

    printf("\nDammi secondo numero: ");
    scanf("%d", &denominatore);

    if (denominatore != 0)
    {
        divisione = numeratore / denominatore;
        printf("\nLa divisione e': %d", divisione);
    }
    else
    {
        printf("\nIl denomiantore non puo' essere zero");
    }

    return 0;
}