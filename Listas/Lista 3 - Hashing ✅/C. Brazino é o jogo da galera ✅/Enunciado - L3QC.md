# Brazino é o jogo da galera 

**Limite de tempo do código: 120ms**

Juquinha foi contratado como freelancer em uma casa de apostas popular, *Brazino*, para ajudá-los a implementar um sistema de adição e remoção de partidas de forma rápida. Ajude Juquinha, criando um sistema que utilize hashing de endereçamento aberto.

Para todas as partidas temos as seguintes informações:

```
<timestamp: int> <nome_da_partida: str>
```

**timestamp** é um inteiro que representa uma data e hora.

Ex:
```
1689217200 ( Quinta-feira, 13 de julho de 2023 00:00:00 [GMT-03:00] )
```

Você deve utilizar o timestamp como "chave" para achar o index/espaço na hashtable, utilizando a seguinte formula:

```
timestamp % tamanho_da_hashtable
```

As partidas devem ser armazenadas em conjunto com outras que acontecem no mesmo timestamp:

Ex:
```
1689217200 Brazil vs Portugal

1689217200 Alemanha vs China
```

As partidas com o mesmo timestamp (as que começam na mesma data e hora) devem ser agrupadas, veja o exemplo na figura a seguir

**Atenção:** a lista de agrupamento tem um tamanho maximo, que é informado no primeiro input.

**Observações:**

- 1: Não é permitido usar dicionarios

- 2: Não é permitido o uso de bibliotecas.

**Exemplo de visualização:** Onde a hashtable tem 5 espaços, a lista tem limite para apenas 3 partidas, e partidas que começam na mesma data estão agrupadas, o quinto espaço (4) está vázio.

![Tabela Hash](https://img001.prntscr.com/file/img001/IvzT02TVSGWhtk_S_MNypg.png)

## Input:

**O Primeiro input:** vão ser dois numeros inteiros X e Y

**X**: representa a quantidade de espaços disponível na hash table.

**Y**: representa a quantidade maxima de partidas que pode haver em um unico espaço.

**ADD** -> Adiciona partidas no "banco de dados" os proximos inputs serão informações das partidas no seguinte formato:

```
<timestamp: int> <nome_da_partida: str>
```

ex:

```
ADD
1689282032 Brazil vs Portugal
1689291234 Sport vs Santa
DONE
```

**OBS: os inputs terminam assim que receber a palavra "DONE"**

**REM** -> Remove partidas do "banco de dados" os proximos inputs serão informações das partidas no seguinte formato:

```
<timestamp: int> <nome_da_partida: str>
```

ex:

```
REM
1689282032 Brazil vs Portugal
1689291234 Sport vs Santa
DONE
```

**OBS: os inputs terminam assim que receber a palavra "DONE"**
**OBS: caso um agrupamento fique vazio (você acabou de remover a ultima partida restante do agrupamento), você deve liberar aquele espaço na hashtable e torna-lo vazio**

**REMT timestamp** -> Remove todas as partidas que acontecem no timestamp especificado

ex:

```
REMT 1689282032
```

**PRINT timestamp** -> Caso um timestamp seja passado você deve mostrar o nome de todas as partidas registradas nesse tempo

ex:

input:
```
PRINT 1689282032
```

output:
```
['Brazil vs Portugal', 'TimeA vs TimeB']
```

Caso nada for passado, você deve imprimir todo o banco de dados armazenado

ex:

input:
```
PRINT
```

output:
```
Slot 0: ['Time1 vs Time2', 'TimeX vs TimeY']
Slot 1: ['Argentina vs Paraguai', 'Venezuela vs Brazil']
Slot 2: Vazio
``` 

## Output:

A maioria dos outputs são para ações que não se concretizaram

```
ADD
```

Caso o sistema não consiga adicionar por falta de espaço na lista/agrupamento, deve mostrar:

```
"partida: {partida_nome} não foi adicionada por falta de espaço na lista!"
```

Caso o sistema não consiga adicionar por falta de espaço na hashtable, deve mostrar:

```
"partida: {partida_nome} não foi adicionada por falta de espaço na hashtable!"
```

onde **partida_nome** é o nome da partida ( ver caso de exemplo )




```
REM
```

Caso o sistema não consiga remover algo que não existe no banco de dados:

```
"partida: {partida_nome} não foi removida porque não pertencia a lista!"
```

onde **partida_nome** é o nome da partida ( ver caso de exemplo )

Caso o sistema não esteja armazenando partidas nesse horario:

```
"o sistema não está armazenando partidas nesse horario!"
```




```
REMT
```

Caso o sistema não esteja armazenando partidas nesse horario:

```
"o sistema não está armazenando partidas nesse horario!"
```




```
PRINT
```

Você deve printar todo o banco de dados no seguinte formato:

```
"Slot {index}: {lista}"
```

onde **index** é o espaço correspondente na hashtable e **lista** é uma lista o nome de todas as partidas naquele devido espaço

Caso não exista partidas naquele espaço você deve printar "Vazio" no lugar da lista

ex:

```
"Slot 0: ['Argentina vs Paraguai', 'Venezuela vs Brazil']"
"Slot 1: Vazio"
```

## Exemplos:

### Caso 1:

Input:
```
3 2
ADD
1 Argentina vs Paraguai
2 Palmeiras vs Nautico
DONE
PRINT
ADD
3 Sport vs Santa
1 Brazil vs Portugal
2 Barcelona vs Flamengo
3 Palmeiras vs Sao Paulo
DONE
PRINT
ADD
2 Fluminense vs Botafogo
999 China vs Alemanha
DONE
REM
2 Fluminense vs Botafogo
999 China vs Alemanha
DONE
REMT 2
PRINT
REM
1 Argentina vs Paraguai
2 Palmeiras vs Nautico
3 Sport vs Santa
1 Brazil vs Portugal
2 Barcelona vs Flamengo
DONE
PRINT
REMT 2
PRINT
```

Output:
```
Slot 0: Vazio
Slot 1: ['Argentina vs Paraguai']
Slot 2: ['Palmeiras vs Nautico']
Slot 0: ['Sport vs Santa', 'Palmeiras vs Sao Paulo']
Slot 1: ['Argentina vs Paraguai', 'Brazil vs Portugal']
Slot 2: ['Palmeiras vs Nautico', 'Barcelona vs Flamengo']
partida: Fluminense vs Botafogo não foi adicionada por falta de espaço na lista!
partida: China vs Alemanha não foi adicionada por falta de espaço na hashtable!
partida: Fluminense vs Botafogo não foi removida porque não pertencia a lista!
o sistema não está armazenando partidas nesse horario!
Slot 0: ['Sport vs Santa', 'Palmeiras vs Sao Paulo']
Slot 1: ['Argentina vs Paraguai', 'Brazil vs Portugal']
Slot 2: Vazio
o sistema não está armazenando partidas nesse horario!
o sistema não está armazenando partidas nesse horario!
Slot 0: ['Palmeiras vs Sao Paulo']
Slot 1: Vazio
Slot 2: Vazio
o sistema não está armazenando partidas nesse horario!
Slot 0: ['Palmeiras vs Sao Paulo']
Slot 1: Vazio
Slot 2: Vazio
```