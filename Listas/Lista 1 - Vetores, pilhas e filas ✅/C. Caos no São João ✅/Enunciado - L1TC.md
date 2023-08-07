# Caos no São João

**Limite de tempo do código: 250ms**

Durante o animado São João de Limoeiro, Pipico, um famoso jogador de futebol pernambucano, começou a sentir fome e sede. Determinado a saciar essas necessidades, ele decidiu ir até a lanchonete local para fazer um lanche. No entanto, ao chegar lá, Pipico se deparou com uma longa fila, o que o deixou insatisfeito. Ele reclamou com o gerente, que prontamente decidiu abrir um novo caixa, criando assim duas filas de atendimento.

Graças à iniciativa do talentoso Pipico, considerado o melhor atacante do futebol pernambucano nos últimos anos, a lanchonete agora opera com dois caixas. A mecânica adotada é a seguinte: sempre que um dos caixas estiver sem fila e chamar o próximo cliente, metade dos clientes que estão na parte de trás da fila do outro caixa será transferida para o caixa disponível, sendo realocados na ordem inversa à qual se encontravam. Em outras palavras, "os últimos serão os primeiros".

Nesse contexto, você foi contratado para desenvolver um sistema capaz de registrar as movimentações das filas nos caixas, além de calcular o valor total arrecadado por cada um deles.

**OBS:** Não é permitido o uso de bibliotecas.

**OBS:** Utilize a estrutura de nó

## Input:

O seu programa deverá iniciar no momento em que a lanchonete abrir (com todas as filas vazias) e sua interface de comunicação seguirá o seguinte padrão:

ENTROU: N C P → Insere o cliente de nome N que irá pagar um total de P reais na fila do caixa C

PROXIMO: C → Chama o próximo cliente ao caixa C considerando e mecânica mencionada acima

FIM → Finaliza o programa.

```
Comando 1
Comando 2
...
```

## Output:

Após o comando ENTROU, imprimir: 

```
N entrou na fila C
```

onde N é o nome do cliente que entrou e C o número do caixa da fila em que ele entrou

Após o comando PROXIMO, imprimir: 

```
N foi chamado para o caixa C
```

onde N é o nome do cliente chamado e C o número do caixa no qual ele foi 
atendido

Após o comando FIM, imprimir: 

```
Caixa 1: R$ T1, Caixa 2: R$ T2
```

onde T1 é o valor total arrecadado pelo caixa 1, e T2 o valor total arrecadado pelo caixa 2, ambos impressos com 2 casas decimais.

## Exemplos:

### Caso 1:

Input:
```
ENTROU: Pipico 1 100.00
ENTROU: Faustão 1 5000.00
ENTROU: Messi 2 350.50
PROXIMO: 2
PROXIMO: 2
PROXIMO: 1
FIM
```

Output:
```
Pipico entrou na fila 1
Faustão entrou na fila 1
Messi entrou na fila 2
Messi foi chamado para o caixa 2
Faustão foi chamado para o caixa 2
Pipico foi chamado para o caixa 1
Caixa 1: R$ 100.00, Caixa 2: R$ 5350.50
```

### Caso 2:

Input:
```
ENTROU: João 1 10.5
ENTROU: Maria 2 15.2
ENTROU: Carlos 1 5.8
PROXIMO: 1
PROXIMO: 2
ENTROU: Ana 2 7.3
ENTROU: Pedro 1 12.7
PROXIMO: 1
PROXIMO: 2
PROXIMO: 1
FIM
```

Output:
```
João entrou na fila 1
Maria entrou na fila 2
Carlos entrou na fila 1
João foi chamado para o caixa 1
Maria foi chamado para o caixa 2
Ana entrou na fila 2
Pedro entrou na fila 1
Carlos foi chamado para o caixa 1
Ana foi chamado para o caixa 2
Pedro foi chamado para o caixa 1
Caixa 1: R$ 29.00, Caixa 2: R$ 22.50
```
