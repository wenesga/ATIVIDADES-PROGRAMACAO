#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
int main(){
UINT CPAGE_UTF8 = 65001;
UINT CPAGE_DEFAULT = GetConsoleOutputCP();
SetConsoleOutputCP(CPAGE_UTF8);
/*____________________________________________*/
    int num1, num2, som, sub, mul, div;
	
    printf("Digite o 1º número: ");
    scanf("%i", &num1);
    printf("Digite o 2º número: ");
    scanf("%i", &num2);

    som = num1 + num2;
    sub = num1 - num2;
    mul = num1 * num2;
    div = num1 / num2;

    printf("\nA Soma é: %i\n", som );
    printf("A Subtração é: %i\n", sub );
    printf("O Produto é: %i\n", mul );
    printf("A Divisão é: %i\n", div );
    
    return 0;
/*____________________________________________*/
SetConsoleOutputCP(CPAGE_DEFAULT);
}