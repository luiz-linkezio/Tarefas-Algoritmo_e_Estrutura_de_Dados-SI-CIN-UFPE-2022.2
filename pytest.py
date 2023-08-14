class Aluno:
  def __init__(self, ident, nome, idade, curso):
    self.ident = ident
    self.nome = nome
    self.idade = idade
    self.curso = curso
    self.amigos = list()
    
class CInterage:
  def __init__(self):
    self.sistema = dict()
  
  def adicionar_aluno(self, aluno):
    ident = int(aluno.ident)
    self.sistema[ident] = aluno
  
  def amizade(self, duplas):
    for dupla in duplas:
      self.sistema[dupla[0]].amigos.append(dupla[1])
      self.sistema[dupla[1]].amigos.append(dupla[0])

  def printar(self, userid):
    print(f"O usuário Adriano tem um total de {len(self.sistema[userid].amigos)} conexões, seus amigos são:", end=" ")
  
    lista_de_amigos = list()
    for amigo in self.sistema[userid].amigos:
      lista_de_amigos.append(self.sistema[amigo].nome)
    lista_de_amigos.sort()
    for amigo in lista_de_amigos:
      if amigo == lista_de_amigos[len(lista_de_amigos)-1]:
        print(amigo, end=".")
      else:
        print(amigo, end=", ")
  
  
cinterage = CInterage()

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
    
    aluno = Aluno(ident, nome, idade, curso)
    cinterage.adicionar_aluno(aluno)
    

conexoes = input().split()
numeros = ""
for i in range(len(conexoes)):
  for caractere in conexoes[i]:
    if caractere.isdigit():
        numeros += caractere
duplas = list()
for i in range(0, len(numeros), 2):
  duplas.append([int(numeros[i]), int(numeros[i+1])])
cinterage.amizade(duplas)
  
cinterage.printar(int(input()))