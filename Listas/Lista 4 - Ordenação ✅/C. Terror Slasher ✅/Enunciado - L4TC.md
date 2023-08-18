# Terror Slasher

**Limite de tempo do código: 200ms**

Filmes de terror do gênero Slasher são muito conhecidos por terem um assassino que mata suas vítimas aleatoriamente enquanto tanto os personagens do filme, quanto nós que assistimos a obra, tentamos adivinhar quem que é o cruel assassino por trás de todo esse mistério. Isabela, Mateus, Joaquim, e Bianca são amantes desse gênero de filme e sempre tentam descobrir quem é o assassino, mas eles tem algo curioso, eles sempre usam métodos de ordenação para buscar adivinhar o suspeito com as maiores chances, onde eles ordenam a lista e descobrem quem é o principal suspeito, acontece que sempre tem alguém que é mais rápido, como eles fazem tudo de cabeça, eles acabam levando 2 minutos para uma troca e 1 minuto para uma comparação, eles anotam o tempo que levaram para descobrir o assassino e então fazem uma competição, onde o vencedor ganha o novo combo da Barbie da BK.

Sabendo que para organização Isabela utiliza Heap Sort Max, Mateus utiliza Quick Sort, Joaquim Selection Sort e Bianca Shell Sort.

OBS: Durante a análise, todos levam mais tempo para trocar dois valores de posição na lista do que para simplesmente compará-los, gastando então 2 minutos para uma troca enquanto gastam apenas 1 minuto para uma comparação.

Não é permitido a utilização de bibliotecas para a realização das ordenações

## Input:

Você receberá os valores que correspondem as probabilidades de ser o suspeito de cada pessoa.

## Output:

Deverá imprimir quem ganhou a disputa e quanto tempo levou para concluir.

Atenção com casos de empate, nesses casos ambos ganham e aparecerão na ordem em que foram apresentados.

## Exemplos:

### Caso 1:

Input:
```
42 137 309 98 74 51 111 165 20 82 223 321 9 19 257 5 32 3 28 14
```

Output:
```
Isabela vai assistir o filme da Barbie com seu combo novo após levar 80 minutos para descobrir o assassino.
```

### Caso 2:

Input:
```
1 50 80 100 120 150 180 199 200 220
```

Output:
```
Bianca vai assistir o filme da Barbie com seu combo novo após levar 22 minutos para descobrir o assassino.
```

### Caso 3:

Input:
```
6 8 13 10
```

Output:
```
Joaquim, Bianca vão assistir o filme da Barbie com seu combo novo após levar 8 minutos para descobrir o assassino.
```
