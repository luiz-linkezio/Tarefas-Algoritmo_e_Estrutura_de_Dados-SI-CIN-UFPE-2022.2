# CInterage

**Limite de tempo do código: 200ms**

Elon Musk e Mark Zuckerberg estão disputando espaço na internet com as redes sociais X e Threads. Porém, com toda essa confusão e instabilidade na web, os alunos do CIn resolveram se afastar desse lampião de fogo doido e passaram a usar uma nova rede social muito melhor e mais estável, feita por estudantes para estudantes, o CInterage.

Todos são bem vidos a colaborar, e você tem um papel importante nesse projeto! Você desenvolverá um algoritmo que representará as conexões dos usuários no formato de grafo. e com capacidade de buscar um usuário e suas conexões na rede.

```
É obrigatório usar POO

Não pode usar libs para construção e busca nos grafos
```

## Input:

**Users** - uma lista de usuários dentro da rede e suas informações

Ex.:

```
[{ "id": 1, "nome": "Adriano", "idade": 18, "curso": "Sistemas de informação" }, ...]
```

**Connections** - uma lista de tuplas com os ids dos usuários que representa a conexão entre os usuário na rede

Ex.:

```
[(1, 2), (4, 5), (4, 3), (2, 3), (5, 1), (3, 1)]
```

**UserId** - um inteiro que representa o id do usuário que será analisado

Ex.:

```
1
```

## Output:

Uma string contendo o nome do usuário analisado, a quantidade de amigos e os nomes dos amigos em ordem alfabética.

```
"O usuário <nome_do_usuario> tem um total de <numero_de_conexoes>, seus amigos são: <nome_amigo_1>, <nome_amigo_2>, <nome_amigo_3>."
```

## Exemplos:

### Caso 1:

Input:
```
[{ "id": 1, "nome": "Adriano", "idade": 18, "curso": "Sistemas de informação" }, { "id": 2, "nome": "Bruno", "idade": 21, "curso": "Engenharia da computação" }, { "id": 3, "nome": "Elen", "idade": 24, "curso": "Sistemas de informação" }, { "id": 4, "nome": "Maria", "idade": 19, "curso": "Ciência da computação" }, { "id": 5, "nome": "Guilherme", "idade": 21, "curso": "Sistemas de informação" }]
[(1, 2), (4, 5), (4, 3), (2, 3), (5, 1), (3, 1)]
1
```

Output:
```
O usuário Adriano tem um total de 3 conexões, seus amigos são: Bruno, Elen, Guilherme.
```

### Caso 2:

Input:
```
[{"id": 6, "nome": "Juliana", "idade": 22, "curso": "Engenharia da Computação"}, {"id": 7, "nome": "Rafael", "idade": 20, "curso": "Engenharia da Computação"}, {"id": 8, "nome": "Fernanda", "idade": 23, "curso": "Sistemas de Informação"}, {"id": 9, "nome": "Pedro", "idade": 25, "curso": "Ciência da Computação"}, {"id": 10, "nome": "Ana", "idade": 19, "curso": "Sistemas de Informação"}]
[(6, 10), (6, 8), (7, 9), (8, 9), (9, 8), (9, 7), (10, 7), (10, 9), (10, 8)]
10
```

Output:
```
O usuário Ana tem um total de 4 conexões, seus amigos são: Fernanda, Juliana, Pedro, Rafael.
```