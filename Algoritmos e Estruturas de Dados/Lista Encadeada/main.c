#include "lista_encadeada.h"
#include <stdio.h>
#include <stdlib.h>

void NumerosPares(){
 TipoLista * lista;
  lista = InicializaLista();
  
//vamos armazenar uma lista de 1 a mil e remover os numeros impares
for (int i = 1; i <= 1000; i++){
  TipoItem * item = InicializaTipoItem();
  Insere(item, lista);
  ModificaValorItem(item,i);
}
 Imprime(lista);
 printf("Pressione enter para continuar...");

 getchar();

for (int i = 999; i >= 0; i--){
  TipoItem *item = acessa(i,  lista);
  if (ChaveDoItem(item) & 1) //verifica se é impar
    Retira(i,lista);
}

Imprime(lista);
  
  
//vamos liberar da memoria
FLVazia(lista); // aqui já libera o TIPOITEM da memória
free(lista); //libera a lista
  
}


int main(void) {
   NumerosPares();
}
