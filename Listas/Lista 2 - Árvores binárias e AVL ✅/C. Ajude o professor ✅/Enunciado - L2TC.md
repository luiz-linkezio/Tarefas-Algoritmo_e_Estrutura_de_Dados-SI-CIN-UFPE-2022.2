# Ajude o professor

**Limite de tempo do código: 200ms**

O professor Vagner é o recente professor contratado pelo CIN para dar aulas ao curso de Sistemas de Informação. Além do SIGA, o professor utiliza um outro sistema para organizar os alunos recém-matriculados na sua disciplina. Porém, conforme o número de alunos aumentava, Vagner estava tendo dificuldades para inserir novos alunos da disciplina e também para retirar aqueles que saíam. O principal problema era o tempo que o sistema demorava para executar essas tarefas e isso o deixava frustrado, pois ele não queria perder seu valioso tempo dedicado ao ensino dos alunos.

Por esse motivo, você, como um inteligente aluno de Algoritmos e Estrutura de Dados, decide ajudar o professor criando uma árvore AVL para a resolução dos seus problemas.

Como você sabe, as árvores AVL realizam automaticamente o balanceamento de seus nós toda vez que uma inserção ou remoção é realizada, garantindo que a altura de todos os nós seja mantida aproximadamente igual. Lembre-se que uma árvore AVL é dita balanceada quando a diferença entre as alturas das sub-árvores não é maior do que um.

## Input:


Em sua árvore, cada aluno será representado por uma string que corresponde a seu nome, e a ordenação dos nós seguirá a prioridade padrão das strings, ou seja, uma ordem alfabética e lexicográfica.

Os inputs serão representados por essa lista de comandos:

• **INSERIR [nome]** : Insere um nó na árvore com o nome do aluno.

• **DELETAR [nome]** : Deleta o nó que tiver esse nome como valor.

• **FIM** : Finaliza a execução do código.

## Output:

Cada comando deverá ter um retorno específico. Confira os retornos:

- **INSERIR [nome]** :

- - Se o nome não existir na árvore: [nome] INSERIDO

- - Se o nome já estiver na árvore: [nome] JA EXISTE

- **DELETAR [nome]** :

- - Se o nome não existir na árvore: [nome] NAO ENCONTRADO

- - Se o nome já estiver na árvore: [nome] REMOVIDO

**DICA: O sistema de remoção é o mesmo utilizado do slide do professor.**

- **FIM** :

- - Para demonstrar que o novo código é eficiente e funciona corretamente, você deverá seguir os seguintes passos:

- - - Se a árvore estiver vazia: ARVORE VAZIA

- - - Se a árvore possuir nós, você deverá retornar o nome dos alunos EM PRÉ ORDEM e a ALTURA total da árvore.

- - Após realizar alguma dessas atividades, o comando FIM deverá finalizar a execução do programa.

- - - **Exemplo de output após o comando "FIM"**:

```
nó1 -> nó2 -> nó3 -> FIM. ALTURA: x
```

**A altura da árvore no output deve ser considerada de acordo com os níveis da árvore**.


## Exemplos:

### Caso 1:

Input:
```
INSERIR Ana
INSERIR Bruno
INSERIR Guilherme
INSERIR Gabriel
INSERIR Geydson
INSERIR Hallan
INSERIR Igor
INSERIR Lucas
DELETAR Bruno
DELETAR Geydson
INSERIR Bruno
FIM
```

Output:
```
Ana INSERIDO
Bruno INSERIDO
Guilherme INSERIDO
Gabriel INSERIDO
Geydson INSERIDO
Hallan INSERIDO
Igor INSERIDO
Lucas INSERIDO
Bruno REMOVIDO
Geydson REMOVIDO
Bruno INSERIDO
Guilherme -> Bruno -> Ana -> Gabriel -> Igor -> Hallan -> Lucas -> FIM. ALTURA: 2
```

### Caso 2:

Input:
```
INSERIR Joao
INSERIR Maria
INSERIR Joao
INSERIR Maria
DELETAR Roberto
DELETAR Joao
DELETAR Maria
FIM
```

Output:
```
Joao INSERIDO
Maria INSERIDO
Joao JA EXISTE
Maria JA EXISTE
Roberto NAO ENCONTRADO
Joao REMOVIDO
Maria REMOVIDO
ARVORE VAZIA
FIM. ALTURA: -1
```