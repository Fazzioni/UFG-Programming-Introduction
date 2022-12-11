#ifndef lista_encadeada
#define lista_encadeada

typedef int Posicao;

typedef int TipoChave;

typedef struct Item TipoItem;

typedef struct Lista TipoLista;

TipoLista *InicializaLista();

void FLVazia(TipoLista *Lista);

int Vazia(TipoLista *Lista);

int Cheia(TipoLista *Lista);

void Insere(TipoItem *Item, TipoLista *Lista);

void InserePosicao(TipoItem *Item, TipoLista *Lista, Posicao p);

void Retira(Posicao p, TipoLista *Lista);

void Imprime(TipoLista *Lista);

TipoItem *InicializaTipoItem();

void ModificaValorItem(TipoItem *Item, TipoChave Chave);

void ImprimeTipoItem(TipoItem *Item);

TipoChave ChaveDoItem(TipoItem *Item);

int ultimoPosicao(TipoLista *Lista);

TipoItem * acessa(int p, TipoLista *Lista);

#endif














