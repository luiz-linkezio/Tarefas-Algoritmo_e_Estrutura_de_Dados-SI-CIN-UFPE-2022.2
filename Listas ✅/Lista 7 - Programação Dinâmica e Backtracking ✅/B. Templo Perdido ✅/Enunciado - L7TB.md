# Templo Perdido

**Limite de tempo do código: 200ms**

Em uma grande expedição arqueológica, exploradores descobrem a existência de um tesouro histórico: um templo hindu que estava escondido há séculos. Os arqueólogos estudaram o ambiente por meses e conseguiram descobrir um corredor que levava a várias salas repletas de colares de rubi, utilizados como oferenda aos deuses Hindus.

Através de arquivos históricos foi descoberto algo que poderia ser muito perigoso para a exploração. Para garantir que ladrões não roubassem as oferendas, a antiga civilização criou um mecanismo para proteger as suas joias. Caso o ladrão roubasse joias de salas vizinhas, o templo seria desmoronado por completo.

Você, junto a equipe de exploração, realizou uma vistoria em cada uma das salas para descobrir a quantidade de colares que existiam e atribuiu valores a cada uma das salas baseado nessa quantidade. Sabendo disso, o chefe da exploração, Volim Habba, pediu para que você crie um código que analise a quantidade máxima de colares que possam ser retirados sem que o templo venha a desabar.

## Input:

Você receberá um número inteiro que se refere ao número de salas dentro do templo e uma lista de números que se refere a quantidade de colares que estão em cada um das salas.

Exemplo:

```
5
14 55 27 38 10
```

## Output:

Após a execução do programa, imprima:

```
{n} colares podem ser retirados.
```

Onde {n} é a soma máxima da quantidade de colares que podem ser retirados.

## Exemplos:

### Caso 1:

Input:
```
5
14 55 27 38 10
```

Output:
```
93 colares podem ser retirados.
```

### Caso 2:

Input:
```
8
49 14 21 15 32 32 39 7
```

Output:
```
141 colares podem ser retirados.
```

### Caso 3:

Input:
```
10
15 36 49 52 46 11 23 105 13 1
```

Output:
```
216 colares podem ser retirados.
```
