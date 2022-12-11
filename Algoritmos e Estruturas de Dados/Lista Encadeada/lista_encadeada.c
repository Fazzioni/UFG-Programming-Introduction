#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/*Como parte do projeto que iremos desenvolver durante a disciplina a tarefa de
hoje consiste na implementação dos tipos abstratos de dados de lista linear
sequencial e lista linear encadeada com alocação dinâmica. Os TADs devem conter
as operações :
*/
// Inicia uma lista vazia

typedef int TipoChave;

typedef struct {
  TipoChave Chave;
} TipoItem;

typedef struct Celula_str *Apontador;

typedef struct Celula_str {
  TipoItem *Item;
  Apontador Prox;
} Celula;

typedef struct {
  Apontador Primeiro;
  Apontador Ultimo;  // deprecated

} TipoLista;

typedef TipoItem Elemento;
typedef int Posicao;


TipoLista *InicializaLista() {
  // Inicializa a lista encadeda

  
  // cria um ponteiro tipo lista para armazenar a estrutura da lista
  TipoLista *lista;

  // aloca na memória
  lista = malloc(sizeof(TipoLista));
  lista->Primeiro = NULL;
  lista->Ultimo = NULL;
  return lista;
}


// Verifica se a lista é vazia
int Vazia(TipoLista *Lista) { return (Lista->Primeiro == NULL); }


void clear(Apontador celula) {
/* 
  remove uma celula recursivamente até o final da lista encadeada
  além de remover da lista já tira libera da memória
*/
  
  if (celula->Prox != NULL)
    clear(celula->Prox);

  
  if (celula->Item != NULL)
    free(celula->Item);

  free(celula);
}


void FLVazia(TipoLista *Lista) {
  /* Remove todos as celulas da lista, deixa completamente vazia*/
  if (Vazia(Lista)) // se a lista está vazia
    return;
  
  // garantir que a lista não é cíclica
  if (Lista->Primeiro == Lista->Ultimo)
    Lista->Primeiro->Prox = NULL;

  clear(Lista->Primeiro); // remove recursivamente todos os itens

  // limpa os ponteiros
  Lista->Primeiro = NULL;
  Lista->Ultimo = NULL;
}


int Cheia(TipoLista *Lista) { // deprecated
  /*
      Nessa estrutura não faz muito sentido, mas podemos pensar quando não há mais memória disponível

  */
  Celula *buffer = malloc(sizeof(Celula));
  int result = (buffer == NULL);
  free(buffer);
  return result;
}

Apontador NovaCelula(TipoItem *tipoitem) {
  /* 
      Cria uma celula sem associar a lista encadeada   
      Essa função é importante para atribuir o tipodeitem em uma celula
  */ 
  Apontador buffer = malloc(sizeof(Celula));
  if (buffer == NULL) { // se n tiver memoria disponível
    printf("Não há memória disponível para alocar mais uma celula!, quer "
           "comprar um pente de memória?\n tá baratinho, entre em contato: "
           "49988301029!\n obrigado!");
    return NULL;
  }
  buffer->Item = tipoitem;
  buffer->Prox = NULL;
  return buffer;
}


void Insere(TipoItem *x, TipoLista *Lista) {
  /*
    Insere um elemento na final da lista
    para inserir um tipoitem, precisamos criar uma celula para apontar para os outros itens da lista
  */
  
  // criar uma celula para guardar o TipoItem
  Celula *c = NovaCelula(x);
  if (c == NULL)
    return;

  // se a lista estiver fazia
  if (Vazia(Lista)) {
    Lista->Primeiro = c;
    Lista->Ultimo = c;
    
  } else {
    // insere no final
    Lista->Ultimo->Prox = c;
    Lista->Ultimo = c;
  }
}


