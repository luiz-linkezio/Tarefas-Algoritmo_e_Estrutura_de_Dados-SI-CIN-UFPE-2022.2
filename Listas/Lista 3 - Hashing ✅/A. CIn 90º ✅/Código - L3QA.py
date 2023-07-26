#Classe da HashTable
class HashTable:
  #Cria uma lista com uma quantidade de listas vazias igual a {size}
  def __init__(self, size):
    self.size = size
    self.table = [[] for _ in range(size)]
  
  #Insere o aluno dentro da lista de índice {key} que está dentro da lista {self.table}
  def inserir(self, aluno, key):
    self.table[key].append(aluno)
  
  #Pra cada key acessada, printa: ({key dos alunos}: {nomes dos alunos})
  def printar(self, keys):
    for key in keys:
      print(f"{key}:", end=" ")
      alunos_temp = list()
      for aluno in self.table[key]:
        alunos_temp.append(aluno)
      print(" ".join(alunos_temp))  
  
#Declaração das listas usadas
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alunos = list() 
keys = list()
keys_sem_repeticao = list()

#Início da classe de HashTable, o tamanho é 10 pq são a quantidade de restos de uma divisão por 10
tabela = HashTable(10)

#Quantidade de alunos
N = int(input())

#Para cada aluno...
for _ in range(N):
  aluno = input()
  
  #Aplicando a fórmula para obter a chave(key)
  key = 0
  for letra in aluno:
    key += (alfabeto.index(letra) + 1)
  key = key % 10
  
  #Inserir o aluno dentro da Key
  tabela.inserir(aluno, key)

  alunos.append(aluno)
  keys.append(key)

#Fazendo uma lista de keys sem repetição e ordenando ela
for chave in keys:
  if chave not in keys_sem_repeticao:
    keys_sem_repeticao.append(chave)
keys_sem_repeticao.sort()    
  
#Printar o que a questão pede: ({key}: {aluno1}, {aluno2}, {aluno3}...)
#Também enviando como argumento as keys que vão ser acessadas
tabela.printar(keys_sem_repeticao)
