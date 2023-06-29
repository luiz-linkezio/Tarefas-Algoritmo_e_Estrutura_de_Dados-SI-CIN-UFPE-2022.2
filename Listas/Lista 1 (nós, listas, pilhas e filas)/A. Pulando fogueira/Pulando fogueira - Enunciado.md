# Pulando fogueira

**Limite de tempo do código: 200ms**

Pular a fogueira é uma brincadeira popularmente praticada na época de São João, uma das festas mais tradicionais e aguardadas do ano.

Um grupo de 4 amigos, Gabriel, João, Edu e Carlos, estavam curtindo uma festa junina que acontecia em seu bairro, quando decidiram brincar de pular fogueiras. No entanto, para deixar a brincadeira mais divertida, definiram algumas regras:

Cada um sorteará uma lista de números aleatórios de 0 a 9 e de tamanho N.

Eles só poderão pular a quantidade de vezes do número na posição em que estão.

Exemplo: 2,3,5,8,9,2,6,7,6,8,9

A pessoa começará pulando duas vezes, porque a lista começa com 2, e parará no número 5 (posição 3). Depois ela poderá pular 5 vezes, porque ela tá no número 5, parando no número 7 (posição 8) e assim em diante até chegar ao fim, ganhando o jogo ou não, caso cair no número 0.

OBS: se o número de pulos que ele precisa dar exceder o N não faz diferença, ele para no final do mesmo jeito.

![Fogueira](https://chniteroi.com.br/pt/sobre-nos-site/blog-site/PublishingImages/festas-juninas-requerem-cuidado-para-evitar-queimaduras-nas-criancas.jpg)

## Input:

O input terá 8 linhas. A primeira é um número inteiro N que corresponde ao tamanho da lista e a segunda linha será a lista junto ao nome do amigo, com os números separados por um espaço. Será um N e uma lista para cada amigo. Exemplo:

```
11
Gabriel 1 3 5 8 9 2 6 7 6 8 9
3
João 2 3 0
1
Edu 0
10
Carlos 4 3 6 7 0 1 6 5 6 8
```


## Output:

O output será uma linha que diz se o amigo perdeu ou ganhou e outra linha que mostrará em quantos números ele parou, caso ele tenha ganhado, ou uma mensagem dizendo que ele não conseguiu, seguindo o exemplo abaixo.

Exemplo:

```
Gabriel conseguiu!
Gabriel precisou pular 3 fogueiras
João conseguiu!
João precisou pular 1 fogueiras
Edu conseguiu!
Edu precisou pular 0 fogueiras
Ah, que pena, Carlos não conseguiu!
```



## Exemplos:

### Caso 1:

Input:
```
11
Gabriel 1 3 5 8 9 2 6 7 6 8 9
3
João 2 3 0
1
Edu 0
10
Carlos 4 3 6 7 0 1 6 5 6 8
```

Output:
```
Gabriel conseguiu!
Gabriel precisou pular 3 fogueiras
João conseguiu!
João precisou pular 1 fogueiras
Edu conseguiu!
Edu precisou pular 0 fogueiras
Ah, que pena, Carlos não conseguiu!
```

### Caso 2:

Input:
```
15
Gabriel 5 2 0 1 9 1 6 3 6 4 9 2 4 5 9
4
João 3 1 0 2
5
Edu 1 1 1 2 8
9
Carlos 4 3 6 7 2 1 1 3 6
```

Output:
```
Gabriel conseguiu!
Gabriel precisou pular 4 fogueiras
João conseguiu!
João precisou pular 1 fogueiras
Edu conseguiu!
Edu precisou pular 4 fogueiras
Carlos conseguiu!
Carlos precisou pular 4 fogueiras
```
