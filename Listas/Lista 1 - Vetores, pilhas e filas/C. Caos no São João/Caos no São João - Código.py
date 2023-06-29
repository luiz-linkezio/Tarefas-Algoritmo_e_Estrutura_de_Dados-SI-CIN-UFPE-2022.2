def arredondar_para_cima(num):
  inteiro = int(num)
  if numero == inteiro:
    return inteiro
  else:
    return inteiro + 1


class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class Cliente:
  def __init__(self, nome, dinheiro):
    self.nome = nome
    self.dinheiro = dinheiro

class Caixa:
  def __init__(self):
    self.head = None
    self.tail = None

  def adicionar(self, fregues):
    new_node = Node(fregues)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.head
      self.head.next = new_node
      self.head = new_node
      
  def checar_quantidade(self):
    if self.head:
      contador = 0
      current = self.head
      while current:
        current = current.prev
        contador += 1
        
      return contador
    
    else:
      return 0
      
  def atendimento(self, fila_atual, caixa):
    current = self.head
    while current and current.prev is not None:
      current = current.prev
    
    if current.data.nome == self.tail.data.nome:
      
      pagamento = current.data.dinheiro
      print(f"{current.data.nome} foi chamado para o caixa {caixa}")
      
      if fila_atual > 1:
        current.next.prev = None
        self.tail = current.next
        current = current.next
      else:
        current = None
        
    while current and current.next is not None:
      if current.next is not None:
        current = current.next
        
    self.head = current
    
    return pagamento
  
  def transferir(self, transferencias, caixa):
    
    for i in range(transferencias):
    
      if self.head is not None:
        if caixa == "caixa2":
          caixa_1.adicionar(self.head.data) 
        
        elif caixa == "caixa1":
          caixa_2.adicionar(self.head.data)
        
        self.head = self.head.prev
        if self.head is not None:
          self.head.next = None
  
  def printar1(self):
    current = self.head
    while current:
      print(current.data.nome)
      current = current.prev

caixa_1 = Caixa()
caixa_2 = Caixa()

dinheiro_caixa_1 = 0
dinheiro_caixa_2 = 0

entrada = None

while entrada != "FIM":
  
  entrada = input()
  entrada = entrada.split()
  
  if entrada[0] == "ENTROU:":
    nome = entrada[1]
    fila = entrada[2]
    dinheiro = entrada[3]
    
    fregues = Cliente(nome, dinheiro)
    
    if fila == "1":
      caixa_1.adicionar(fregues)
      print(f"{nome} entrou na fila 1")
      
    elif fila == "2":
      caixa_2.adicionar(fregues)
      print(f"{nome} entrou na fila 2")
      
  elif entrada[0] == "PROXIMO:":
    fila = entrada[1]
    
    if fila == "1":
      if caixa_1.checar_quantidade() == 0:      
        caixa_2.transferir(arredondar_para_cima((caixa_2.checar_quantidade()/2)), "caixa2")
      dinheiro_caixa_1 += float(caixa_1.atendimento(caixa_1.checar_quantidade(), "1")) 
      
    elif fila == "2":
      if caixa_2.checar_quantidade() == 0:
        caixa_1.transferir(arredondar_para_cima((caixa_1.checar_quantidade()/2)), "caixa1")
      dinheiro_caixa_2 += float(caixa_2.atendimento(caixa_2.checar_quantidade(), "2")) 
    
    
  entrada = entrada[0]

print(f"Caixa 1: R$ {dinheiro_caixa_1:.2f}, Caixa 2: R$ {dinheiro_caixa_2:.2f}")
