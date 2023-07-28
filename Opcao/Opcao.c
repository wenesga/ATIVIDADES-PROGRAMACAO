#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
main(void){
     setlocale(LC_ALL, "Portuguese");
     char ch;

     printf("MENU de Escolhas\n\n");
     printf("1. Opção a \n");
     printf("2. Opção b \n\n");
     printf("Entre com sua escolha: \n\n");
     ch = getchar();

     switch(ch){
       case '1':
         printf(">> Opção 1 foi selecionada\n\n");
         break;
       
       case '2':
         printf(">> Opção 2 foi selecionada\n\n");
         break;
       
       default:
         printf(">> Nenhuma Opção selecionada\n\n");
     }
     system("pause");
}
