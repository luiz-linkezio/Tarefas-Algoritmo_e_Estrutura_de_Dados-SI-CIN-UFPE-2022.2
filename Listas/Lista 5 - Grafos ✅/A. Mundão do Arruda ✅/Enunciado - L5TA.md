# Mundão do Arruda

**Limite de tempo do código: 200ms**

Grafite, ídolo do gigantesco Santa Cruz, o maior time do estado, deseja chegar ao palácio do futebol pernambucano, o estádio do Arruda, para prestigiar a torcida e comprar a nova e belíssima camisa do santinha. Infelizmente a idade chega pra todos e Grafite não lembra com certeza como faz para chegar ao Arruda, então ele decide perguntar para Diego Souza e Kieza, seus filhinhos no futebol, como fazer para chegar lá, frustados por serem filhos de Grafite, Diego Souza e Kieza decidem apenas citar os pontos de recife no mapa e a direção para onde eles podem levar, fazendo com que Grafite deva escolher o caminho que o levará para o Arruda. Felizmente ele encontra você, estudante de Algoritmos e Estruturas de Dados no CIN, que decide mostrar para ele qual o melhor caminho que o fará chegar no Arruda.

## Input:

Na primeira linha serão informados os N pontos de recife que deverão ser conectados para formar o caminho, separados por espaço. O primeiro nome é o ponto de partida, e o último nome é o glorioso estádio do Arruda.

Em sequência, serão informadas as conexões que cada ponto terá. O primeiro nome informado será referido como 0 (zero), o segundo como 1, e assim sucessivamente até N-1. A primeira linha das conexões dizem respeito aos pontos conectados ao ponto 0, a segunda linha ao ponto 1, e assim sucessivamente.

## Output:

Será informado o melhor caminho e o seu tamanho, caso exista.

## Exemplos:

### Caso 1:

Input:
```
CIN Shopping-Recife Jaqueira Arena-de-Pernambuco Passo-da-Alfandega Curado Jaboatão Arruda
1 5
0 2 3
1 7
1 4 5
2 3 6
0 3 6
4 5
2
```

Output:
```
Grafite precisou passar por 4 pontos através do caminho CIN -> Shopping-Recife -> Jaqueira -> Arruda.
```

### Caso 2:

Input:
```
UFPE Aflitos UPE Boa-Viagem Marco-Zero Arruda
1 4
0 3
3 4
1 2 5
0 2 5
3 4
```

Output:
```
Grafite precisou passar por 3 pontos através do caminho UFPE -> Marco-Zero -> Arruda.
```

### Caso 3:

Input:
```
Ilha-do-Retiro Madalena CCEN Varzea Mirabilandia Santo-Amaro Arruda
2 4 5
6
3
2 4
0 3
0
1
```

Output:
```
Infelizmente Grafite não pode chegar no Arruda.
```