void Retira(Posicao p, TipoLista *Lista) {
  /*
     Remove um elemento de uma posição específica
  */
  
  if (p < 0)
    return;

  //pega o elemento anterior de p
  Apontador anterior = Lista->Primeiro;
  
  if (anterior == NULL)
    return;

  for (int i = 0; i < p - 1; i++) {
    anterior = anterior->Prox;
    if (anterior == NULL) {
      printf("Índice inválido!");
      return;
    }
  }
  int set_ultimo = 0;

  Apontador el;
  if (p == 0) {

    el = Lista->Primeiro;
    Lista->Primeiro = el->Prox;

    if (el == Lista->Ultimo) {
      Lista->Ultimo = el->Prox;
      if (Lista->Ultimo == NULL)
        Lista->Ultimo = Lista->Primeiro;
    }

  } else {
    el = anterior->Prox;
    anterior->Prox = el->Prox;

    if (Lista->Ultimo == el)
      Lista->Ultimo = anterior;
  }

  if (el->Item != NULL)
    free(el->Item);
  free(el);
}

// imprime o elemento da lista
void ImprimeTipoItem(Elemento *x) { printf("Chave: %d\n", x->Chave); }

TipoChave ChaveDoItem(TipoItem *Item) {return Item->Chave; }


void Imprime(TipoLista *Lista) {
  /*
    Imprime todos os elementos da lista
  */
  if (Vazia(Lista))
    return;

  Apontador el = Lista->Primeiro;
  int indice = 0;
  do {
    printf("posicao[%d]: ", indice);
    ImprimeTipoItem(el->Item);
    el = el->Prox;
    indice++;
  } while (el != NULL);
}


// essas funções são necessárias pq o valor armazenado na lista é um TAD

TipoItem *InicializaTipoItem() {
  /*
    INICIALIZA O TIPO DE ITEM
  */
  
  // cria um tipo de item para colocar na celula
  Elemento *el = malloc(sizeof(Elemento));

  if (el == NULL) {
    printf("SEM MEMÓRIA SUFICIENTE!");
    return NULL;
  } else {
    // inicia a chave com valor zero
    el->Chave = 0;
    return el;
  }
}

// modifica o valor do tipo da lista
void ModificaValorItem(TipoItem *item, TipoChave chave) { item->Chave = chave; }


int ultimoPosicao(TipoLista *lista) {
  /*
    Retorna o indíce da ultima posição da lista
  */
  
  if (Vazia(lista))
    return -1;

  int indice = 0;
  Apontador el = lista->Primeiro;
  while (el->Prox != NULL)
    indice++, el = el->Prox;

  if (el != lista->Ultimo)
    printf("Há um bug, o ultimo elemento é diferente da lista.ultimo! "
           "parábens, você é um exelente QA tester!");

  return indice;
}

Apontador acessa_apontador(int p, TipoLista *Lista) {
  /*
    Acesa um elemento da lista pelo indice
    retorna um apontador de celula
  */ 
  
  Apontador el = Lista->Primeiro;

  while( p-- > 0){
    if (el == NULL)
      return NULL;
     el = el->Prox;
  }
    
  return el;
}


TipoItem *acessa(int p, TipoLista *Lista) {
  /*
    Acesa um elemento da lista pelo indice
    retorna um tipoitem
  */ 
 Apontador ap = acessa_apontador(p, Lista);
  
 if (ap == NULL)
    return NULL;
  
  return ap->Item;
}



void InserePosic(TipoItem *x, TipoLista *Lista, Posicao p) {
  /*
   Insere elemento em posição específica, menor do que o tamanho atual da lista
  */

  
  // vmaos criar uma nova chave
  Celula *c = NovaCelula(x);
  if (c == NULL)
    return;

  c->Item = x;

  int set_ultimo = 0;

  Apontador buffer;

  if (p == 0) {
    set_ultimo = (Lista->Ultimo == Lista->Primeiro);

    c->Prox = Lista->Primeiro;
    Lista->Primeiro = c;
  } else {
    if (Vazia(Lista)) {
      printf("Posicao inválida\n");
      free(c);
      return;
    }

    // pega um elemento anterior
    Apontador anterior = Lista->Primeiro;
    for (int i = 0; i < p - 1; i++) {
      anterior = anterior->Prox;

      if (anterior == NULL) {
        printf("Indice maior que o número de elementos\n");
        free(c);
        return;
      }
    }

    set_ultimo = (Lista->Ultimo == anterior);

    c->Prox = anterior->Prox;
    anterior->Prox = c;
  }

  if (set_ultimo)
    Lista->Ultimo = c;
}
