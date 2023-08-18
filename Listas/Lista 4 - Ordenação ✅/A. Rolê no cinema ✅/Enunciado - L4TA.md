# Rolê no cinema

**Limite de tempo do código: 100ms**

No cinema, muitos filmes sensacionais de diferentes gêneros estão em cartaz, como, por exemplo, Barbie, filme que foi feito para nos fazer refletir sobre a história da humanidade, ou como Oppenheimer, feito para dar boas gargalhadas com os amigos. Geydson Renan, Lucas Campos e Luiz Henrique são melhores amigos da faculdade e resolveram aproveitar a oportunidade para dar um rolê no cinema. No entanto, com tantos filmes bons, eles não conseguem escolher o que assistir primeiro. Por isso, alunos inteligentes que são, decidiram criar um algoritmo de merge sort que ordena os nomes dos filmes e, dessa forma, decidirão assistir ao filme que for a mediana da lista ordenada. Duas listas contendo nomes diferentes de filmes serão dadas, cada lista já ordenada em ordem alfabética. E você deverá uni-las em uma única lista, ordenando-a, para no final informar o filme que estiver na posição de mediana da lista. (Os tamanhos das listas vão ser todas ímpares)

```
ATENÇÃO: Usar Mergesort!
```

## Input:

Será dado duas listas ordenadas com nomes de filmes diferentes separados por vírgulas e sem espaço.

Exemplo:

```
[Barbie,Elementos,Missao_Impossivel,Transformers]
[Oppenheimer,Pequena_Sereia,Sobrenatural]
```

## Output:

Você deverá informar o filme que estiver na posição de mediana depois da lista unida da seguinte maneira:

```
‘Os amigos decidiram assistir a [nome do filme] que estava na posição [índice do filme na lista] da lista.’
```

Sendo a contagem de posições de 1 a n.

Exemplo:

```
Os amigos decidiram assistir a Oppenheimer que estava na posição 4 da lista.
```

## Exemplos:

### Caso 1:

Input:
```
Barbie,Elementos,Missao_Impossivel,Transformers
Oppenheimer,Pequena_Sereia,Sobrenatural
```

Output:
```
Os amigos decidiram assistir a Oppenheimer que estava na posição 4 da lista.
```