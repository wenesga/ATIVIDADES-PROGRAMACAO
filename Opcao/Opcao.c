#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
main(void){
     setlocale(LC_ALL, "Portuguese");
     char ch;

     printf("MENU de Escolhas\n\n");
     printf("1. Op��o a \n");
     printf("2. Op��o b \n\n");
     printf("Entre com sua escolha: \n\n");
     ch = getchar();

     switch(ch){
       case '1':
         printf(">> Op��o 1 foi selecionada\n\n");
         break;
       
       case '2':
         printf(">> Op��o 2 foi selecionada\n\n");
         break;
       
       default:
         printf(">> Nenhuma Op��o selecionada\n\n");
     }
     system("pause");
}
