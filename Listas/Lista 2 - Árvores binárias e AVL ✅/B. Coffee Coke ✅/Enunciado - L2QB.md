# Coffee Coke

**Limite de tempo do código: 250ms**


A cozinha do Cin é um espaço acolhedor e de muito respeito entre os alunos. Lá se encontra a gloriosa geladeira do Cin, que oferece a oportunidade dos alunos colocarem suas comidas para não estragarem, mas a geladeira tem sofrido com muitos imprevistos e incertezas pela sua vulnerabilidade a furtos muitas vezes sem explicações. Taylor Switch, aluna do terceiro período de Sistemas de Informação, é uma adoradora compulsiva de um refrigerante específico que pode fazer milagres: a Coca Café. Após comprar sua coca café na vendinha perto da sua casa, Taylor Switch decidiu confiar na bondade das pessoas e colocou sua humilde coca café dentro da geladeira. Distraída após tentar comprar ingressos de uma cantora famosa usando os computadores do Cin, acabou por se esquecer da sua coca café e foi embora sem nada. Três dias após o acontecimento, crente que ninguém havia sequer tocado no seu precioso líquido, T-Switch, assim que chegou no Cin, foi logo checar se a coca estava lá. A coca tinha sido **RAPTADA**.

Indignada com o crime, Taylor, a famosa "loira dedo podre pra macho", publicou no email do Cin toda sua indignação e, não satisfeita, pediu a sua ajuda para tentar encontrar o possível ladrão de sua coca. Seu objetivo é, através dos dados que o setor de segurança do Cin lhe disponibilizar e as respostas no email dela, conseguir determinar o possível ladrão, utilizando uma estrutura de árvores binárias para melhor otimização. Você deve construir uma árvore a partir dos CPFs dos suspeitos, onde o nó mais a esquerda representa o menor cpf em termos numéricos e o mais a direita o maior.

## Input:

Inicialmente você receberá os dados disponibilizados pelo setor de segurança do Cin, ou seja, o nome dos suspeitos que acessaram a geladeira durante os 3 dias que deverão ser adicionados na árvore. Os dados iniciarão após a string "**--- SUSPEITOS ---**" com o comando "**ADD**" seguidos pelo cpf do indivíduo e o nome, como exemplo:

```
---SUSPEITOS---
ADD 52639874525 Pedro
ADD 36485963257 Lara
ADD 75589632415 Gabriel
```

Após acabar a lista de suspeitos, o input começará a ser relacionado a interação após a string "**--- REAÇÕES ---**" de alguns suspeitos ao email da Taylor, podendo ser dividido em alguns comandos:

"**<nome-do-suspeito> disse que achou a coca saborosa.**" - O suspeito vira a raiz da árvore, seguindo os movimentos da imagem a seguir:
![Árvore](https://user-images.githubusercontent.com/104574086/221431025-2f7d62d3-61db-4632-bcd9-7ecf58ed4e9a.png)
"**<nome-do-suspeito> doou uma coca café para a Taylor!**" - O suspeito deixa de ser suspeito e é excluído da árvore.

"FIM" - Marca o fim de todos os comandos.

## Output:

Se o input for "**<nome-do-suspeito> disse que achou a coca saborosa.**", deve-se printar: "**<nome-do-suspeito> virou o principal suspeito e estava no nível <nível-ao-qual-o-suspeito-se-encontra-na-árvore>**.".

Se o input for "**<nome-do-suspeito> doou uma coca café para a Taylor!**", deve-se printar: "**<nome-do-suspeito> deixou de ser o principal suspeito e estava no nível <nível-ao-qual-o-suspeito-se-encontra-na-árvore>.**".

Se o input for "**FIM**", deve-se printar o indivíduo que está na raiz da árvore da seguinte forma: "**<nome-da-pessoa-da-raiz> foi declarado o ladrão da coca!**"

O **nível** da raiz é **0** (ZERO).

Caso o nó a ser excluído da árvore tenha dois filhos, determinamos que deve ser chamado o **SUCESSOR** (filho a direita do nó a ser excluído) para substituir o nó excluído.

**Obs:** não será pedido pra excluir um elemento que seja a raiz em nenhum momento.

**A árvore deve ser feita em POO utilizando o conceito de nó sem a utilização de bibliotecas que ajudem a criar essa estrutura e também sem a utilização de listas, dicionários ou tuplas DENTRO das classes.**

## Exemplos:

### Caso 1:

Input:
```
--- SUSPEITOS ---
ADD 35287695009 Pipico
ADD 68930542187 Gabigol
ADD 52740983662 Love
ADD 91623805430 Neymar
ADD 75319260843 Messi
--- REAÇÕES ---
Neymar disse que achou a coca saborosa.
Love doou uma coca café para a Taylor!
FIM
```

Output:
```
Neymar virou o principal suspeito e estava no nível 2.
Love deixou de ser o principal suspeito e estava no nível 3.
Neymar foi declarado o ladrão da coca!
```

### Caso 2:

Input:
```
--- SUSPEITOS ---
ADD 78966423156 CanetaAzul
ADD 56899412321 Dillera
ADD 51021063487 Fallen
ADD 89456784123 Agostinho
ADD 90125066358 Pele
--- REAÇÕES ---
CanetaAzul disse que achou a coca saborosa.
Pele doou uma coca café para a Taylor!
Dillera doou uma coca café para a Taylor!
Agostinho disse que achou a coca saborosa.
FIM
```

Output:
```
CanetaAzul virou o principal suspeito e estava no nível 0.
Pele deixou de ser o principal suspeito e estava no nível 2.
Dillera deixou de ser o principal suspeito e estava no nível 1.
Agostinho virou o principal suspeito e estava no nível 1.
Agostinho foi declarado o ladrão da coca!
```

### Caso 3:

Input:
```
--- SUSPEITOS ---
ADD 55688745966 Gleybson
ADD 35482878963 Aragão
ADD 80658405632 Tonho
ADD 84566982356 Clarinha
ADD 04428922451 Bia
ADD 47401602673 Rodrigo
ADD 69987443038 Mariana
ADD 79800443079 Bruno
--- REAÇÕES ---
Aragão doou uma coca café para a Taylor!
Tonho doou uma coca café para a Taylor!
Rodrigo doou uma coca café para a Taylor!
Mariana disse que achou a coca saborosa.
FIM
```

Output:
```
Aragão deixou de ser o principal suspeito e estava no nível 1.
Tonho deixou de ser o principal suspeito e estava no nível 1.
Rodrigo deixou de ser o principal suspeito e estava no nível 1.
Mariana virou o principal suspeito e estava no nível 2.
Mariana foi declarado o ladrão da coca!
```