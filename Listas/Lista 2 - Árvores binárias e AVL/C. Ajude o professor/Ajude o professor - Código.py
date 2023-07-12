#classe de nó
class Node:
  def __init__(self, nome):
    self.valor = nome
    
    self.filhoD = None
    self.filhoE = None
    self.pai = None
    self.fator_balanceamento = 0

#classe de árvore binária
class Arvore_bi:
  
  def __init__(self):
    self.raiz = None
  
  #adicionar elemento na árvore
  def adicionar(self, nome):
    
    node = Node(nome)
    
    #se for o primeiro nó  
    if self.raiz == None:
      self.raiz = node
  
    #se não for o primeiro nó
    else:
      entrou = False
      item_atual = self.raiz
      #enquanto não entrar na árvore, o algoritmo vai ficar descendo até encontrar um local
      while not entrou:
        
        #se for maior, vai pra direita
        if item_atual.valor < node.valor:
          if item_atual.filhoD == None:
            item_atual.filhoD = node
            item_atual.filhoD.pai = item_atual
            
            entrou = True 
            
          else:
            item_atual = item_atual.filhoD
        
        #se for menor, vai pra esquerda    
        elif item_atual.valor > node.valor:
          if item_atual.filhoE == None:
            item_atual.filhoE = node
            item_atual.filhoE.pai = item_atual
            
            entrou = True
            
          else:
            item_atual = item_atual.filhoE
      
      #atualização e balanceamento
      self.atualizar_fatores_balanceamento_abaixo()
      self.balanceamento(node)
      self.atualizar_fatores_balanceamento_abaixo()
  
  #Percorre a árvore de baixo pra cima, atualizando os fatores de balanceamento(não usei este método na versão final)
  def atualizar_fatores_balanceamento_acima(self, no_atual):
    while no_atual is not None:
      no_atual.fator_balanceamento = self.obter_altura(no_atual.filhoD) - self.obter_altura(no_atual.filhoE)
      no_atual = no_atual.pai
  
  #percorre a árvore inteira a partir da raiz ou algum ponto à escolha, depois vai obtendo a altura de ambos os lados para atualizar o fator de balanceamento    
  def atualizar_fatores_balanceamento_abaixo(self, no_atual=None):
    if self.raiz:
      if no_atual == None:
        no_atual = self.raiz
    
      no_atual.fator_balanceamento = self.obter_altura(no_atual.filhoD) - self.obter_altura(no_atual.filhoE)  
        
      if no_atual.filhoE:
        self.atualizar_fatores_balanceamento_abaixo(no_atual.filhoE)
      if no_atual.filhoD:
        self.atualizar_fatores_balanceamento_abaixo(no_atual.filhoD)  

  #Obtém a altura dos lados e vai pegando só o maior valor
  def obter_altura(self, no_atual):
    if no_atual is None:
      return 0
    
    altura_esquerda = self.obter_altura(no_atual.filhoE) if no_atual.filhoE else 0
    altura_direita = self.obter_altura(no_atual.filhoD) if no_atual.filhoD else 0
    
    return max(altura_esquerda, altura_direita) + 1

  #remove um nó específico a partir do valor deste nó, e quem assume é o menor sucessor
  def remocao(self, nome):
    
    #O nó é achado a partir do valor dele
    no_atual = (self.busca(nome))[0]
    
    #nó que for ser removido tem 2 filhos
    if no_atual.filhoD and no_atual.filhoE:
      
      #armazenando o sucessor primário
      filhoD = no_atual.filhoD
      
      #pegando o menor sucessor possível a partir do sucessor primário  
      no_temporario = no_atual.filhoD
      while no_temporario.filhoE is not None: 
        no_temporario = no_temporario.filhoE
      
      #se o pai do nó sucessor NÃO for o nó que está sendo removido
      if no_temporario.pai  != no_atual:
        no_temporario.pai.filhoE = no_temporario.filhoD
      
        if no_temporario.filhoD:  
          no_temporario.filhoD.pai = no_temporario.pai
      
      #ligando o nó sucessor ao filho da esquerda do nó que está sendo removido
      no_atual.filhoE.pai = no_temporario
      no_temporario.filhoE = no_atual.filhoE
      
      #se o filho à direita do nó que está sendo removido não for o nó sucessor
      if no_atual.filhoD != no_temporario:
      
        no_temporario.filhoD = no_atual.filhoD
        no_atual.filhoD.pai = no_temporario
    
      #se o nó que está sendo removido tem pai, faz a troca das relações com o pai do nó removido para o nó sucessor
      if no_atual.pai:
        
        no_temporario.pai = no_atual.pai
        
        if no_atual == no_atual.pai.filhoE:
          no_atual.pai.filhoE = no_temporario
        elif no_atual == no_atual.pai.filhoD:
          no_atual.pai.filhoD = no_temporario
          
      #se não, o sucessor fica sem pai e se torna a raiz  
      else:
        no_temporario.pai = None
        self.raiz = no_temporario
  
      #atualizar fatores de balanceamento e balancear a partir do sucessor
      self.atualizar_fatores_balanceamento_abaixo()
      self.balanceamento(filhoD)
      self.atualizar_fatores_balanceamento_abaixo()
  
    #se o nó que for removido tiver APENAS o filho à direita
    elif no_atual.filhoD and not no_atual.filhoE:
      
      #armazenando o sucessor
      filhoD = no_atual.filhoD
      
      #se o nó que está sendo removido tem pai, faz a troca das relações com o pai do nó removido para o nó sucessor
      if no_atual.pai:
        
        if no_atual == no_atual.pai.filhoE:
          no_atual.pai.filhoE = no_atual.filhoD
        elif no_atual == no_atual.pai.filhoD:
          no_atual.pai.filhoD = no_atual.filhoD
          
        no_atual.filhoD.pai = no_atual.pai
      
      #se não, o sucessor fica sem pai e se torna a raiz    
      else:
        no_atual.filhoD.pai = None
        self.raiz = no_atual.filhoD
      
      #atualizar fatores de balanceamento e balancear a partir do sucessor
      self.atualizar_fatores_balanceamento_abaixo()
      self.balanceamento(filhoD)
      self.atualizar_fatores_balanceamento_abaixo()
    
    #se o nó que for removido tiver APENAS o filho à esquerda
    elif no_atual.filhoE and not no_atual.filhoD:  
    
      #armazenando o sucessor
      filhoE = no_atual.filhoE
    
      #se o nó que está sendo removido tem pai, faz a troca das relações com o pai do nó removido para o nó sucessor
      if no_atual.pai:
        
        if no_atual == no_atual.pai.filhoE:
          no_atual.pai.filhoE = no_atual.filhoE
        elif no_atual == no_atual.pai.filhoD:
          no_atual.pai.filhoD = no_atual.filhoE
        
        no_atual.filhoE.pai = no_atual.pai
      
      #se não, o sucessor fica sem pai e se torna a raiz    
      else:
        no_atual.filhoE.pai = None
        self.raiz = no_atual.filhoE
      
      #atualizar fatores de balanceamento e balancear a partir do sucessor
      self.atualizar_fatores_balanceamento_abaixo()
      self.balanceamento(filhoE)
      self.atualizar_fatores_balanceamento_abaixo()
    
    #se o nó que for removido não tiver filho
    else:
      
      #armazenando o pai do nó que for ser removido
      pai = no_atual.pai
      
      #se o nó que for removido tem pai, o pai vai apontar pra None
      if no_atual.pai:
        if no_atual == no_atual.pai.filhoE:
          no_atual.pai.filhoE = None
        elif no_atual == no_atual.pai.filhoD:
          no_atual.pai.filhoD = None
      
      #se o nó que for removido, que não tem filho, também não tiver pai, então a árvore fica vazia
      else:
        self.raiz = None
    
      #atualizar fatores de balanceamento e balancear a partir do pai do nó que foi removido ou de ninguém(em caso de árvore vaiza).
      self.atualizar_fatores_balanceamento_abaixo()
      self.balanceamento(pai)
      self.atualizar_fatores_balanceamento_abaixo()
  
  #giro pra esquerda
  def girar_esquerda(self, no_atual):

    #armazenando relacionados ao nó que tá girando
    avo = None
    filhoE = None

    #declarando apontadores temporários 
    pai = no_atual.pai
    if no_atual.pai.pai:
      avo = no_atual.pai.pai
    if no_atual.filhoE:
      filhoE = no_atual.filhoE
    
    # invertendo papel de pai e filho com o nó atual e o pai dele
    no_atual.filhoE = pai
    pai.pai = no_atual
    
    #no atual jogando filho pro outro lado
    if filhoE:
      filhoE.pai = pai
      pai.filhoD = filhoE
    else:
      pai.filhoD = None
    
    #se no_atual tem avô, vira pai, se não, no atual vira raiz
    if avo:
      no_atual.pai = avo
      
      if avo.filhoE == pai:
        avo.filhoE = no_atual
      elif avo.filhoD == pai:
        avo.filhoD = no_atual
    
    else:
      no_atual.pai = None
      self.raiz = no_atual
    

      
  def girar_direita(self, no_atual):

    #armazenando relacionados ao nó que vai girar
    avo = None
    filhoD = None

    #declarando apontadores temporários 
    pai = no_atual.pai
    if no_atual.pai.pai:
      avo = no_atual.pai.pai
    if no_atual.filhoD:
      filhoD = no_atual.filhoD
    
    # invertendo papel de pai e filho com o nó atual e o pai dele
    no_atual.filhoD = pai
    pai.pai = no_atual
    
    #no atual jogando filho pro outro lado
    if filhoD:
      filhoD.pai = pai
      pai.filhoE = filhoD
    else:
      pai.filhoE = None
    
    #se no_atual tem avô, vira pai, se não, no atual vira raiz
    if avo:
      no_atual.pai = avo
      
      if avo.filhoD == pai:
        avo.filhoD = no_atual
      elif avo.filhoE == pai:
        avo.filhoE = no_atual
    
    else:
      no_atual.pai = None
      self.raiz = no_atual
  
  #balanceia de baio pra cima
  def balanceamento(self, no_atual=None):
    
    #só balanceia se existir árvore  
    if self.raiz:
    
      desbalanceada = False
    
      #se não tiver um ponto de partida, começa na raiz
      if no_atual is None:
        no_atual = self.raiz
      
      if no_atual.fator_balanceamento > 1:
        if no_atual.filhoD.fator_balanceamento > -1:
          self.girar_esquerda(no_atual.filhoD)
        elif no_atual.filhoD.fator_balanceamento < 0:
          self.girar_direita(no_atual.filhoD.filhoE)
          self.girar_esquerda(no_atual.filhoD)
        
      elif no_atual.fator_balanceamento < -1:
        if no_atual.filhoE.fator_balanceamento < 0:
          self.girar_direita(no_atual.filhoE)
        elif no_atual.filhoE.fator_balanceamento > -1:
          self.girar_esquerda(no_atual.filhoE.filhoD)
          self.girar_direita(no_atual.filhoE)
    
      self.atualizar_fatores_balanceamento_abaixo()
    
      if no_atual.pai:
        self.balanceamento(no_atual.pai)
  
  #percorre a árvore toda pra buscar um elemento, pode não encontrar
  def busca(self, nome, altura=0, no_atual=None):
    
    #altura 0 é a raiz
    if altura == 0:
      no_atual = self.raiz
    
    #se achou quem queria, retorna o nó e a altura
    if no_atual and nome == no_atual.valor:
      return no_atual, altura
    
    #se não achou, pesquisa no antecessor se ele existir
    elif no_atual and no_atual.filhoE and nome < no_atual.valor:
      altura += 1
      return self.busca(nome, altura, no_atual.filhoE)
    
    #se não achou, pesquisa no sucessor se ele existir  
    elif no_atual and no_atual.filhoD and nome > no_atual.valor:
      altura += 1
      return self.busca(nome, altura, no_atual.filhoD)
    
    #não encontrou na árvore inteira, retorna com None e altura zero  
    else:
      return None, 0  
  
  #percorre a árvore inteira e printa todos os valores em pré-ordem
  def printar(self):
    #começa da raiz
    no_atual = self.raiz

    self.printar_auxiliar_recursivo(no_atual)
  
  #recursão do print
  def printar_auxiliar_recursivo(self, no_atual):
    
    #se o nó atual existir, printa
    if no_atual:
      print(no_atual.valor,"->", end=" ")
      #print(no_atual.fator_balanceamento)
    
    #depois, se um ou mais filho existir, percorre pra ele(s)
    
    if no_atual and no_atual.filhoE:
      self.printar_auxiliar_recursivo(no_atual.filhoE)
      
    if no_atual and no_atual.filhoD:
      self.printar_auxiliar_recursivo(no_atual.filhoD)     

