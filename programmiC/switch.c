#include <stdio.h>

int main(){ 
    int scelta;
    printf("Menu del giorno:\n1 Aragoste\n2 Scampi\n3 Mal di pancia\nScelta: ");
    scanf("%d", &scelta);

    switch(scelta){
        case 1:
            printf("\nEcco l'Argosta");
            break;
        case 2:
            printf("\nMi spiace gli scampi sono finiti");
        case 3:
            printf("\nLe porto un malox?");
            break;
        default:
            printf("\nNon accettiamo fuori menu'");
    }
    return 0;

}