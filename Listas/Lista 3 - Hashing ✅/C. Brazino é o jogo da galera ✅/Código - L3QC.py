#Classe da HashTable
class HashTable:
  #Cria uma lista com uma quantidade de listas vazias igual a {size}
  def __init__(self, size, in_size):
    self.size = size
    self.table = [[] for _ in range(size)]
    self.horarios = [None for _ in range(size)]
    self.in_size = in_size
  
  #Insere o jogo dentro da lista de índice {key} que está dentro da lista {self.table}
  #Também armazena o horário daquela key na lista {self.horarios} que armazena na mesma key da outra lista
  def ADD(self, partida, key, horario, key_original):
    #Verificando se o horário está correto ou se não tem horário no índice
    if horario == self.horarios[key] or self.horarios[key] == None:
      #Verificando se há espaço na lista do horário determinado
      if len(self.table[key]) < self.in_size:
        #Definição de horário se o índice já não tiver horário antes
        if self.table[key] == []:
          self.horarios[key] = horario
        self.table[key].append(partida)
      else:
        #Se a partida era no horário correto, mas não conseguiu entrar porque o horário estava lotado, então ela não entra em nenhum lugar da hash
        print(f"partida: {partida} não foi adicionada por falta de espaço na lista!")  
    else:
      #Caso a partida tenha tentado entrar em um índice e falhado POR CAUSA DO HORÁRIO ERRADO, então ele parte pra tentar no índice sucessor,se chegar ao final da hash, ele vai pro início(caso o início não seja o primeiro índice que a partida foi inserida pra tentar entrar) até chegar no índice antecessor do índice da sua primeira tentativa 
      if (len(self.table)-1) > key and key+1 != key_original:
        self.ADD(partida, key+1, horario, key_original)
      elif (len(self.table)-1) == key and 0 != key_original:
        self.ADD(partida, 0, horario, key_original)
      #Caso mesmo assim a partida ainda não ache espaço, ela não entra em nenhum lugar da hash
      else:  
        print(f"partida: {partida} não foi adicionada por falta de espaço na hashtable!")
  
  #Remove a partida da hash, caso ela se encontre na hash
  def REM(self, partida, key, horario):
    if horario in self.horarios:
      indice_h = self.horarios.index(horario)
      if partida in self.table[indice_h]:
        self.table[indice_h].remove(partida)
        #Se a lista ficou vazio depois da remoção, o horário é removido também
        if self.table[indice_h] == []:
          self.horarios[indice_h] = None
      else:
        #Caso o horário exista, mas o jogo escolhido não esteja nele
        print(f"partida: {partida} não foi removida porque não pertencia a lista!")
    #Caso o horário fornecido não esteja em nenhuma partida da hash
    else:
      print("o sistema não está armazenando partidas nesse horario!")
  
  #Remove todas as partidas de um horário específico, caso o horário exista na HashTable
  def REMT(self, key, horario):
    if horario in self.horarios:
      indice_h = self.horarios.index(horario)
      #Removendo o horário, já que nenhuma partida vai acontecer
      self.table[indice_h] = []
      self.horarios[indice_h] = None
    else:
      #Se o horário não existia na hashtable
      print("o sistema não está armazenando partidas nesse horario!")
  
  #Printa todas as partidas de todos os horários  
  def printar_tudo(self):
    indice = 0
    for slot in self.table:
      if slot == []:
        print(f"Slot {indice}: Vazio")
      
      else:
        print(f"Slot {indice}: {slot}")
    
      indice += 1    


#Armazena o tamanho da HashTable e o tamanho dos Slots de horários
xy = input().split()
#Separando o horário e o nome da partida
partidas = HashTable(int(xy[0]), int(xy[1]))

try:
  #Recebendo os inputs
  while True:
    entrada = input()
    entrada_splitada = entrada.split()
    
    #Tentativa de inserção de uma partida em um dos horários
    if entrada == "ADD":
      while entrada != "DONE":
        entrada = input()
        if entrada != "DONE":
          entrada_splitada = entrada.split()
          
          horario = int(entrada_splitada[0])
          key = int(entrada_splitada[0])
          key %= int(xy[0])
          
          partida = ""
          for contador in range(len(entrada_splitada)-1):
            if contador != len(entrada_splitada)-2:
              partida += entrada_splitada[contador+1]+" "
            else:
              partida += entrada_splitada[contador+1]
  
          partidas.ADD(partida, key, horario, key)
    
    #Tentativa de remoção de uma partida de um dos horários
    elif entrada == "REM":
      while entrada != "DONE":
        entrada = input()
        if entrada != "DONE":
          entrada_splitada = entrada.split()
          
          horario = int(entrada_splitada[0])
          key = int(entrada_splitada[0])
          key %= int(xy[0])
          
          partida = ""
          for contador in range(len(entrada_splitada)-1):
            if contador != len(entrada_splitada)-2:
              partida += entrada_splitada[contador+1]+" "
            else:
              partida += entrada_splitada[contador+1]
          
          partidas.REM(partida, key, horario)
    
    #Tentativa de remoção de todas as partidas de um horário da HashTable
    elif entrada_splitada[0] == "REMT":
      horario = int(entrada_splitada[1])
      key = int(entrada_splitada[1])
      key %= int(xy[0])
      
      partidas.REMT(key, horario)
    
    #Prints da HashTable, um print pra printar todas as partidas da HashTable e outro print pra printar apenas as partidas de um horário específico da HashTable  
    elif entrada_splitada[0] == "PRINT":
      partidas.printar_tudo()
      
#Quando o console parar de fornecer inputs, o código termina      
except EOFError:
  pass


