class Aluno:
  def __init__(self, ident, nome, idade, curso):
    #Iniciando os valores do vértice
    self.ident = ident
    self.nome = nome
    self.idade = idade
    self.curso = curso
    self.amigos = list()

#Classe de grafo    
class CInterage:
  #Dicionário que será responsável pelo grafo
  def __init__(self):
    self.sistema = dict()
    
  #Adicionar vértice ao grafo
  def adicionar_aluno(self, aluno):
    ident = int(aluno.ident)
    self.sistema[ident] = aluno
  
  #Formando arestas duplamente direcionadas entre dois vértices
  def amizade(self, duplas):
    for dupla in duplas:
      self.sistema[dupla[0]].amigos.append(dupla[1])
      self.sistema[dupla[1]].amigos.append(dupla[0])

  #Printando o que a questão quer: as conexões de um vértice específico e a quantidade delas
  def printar(self, userid):
    print(f"O usuário {self.sistema[userid].nome} tem um total de {len(self.sistema[userid].amigos)} conexões, seus amigos são:", end=" ")
  
    lista_de_amigos = list()
    for amigo in self.sistema[userid].amigos:
      lista_de_amigos.append(self.sistema[amigo].nome)
    lista_de_amigos.sort()
    for amigo in lista_de_amigos:
      if amigo == lista_de_amigos[len(lista_de_amigos)-1]:
        print(amigo, end=".")
      else:
        print(amigo, end=", ")

  
#Iniciando a classe de grafo  
cinterage = CInterage()

#Tratando a primeira string de entrada
string = input()
string_splitada = string.split('"')
lista_info = list()
for i in range(len(string_splitada)):
  
  if string_splitada[i] == "id":
    ident = ""
    for caractere in string_splitada[i+1]:
      if caractere.isdigit():
        ident += caractere
    ident = int(ident)
    lista_info.append(ident)
    
  if string_splitada[i] == "nome":
    nome = string_splitada[i+2]
    lista_info.append(nome)  
  
  if string_splitada[i] == "idade":
    idade = ""
    for caractere in string_splitada[i+1]:
      if caractere.isdigit():
        idade += caractere
    idade = int(idade)
    lista_info.append(idade)
    
  if string_splitada[i] == "curso":
    curso = string_splitada[i+2]
    lista_info.append(curso)
    
    #Adicionando os valores do vértice
    aluno = Aluno(ident, nome, idade, curso)
    #Adicionando o vértice ao grafo
    cinterage.adicionar_aluno(aluno)

#Tratando a string da segunda entrada
conexoes = input().split()
numeros_lista = list()
for i in range(len(conexoes)):
  numero = ""
  for caractere in conexoes[i]:
    if caractere.isdigit():
        numero += caractere
  numeros_lista.append(numero)
#Adicionando as arestas aos vértices, formando conexões duplamente direcionadas  
duplas = list()
for i in range(0, len(numeros_lista), 2):
  duplas.append([int(numeros_lista[i]), int(numeros_lista[i+1])])

#Formando as conexões duplamente direcionadas e printando elas logo em seguida
cinterage.amizade(duplas)
cinterage.printar(int(input()))