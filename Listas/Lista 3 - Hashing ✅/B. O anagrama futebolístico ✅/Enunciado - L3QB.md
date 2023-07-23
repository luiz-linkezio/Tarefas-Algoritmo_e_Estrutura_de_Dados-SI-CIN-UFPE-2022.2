# O anagrama futebolístico

**Limite de tempo do código: 100ms**

Você é o mais novo jogador do Malandrote da Abdias, o time da desonestidade anti-esportiva. Porém, no dia da sua chegada em Recife tinham uns 100 tabacudos esperando Diego Souza voltar às 3 da manhã de uma terça-feira 🤣🤣🤣. Revoltado com tamanha tabaquisse, você resolveu rescindir o contrato e ir jogar em outro time na capital pernambucana. Como o falecido Santa Cruz não existe mais, Deus o tenha, você escolheu o papai do Sport, o gigantesco Clube Náutico Capibaribe. Sua recepção foi muito bem feita entre os incríveis e talentosíssimos atletas, agora só resta escolher o seu grupinho de amigos no elenco para curtir um churrasquinho com pagode nos dias de folga. Para isso, você usou suas incríveis habilidades de algoritmos adquiridas na sua vida pré futebol, utilizando Hashing.

Mostre as opções de grupos de amigos disponíveis para você se juntar, cada grupinho é unido por ter exatamente as mesmas letras no nome, ou seja, **anagramas**.

**DICA: Utilize a tabela Ascii, faça soma das letras para inserir na Hash Table e se atente as colisões**

- ord(char) retorna um número

- chr(num) retorna um carácter

**PROIBIDO USAR DICIONÁRIO**

Cuidado com a complexidade do código.

## Input:

N: Quantidade de jogadores, utilize como tamanho do hash table

- Várias linhas com os nomes dos atletas

## Output:

- Caso não tenha anagrama presente do nome no índice do Hash table: **{NOME} criou um grupinho**
- Caso haja uma colisão e o jogador é um anagrama do grupinho que já contenha alguém : **{NOME} entrou no grupinho**
- Caso não consiga entrar no grupinho, ou seja, haja uma colisão e não é um anagrama daquele grupo: **{NOME} tentou entrosar, mas foi descoberto**
- Após comando "FIM": **Grupinhos: [LISTAS DE GRUPOS]**

EX: **Grupinhos: [ [Fulano, Foluna, Faluno], [Beltrano, Boltrena]....]**

## Exemplos:

### Caso 1:

Input:
```
7
jael
souza
vagner
jeal
zasou
kuki
kieza
FIM
```

Output:
```
jael criou um grupinho
souza criou um grupinho
vagner tentou se entrosar, mas foi descoberto
jeal entrou no grupinho
zasou entrou no grupinho
kuki tentou se entrosar, mas foi descoberto
kieza criou um grupinho
Grupinhos:[['kieza'], ['souza', 'zasou'], ['jael', 'jeal']]
```