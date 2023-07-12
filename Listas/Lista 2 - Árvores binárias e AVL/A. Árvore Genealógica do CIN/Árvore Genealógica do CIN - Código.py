class Node:
  def __init__(self, valor, altura=0):
    self.valor = valor
    self.filhoD = None
    self.filhoE = None
    self.altura = altura
  

class Arvore_bi:
  
  def __init__(self):
    self.raiz = None
  
  def criarArvore(self, lista):
    
    for i in lista:     
      node = Node(i)
      
      if self.raiz == None:
        self.raiz = node
  
      else:
        entrou = False
        item_atual = self.raiz
        while not entrou:
          if item_atual.valor < node.valor:
            if item_atual.filhoD == None:
              item_atual.filhoD = node
              node.pai = item_atual
              entrou = True                    
            else:
              item_atual = item_atual.filhoD
          elif item_atual.valor > node.valor:
            if item_atual.filhoE == None:
              item_atual.filhoE = node
              node.pai = item_atual
              entrou = True
            else:
              item_atual = item_atual.filhoE
  
  def printar(self):
    no_atual = self.raiz

    self.printar_auxiliar_recursivo(no_atual)

  def printar_auxiliar_recursivo(self, no_atual):
    
    if no_atual.filhoE and no_atual.filhoD:
      print(f"{no_atual.valor} é mãe de {no_atual.filhoE.valor} e {no_atual.filhoD.valor}.")
    elif no_atual.filhoE:
      print(f"{no_atual.valor} é mãe de {no_atual.filhoE.valor}.")
    elif no_atual.filhoD:
      print(f"{no_atual.valor} é mãe de {no_atual.filhoD.valor}.")
    
    if no_atual.filhoE:
      self.printar_auxiliar_recursivo(no_atual.filhoE)
      
    if no_atual.filhoD:
      self.printar_auxiliar_recursivo(no_atual.filhoD)

  
nomes = input()
nomes_splitado = nomes.split()

arvore_genealogica = Arvore_bi()
arvore_genealogica.criarArvore(nomes_splitado)
arvore_genealogica.printar()