#constrói a árvore
arvore = Arvore_bi()

#entrada
entrada = input()

while entrada != "FIM":
  entrada_splitada = entrada.split()

  #verifica se é pra inserir e depois insere o elemento da árvore caso ele já não esteja lá
  if entrada_splitada[0] == "INSERIR":
    if (arvore.busca(entrada_splitada[1]))[0] is None:
      arvore.adicionar(entrada_splitada[1])
      print(f"{entrada_splitada[1]} INSERIDO")
    else: 
      print(f"{entrada_splitada[1]} JA EXISTE")

  #verifica se é pra remover e depois remove o elemento da árvore, se ele estiver lá
  elif entrada_splitada[0] == "DELETAR":
    if (arvore.busca(entrada_splitada[1]))[0] is not None:
      arvore.remocao(entrada_splitada[1])
      print(f"{entrada_splitada[1]} REMOVIDO")
    else:
      print(f"{entrada_splitada[1]} NAO ENCONTRADO")
      
  entrada = input()

#se a árvore for vazia, mostra que está vazia e mostra a altura total da árvore
if arvore.raiz is None:
  print("ARVORE VAZIA")
  print(f"FIM. ALTURA: -1")
#se a árvore não for vazia, printa os elementos em pré-ordem e mostra a altura total da árvore
else:
  arvore.printar()
  print(f"FIM. ALTURA: {arvore.obter_altura(arvore.raiz)-1}")