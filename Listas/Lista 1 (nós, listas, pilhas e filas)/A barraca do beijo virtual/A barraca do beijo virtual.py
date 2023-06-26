class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class Beijos:
  def __init__(self):
    self.head = None
    self.tail = None

  def adicionar(self, nome):
    new_node = Node(nome)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def adicionar_topo(self, nome):
    new_node = Node(nome)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remover_nome(self, nome):
    current = self.head
    encontrou = False

    while current:
      if nome == current.data and not encontrou:
        encontrou = True

        if current.prev is not None:
          current.prev.next = current.next
        else:
          self.head = current.next
          if self.head is not None:
            self.head.prev = None

        if current.next is not None:
          current.next.prev = current.prev
        else:
          self.tail = current.prev
          if self.tail is not None:
            self.tail.next = None

      current = current.next

  def printar1(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def printar2(self):
    current = self.tail
    while current:
      print(current.data)
      current = current.prev

  def procurar_nome(self, nome):
    current = self.head
    while current:
      if nome == current.data:
        return True
      current = current.next

    return False

usuario = input()
usuario = usuario.split()
usuario = usuario[1]

beijos_lista = Beijos()
registro = []

entrada = False
while entrada != "FIM":

  entrada = input()
  entrada = entrada.split()

  if entrada[0] == "BEIJO" and entrada[1] not in registro:
    registro.append(entrada[1])
    beijos_lista.adicionar(entrada[1])

  elif entrada[0] == "SUPERBEIJO":
    if beijos_lista.procurar_nome(entrada[1]):
      beijos_lista.remover_nome(entrada[1])
      beijos_lista.adicionar(entrada[1])
    else:
      registro.append(entrada[1])
      beijos_lista.adicionar(entrada[1])

  elif entrada[0] == "XODÓ" and entrada[1] in registro:
    registro.remove(entrada[1])
    beijos_lista.remover_nome(entrada[1])

  elif entrada[0] == "MOSTRAR":
    if registro == []:
      print("Histórico vazio.")
    else:
      beijos_lista.printar2()

  entrada = entrada[0]

print(f"O histórico final do usuário {usuario} é:")

if registro == []:
  print("Histórico vazio.")
else:
  beijos_lista.printar2()
