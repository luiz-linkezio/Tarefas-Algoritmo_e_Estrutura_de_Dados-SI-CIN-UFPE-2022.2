# Árvore Genealógica do CIN

**Limite de tempo do código: 200ms**

Uma família Curiosa

Na família de João, há uma curiosa tradição: nunca repetir o nome das mulheres da família. Outro fato estranho na família é que cada mulher só tem no máximo 2 filhas, em qualquer geração. Essa tradição começou há muitas gerações atrás, e desde então a família guarda uma árvore genealógica com todos os nomes femininos que já foram usados na família. Além disso, esses nomes são sempre guardados numa ordem tal que, se forem inseridos numa árvore de busca binária, com a comparação entre as chaves feita pela ordem lexicográfica, a árvore da família é perfeitamente reconstruída.

Por exemplo, se a lista guardada for:

Maria, Josefina, Renata, Zulmira, Adriana, isso significa que

Maria é Mãe de Josefina e Renata, Josefina é Mãe de Adriana, Renata é Mãe de Zulmira

Ajude a reconstruir a árvore genealógica feminina de João. Como no exemplo, acima, você deve a partir da raiz imprimir de quem o nó raiz é mãe, em seguida as mães da sub-árvore da esquerda e depois as mães da sub-árvore da direita, seguindo a mesma estratégia.

OBS: NÃO PRECISA ORDENAR

class Node:

```
def __init__(self, valor):

    self.valor = valor
    self.filhoD = None
    self.filhoE = None
```

class Arvore:

```
def __init__(self):
    self.raiz = None

def criarArvore(self, lista):
    
    for i in lista:     
      node = Node(i)
      if self.raiz == None:
          self.raiz = node

      else:
          entrou = False
          item_atual = self.raiz
          while not entrou:
              if item_atual.valor < node.valor:
                  if item_atual.filhoD == None:
                      item_atual.filhoD = node
                      node.pai = item_atual
                      entrou = True                    
                  else:
                      item_atual = item_atual.filhoD
              else:
                  if item_atual.filhoE == None:
                      item_atual.filhoE = node
                      node.pai = item_atual
                      entrou = True
                  else:
                      item_atual = item_atual.filhoE
```

## Input:


```
Maria Josefina Renata Zulmira Adriana
```


## Output:

```
Maria é mãe de Josefina e Renata.
Josefina é mãe de Adriana.
Renata é mãe de Zulmira.
```

## Exemplos:

### Caso 1:

Input:
```
Maria Josefina Renata Zulmira Adriana
```

Output:
```
Maria é mãe de Josefina e Renata.
Josefina é mãe de Adriana.
Renata é mãe de Zulmira.
```

### Caso 2:

Input:
```
Clara Barbara Ana Mariana Leticia Antonia Paula
```

Output:
```
Clara é mãe de Barbara e Mariana.
Barbara é mãe de Ana.
Ana é mãe de Antonia.
Mariana é mãe de Leticia e Paula.
```