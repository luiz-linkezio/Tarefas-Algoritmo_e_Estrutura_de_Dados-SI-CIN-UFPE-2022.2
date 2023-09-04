# A missão Lazarus

**Limite de tempo do código: 150ms**

As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie. Considere que você está a bordo da Endurance, nave utilizada para essa missão. Chegando à nossa possível nova galáxia cabe a você ajudar sua equipe a decidir quais são os possíveis caminhos de visitação entre os planetas candidatos. Para isso você pensará em todas as possibilidades de visitação nesse novo sistema "solar" que orbita o buraco negro Gargantua.

Faça todos os subsets possíveis para essa lista de planetas e diga quantos caminhos a sua equipe pode vir a escolher!

PS: Leve em consideração que existe a possibilidade do "combustível da nave não ser o suficiente", ou seja, não visitar nenhum planeta (Conjunto vazio). Além disso, não há nenhuma repetição entre essas possibilidades.

Exemplo: [Planeta X, Planeta Y] é o mesmo de [Planeta Y, Planeta X] e também está inválido, pois tem que ser em ordem alfabética.

Imagem de auxílio:

![Grafo](https://i.stack.imgur.com/b03V4.png)

## Input:

Você receberá uma lista de N planetas candidatos à visitação.

## Output:

Imprima a quantidade de possibilidades de ordem de visitação entre esses planetas e todos os subsets possíveis sem repetições e em ordem alfabética .

Exemplo:

```
O número de subsets de visitação é X
São eles: [ [], [X], [X,Y], [X,Y,Z}....]
```

## Exemplos:

### Caso 1:

Input:
```
Planeta de Miller, Planeta de Edmunds, Planeta de Dr. Mann
```

Output:
```
O número de subsets de visitação é 8
São eles: [[], ['Planeta de Dr. Mann'], ['Planeta de Dr. Mann', 'Planeta de Edmunds'], ['Planeta de Dr. Mann', 'Planeta de Edmunds', 'Planeta de Miller'], ['Planeta de Dr. Mann', 'Planeta de Miller'], ['Planeta de Edmunds'], ['Planeta de Edmunds', 'Planeta de Miller'], ['Planeta de Miller']]
```
