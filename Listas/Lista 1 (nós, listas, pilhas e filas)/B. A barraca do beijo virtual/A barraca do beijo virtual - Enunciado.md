# A barraca do beijo virtual

**Limite de tempo do código: 200ms**

Em meio ao caos universitário e nas proximidades da melhor época festiva do nosso país, Milone e Millahy, dois amigos universitários do Cin, tiveram uma grande ideia: criar um app de pegação que englobasse apenas as pessoas que possuem vínculos com a UFPE, onde as pessoas se curtem e, caso seja recíproco, o app abre o chat para marcar o local do beijo. O app possui as mesmas funcionalidades do aplicativo de relacionamentos mais famoso (likes e matchs) mas o diferencial seria uma página de beijos (likes), que o usuário recebeu, disponível de graça. Além disso, eles decidiram mudar o nome de algumas funcionalidades para entrar no clima do São João. O "like" virou "beijo", que é utilizado para curtir uma pessoa. O "match" virou "xodó", termo usado quando dois perfis se curtem e, portanto, saem da lista de beijos. Contudo, os garotos pularam a cadeira de algoritmos e não sabem como implementar tal tarefa, ou seja, precisam da SUA ajuda. O seu objetivo é criar uma lista do histórico de curtidas de um só perfil a partir de uma lista de comandos e, após organizá-la, printar os nomes de quem deu beijo (like) na ordem inversa (o primeiro a dar beijo se torna o último a aparecer no output).

## Input:

O programa receberá uma quantidade indefinida de entradas e deverá encerrar quando o comando final “FIM” for dado. Comandos:

NOME <nome-do-usuário>
BEIJO <nome-de-quem-deu-a-curtida>
SUPERBEIJO <nome-de-quem-deu-o-superlike>
XODÓ <nome-de-quem-deu-o-match>
MOSTRAR
FIM

O comando "**NOME**" indica o nome do perfil e só aparece no início da lista de comandos.

O comando "**BEIJO**" adiciona o <nome> na lista de beijos. Não pode aparecer duas vezes com o mesmo nome.

O comando "**SUPERBEIJO**" move o <nome> para o topo da lista e, caso o <nome> não esteja na lista, ele é adicionado normalmente.

O comando "**XODÓ**" exclui o <nome> da lista.

O comando "**MOSTRAR**" imprime o histórico de beijos.

O comando "**FIM**" representa o fim da lista de comandos.

**O CÓDIGO DEVE APRESENTAR OBRIGATORIAMENTE UMA ESTRUTURA EM POO E LISTA DUPLAMENTE ENCADEADA COM NÓS.**

**NÃO PODE UTILIZAR BIBLIOTECAS QUE FACILITEM OU CRIEM LISTAS DUPLAMENTE ENCADEADAS**

**DICA:** A questão se assemelha com uma estrutura de pilhas.

## Output:

Após o comando "MOSTRAR" será impresso o histórico, exemplo:

```
VALTER
LUCAS
...
```

Após o comando "FIM" será impresso o histórico final com a frase "O histórico final do usuário <nome-do-usuário> é:", exemplo:

```
---input---

NOME João
BEIJO Lucas
BEIJO Fernanda
FIM

---output---

O histórico final do usuário João é:
Fernanda
Lucas
```

**Em ambos os casos, se não houver ninguém na lista, deverá ser impresso, no lugar do histórico, a frase "Histórico vazio."**

## Exemplos:

### Caso 1:

Input:
```
NOME JeanL
BEIJO Raluca
BEIJO Diggo
SUPERBEIJO Yanni
XODÓ Raluca
MOSTRAR
SUPERBEIJO Diggo
FIM
```

Output:
```
Yanni
Diggo
O histórico final do usuário JeanL é:
Diggo
Yanni
```

### Caso 2:

Input:
```
NOME Raluca
SUPERBEIJO Thayse
SUPERBEIJO Teri
BEIJO Diggo
MOSTRAR
XODÓ Teri
XODÓ Diggo
XODÓ Thayse
MOSTRAR
BEIJO JeanL
SUPERBEIJO JeanL
XODÓ JeanL
FIM
```

Output:
```
Diggo
Teri
Thayse
Histórico vazio.
O histórico final do usuário Raluca é:
Histórico vazio.
```
