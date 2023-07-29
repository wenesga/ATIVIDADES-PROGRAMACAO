#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main(){
	
	setlocale(LC_ALL, "");
	
    int num1, num2, som, sub, mul, div;
	
    printf("Digite o 1º número: ");
    scanf("%i", &num1);
    printf("Digite o 2º número: ");
    scanf("%i", &num2);

    som = num1 + num2;
    sub = num1 - num2;
    mul = num1 * num2;
    div = num1 / num2;

    printf("\nA Soma: %i\n", som );
    printf("A Subtrção: %i\n", sub );
    printf("O Produto: %i\n", mul );
    printf("A Divisão: %i\n", div );
    
    return 0;
}