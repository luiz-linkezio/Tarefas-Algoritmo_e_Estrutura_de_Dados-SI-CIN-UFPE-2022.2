# Um balde bem Barbiezinha

**Limite de tempo do código: 300ms**

Esse fim de semana tivemos a estreia do live action da Barbie. O Cinema da UFPE estará promovendo a exibição do filme para seus estudantes. Desta maneira, para promover a participação da comunidade acadêmica, o Cine UFPE realizará um sorteio de um balde de pipoca personalizado para cada sessão exibida. O prêmio do sorteio será: "Um balde bem Barbiezinha", um balde de pipoca no formato de bolsa na cor rosa.

Você será responsável por indicar quem foi o ganhador do sorteio. Para isto, você receberá duas entradas, um inteiro N que indica a posição do ganhador do sorteio e uma lista de tuplas não ordenada contendo o nome da fila e número da poltrona do participante.

Para saber o resultado você deverá ordenar a lista dos participantes usando **BUBBLE SORT** e o ganhador do prêmio será aquele que ocupa a posição **N** na lista **ORDENADA**.

Importante:

- Cada uma das cadeiras tem um nome e um número, ("A", 1), ("B", 2), ("C", 4).
- A primeira cadeira da primeira fila é chamada de ("A", 1), a ultima cadeira da primeira fila é chamada de ("A", 23). A primeira cadeira da ultima fila é chamada de ("Z", 1), a ultima cadeira da ultima fila é chamada de ("Z", 23).
- Todas as filas tem o mesmo número de cadeiras.

## Input:

**N** - Número do sorteado.

**PARTICIPANTES** - Uma lista de tuplas, não ordenada, com as cadeiras participantes do sorteio.

## Output:

Uma mensagem com as informações do vencedor:

```
O vencedor está na fila {NOME_DA_FILA} poltrona {NÚMERO_DA_POLTRONA}!
```

## Exemplos:

### Caso 1:

Input:
```
3
B2 A1 C3
```

Output:
```
O vencedor está na fila C poltrona 3!
```

### Caso 2:

Input:
```
4
D4 A2 B1 C3 E5
```

Output:
```
O vencedor está na fila D poltrona 4!
```

### Caso 3:

Input:
```
2
B2 B1 A2 A3 A1 D4 C3
```

Output:
```
O vencedor está na fila A poltrona 2!
```