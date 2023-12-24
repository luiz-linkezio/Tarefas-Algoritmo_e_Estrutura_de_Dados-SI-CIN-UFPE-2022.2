# CIn 90º

**Limite de tempo do código: 200ms**

A temporada mais esperada do ano chegou para a UFPE, estamos na época de calouradas! O Centro de Informática está promovendo a maior e melhor calourada do semestre, a CIn 90º. A coisa vai esquentar! E para fazer uma boa calourada precisamos dos ingredientes certos, nesse caso, um espaço legal, um "breguinha chave" e muita, muita, muita gente.

Você está na organização da calourada e ficou responsável por cuidar da entrada dos alunos no espaço do evento. A lista de alunos é gigantesca e o custo computacional para realizar as pesquisas por nome na entrada do evento é enorme. Se esse problema não for resolvido, chegaremos no fim da calourada e mais da metade das pessoas ainda estarão esperando para entrar. Para resolver isso, você criará um programa capaz de adicionar os nomes em uma **Tabela Hash**. Indexando os nomes dos alunos e melhorando a busca por nome teremos a calourada mais quente da história.

Cada nome gera um código hashing. Esse código hashing é gerado por uma função de hashing.

Seu trabalho é criar, seguindo as instruções a seguir, um programa capaz de receber uma lista de nomes, gerar um código hashing, e adicionar esse nome em uma tabela hash.

Para código hashing, considere:

- Cada letra terá um valor numérico, a = 1, b = 2, c = 3...
- As letras estarão sempre em maiúsculo e sem acento
- O código é gerado pela soma de todos os valores numéricos de cada letra mod 10.

Ex.:

"ANA": (1 + 14 + 1) MOD 10 = 6

"GEYDSON": (7 + 5 + 25 + 4 + 19 + 15 + 14) MOD 10 = 9


Pode usar lista (Python List)

Não pode usar dicionário (Python dict)

Atenção com o uso excessivo de trechos com O(nˆ2)

Obrigatório usar Tabela Hash

## Input:

**N**: Quatidade de nomes que serão inseridos na tabela hash.

Várias entradas

**NOME**: Nome do estudante (sempre em maiuscula).

## Output:

**TABELA HASH**: uma tabela impressa linha a linha contendo o index e os nomes dos estudantes separados por espaço.

## Exemplos:

### Caso 1:

Input:
```
5
ANA
GEYDSON
GUILHERME
LUCAS
BRUNO
```

Output:
```
0: BRUNO
6: ANA LUCAS
8: GUILHERME
9: GEYDSON
```

### Caso 2:

Input:
```
5
SERGIO
BRUNA
JAMILSON
NEILA
FRED
```

Output:
```
1: NEILA
3: SERGIO JAMILSON FRED
6: BRUNA
```
