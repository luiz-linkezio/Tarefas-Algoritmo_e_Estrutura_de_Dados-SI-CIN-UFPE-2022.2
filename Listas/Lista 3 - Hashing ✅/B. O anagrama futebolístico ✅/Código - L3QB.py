class HashTable:
  #Cria uma lista com uma quantidade de listas vazias igual a {size}
  def __init__(self, size):
    self.size = size
    self.table = [[] for _ in range(size)]
  
  #Tenta inserir o jogador dentro da lista de índice {key} que está dentro da lista {self.table}
  #Para inseri-lo ou não, deve-se verificar as regras impostas pela questão
  #Também está printando o que a questão pede em cada situação
  def inserir(self, nome, key):
    if self.table[key]:
      if verificar_anagrama(self.table[key][0], nome) == True:
        self.table[key].append(nome)
        print(f"{nome} entrou no grupinho")
      else:
        print(f"{nome} tentou se entrosar, mas foi descoberto")
    else:  
      self.table[key].append(nome)
      print(f"{nome} criou um grupinho")
  
  #Printa a lista {self.table} sem os grupinhos vazios
  def printar(self):
    grupos_vazios = list()
    contador_de_vazios = 0
    
    for grupinho in self.table:
      if grupinho == []:
        contador_de_vazios += 1
    for _ in range(contador_de_vazios):
      self.table.remove([])
      
    print(f"Grupinhos:{self.table}") 

#Função que verifica se duas palavras são anagramas uma da outra
def verificar_anagrama(palavra1, palavra2):
  if sorted(palavra1) == sorted(palavra2):
    return True
  else:
    return False

#Número de jogadores, que também é o tamanho da lista hash, pois a possibilidade mais distribuída é um jogador para cada espaço na lista
N = int(input())

#Iniciando a classe
grupinhos = HashTable(N)

#Coletando os nomes, criando as keys e fazendo as tentativas de inserção
for _ in range(N):
  nome = input()
  key = 0
  for letra in nome:
    key += ord(letra)
  key %= N
    
  grupinhos.inserir(nome, key)  

  
#Printando o que a questão pede no final  
grupinhos.printar()
    
