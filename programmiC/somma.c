#include <stdio.h>


int main(){
    int primo_numero;
    int secondo_numero;
    int somma;

    printf("Dammi in primo numero: ");
    scanf("%d", &primo_numero);

    printf("\nDammi secondo numero: ");
    scanf("%d", &secondo_numero);

    somma = primo_numero + secondo_numero;

    printf("\nLa somma e': %d (0x%x)", somma, &somma);

    return 0;
}